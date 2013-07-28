from datetime import datetime
import sys

class FacebookMessageThread:

  def __init__(self,message_object,graph_api):

    """
    pass in a message thread. this contains a dict with keys:
    1) comments (this is a dict contiaing the message data as a list
    of short messages
    2) updated_time a string with the date and time of the message thread
    3) unseen (bool)
    4) unread (bool)
    5) id (string) a number that can be used to request the thread from the graph api
    """
    #process the dict
    #self.next_message_id = message_object["paging"]["next"]
    #self.previous_message_id = message_object["paging"]["previous"]
    
    self.graph_ = graph_api
    
    self.update_time = FacebookMessageThread.get_time(message_object["updated_time"])
    self.participants = FacebookMessageThread.get_participants(message_object["to"])

    self.is_unseen = message_object["unseen"]
    self.is_unread = message_object["unread"]
    self.message_id = message_object["id"]
    
    self.messages = ""
    
    try:
      
      self.message_content = message_object["comments"]
      
      #self.messages = self.get_message_content(message_object["comments"])
    except KeyError:
      
      self.message_content = {"data":""}
      
 
 
  @staticmethod
  def get_time(time_string):
    #u'2013-06-11T07:40:18+0000'
    date,time = time_string.split('T')
    date = date.split('-')
    date = map(int,date)
    time = time.split(':')
    time[2] = time[2].split('+')[0]
    time = map(int,time)
    dt = datetime(date[0],date[1],date[2],time[0],time[1],)
    return dt
    
  @staticmethod   
  def get_participants(participant_data):

    participants = []
    try:
      participants_list = participant_data['data']
      for participant in participants_list:
        participants.append( participant['name'] )
    except:
      participants.append( participant_data['name'] )
      
    return participants

  def get_message_content(self):#, message_content):

    """
    message content contains a dict containing a paging reference
    and a data list
    """

    messages = []

    while True:
      
      
      for message in self.message_content['data']:
        
        try:
          messages.append( FacebookMessage(message) )
        except:
          pass
        #yield FacebookMessage(message) 

      try:
        self.message_content = self.graph_.next(self.message_content)
      #if message_content['data'] == '':
      except KeyError:
        break
    
    return messages

class FacebookMessage:

  def __init__(self,message_data):

    self.created_time = FacebookMessageThread.get_time(message_data['created_time'])
    try:
      self.message_text = message_data['message']
    except KeyError: #this is probably a photo or a file
      self.message_text = ""
      
    self.author = FacebookMessageThread.get_participants(message_data['from'])

    self.id = message_data['id']

