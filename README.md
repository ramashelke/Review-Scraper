# Review-Scraper

The script defines a function run() that accepts the url to a movie on RottenTomatoes. It creates a text file that includes the following information for each review in the first 2 review pages for the movie:

- the name of the critic 

- the rating. The rating is 'rotten' ,  'fresh', or 'NA' if the review doesn't have a rating.

- the source (e.g 'New York Daily News') of the review. This is 'NA' if the review doesn't have a source.

- the text of the review. This is 'NA' if the review doesn't have text.

- the date of the review. This is 'NA' if the review doesn't have a date.

The file includes one line for each review. The reviews in the file appears in the same order as they do on the website. The 5 values are separated by a TAB. 
