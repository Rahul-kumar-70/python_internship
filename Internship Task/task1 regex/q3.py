"""
Q3. What is the most frequent word in the following paragraph?
paragraph=
'I love teaching. If you do not love teaching what else
can you love. I love Python if you do not love something which can
give you all the capabilities to develop an application what else can
you love'.
sy[(6, love),(5,you),(3,can),(2,what),(2,teaching),(2,not),(2,else),(2,do),(2,I),(1,which),(1,to),(1, the),(1,something),
(1, if),(1,give),(1,develop),(1,capabilities),(1,application),(1,an),(1,all),(1,Python),(1,If)]

"""
import re
def most_frequent(paragraph):
    pattern = r'\w+'
    match = re.findall(pattern, paragraph)
    d = {}
    for i in match:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return sorted(d.items(), key=lambda item: item[1], reverse=True)
paragraph = '''I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can
                  give you all the capabilities to develop an application what else can you love'''
print(most_frequent(paragraph))