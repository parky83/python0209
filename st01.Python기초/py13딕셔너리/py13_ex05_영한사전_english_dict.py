english_dictionary = dict()

english_dictionary["one"] = "하나"
english_dictionary["two"] = "둘"
english_dictionary["three"] = "셋"
english_dictionary["four"] = "넷"
english_dictionary["five"] = "다섯"
english_dictionary["six"] = "여섯"
english_dictionary["seven"] = "일곱"
english_dictionary["eight"] = "여덟"
english_dictionary["nine"] = "아홉"
english_dictionary["ten"] = "열"

word = input("단어를 입력하시오: ")
print(english_dictionary.get(word, "없음"))
