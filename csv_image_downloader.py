import os
import pandas as pd
import requests


folder_path = 'E:\\images2'  

# Create the folder if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Load the CSV file
csv_filename = 'flipkartcompleteduplicate.csv.csv'  
df = pd.read_csv(csv_filename)

# Extract image URLs from the CSV
image_urls = df['Image URL'] 

# Download images
for index, image_url in enumerate(image_urls, start=1):
    if pd.notna(image_url):  # Check for NaN values
        response = requests.get(str(image_url))  # Convert to string to handle NaN
        if response.status_code == 200:
            image_filename = os.path.join(folder_path, f"image_{index}.jpg")
            with open(image_filename, 'wb') as f:
                f.write(response.content)
            print(f"Image {index} downloaded: {image_filename}")
        else:
            print(f"Failed to download image {index} from URL: {image_url}")
    else:
        print(f"Skipping invalid URL at index {index}")

