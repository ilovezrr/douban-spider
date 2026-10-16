import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/movies.csv")

# 1. 评分分布直方图
df["rating"].plot(kind="hist", bins=20, title="豆瓣 Top250 评分分布")
plt.xlabel("评分")
plt.savefig("data/rating_dist.png", dpi=150, bbox_inches="tight")

# 2. 年份 Top 10
print(df["year"].value_counts().head(10))

# 3. 平均评分 / 最高最低
print(f"平均分: {df['rating'].mean():.2f}")
print(f"最高: {df.loc[df['rating'].idxmax(), 'title']}")