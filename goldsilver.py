from bs4 import BeautifulSoup as BS
import requests
def get_price(url):
    data = requests.get(url)
    soup = BS(data.text, 'html.parser')
    ans = soup.find("div", class_ = "BNeawe s3v9rd AP7Wnd").text
    return ans


url = "https://www.google.com / search?q = gold + price"
ans = get_price(url)
#printing the final output
print(ans)
