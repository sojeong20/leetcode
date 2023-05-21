class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = [word for word in re.sub('[^\w]', ' ', paragraph).lower().split() if word not in banned]

        counts = collections.Counter(paragraph)

        return counts.most_common(1)[0][0]