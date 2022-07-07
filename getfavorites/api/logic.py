from rest_framework_simplejwt.tokens import AccessToken, TokenError
import requests
import json


def get_comics_id():
    url = 'http://172.17.0.2:8000/searchComics/comics/'
    resp = requests.get(url)
    comics = resp.content
    comics = json.loads(comics.decode('utf-8'))
    comicdata = comics[0]
    comicdata = comicdata[1]
    comics_id = []
    for result in comicdata:
        dict1 = {}
        dict1['id'] = result['id']
        comics_id.append(dict1)
    return comics_id


def get_user_token(authdata):
    resp = requests.post(
        'http://172.17.0.3:8000/users/authentication/', authdata)
    token = resp.content
    token = json.loads(token.decode('utf-8'))
    token = token['access']
    try:
        access_token = AccessToken(token)
        print(access_token)
    except(TokenError):
        raise('Token not valid')

    return access_token


def get_comics(secrets, comic_id):
    url = 'https://gateway.marvel.com:443/v1/public/comics/' + \
        str(comic_id) + secrets
    resp = requests.get(url)
    comics = resp.content
    comics = json.loads(comics.decode('utf-8'))
    comicdata = comics['data']
    comicresults = comicdata['results']
    comics = []
    for result in comicresults:
        dict1 = {}
        dict1['id'] = result['id']
        dict1['title'] = result['title']
        comicimages = result['thumbnail']
        dict1['image'] = comicimages['path'] + '.' + comicimages['extension']
        comicdates = result['dates']
        for comicdat in comicdates:
            if comicdat['type'] == 'onsaleDate':
                dict1['onsaledate'] = comicdat['date']
        comiccharacters = result['characters']
        characters = comiccharacters['items']
        for character in characters:
            dict1['characters'] = character['name']
        comics.append(dict1)
    return comics


secrets = "?ts=1&apikey=7fc9910ea80c6222e9053658f3d21f54&hash=4aeb4b73dc0c3b8b387dba00dce092c5"
authdata = {'username': 'anibal', 'password': 'perro123'}

comic_id = 1308
access_token = get_user_token(authdata)
comics_id = get_comics_id()
comics = get_comics(secrets, comic_id)
