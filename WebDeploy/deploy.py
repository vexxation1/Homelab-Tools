from icecream import ic 
import configparser
import os

ic.configureOutput(prefix='DEBUG >> ')


def loadConfig(conf):
    config = configparser.ConfigParser()
    config.read(conf)

    BACKUP = config['PATHS']['BACKUP']
    DEPLOYMENT = config['PATHS']['DEPLOYMENT']
    #DEVELOPMENT = config['PATHS']['DEVELOPMENT']
    FILENAME =  config['MISC']['FILENAME']


def main():
    return 0



if __name__ == '__main__':
    main()