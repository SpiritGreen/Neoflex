"""
Извлеките доменное имя из URL-адреса

Необходимо написать функцию, которая при задании URL адреса в виде строки анализирует
только доменное имя и возвращает его в виде строки.

Пример вывода функции:

url = "http://github.com/carbonfive/raygun" -> domain name = "github"

url = "http://www.zombie-bites.com" -> domain name = "zombie-bites"

url = "https://www.cnet.com" -> domain name = cnet
"""


def extract_domain_from_url(url):
    # removing unnecessary spaces at the beginning and end in url:
    url = url.strip()

    # clearing the beginning of url:
    if url.startswith('http://'):
        result = url[7:]
    elif url.startswith('https://'):
        result = url[8:]
    else:
        result = url
    if result.startswith('www.'):
        result = result[4:]

    # clearing the end of the url:
    dot_id = result.find('.')
    result = result[:dot_id]
    return result


url1 = 'http://github.com/carbonfive/raygun'
url2 = 'http://www.zombie-bites.com'
url3 = 'https://www.cnet.com'
url4 = 'github.com/carbonfive/raygun'
url5 = 'www.cnet.com'

print(extract_domain_from_url(url1))
print(extract_domain_from_url(url2))
print(extract_domain_from_url(url3))
print(extract_domain_from_url(url4))
print(extract_domain_from_url(url5))
