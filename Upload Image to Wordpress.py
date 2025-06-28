from requests import post
import base64

api_endpoints = 'https://carcareia.com/wp-json/wp/v2/media'
wp_user = 'carcareia11'
wp_pass = '9cfK Yh4y 6tm7 6tse fAON jlc7'
wp_credential = f'{wp_user}:{wp_pass}'
token = base64.b64encode(wp_credential.encode('utf-8'))
headers = {
    'Authorization': f'Basic {token.decode()}',
    'User-Agent': 'Firefox/5.0'
}

file = open('SkysCars.jpg', 'rb')
media = {'file': file}
res = post(api_endpoints, headers= headers, files= media)
file.close()

print(res.status_code)