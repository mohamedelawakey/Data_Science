from bs4 import BeautifulSoup
import pandas as pd
import requests

def scrap():
  response = requests.get('https://wuzzuf.net/search/jobs/?q=Machine%20Learning%20&a=hpb')

  soup = BeautifulSoup(response.content, 'lxml')

  title = soup.find("h2", {'class':'css-m604qf'})
  titles = soup.find_all("h2", {'class':'css-m604qf'})
  title_list = [title.text for title in titles]
  links_list = [title.a['href'] for title in titles]

  occupations = soup.find_all('div', {'class':'css-1lh32fc'})
  occupation_list = [occupation.text[:9] + ' / ' + occupation.text[9:] for occupation in occupations]

  companies = soup.find_all('a', {'class':'css-17s97q8'})
  companies_list = [company.text.replace(' -', '') for company in companies]

  exp = soup.find_all('div', {'class' : 'css-y4udm8'})
  exp_list = [exps.text for exps in exp]

  screped_data = {}
  screped_data['Title'] = title_list
  screped_data['Links'] = links_list
  screped_data['Company'] = companies_list
  screped_data['Occupation'] = occupation_list
  screped_data['Experience'] = exp_list

  data = pd.DataFrame(screped_data)
  data.to_csv('wuzzuf_scraped.csv', index = False)
  print("Jobs Scraped Successfully")
  return data

if __name__ == '__main__':
    scrap()

