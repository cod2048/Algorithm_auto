class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        word_dict = dict()
        new_paragraph = ""

        for letter in paragraph:
            if letter == " ":
                new_paragraph += letter
            if letter.isalnum() == False:
                new_paragraph += " "
            else:
                new_paragraph += letter
        
        word_list = [word for word in new_paragraph.split() if word]

        for word in word_list:
            if word in banned:
                continue

            if word in word_dict:
                word_dict[word] += 1

            else:
                word_dict[word] = 1

        most_word = sorted(word_dict.items(), key = lambda x : x[1], reverse = True)

        return most_word[0][0]
