from fileinput import filename
import os
from typing import Dict
from urllib.request import urlopen
#from domain import get_domain_name
from pre_process import prep,file_preprocess
from urllib.parse import urlparse
import pickle

# from main import PROJECT_NAME


# Each website is a separate project (folder)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('Creating directory ' + directory)
        os.makedirs(directory)


# Create queue and crawled files (if not created)
def create_data_files(project_name, base_url):
    queue = os.path.join(project_name , 'queue.txt')
    crawled = os.path.join(project_name,"crawled.txt")
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')
        
        
# Get sub domain name (name.example.com)
#def get_sub_domain_name(url):
#try:
  #return urlparse(url).netloc#except:
 #return ''
 # Updates user display, fills queue and updates files

# Create a new file
def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)


# Add data onto an existing file
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


# Delete the contents of a file
def delete_file_contents(path):
    open(path, 'w').close()


# Read a file and convert each line to set items
def file_to_set(file_name):
    results = set()
    try:
        with open(file_name, 'rt') as f:
            for line in f:
                results.add(line.replace('\n', ''))
        return results
    except:
        pass


# Iterate through a set, each item will be a line in a file
def set_to_file(links, file_name):
    with open(file_name,"w") as f:
        for l in sorted(links):
            f.write(l+"\n")

def create_link_file():
    links=set()
    with open('ku search/crawled.txt', 'rt') as f:
        for line in f:
            links.add(line)
    i=0
    url_list =[]
    for l in sorted(links):
        i=i+1
        try:
            with urlopen(l) as response:
                link_data = response.read()
                url_list.append(l)
               
            filepath= ("ku search" + '/'+'doc'+str(i)+'.txt')
            with open(filepath, 'w') as f:
                f.write(file_preprocess(str(link_data)))
        except:
            continue
    tfile = open(r'pickel files/doc_urls.pkl', 'wb')
    pickle.dump(url_list, tfile)
    tfile.close()
    
# Get the domain name of search directory
def get_domain_name(url):
    try:
        results = (urlparse(url).netloc).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''


