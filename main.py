from ast import Continue
import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *

#This module will create multiple threads for crawling and it will call the functions defined in general 
#Also it will call the spider to creat queue and crawled files.

PROJECT_NAME = 'ku search'
HOMEPAGE = 'http://www.ku.edu/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
CRAWLED_FILE = 'ku search/spider/crawled/.txt'
QUEUE_FILE = 'ku search/spider/queue.txt'
NUMBER_OF_THREADS = 8
queue = Queue()
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


# this will Create the worker threads and it will die after finishing the job
def create_threads():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=thread_work)
        t.daemon = True
        t.start()


# This will keep on checking for the current job ,so that the other threads do the next job in the queue
def thread_work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


# queued links will be treated as new jobs
def create_jobs():
    #using exception handling in case the error occurs for duplicate link
    try:
        for link in file_to_set(QUEUE_FILE):
            queue.put(link)
        queue.join()
        crawl()
    except:
        pass

# This where the actual crawlling happens
# it uses all the functions and methods defined for the crawlling job
def crawl():
    try:
        queued_links = file_to_set(QUEUE_FILE)
        if len(queued_links) > 0 and len(Spider.crawled)<=1000:
            print(str(len(queued_links)) + ' links in the queue')
            create_jobs()
    except:
        pass
    
create_threads()
crawl()
create_link_file()





