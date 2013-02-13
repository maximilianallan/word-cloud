#!/usr/bin/python

import sys
import operator
from pytagcloud import create_tag_image, make_tags
from pytagcloud.lang.counter import get_tag_counts

if __name__ == '__main__':

    try:
        infile = open('text.txt','r')
    except:
        print "could not open file! exiting..."
        sys.exit()


    
    words_as_string = infile.read()
    words_as_string = words_as_string.replace('\n',' ')
    words_as_string = ''.join(ch for ch in words_as_string if ch.isalpha() or ch == ' ')
    words_as_list = words_as_string.split(' ')

    unique_words = list(set(words_as_list))
    
    count_of_words = []

    for item in unique_words:
        count_of_words.append( (item, words_as_list.count(item)) )
    
        
    
    sorted_words = sorted(count_of_words,key=operator.itemgetter(1))
    
    max_count = (sorted_words[0])[1]

    for (item,index) in zip(sorted_words,range(len(sorted_words))):
        sorted_words[index] = (item[0],item[1]*300/max_count)

    #    if item[0] == ' ':
    #        continue
    #    if item[1] > 4:
    #        print item[0] + " appears " + str(item[1]) + " times"
 
    
    
 
    
    tags = make_tags(get_tag_counts(words_as_string), maxsize=160)
    
    #create_tag_image(tags[0:400], 'cloud_large.png', size=(1800, 1200), fontname='Lobster')

    create_tag_image(tags[0:1013], 'cloud_large.png', size=(1800, 1200), fontname='Lobster')
