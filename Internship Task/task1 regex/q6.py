"""
Clean the following text. After cleaning, count three most
frequent words in the string.
 sentence = %I $am@% a %tea@cher%, &amp;and&amp; I
lo%#ve %tea@ching%;. There $is nothing; &amp;as&amp; mo@re
rewarding as educa@ting &amp;and&amp; @emp%o@wering
peo@ple. ;I found tea@ching m%o@re interesting
tha@n any other %jo@bs. %Do@es thi%s mo@tivate
yo@u to be a tea@cher!?

print(clean_text(sentence)); I am a teacher and I love teaching
There is nothing as more rewarding as educating and
empowering people I found teaching more interesting than any
other jobs Does this motivate you to be a teacher
print(most_frequent_words(cleaned_text)) # [(3,I), (2,teaching), (2,teacher)]
"""
import re
def clean_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text
sentence='''%I $am@% a %tea@cher%, and I
            lo%#ve %tea@ching%;. There $is nothing; &amp;as&amp; mo@re
            rewarding as educa@ting and @emp%o@wering
            peo@ple. ;I found tea@ching m%o@re interesting
            tha@n any other %jo@bs. %Do@es thi%s mo@tivate
            yo@u to be a tea@cher!?
        '''
def most_frequent_words():
    d = {}
    for i in clean_text(sentence).split():
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    a=sorted(d.items(), key=lambda item: item[1], reverse=True)
    return a[:3]

print(most_frequent_words())

