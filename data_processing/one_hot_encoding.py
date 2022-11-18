import pandas as pd
from typing import Sequence, Dict, Optional, Tuple

def one_hot_encoder(df: pd.DataFrame, column_list: Sequence[str] = None) -> pd.DataFrame:
  """_summary_

  Args:
      df (pd.DataFrame): Input dataframe
      column_list (Sequence[str], optional): List of all columns to convert to dummy. Defaults to None.

  Returns:
      pd.DataFrame: _description_
  """  
  #ffgfdd
  # ['hola']
  return df