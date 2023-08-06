import pandas as pd
import numpy as np
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI

data_dict = {
	"country": [
		"Delhi",
		"Mumbai",
		"Kolkata",
		"Chennai",
		"Jaipur",
		"Lucknow",
		"Pune",
		"Bengaluru",
		"Amritsar",
		"Agra",
		"Kola",
	],
	"annual tax collected": [
		19294482072,
		28916155672,
		24112550372,
		34358173362,
		17454337886,
		11812051350,
		16074023894,
		14909678554,
		43807565410,
		146318441864,
		np.nan,
	],
	"happiness_index": [9.94, 7.16, 6.35, 8.07, 6.98, 6.1, 4.23, 8.22, 6.87, 3.36, np.nan],
}

df = pd.DataFrame(data_dict)
df.head()
