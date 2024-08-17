import os
from database import Database
from file_processing import load_data_from_files

def main():
  directory = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')
  combined_df = load_data_from_files(directory, file_extension='.txt', names=['Name', 'Gender', 'Count'], header=None, add_year = True)

  combined_df = combined_df[['Name', 'Gender', 'Count', 'Year']]

  db = Database()
  db.create_table('names', ['Name', 'Gender', 'Count', 'Year'])

  for _, row in combined_df.iterrows():
    print(row.tolist())
    db.insert_into('names', row.tolist())
  
  results = db.query('names', conditions={'Year': lambda x: x == 1880})
  print(results)  

if __name__ == '__main__':
  main()