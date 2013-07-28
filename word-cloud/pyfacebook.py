import facebook

from facebook_utils import FacebookMessage,FacebookMessageThread

class FacebookInterface(object):

  def __init__(self,path_to_access_token):
    #open a connection to the facebook graph
    with open(path_to_access_token,'r') as access_token_file:
      access_token = access_token_file.read()
      self.graph_ = facebook.GraphAPI(access_token)
    
  @property
  def user(self):
    try:
      self.user_
    except:
      self.user_ = self.graph_.get_object("me")
    return self.user_
    
  @property
  def friends(self):
    try:
      self.friends_
    except:
      self.friends_ = self.graph_.get_connections(self.user["id"], "friends")
    return self.friends_
    
  @property
  def graph(self):
    return self.graph_
  

class FacebookInboxInterface(FacebookInterface):

  def __init__(self,path_to_access_token):
    super(FacebookInboxInterface,self).__init__(path_to_access_token)
        
  def get_messages_from_friend(self,friend_name):
      
    self.friend = friend_name
            
    inbox  = self.graph_.get_object('me/inbox')
    #inbox is dict { paging , data , summary }
    
    message_thread = []
    while True:
        
      #when get to end will have to use paging to go to next
      for raw_message_thread in inbox['data']: 
        
        message = FacebookMessageThread(raw_message_thread,self.graph_)
        if friend_name in message.participants and len(message.participants) == 2:
          
          message_thread.append(message)
          content = message_thread[-1].get_message_content()
          message_thread[-1].messages = content
          
      try:
        inbox = self.graph_.next(inbox)
      except KeyError:
        break
      
    return message_thread
      
  def get_messages_as_string(self):
        
    messages_as_string = ''

    for message_id in self.messages:
           
      message_content = self.get_message_content(message_id)
      messages_as_string += self.clean_message(message_content)

    return messages_as_string

  def get_message_content(self,message_id):

    content = ''
    #retrieve the content from the facebook graph
    return content

  def clean_message(self,message_content):
        
    #remove punctuation and undersirable chars
    pass

        

        
        
            
        

        
