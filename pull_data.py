from google.colab import auth
auth.authenticate_user()
print('Authenticated')
from google.cloud import bigquery
import os

def main():
    project_id = 'still-gravity-200620'
    os.environ["GOOGLE_CLOUD_PROJECT"] = project_id
    client = bigquery.Client(project=project_id)

    query = """
            SELECT child_body, parent_body
            FROM `still-gravity-200620.comment_pairs.all_comment_pairs_10` 
            limit 20
            """
    df = client.query(query).to_dataframe()
    print("Length of dataframe: ")
    print(len(df.index))

if __name__ == '__main__':
    main()
