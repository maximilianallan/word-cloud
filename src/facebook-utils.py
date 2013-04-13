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
        self.update_date = get_data(message_object["updated_time"])

        self.participants = get_participants(message_object["to"])
        self.is_unseen = message_object["unseen"]
        self.is_unread = message_object["unread"]
        self.message_id = message_object["id"]

        (self.next_message_set,self.message_set) = FacebookMessageThread.get_message_content(message_object["comments"])
        

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
        
        
        
                                    
        
