# url =  " https://www.securitylab.ru/news/529102.php "
#
# article_id = url.split("/")[-1]
# article_id = article_id[:-4]
# print(article_id)
import json

with open("news_dict.json") as file:
    news_dict = json.load(file)

search_id = "529102123"

if search_id in news_dict:
    print("новина вже є в словнику пропускаємо ітерацію")
else:
    print("свіжа новина добавляємо в словник")