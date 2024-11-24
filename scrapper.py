import subprocess
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# filename = 'gibran.csv'
search_keyword = '#KabinetMerahPutih since:2024-10-01 until:2024-11-24 lang:id'
limit = 1000
twitter_auth_token = os.getenv('TWITTER_AUTH_TOKEN')  # Get the token from .env

command = [
    'npx', '-y', 'tweet-harvest@2.6.1',
    # '-o', filename,
    '-s', search_keyword,
    '--tab', 'LATEST',
    '-l', str(limit),
    '--token', twitter_auth_token
]

subprocess.run(command)