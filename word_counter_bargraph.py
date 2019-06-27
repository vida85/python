import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import os
import collections


# upload a file from OS
os.chdir('C:\\Users\\vidas\\Onedrive\\Desktop')
filetxt = input('Enter text file to count: ')
with open(filetxt, 'r') as file:
    ff = file.read()
    filetext = ff.lower()

# create a list from every word in filetxt
filetext.strip()
lst = filetext.split()
#[print(words) for words in lst]

# create an empty set
ex = set(lst)

remove_words = ['to', 'my', 'dear', 'it', 'i', 'this', 'of', 'is', 'a', 'we', 'the', 'what', 'brethren,', 'for']
[lst.remove(word) for word in remove_words if word in lst]

# counts multiple same words appearance in filetxt and prints results
count = collections.Counter(lst)
keys = count.keys()
nums = count.values()
common = count.most_common()
# print(count.most_common(10))

value = []
c = 1
for v in nums:
    if c >= 15:
        break
    else:
        value = value + [v]
        c += 1

key = []
c = 1
for k in keys:
    if c >= 15:
        break
    else:
        key = key + [k]
        c += 1
print([f"{k}: {v}" for k, v in zip(key, value)])


# prints each word and it's word count
# [print(f'{words}:{nums}') for words, nums in count.items()]

# prints ex
# [print(words) for words in ex]


words_count = key
y_pos = np.arange(len(words_count))
performance = value

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, words_count)
plt.ylabel(f'Num of times words are repeated in {filetxt}')
plt.title(f'Words Used in {filetxt}')

plt.show()
