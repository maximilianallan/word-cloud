import facebook

from facebook_utils import FacebookMessage

class FacebookInterface:

    def __init__(self,path_to_access_token):
        with access_token as open(path_to_access_token,'r'):
            self.graph = facebook.GraphAPI(access_token)
        try:
            self.graph
        except:
            raise Exception('Could not open access token')

        self.get_user()

    def get_user(self):
        try:
            self.user
        except:
            self.user = graph.get_object("me")
        return self.user
    

    def get_friends(self):
        return graph.get_connections(self.user["id"], "friends")

    

class FacebookMessageInterface(FacebookInterface):

    def __init__(self,path_to_access_token):
        super.__init__(path_to_access_token)
        
    def get_messages_from_friend(self,friend_name):
        self.friend = friend_name
        #returns a dict containing: paging (id for request of next/previous page of messages), data, a list of messages/conversations and a summary
        messages = self.graph['me/inbox']
        
        

        while True:
            
        
        #parse the inbox for messages from this friend
        
        #raise exception if no messages found
    

    def get_messages_as_string(self):
        
        messages_as_string = ''

        for message_id in self.messages:
            
            message_content = self.get_message_content(message_id)
            '' += self.clean_message(message_content)

        return messages_as_string

    def get_message_content(self,message_id):

        content = ''
        #retrieve the content from the facebook graph
        return content

    def clean_message(self,message_content):
        
        #remove punctuation and undersirable chars

        

        
        
            
        

        
