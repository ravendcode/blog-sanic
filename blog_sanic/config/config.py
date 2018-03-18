import argparse
import os
from dotenv import load_dotenv

load_dotenv()

parser = argparse.ArgumentParser(description='App config')
parser.add_argument('-env', type=str, default=os.getenv('ENV', 'production'),
                    help='server environment')
parser.add_argument('-port', type=int, default=os.getenv('PORT', 80),
                    help='server listening port')

args = parser.parse_args()

ENV = args.env
PORT = args.port
DEBUG = ENV != 'production'
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STATIC_DIR = os.path.join(BASE_DIR, 'static')
NODE_MODULES_DIR = os.path.join(BASE_DIR, 'node_modules')

print('ENV is {}'.format(ENV))
