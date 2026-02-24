import pandas as pd
from pathlib import Path
import json


filepath = Path("temp.json")
with open(filepath) as f:
    data = json.load(f)

df = pd.DataFrame.from_dict(data)

#df = pd.read_json(filepath)