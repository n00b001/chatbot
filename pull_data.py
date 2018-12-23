import csv
import os

from google.cloud import bigquery

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "g_credentials.json"


def main():
    client = bigquery.Client()

    query = """
            SELECT child_body, parent_body
            FROM `still-gravity-200620.comment_pairs.all_comment_pairs_10` 
            limit 20
            """
    df = client.query(query).to_dataframe()
    print("Length of dataframe: ")
    print(len(df.index))

    x = df[["parent_body"]]
    x = x.replace("\n", " <newlinechar> ")
    x = x.replace("\r", " <returnchar> ")
    x = x.replace('"', "'")

    y = df[["child_body"]]
    y = y.replace("\n", " <newlinechar> ")
    y = y.replace("\r", " <returnchar> ")
    y = y.replace('"', "'")

    x.to_csv("nmt-chatbot/new_data/train.from", header=None, index=None, sep=' ', quoting=csv.QUOTE_MINIMAL)
    y.to_csv("nmt-chatbot/new_data/train.to", header=None, index=None, sep=' ', quoting=csv.QUOTE_MINIMAL)


if __name__ == '__main__':
    main()
