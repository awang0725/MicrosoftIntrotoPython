# import os

# os_version = os.getenv('OS')
# print(os_version)

from dotenv import load_dotenv

load_dotenv()
import os

password = os.getenv('PASSWORD')

print(password)