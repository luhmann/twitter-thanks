import os

from TwitterSearch import *
import yaml


def load_config():
    config_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config')
    config_file = os.path.join(config_dir, 'config.yml')
    with open(config_file) as f:
        config = yaml.load(f)

    return config


try:
    config = load_config()
    tso = TwitterSearchOrder()
    tso.setKeywords(['#thankyou'])
    # tso.setLanguage('de')
    tso.setCount(10)
    tso.setGeocode(52.5085378, 13.4557724, 20000)
    tso.setIncludeEntities(False)

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key=config['api_key'],
        consumer_secret=config['api_secret'],
        access_token=config['access_token'],
        access_token_secret=config['access_token_secret']
    )

    for tweet in ts.searchTweetsIterable(tso):
        if tweet['coordinates']:
            print tweet['coordinates'], tweet['text']

except TwitterSearchException as e:
    print(e)
