import urllib.request as req

while True:
    url = input('请输入URL:')

    response = req.urlopen(url)
    html = str(response.read())
    index = html.find('charset')
    decode = ''

    

    for each in html[index+8:]:
        if (not each.isdigit()) and (not each.isalpha()):
            index += 1
        else:
            break
        
    for each in html[index+8:]:    
        if each in ('"',';',' '):
            break
        decode += each

    print(decode)
