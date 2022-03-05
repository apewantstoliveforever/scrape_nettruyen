import pandas as pd
import numpy as np
import math
from matplotlib.ticker import FuncFormatter

import matplotlib.pyplot as plt
file = pd.read_csv (r'a - a (1).csv', encoding="utf8")
df = pd.DataFrame(file, columns= ["title","chapternumber","eyes","comment","heart","kind",'k2','k3','k4','k5','k6','k7','k8','k9','k10','k11','k12','k13','k14','k15','k16'])
print (df)

allkind = ['Action', 'Fantasy', 'Manhua', 'Shounen', 'Supernatural', 'Adventure', 'Mystery', 'Martial Arts', 'Drama', 'Ngôn Tình', 'Romance', 'Shoujo', 'Comedy', 'Historical', 'Chuyển Sinh', 'Xuyên Không', 'Manga', 'School Life', 'Trinh Thám', 'Smut', 'Harem', 'Webtoon', 'Cổ Đại', 'Manhwa', 'Shounen Ai', 'Soft Yaoi', 'Seinen', 'Horror', 'Comic', 'Tạp chí truyện tranh', 'Adult', 'Thiếu Nhi', 'Psychological', 'Sports', 'Mature', 'Đam Mỹ', 'Ecchi', 'Tragedy', 'Cooking', 'Doujinshi', 'Slice of Life', 'One shot', '16+', 'Anime', 'Josei', 'Soft Yuri', 'Sci-fi', 'Gender Bender', 'Shoujo Ai', 'Live action', 'Yuri', 'Truyện scan', 'Việt Nam', 'Yaoi', 'Mecha']
sum_eyes = []
sum_comments = []
sum_hearts = []
for i in allkind:
    t = df[df["kind"]==i].sum(numeric_only= True)["eyes"]
    t1 = 0
    for j in range(2,17):
        t2 = df[df[f"k{j}"] == i].sum(numeric_only=True)["eyes"]
        t1 += t2
    t += t1
    sum_eyes.append(round(t))

for i in allkind:
    t = df[df["kind"]==i].sum(numeric_only= True)["comment"]
    t1 = 0
    for j in range(2,17):
        t2 = df[df[f"k{j}"] == i].sum(numeric_only=True)["comment"]
        t1 += t2
    t += t1
    sum_comments.append(round(t))

for i in allkind:
    t = df[df["kind"]==i].sum(numeric_only= True)["heart"]
    t1 = 0
    for j in range(2,17):
        t2 = df[df[f"k{j}"] == i].sum(numeric_only=True)["heart"]
        t1 += t2
    t += t1
    sum_hearts.append(round(t))

d1 = pd.DataFrame({'kind':allkind, 'eyes':sum_eyes})
d2 = pd.DataFrame({'kind':allkind, 'comment':sum_comments})
d3 = pd.DataFrame({'kind':allkind, 'heart':sum_hearts})

def millions_formatter(x, pos):
    return f'{x / 1000000}'

labels = allkind
ax = d1.plot.bar(x='kind', y='eyes', rot=0)
ax.yaxis.set_major_formatter(FuncFormatter(millions_formatter))
ax.set_ylabel('read (in millions)')
plt.title('Number of reads')
plt.xticks(ticks=range(len(allkind)), labels=labels, rotation=90)

labels = allkind
bx = d2.plot.bar(x='kind', y='comment', rot=0)
bx.yaxis.set_major_formatter(FuncFormatter(millions_formatter))
bx.set_ylabel('comments (in millions)')
plt.title('Number of comments')
plt.xticks(ticks=range(len(allkind)), labels=labels, rotation=90)

labels = allkind
cx = d3.plot.bar(x='kind', y='heart', rot=0)
cx.yaxis.set_major_formatter(FuncFormatter(millions_formatter))
cx.set_ylabel('likes (in millions)')
plt.xticks(ticks=range(len(allkind)), labels=labels, rotation=90)
plt.title('Number of likes')

plt.show()