from textblob import TextBlob
import sys,tweepy
import matplotlib.pyplot as plt
def percentage(part,whole):
    return 100*float(part)/float(whole)
    #establish connection with api
consumer_key="3uycRKy1FFi9pnvpOOMa7Tdm0"
consumer_secret="xpMp1344JM5RgK7F4iuaUbGOyCbtvYYCgAfPBvsrMB12wPcuPj"
access_token="1009149878734241792cpV7sYZrcoyqUKAcQLwUFASjAbX5Ny"
access_token_secret="qnLZJSU2Ohj434x1SfCPMZGGxYO82u3JwihMmABQClubH"
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
search_term=input("enter keyword/hastag to search about:")
no_of_search_term=int(input("enter how many tweets to analyse:"))
tweets=tweepy.curor(api.search,q=search_term,lang='English').items(no_of_search_term)
positive=0
negative=0
neutral=0
polarity=0
for tweet in tweets:
    print(tweets.text)
    analysis=TextBlob(tweets.text)
    polarity +=analysis.sentiment.polarity
    if analysis.sentiment.polarity==0.00:
        neutral+=1
    elif analysis.sentiment.polarity<0.00:
        negative+=1
    elif analysis.sentiment.polarity>0.00:
        positive+=1
        positive=percentage(positive,no_of_search_term)
negative=percentage(negative,no_of_search_term)
neutral=percentage(neutral,no_of_search_term)
polarity=percentage(polarity,no_of_search_term)
positive=format(positive,'.2f')
negative=format(negative,'.2f')
neutral=format(neutral,'.2f')
polarity=format(poarity,'.2f')
print('how people reacting on '+search_term+'by analysising' +str(no_of_search_term)+'tweets.')
if polarity==0.00:
    print('neutral')
elif polarity<0.00:
    print('negative')
elif polarity>0.00:
    print('positive')
    labels=['positive['+str(positive)+'%]','neutral['+str(neutral)+'%]','negative['+str(negative)+'%]']
    size=[positive,negative,neutral]
    colors=['green','red','blue']
    patches,text=plt.pie(size,colors=colors,startangle=90)
    plt.title('how people reacting on '+search_term+'by analysising' +str(no_of_search_term)+'tweets.')
    plt.axis('equal')
plt.tightlayout()
plt.show()