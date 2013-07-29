import sys
import operator
from pytagcloud import create_tag_image, make_tags
from pytagcloud.lang.counter import get_tag_counts
from pyfacebook import FacebookInboxInterface
import argparse
import random

parser = argparse.ArgumentParser(description="Generate a visual word cloud from messages with a user.")
parser.add_argument('name', type=str, help="The user's full name as it appears on Facebook (enclose in quote marks).")
args = parser.parse_args()
  
fb = FacebookInboxInterface("access_token.txt")
message_threads = fb.get_messages_from_friend(args.name)

words = ""
for i in message_threads:
  for m in i.messages:
    words += m.message_text

if words == "":
  print "Error, could not find messages from " + args.name
  print "Exiting..."
  sys.exit(1)
    
words = words.replace("\n"," ")
cleaned_words = ''.join(ch for ch in words if ch.isalpha() or ch == ' ')


cleaned_words = cleaned_words.split(" ")
unique_words = list(set(cleaned_words))

count_of_words = [ (word,cleaned_words.count(word)) for word in unique_words ]
        
tag_words = ""
for word,count in count_of_words:
  if count > 1:
    tag_words += (word + " ") * (count)
  elif len(word) < 7 and random.random() < 0.3:
    tag_words += (word + " ")
  
"""
sorted_words = sorted(count_of_words,key=operator.itemgetter(1))
    
max_count = (sorted_words[0])[1]

for (item,index) in zip(sorted_words,range(len(sorted_words))):
  sorted_words[index] = (item[0],item[1]*300/max_count)
"""
   
 
tags = make_tags(get_tag_counts(tag_words), maxsize=160)
    
#create_tag_image(tags[0:400], 'cloud_large.png', size=(1800, 1200), fontname='Lobster')

length = 1013
if length >= len(tags):
  length = len(tags)-1

create_tag_image(tags[0:length], 'cloud.png', size=(1800, 1200), fontname='Lobster')
