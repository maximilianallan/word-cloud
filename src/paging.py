import json, urlparse



class FacebookPagingHandler(object):

    def __init__(self):
        pass

    def parse_paging_string(self,paging_string):
        
        query = urlparse.parse_qs(paging_string)

        return query 

    """use facebook.py request method"""

class MessagePagingHandler(FacebookPagingHandler):
    
    def __init__(self,paging_inst):
        super(FacebookPagingHandler,self)
        (next,previous) = paging_inst['next'],paging_inst['previous']
        self.next_query_ = self.parse_paging_string(next)
        self.previous_query_ = self.parse_paging_string(previous)

    def get_next(self):



fb_dump = open('dumpfb.txt', 'w')

my_posts = graph.get('me/posts')

try:
     while my_posts["data"]:
         all_posts = all_posts + my_posts["data"]
         next = my_posts['paging']['next']
         query = urlparse.parse_qs(urlparse.urlparse(next).query)
         until = query["until"]
         limit = query["limit"]
         my_posts = graph.get('me/posts', until = until, limit = limit)
     fb_dump.write(json.dumps(all_posts, indent=4))
except GraphAPI.OAuthError, e:
     print e.message
