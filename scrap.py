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
        headers = {
            'Content-Type': "application/json",
        }
        res = requests.post("http://127.0.0.1:9000/api/question/", data=json.dumps(data), headers=headers)
        print(res.status_code)

    print(questions)

def main():
    urls = [
        'https://www.indiabix.com/aptitude/problems-on-trains/',
        'https://www.indiabix.com/aptitude/profit-and-loss/',
        'https://www.indiabix.com/aptitude/calendar/'
    ]
    for url in urls:
        scrap(url)

if __name__ == "__main__":
    main()