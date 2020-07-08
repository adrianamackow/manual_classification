from bs4 import BeautifulSoup
import json
import os


path_to_html_directory = "C:\\Users\\mackow\\PycharmProjects\\mgr\\komentarze\\html"
html_files = [html for html in os.listdir(path_to_html_directory) if html.endswith(".html")]
print(html_files)
path_to_json_directory = "C:\\Users\\mackow\\PycharmProjects\\mgr\\komentarze\\json_files"


def get_number_of_files():
    return len(os.listdir(path_to_json_directory))

j=0


for file in html_files:
    print("new file")
    path_to_html_file = path_to_html_directory + '\\' + file
    soup = BeautifulSoup(open(path_to_html_file), "html.parser")
    all = soup.find_all('div', {'class': "cBody"})
    plusvotes = soup.find_all('span', {'itemprop': "upvoteCount"})
    minusvotes = soup.find_all('span', {'itemprop': "downvoteCount"})
    assert len(all) == len(plusvotes) == len(minusvotes)
    global_dict = {}
    add_to_idx = get_number_of_files()

    for i in range(len(all)):
        comment = all[i].text
        comment = comment.replace("±", "ą")
        comment = comment.replace("¶", "ś")
        comment = comment.replace("¦", "ś")
        comment = comment.replace("ľ", "ż")
        comment = comment.replace("Ľ", "ź")
        comment = comment.replace("ˇ", "Ą")
        comment = comment.replace("np.", "np")
        comment = comment.replace("m.in", "m in")
        comment = comment.replace("sw.", "sw")
        comment = comment.replace("św.", "św")
        comment = comment.replace("d.", "d")
        comment = comment.replace("etc.", "etc")
        comment = comment.replace("tzw.", "tzw")
        comment = comment.replace("ps.", "ps")
        comment = comment.replace("PS.", "PS")
        comment = comment.replace("tj.", "tj")
        comment = comment.replace("1.", "1")
        comment = comment.replace("2.", "2")
        comment = comment.replace("3.", "3")
        comment = comment.replace("4.", "4")
        comment = comment.replace("5.", "5")
        comment = comment.replace("6.", "6")
        comment = comment.replace("7.", "7")
        comment = comment.replace("8.", "8")
        comment = comment.replace("9.", "9")
        comment = comment.replace("0.", "0")
        comment = comment.replace("q.", "q")
        comment = comment.replace("k.", "k")


        temp = {}
        list_1 = [x for x in comment.split(".") if x != ""]
        if len(list_1) > 1:
            for c in list_1:
                if len(c) > 0:
                    j += 1
                    temp.update({
                    "komentarz": c,
                    "tak": plusvotes[i].text,
                    "nie": minusvotes[i].text
                    })
                    global_dict.update(temp)
                    with open(path_to_json_directory + "\\{}.json".format(get_number_of_files()+1), "w", encoding='utf8') as f:
                        json.dump(temp, f, ensure_ascii=False)

        else:
            if len(comment) > 0:
                j += 1
                temp.update({
                    "komentarz": comment,
                    "tak": plusvotes[i].text,
                    "nie": minusvotes[i].text
                })
                global_dict.update(temp)
                with open(path_to_json_directory + "\\{}.json".format(get_number_of_files()+1), "w", encoding='utf8') as f:
                    json.dump(temp, f, ensure_ascii=False)


