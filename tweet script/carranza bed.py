import tweepy
auth = tweepy.OAuthHandler("WRAIqryVzGsQjixyHBe0XbXRE", "T2JqnoJVgoBGn3SabkpZXp0BpyLfGknIGQp90VkZSbYhogwYLr")
auth.set_access_token("1520563382058893318-ewdmvabwArERpkNzGGzDTB6mcKQou3", "ulbOQydUpTLtEDs1Q4KyZMf0d8j1N9qwX7vIgA66D69rx")
api = tweepy.API(auth)
print ("Tweet Message!")
print ("Twitter For?")
tweet = input("Conjure Up A Tweet")
api.update_status(status =(tweet))
print ("Done!")