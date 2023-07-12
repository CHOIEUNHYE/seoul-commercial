import os
import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS
import csv

# instantiate the app
app = Flask(__name__,static_folder='uploads')
app.config.from_object(__name__)


# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


def search_by_name(keyword):
    file_path = os.path.join(os.path.join('uploads', 'seoul_commercial_district.csv'))
    result = []

    with open(file_path, 'r', encoding="utf-8") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row['상호명'] == keyword:
                result.append(row)
    return result

@app.route('/search', methods=['GET'])
def search():
    keyword = request.args.get('keyword')
    if not keyword:
        return jsonify([])
    
    else:
        result = search_by_name(keyword)
        return jsonify(result)
    





def chart_data(keyword):
    file_path = os.path.join(os.path.join('uploads', 'seoul_commercial_district.csv'))
    result = []

    df = pd.read_csv(file_path,encoding="utf-8")
    category_df = df.loc[df["상권업종대분류명"]==keyword]
    city_county_count = category_df.groupby(by='시군구명').count()['상호명']
    return city_county_count.to_dict()


@app.route('/chart', methods=['GET'])
def chart():
    keyword = request.args.get('value')
    # keyword = '소매' //test위한 키워드 고정
    if not keyword:
        return jsonify([])
    else:
        result = chart_data(keyword)
        return jsonify(result)



if __name__ == '__main__':
    app.run()