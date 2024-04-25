class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        word_list = [word for word in re.sub(r"[^\\w]", " ", paragraph).split() if word]
        word_dict = dict()

        for word in word_list:
            if word in banned:
                continue

            if word in word_dict:
                word_dict[word] += 1

            else:
                word_dict[word] = 1

        most_word = sorted(word_dict.items(), key = lambda x : x[1], reverse = True)

        return most_word[0][0]