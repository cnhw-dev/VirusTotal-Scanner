import csv
import requests
import time
import json


API_KEY = 'YOURTOKEN'
CSV_FILE_PATH = 'path/to/urls.csv'
OUTPUT_FILE_PATH = '/path/to/output/analysis_results.json'
POLL_INTERVAL = 15 #limite de 4 requests par minute avec le API Community


def read_urls_from_csv(file_path):
    urls = []
    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row:
                urls.append(row[0])
    return urls


def get_analysis_id(url, api_key):
    headers = {
        'x-apikey': api_key
    }
    response = requests.post(
        'https://www.virustotal.com/api/v3/urls',
        headers=headers,
        files={'url': (None, url)}
    )
    if response.status_code == 200:
        return response.json().get('data', {}).get('id')
    else:
        print(f"Error submitting URL {url}: {response.status_code}")
        return None

def get_analysis_report(analysis_id, api_key):
    headers = {
        'x-apikey': api_key
    }
    response = requests.get(
        f'https://www.virustotal.com/api/v3/analyses/{analysis_id}',
        headers=headers
    )
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error retrieving analysis report for ID {analysis_id}: {response.status_code}")
        return None


def main():
    urls = read_urls_from_csv(CSV_FILE_PATH)

    with open(OUTPUT_FILE_PATH, 'w') as output_file:
        output_file.write('[\n')

        for i, url in enumerate(urls):
            print(f"Processing URL: {url}")
            analysis_id = get_analysis_id(url, API_KEY)
            if analysis_id:
                print(f"Analysis ID: {analysis_id}. Waiting for analysis to complete...")
                time.sleep(POLL_INTERVAL)
                report = get_analysis_report(analysis_id, API_KEY)
                if report:
                    result = {
                        'url': url,
                        'analysis_id': analysis_id,
                        'report': report
                    }
                    json.dump(result, output_file, indent=4)
                    if i < len(urls) - 1:
                        output_file.write(',\n')

        output_file.write('\n]')

    print(f"Analysis complete. Results saved to {OUTPUT_FILE_PATH}")

if __name__ == '__main__':
    main()
