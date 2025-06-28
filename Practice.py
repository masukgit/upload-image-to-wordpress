from requests import post
import base64

api_endpoints = 'https://carcareia.com/wp-json/wp/v2/posts'
wp_user = 'carcareia11'
wp_pass = '9cfK Yh4y 6tm7 6tse fAON jlc7'
wp_credential = f'{wp_user}:{wp_pass}'
token = base64.b64encode(wp_credential.encode('utf-8'))
headers = {
    'Authorization': f'Basic {token.decode()}',
    'User-Agent': 'Firefox/5.0'
}

content = '<!-- wp:paragraph --><p>Mr. Younus is rejected to meet by Mr. Kiar Starmar, the prime minister of the people republic of England</p><!-- /wp:paragraph -->'
data = {
    'title': 'Kiar Starmar is the player',
    'slug': 'kiar-starmar-the-player',
    'content': content,
    'status': 'draft',
    'featured_media': '4059'
}

res = post(api_endpoints, headers= headers, data= data)