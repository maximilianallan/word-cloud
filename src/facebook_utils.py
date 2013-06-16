from datetime import datetime

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

        self.update_time = get_time(message_object["updated_time"])
        self.participants = get_participants(message_object["to"])
        self.is_unseen = message_object["unseen"]
        self.is_unread = message_object["unread"]
        self.message_id = message_object["id"]

        (self.next_message_set,self.message_set) = FacebookMessageThread.get_message_content(message_object["comments"])
        

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

    @staticmethod
    def get_participants(participant_string):
        participants_list = participant_string['data']
        participants = []
        for participant in participants:
            participants.append( participant['name'] )
        return participants



    @staticmethod
    def get_message_content(message_content):

        """
        message content contains a dict containing a paging reference
        and a data list
        """

        paging = message_content['paging']
        messages = []
        
        for message in message_content['data']:

            messages.append( FacebookMessage(message) )

        return (paging,messages)


class FacebookMessage:

    def __init__(self,message_data):

        self.created_time = FacebookMessageThread.get_time(message_data['created_time'])
        self.message_text = message_data['message']
        self.author = FacebookMessageThread.get_participants(message_data['from'])
        self.id = message_data['id']
        
        
                                    
        
