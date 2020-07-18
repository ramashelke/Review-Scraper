
'''
The script will be used to extract the critic, rating, source, date,
 and text of 40 reviewers from 2 pages of reviews on RottenTomatoes.

'''
from bs4 import BeautifulSoup
import re
import time
import requests


def getCritic(review):
    criticChunk=review.find('a',{'href':re.compile('/critic/')})
    if criticChunk: 
        critic=criticChunk.text#.encode('ascii','ignore'). text in that element is fetched, which is the name
        if not critic:
            return 'NA' #NA because sometimes there r no critics
        else: 
            return critic
    else:
        return 'NA'
    
def getRating(review):
    rating='NA'
    ratingChunk=review.find('div',{'class':re.compile('review_icon')})
    """<div class="review_icon icon small rotten"></div>"""
    ratingChunk=str(ratingChunk)
    if(ratingChunk.find('rotten')>0): 
        rating='rotten'
    if(ratingChunk.find('fresh')>0): 
        rating='fresh'
    return rating
    
def Text(review):
    textChunk=review.find('div',{'class':'the_review'})
    if textChunk: 
        text=textChunk.text.strip()
        if not text:
            return 'NA'  #NA because sometimes there r no reviews
        else: 
            return text
    else:
        return 'NA'
    
def getSource(review):
    sourceChunk=review.find('a',{'href':re.compile('/source')})
    if sourceChunk:
        source=sourceChunk.text
        if not source:
            return 'NA'  #NA because sometimes there r no reviews
        else: 
            return source
    else:
        return 'NA'
    
def getDate(review):
    date='NA'
    dateChunk=review.find('div',{'class':re.compile('review-date subtle small')})
    if dateChunk:
        date=dateChunk.text
        if not date:
            return 'NA'
        else: 
            return date
    else:
        return 'NA'

def run(url):
    pageNum=2 # number of pages to collect
    fw=open('reviews.txt','w')
    for p in range(1,pageNum+1): # for each page 
        print ('page',p)
        html=None
        if p==1: 
            pageLink=url # url for page 1
        else: 
            pageLink=url+'?page='+str(p)+'&sort=' # make the page url
		
        for i in range(5): # try 5 times
            try:
                #use the browser to access the url
                response=requests.get(pageLink,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
                html=response.content # get the html
                break # we got the file, break the loop
            except Exception as e:# browser.open() threw an exception, the attempt to get the response failed
                print ('failed attempt',i)
                print ('Exception in requesting',e)
                time.sleep(2) # wait 2 secs
		
        if not html:
            continue # couldnt get the page, ignore
        #print(html)
        soup = BeautifulSoup(html.decode('ascii', 'ignore'),'html.parser') # parse the html 
        reviews=soup.findAll('div', {'class':re.compile('review_table_row')}) # get all the review divs

        for review in reviews:
            critic=getCritic(review)# finds and returns the name of the critic from the given review object
            rating=getRating(review) # finds and returns the rating from the given review object. The return value should be 'rotten' ,  'fresh', or 'NA' if the review doesn't have a rating.
            source=getSource(review) # finds and returns the source (e.g 'New York Daily News') of the review from the given review object. The return value should be 'NA' if the review doesn't have a source.
            #date is there , but you are saying NA
            date=getDate(review)  ##finds and returns the date of the review from the given review object. The return value should be  'NA' if the review doesn't have a date.
            text=Text(review) # finds and returns the number of characters in the text of the review from the given review object. The return value should 'NA' if the review doesn't have text.
            #print(critic, rating, source, date,text)
            s= f"{critic}\t{rating}\t{source.strip()}\t{text}\t{date.strip()} \n"
            fw.write(s)

if __name__=='__main__':
    url='https://www.rottentomatoes.com/m/space_jam/reviews/'
    run(url)


