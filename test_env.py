# test_env.py
from decouple import config

def test_env_vars():
    print("TWITTER_API_KEY:", config('TWITTER_API_KEY'))
    print("TWITTER_API_SECRET_KEY:", config('TWITTER_API_SECRET_KEY'))
    print("TWITTER_ACCESS_TOKEN:", config('TWITTER_ACCESS_TOKEN'))
    print("TWITTER_ACCESS_TOKEN_SECRET:", config('TWITTER_ACCESS_TOKEN_SECRET'))

if __name__ == "__main__":
    test_env_vars()