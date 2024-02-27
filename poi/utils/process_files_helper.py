import csv
import json
from ast import literal_eval
import xml.etree.ElementTree as ET


def calculate_average_rating(ratings):
    return sum(ratings) / len(ratings) if ratings else None


def process_files(file_path):
    poi_list = []
    if file_path.endswith('.csv'):
        process_csv(file_path, poi_list)
    elif file_path.endswith('.json'):
        process_json(file_path, poi_list)
    elif file_path.endswith('.xml'):
        process_xml(file_path, poi_list)

    return poi_list


def process_csv(file_path, poi_list):
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            ratings = literal_eval(row['poi_ratings'])
            avg_rating = calculate_average_rating(ratings)
            poi_dict = {
                'external_id': row['poi_id'], 'name': row['poi_name'], 'category': row['poi_category'], 'avg_rating': avg_rating
            }
            poi_list.append(poi_dict)


def process_json(file_path, poi_list):
    with open(file_path, 'r') as file:
        json_reader = json.load(file)
        for row in json_reader:
            ratings = row['ratings']
            avg_rating = calculate_average_rating(ratings)
            poi_dict = {
                'external_id': row['id'], 'name': row['name'], 'category': row['category'], 'avg_rating': avg_rating
            }
            poi_list.append(poi_dict)


def process_xml(file_path, poi_list):
    tree = ET.ElementTree(file=file_path)
    root = tree.getroot()

    for poi_records in root.findall('.//DATA_RECORD'):
        ratings = poi_records.find('pratings').text
        ratings = [int(rating) for rating in ratings.split(',')]

        data_dict = {
            'external_id': poi_records.find('pid').text,
            'name': poi_records.find('pname').text,
            'category': poi_records.find('pcategory').text,
            'avg_rating': calculate_average_rating(ratings)
        }
        poi_list.append(data_dict)