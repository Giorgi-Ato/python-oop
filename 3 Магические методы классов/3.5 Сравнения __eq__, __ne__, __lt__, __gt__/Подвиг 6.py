class Morph:
    def __init__(self, *args):
        self.txt = list(map(lambda x: x.strip('.,?!').lower(), args))

    def add_word(self, word):
        if word not in self.txt:
            self.txt.append(word)

    def get_words(self):
        return tuple(self.txt)

    def __eq__(self, other):
        return other.lower() in self.txt

dict_words = [Morph('связь', 'связи', 'связью', 'связи', 'связей', 'связям', 'связями', 'связях'),
                  Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами',
                        'формулах'),
                  Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам',
                        'векторами', 'векторах'
                        ),
                  Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам',
                        'эффектами', 'эффектах'
                        ), Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях'
                                 )]

text = input().lower().strip('.')
text = [i for i in text.split()]
cnt = 0
for i in text:
    for j in dict_words:
        if i == j:
            cnt += 1

print(cnt)
