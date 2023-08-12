import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI

df = pd.read_csv("supermarket_sales.csv")
df = df[['Gender', 'Product line', 'Total']]

OPENAI_API_KEY = "k-mtujzCGAyXF5x2gLcLBDT3BlbkFJVLdrDwDxsKnpEkhzV7t"
llm = OpenAI(api_token= OPENAI_API_KEY)

pandas_ai = PandasAI(llm)

answer = pandas_ai.run(df, prompt="What is the total in Total line")
print(answer)