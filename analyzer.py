import os
import pprint
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

pd.set_option('display.max_columns', None)

print(*[x.split('.')[0] for x in os.listdir("opinions")], sep="\n") #<- list comprehension

product_id = input("Enter product ID: ")

opinions = pd.read_json(f"./opinions/{product_id}.json")

#opinions['stars']
#opinions.stars

opinions_count = opinions.shape[0]
pros_count = opinions.pros.map(bool).sum()
cons_count = opinions.cons.map(bool).sum()
avarage_score = opinions.stars.mean()


#print(opinions_count)
#print(pros_count)
#print(cons_count)
#print(avarage_score)


print(f"""There are {opinions_count} opinions in data set.
For {pros_count} opinions in list of advantages is avalible.
For {cons_count} opionis list of disadvanages is avalible.
Avarage score is {avarage_score:.1f}""")


recommendations = opinions.recommendation.value_counts(dropna=False).sort_index()
print(recommendations)

plt.figure(figsize=(7, 4))
recommendations.plot.pie(
    label = "",
    labels = ['Don\'t recommend', 'Recommend', 'No opinion'],
    colors = ['crimson', 'forestgreen', 'lightblue'],
    autopct = "%1.1f%%",
    pctdistance = 1.2,
    labeldistance = 1.4
)
plt.title("Share of recommendations in opinions")
plt.legend(bbox_to_anchor=(1.0,1.0))
plt.tight_layout()
plt.savefig(f"./figures/{product_id}_pie.png")
plt.close()

stars = opinions.stars.value_counts().reindex(np.arange(0, 5.5, 0.5), fill_value=0)
stars.plot.bar()
for index, value in enumerate(stars):
    plt.text(index, value+2, str(value), ha='center')

plt.xlabel("Rating")
plt.ylabel("Number of opinions")
plt.title("Frequency of ratings")
plt.savefig(f"./figures/{product_id}_bar.png")
#plt.show()
plt.close()
#print(type(opinions))
#print(type(opinions.stars))
stars_recommendations = pd.crosstab(opinions.stars, opinions.recommendations)
print(stars_recommendations)