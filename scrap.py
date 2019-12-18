import requests
from bs4 import BeautifulSoup
import json


def scrap(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # content = soup.find(class_="entry-content")
    paragraphs = soup.find_all(class_="bix-div-container")
    questions = []
    _options = ['A', 'B', 'C', 'D', 'E', 'F']
    for paragraph in paragraphs:
        question = paragraph.find(class_='bix-td-qtxt').find('p').text
        # print(paragraph.prettify())

        options = paragraph.find_all(class_='bix-td-option', width='99%')
        options = [option.text for option in options]
        answer = paragraph.find(class_='jq-hdnakqb').text
        answers = [False]*len(options)
        idx = _options.index(answer)
        answers[idx] = True
        options = dict(zip(options, answers))
        explanation = paragraph.find(class_="bix-ans-description")
        # questions.append({
        #     "question": question,
        #     "options": options,
        #     "explanation": explanation
        # })
        data = {
            "question": question,
            "options": options,
            "explanation": str(explanation)
        }
        imgs = explanation.find_all('img')
        for image in imgs:
            download_file('https://indiabix.com{}'.format(image['src']))
        # headers = {
        #     'Content-Type': "application/json",
        # }
        # res = requests.post("http://127.0.0.1:9000/api/question/", data=json.dumps(data), headers=headers)
        # print(res.status_code)


def main():
    urls = [
        'https://www.indiabix.com/aptitude/problems-on-trains/',
        # 'https://www.indiabix.com/aptitude/profit-and-loss/',
        # 'https://www.indiabix.com/aptitude/calendar/'
    ]
    for url in urls:
        scrap(url)

def download_file(url):
    print(url)
    local_filename = url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
                    # f.flush()
    return local_filename

if __name__ == "__main__":
    main()