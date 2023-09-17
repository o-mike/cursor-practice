import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri

pandas2ri.activate()

# R script
r_script = """
library(datasets)
df <- mtcars
df$mpg <- df$mpg * 1.5
df
"""

# Execute the R script
r_df = robjects.r(r_script)

# Convert R dataframe to pandas dataframe
pandas_df = pandas2ri.rpy2py(r_df)
# Save pandas dataframe to csv
pandas_df.to_csv("output.csv", index=False)
