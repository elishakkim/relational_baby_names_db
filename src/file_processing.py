import os
import pandas as pd

def load_data_from_files(directory, file_extension = '.txt', read_func=None, **kwargs):
  """
  Load and combine data file in a directory

  Parameters: 
  - directory (str): The path to the directory containing the files.
  - file_extension (str): The file extensions to filter files (default is ".txt")
  - read_func (callable): A custom function to read individual files (default is pd.read_csv)
  - **kwargs: Additional arguments to pass to the read_func.

  Returns: 
  - pd.DataFrame: Combined DataFrame containing data from all files
  """
  add_year = kwargs.pop('add_year', False)
  data_frames = []

  for filename in os.listdir(directory):
    if filename.endswith(file_extension):
      file_path = os.path.join(directory, filename)
      print(f'Processing file: {file_path}')

      if read_func is None:
        df = pd.read_csv(file_path, **kwargs)
      else:
        df = read_func(file_path, **kwargs)
      
      if add_year:
        year = filename[3:7]
        df['Year'] = int(year)

      data_frames.append(df)

  combined_df = pd.concat(data_frames, ignore_index=True)
  return combined_df
