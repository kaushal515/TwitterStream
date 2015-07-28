from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = '470mh8ugX5mmNglThuh5EXnJz'
csecret = 'fvTjxsvLCeGxyfdwG0OQcPSzk29aAW6xAKZFcZUqKRl6IT6dHQ'
atoken = '310147954-kvyysAC3h4Fy7DHErqpLfCwAb1YS67yL8sw8nXxb'
asecret = 'aOdv6rdjZ1FvnI8jtOdzLqBt7E77CRotd0gbpIMMYIf5g'

class listner(StreamListener):
    def on_data(self, data):
        print (data)
        return(True)

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken,asecret)
#set_access_token(self,atoken,asecret)
twitterStream= Stream(auth, listner())
twitterStream.filter(track=["APJ"])

        
