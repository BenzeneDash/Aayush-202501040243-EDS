# 📊 Twitter US Airline Sentiment Analysis
# Author: Aayush Rajput

import pandas as pd
import numpy as np


# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv("Tweets.csv")
df['tweet_created'] = pd.to_datetime(df['tweet_created'], errors='coerce')

print("\n================ DATA LOADED ================\n")
print(df.head())


# -----------------------------
# 1. SENTIMENT DISTRIBUTION
# -----------------------------
print("\n1️ Sentiment Distribution")
print(df['airline_sentiment'].value_counts())


# -----------------------------
# 2. MOST NEGATIVE AIRLINE
# -----------------------------
print("\n2️ Airline with Highest Negative Sentiment")
neg = df[df['airline_sentiment'] == 'negative'].groupby('airline').size()
print(neg.idxmax())


# -----------------------------
# 3. MOST POSITIVE AIRLINE
# -----------------------------
print("\n3️ Airline with Highest Positive Sentiment")
pos = df[df['airline_sentiment'] == 'positive'].groupby('airline').size()
print(pos.idxmax())


# -----------------------------
# 4. SENTIMENT PERCENTAGE
# -----------------------------
print("\n4️ Sentiment Percentage")
print(df['airline_sentiment'].value_counts(normalize=True) * 100)


# -----------------------------
# 5. SENTIMENT TREND OVER TIME
# -----------------------------
print("\n5️ Sentiment Trend (Sample)")
trend = df.groupby(df['tweet_created'].dt.date)['airline_sentiment'].value_counts()
print(trend.head(10))


# -----------------------------
# 6. MOST COMMON NEGATIVE REASON
# -----------------------------
print("\n6️ Most Common Negative Reason")
print(df['negativereason'].value_counts().idxmax())


# -----------------------------
# 7. DELAY COMPLAINT AIRLINE
# -----------------------------
print("\n7️ Airline with Most Delay Complaints")
delay = df[df['negativereason'] == 'Late Flight'].groupby('airline').size()

if not delay.empty:
    print(delay.idxmax())
else:
    print("No data")


# -----------------------------
# 8. SENTIMENT PER AIRLINE
# -----------------------------
print("\n8️ Sentiment per Airline")
print(df.groupby('airline')['airline_sentiment'].value_counts())


# -----------------------------
# 9. CONFIDENCE SCORE
# -----------------------------
print("\n9️ Average Sentiment Confidence")
print(df.groupby('airline')['airline_sentiment_confidence'].mean())


# -----------------------------
# 10. LOW CONFIDENCE TWEETS
# -----------------------------
print("\n 10 Low Confidence Tweets")
print(df[df['airline_sentiment_confidence'] < 0.5].head())


# -----------------------------
# 11. PEAK HOUR
# -----------------------------
df['hour'] = df['tweet_created'].dt.hour
print("\n11 Peak Tweet Hour")
print(df['hour'].value_counts().idxmax())


# -----------------------------
# 12. TIMEZONE ANALYSIS
# -----------------------------
print("\n1️2️ Top Timezones")
print(df['user_timezone'].value_counts().head())


# -----------------------------
# 13. WORD COUNT ANALYSIS
# -----------------------------
df['word_count'] = df['text'].astype(str).apply(lambda x: len(x.split()))
print("\n1️3️ Average Word Count")
print(np.mean(df['word_count']))


# -----------------------------
# 14. LONGEST TWEETS
# -----------------------------
print("\n1️4️ Longest Tweets")
print(df.sort_values(by='word_count', ascending=False).head())


# -----------------------------
# 15. WORD COUNT VS SENTIMENT
# -----------------------------
print("\n1️5️ Word Count vs Sentiment")
print(df.groupby('airline_sentiment')['word_count'].mean())


# -----------------------------
# 16. HIGHLY NEGATIVE TWEETS
# -----------------------------
print("\n1️6️ Highly Negative Tweets")
print(df[(df['airline_sentiment'] == 'negative') &
         (df['airline_sentiment_confidence'] > 0.9)].head())


# -----------------------------
# 17. PIVOT TABLE
# -----------------------------
print("\n1️7️ Pivot Table")
pivot = pd.pivot_table(df,
                       values='tweet_id',
                       index='airline',
                       columns='airline_sentiment',
                       aggfunc='count')
print(pivot)


# -----------------------------
# 18. DUPLICATES
# -----------------------------
print("\n1️8️ Duplicate Tweets")
print(df[df.duplicated(subset='text')].head())


# -----------------------------
# 19. AIRLINE RANKING
# -----------------------------
print("\n1️9️ Airline Ranking (Positive Sentiment)")
rank = df[df['airline_sentiment'] == 'positive'].groupby('airline').size().rank(ascending=False)
print(rank)


# -----------------------------
# 20. FILTERED DATA
# -----------------------------
print("\n2️0️ United Negative Tweets")
print(df[(df['airline'] == 'United') &
         (df['airline_sentiment'] == 'negative')].head())
