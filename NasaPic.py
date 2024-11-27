
import requests
from PIL import Image
from io import BytesIO
#Key
api_key = "rxftxUweV1AsYTBoh0RTQ4gIH7iOcAUQCy8XZgsc"
rover = "curiosity" #Changeable to Spirit or Opportunity rovers
sol = 1000  #Martian sol (day), changeable to any day

#API endpoint
url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/photos?sol={sol}&api_key={api_key}"

#Send GET request
response = requests.get(url)

#Process the response
if response.ok:
    photos = response.json()["photos"]
    print(f"Found {len(photos)} photos for sol {sol} from {rover.capitalize()} rover.")
    for photo in photos[:5]:  # Print details of the first 5 photos, changeable to first x photos or last x photos
        print("ID:", photo["id"])
        print("Camera:", photo["camera"]["full_name"])
        print("Image URL:", photo["img_src"])
        my_url = photo["img_src"]
        my_req = requests.get(my_url)
        my_img = Image.open(BytesIO(my_req.content))
        my_img.show()

else:
    print(f"Failed to fetch data. Status code: {response.status_code}")

