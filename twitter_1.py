from textblob import TextBlob 
import sys, tweepy
import matplotlib.pyplot as plt 


def percentage(part,whole):
	return 100*float(part)/float(whole)


#we are extracting here keys and tokens from twitter.
consumerKey="xxxxxxxxxxx"
consumerSecret="xxxxxxxxxxx"
accessToken="xxxxxxxxxxx"
accessTokenSecret="xxxxxxxxxxx"

#attempting authentication
auth= tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api=tweepy.API(auth)

#taking inputs
searchTerm=input("Enter topic you want to sarch:")
noOfSearchTerms=int(input("Enter how many tweets to analyze:"))

tweets= tweepy.Cursor(api.search, q=searchTerm, lang="English").items(noOfSearchTerms)
 
positive=0
negative=0
neutral=0
polarity=0

for tweet in tweets:
	print(tweet.text)
	analysis= TextBlob(tweet.text)
	polarity += analysis.sentiment.polarity

	if(analysis.sentiment.polarity==0):
		neutral+=1
	elif(analysis.sentiment.polarity<0.00):
		negative+=1
	elif(analysis.sentiment.polarity>0.00):
		positive+=1
#calculating the percentage
positive= percentage(positive, noOfSearchTerms)
negative= percentage(negative, noOfSearchTerms)
negative= percentage(neutral, noOfSearchTerms)


positive= format(positive, '.2f')
negative= format(negative, '.2f')
neutral= format(neutral, '.2f')
#printing our result
print("How people are reacting "+ searchTerm+ "by analyzing "+ str(noOfSearchTerms)+"Tweets")

if(polarity==0):
	print("Neutral")
elif(polarity<0):
	print("Negative")
elif(polarity>0):
	print("positive")

#printing pichart
labels=['Positive ['+str(positive)+'%]', 'Neutral ['+str(neutral)+'%]', 'Negative ['+str(negative)'%]']
sizes=[positive,neutral,negative]
colors= ['blue','gold','red']
patches, texts=plt.pie(sizes, colors=colors, startangle=90)
plt.legend(Patches, labels, loc="best")
plt.title('How people are reacting '+ searchTerm+ 'by analyzing '+ str(noOfSearchTerms)+'Tweets.')
plt.axis('equal')
plt.tight_layout()
plt.show()