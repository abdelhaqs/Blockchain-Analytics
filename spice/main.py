from __future__ import annotations
import os
from dotenv import load_dotenv
import polars as pl
import spice

# Load environment variables from .env file
load_dotenv()

# Fetch data using spice.query, which returns a Polars DataFrame
df_polars = spice.query(3906619)

# Display the first few rows of the Polars DataFrame
print(df_polars)
