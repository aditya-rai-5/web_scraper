import pandas as pd
import os

# Create required CSV files
data_dir = "schedular/data"
os.makedirs(data_dir, exist_ok=True)

# urls.csv with the provided URL
urls_csv_path = os.path.join(data_dir, "urls.csv")
urls_df = pd.DataFrame({"url": ["https://www.iiti.ac.in"]})
urls_df.to_csv(urls_csv_path, index=False)

# output_data.csv with headers only
output_data_path = "schedular/output_data.csv"
output_df = pd.DataFrame(columns=[
    "row_id", "url", "title", "keywords", "description", "body_text", "error", "status"
])
output_df.to_csv(output_data_path, index=False)

# final_integrated_data.csv with headers only
final_data_path = "schedular/final_integrated_data.csv"
final_df = pd.DataFrame(columns=["filename", "content", "source"])
final_df.to_csv(final_data_path, index=False)

# Return file paths
urls_csv_path, output_data_path, final_data_path
