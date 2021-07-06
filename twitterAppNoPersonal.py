#for this program to run you will need the following programs installed
#install by using pip. install x
#tweepy
#twitter
#numpy
#pandas
#matplotlib

#imports StreamListener for getting live tweets
from tweepy.streaming import StreamListener
#allows user to verify details that allow them to user twitter api
from tweepy import OAuthHandler
#imports stream for getting live tweets
from tweepy import Stream
#imports twitter
#import twitter
#imports tweepy for allowing users 
import tweepy
#imports numpy as np allows mathermatical calculations0
import numpy as np
#imports pandas as pd allows for data manipulation
import pandas as pd
#imports random
import random
#imports matplotlib allows for visulising data 
import matplotlib.pyplot as plt
#import
from tkinter import *
#from tkinter import ttk


#access keys and tokens for accessing twitter must have a twitter account to use the program
#removed from public file
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""


#sets consumer code so they can be used in the program
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
#api is accessed through this
api = tweepy.API(auth)



#creates a function called textSearch this function is used for searching for specific words in certain peoples timeline
def textSearch():
    #sets found to false
    found = False
    #creates a list called tweets
    tweets = []
    #asks user what twitter account they want to search for
    user = input("What user would you like to search for?")
    #run this for 1 times
    for x in range(1):
        #attempted to do this code if that does work print "account not found"
        try:
            #for every tweet in specifyed userstimes line add to the list tweets
            #count is set to 1000 tweets api only allows a certain number so 1000 reaches the maximum
            #tweet_mode is "extended" as when the code was made the max tweet was 140characters now the max is 240 so needed to manually update it
            for tweet in api.user_timeline(screen_name = user,count = 1000,tweet_mode = "extended"):
                #puts all the text from the tweet into the list. encodes and decodes to stop emojis creating errors
                tweets.append(tweet.full_text.encode('unicode-escape').decode('UTF-8'))
            #asks user what word they want to seatch for    
            search = input("What word would you like to search for?")
            #run for length of list
            for x in range(len(tweets)):
                
                #if the word the user searched for is in the list print found and the tweet and set found to true
                if search in tweets[x]:
                    print("found")
                    print(tweets[x])
                    found = True
            #if the word is not then found will remain false so print "not found"
            if found != True:
                print("Not Found")
        #tweepy error will apear if account doesnt exist so print account doesnt exist
        except:
            print("account doesnt exist")




#this function allows the user to search for key words that were tweeted from aberdeen
def aberdeenTweets():
    #asks user what word they want to search for
    ask = input("Enter what word or phrase would you like to search for in Aberdeen:")
    #creates a list called tweets
    tweets = []
    #run this for 1 times
    for x in range(1):
        #attempted to do this code if that does work print "Error"
        try:
            #api searches for any tweet that contains the word that is english and was tweeted from aberdeen with a range of 5km 
            for tweet in api.search(q = ask,count = 1000,lang = "en",geocode="57.15116,-2.13902,5km"):
                #puts all the text from the tweet into the list. encodes and decodes to stop emojis creating errors 
                tweets.append(tweet.text.encode('unicode-escape').decode('UTF-8'))
            #run for length of list
            for x in range(len(tweets)):
                #if the word the user entered is in the list print the tweet with "tweeted in aberdeen"
                if ask in tweets[x]:
                    
                    print(tweets[x])
                    print("Tweeted in Aberdeen")
            #if the word is not then found will remain false so print "not found"
            if len(tweets) == 0:
                print("no results found")
        #error message
        except:
            print("Error")




#function for showing user timeline            
def ShowUserTimeline():
    #asks user what twitter account they want to search for
    ask = input("Enter what users timeline you want to view:")
    #runs 1 time
    for x in range(1):
        #will run if no errors and if errors prints cant find error
        try:
            #for every tweet in specifyed userstimes line add to the list tweets
            #count is set to 1000 tweets api only allows a certain number so 1000 reaches the maximum 
            for tweet in api.user_timeline(screen_name = ask,count = 1000,tweet_mode = "extended"):
                print(tweet.created_at,tweet.full_text.encode('unicode-escape').decode('UTF-8'))
        #error for no account so print"could not find user"
        except:
            print("Could not find user")


#function for calculating mean likes
def meanLikes():
    #asks user what twitter account they want to search for
    ask = input("Enter user to find average like count:")
    #creates a list called tweets
    tweets = []
    for x in range(1):
        try:
            #appends each tweet into tweets list
            #calls api to search users timeline and sets screen_name to ask
            #count is set to 1000 tweets api only allows a certain number so 1000 reaches the maximum
            #tweet_mode is "extended" as when the code was made the max tweet was 140characters now the max is 240 so needed to manually update it
            for tweet in api.user_timeline(screen_name = ask,count = 1000,tweet_mode = "extended"):
                 tweets.append(tweet)
            #prints mean
            #calls the program numpy as np to collect every favorite count then calculates the mean
            print(ask + "s  average favourts count:" + str(np.mean([tweet.favorite_count for tweet in tweets])))
            #pandas puts the data into a dataframe with the number of favorites and the date created sets the x and y axis for the graph 
            time_likes = pd.Series(data = np.array([tweet.favorite_count for tweet in tweets]), index = np.array([tweet.created_at for tweet in tweets]))
            #defines the size of the graph and the colour of the line
            time_likes.plot(figsize=(16, 4), color='blue')
            #displays the graph and calls the matplotlib program
            plt.show()
        #if account doesnt exist error will occour and message will be printed
        except:
            print("Account doesnt exist")
               


#function for calculating the average length of the tweet
def averageLength():
    #asks user what twitter account they want to search for
    ask = input("Enter user to find average character length count:")
    #creates a list called tweets
    tweets = []
    #runs 1 time
    for x in range(1):
        #if the code in try works then it will run it if not it will print"account not found"
        try:
            #count is set to 1000 tweets api only allows a certain number so 1000 reaches the maximum
            #tweet_mode is "extended" as when the code was made the max tweet was 140characters now the max is 240 so needed to manually update it
            for tweet in api.user_timeline(screen_name = ask,count = 1000,tweet_mode = "extended"):
                #append the length of tweet into the list tweets
                tweets.append(len(tweet.full_text.encode('unicode-escape').decode('UTF-8')))
            print(ask + "'s average character count is:" + str(np.mean(tweets)))
        #if account doesnt exist error will occour and message will be printed
        except:
            print("Account not found")



#creates function to display user data
def displayUserData():
    #asks user what twitter account they want to search for
    ask = input("Enter the user you want to get details from:")
    #runs the code once
    for x in range(1):
        #if the code in try works then it will run it if not it will print"account not found"
        try:
            #calls api to user details
            user = api.get_user(ask)
            #prints the users name
            print("Name:", user.name)
            #prints the users id
            print("User id:", user.id_str)
            #prints the users bio
            print("Description:", user.description.encode('unicode-escape').decode('UTF-8'))
            #prints the users location if avaliable
            print("Location:",user.location)
            #prints users time zone if avaliable
            print("Time zone:", user.time_zone)
            #prints the number of account the user is following
            print("Following:",user.friends_count)
            #prints the number of followers the user has
            print("Number of Followers:",user.followers_count)
            #prints the number of tweets the user has
            print("Number of tweets:", str(user.statuses_count))
            #prints the data the user created the account
            print("User created account at:",user.created_at)
            #prints if the user is verifyed
            print("Is the user verifyed:",user.verified)
            #if account doesnt exist error will occour and message will be printed
        except:
            print("Could not find user")




def meanRetweets():
    #asks user what twitter account they want to search for
    ask = input("Enter user to find average retweet count:")
    #creates a list called tweets
    tweets = []
    for x in range(1):
        try:
            #calls api to call users timeline and screen_name is called
            #count is set to 1000 tweets api only allows a certain number so 1000 reaches the maximum
            #tweet_mode is "extended" as when the code was made the max tweet was 140characters now the max is 240 so needed to manually update it
            for tweet in api.user_timeline(screen_name = ask,count = 1000,tweet_mode = "extended"):
                #appends the tweet to tweets list
                tweets.append(tweet)
            #prints mean
            #calls the program numpy as np to collect every retweet count avaliable then calculates the mean
            print(ask + "s average retweet count:" + str(np.mean([tweet.retweet_count for tweet in tweets])))
            #pandas puts the data into a dataframe with the number of retweets and the date created sets the x and y axis for the graph 
            time_retweets = pd.Series(data = np.array([tweet.retweet_count for tweet in tweets]), index = np.array([tweet.created_at for tweet in tweets]))
            #defines the size of the graph and the colour of the line
            time_retweets.plot(figsize=(16, 4), color='blue')
            #displays the graph and calls the matplotlib program
            plt.show()
        #if user not found print"user not found"
        except:
            print("user not found")



#creates function that will update the users timeline with random tweet
def updateStatus():
    #num varible is created by calling random and the random number is between 1-1000000
    num = random.randint(1,1000000)
    #updates the users status with the random number
    update = api.update_status("random number created:" + str(num))
    #tweet user just created is displayed with the time created
    for tweet in  api.user_timeline(count = 1,tweet_mode = "extended"):
        print(tweet.created_at,tweet.full_text)
        
    

#tkinter

#window is equal to TK calls tkinter
window = Tk()

#sets the title of window "twitter app"
window.title("Twitter App")

#sets background colour to black
window.configure(background = "black")

#sets the size of window
window.geometry("583x225")

#creates text with the colour white and the font 12 bold and sets it to row 1 column 1
Label(window,text = "Twitter App\nPick what function you want to run\n(functions will run in python shell)\n(max amount of tweets 200)",bg="black",fg = "white", font="none 12 bold").grid(row=1,column=1)

#creates button that is called "aberdeen tweets that calls the function aberdeenTweets when press and set in row 2 column 1
Button(window,text = "Aberdeen tweets", command = aberdeenTweets).grid(row = 2, column = 1, sticky = W)

#creates button that is called "Find Average Retweets2 that calls the function meanRetweets when press and set in row 4 column 1
Button(window,text = "Find Average Retweets", command = meanRetweets).grid(row = 4, column = 1, sticky = W)

#creates button that is called "Find Average length that calls the function averageLength when press and set in row 6 column 1
Button(window,text = "Find Average length", command = averageLength).grid(row = 6, column = 1, sticky = W)

#creates button that is called "Search for word that calls the function textSearch when press and set in row 8 column 1
Button(window,text = "Search for word", command = textSearch).grid(row = 8, column = 1, sticky = W)


#creates button that is called "Find Average likes that calls the function meanLikes when press and set in row 2 column 5
Button(window,text = "Find Average likes", command = meanLikes).grid(row = 2, column = 5, sticky = W)

#creates button that is called "Update status with random word" that calls the function updateStatus when press and set in row 4 column 5
Button(window,text = "Update status with random word", command = updateStatus).grid(row = 4, column = 5, sticky = W)

#creates button that is called "Find Users Data" that calls the function displayUserData when press and set in row 6 column 5
Button(window,text = "Find Users Data", command = displayUserData).grid(row = 6, column = 5, sticky = W)

#creates button that is called "display timeline" that calls the function ShowUserTimeline when press and set in row 8 column 5
Button(window,text = "display timeline", command = ShowUserTimeline).grid(row = 8, column = 5, sticky = W)



#done aberdeenTweets()     
#done meanRetweets() 
#done averageLength()
#done textSearch()
#done meanLikes()
#done updateStatus()
#done displayUserData()
#done ShowUserTimeline()