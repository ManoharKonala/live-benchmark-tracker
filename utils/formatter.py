import pandas as pd

def format_markdown_table(data):
    df = pd.DataFrame(data)
    return df.to_markdown(index=False)
