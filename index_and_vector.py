#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 10 15:55:41 2022

@author: jaypalsingh
"""
import os
from collections import defaultdict
import pickle
import math
from pre_process import file_preprocess,Query_preprocess

def create_postings(files):
    terms_bag = set()
    postings = {}
    postings = defaultdict(dict)
    for id in range(0,len(files)):
        if os.path.splitext(files[id])[1] == ".txt":
            f = open("./ku search/"+files[id], 'r', encoding="utf8")
        
            document_read = f.read()
            f.close()
            term_list = document_read.split()
      		#Set creates a set of tokens in the documents
            
            unique_terms = set(term_list)
            terms_bag = terms_bag.union(unique_terms)
            
      		# set the postings, with the values equal to the frequency of terms in the document
            for term in unique_terms:
                postings[term][id] = term_list.count(term)
    return terms_bag,postings
            
def idf_data(postings):
    idf = {}
    global files        
    for terms, df in postings.items():
        idf[terms] = round(math.log10(float(len(files)))/float(len(postings[terms])),3)
    return idf

def vector_and_normalize(files,terms_bag_sorted,idf):
          
    doc_vector, temp1 = [], []
    #creating vectors for each document
    #using the idf function 
    for docs in files:
        for terms in terms_bag_sorted:
            temp1.append(idf[terms]*(docs.count(terms)))
        #append the values to the universal vector
        doc_vector.append(temp1)
        temp1 = []

    #normalizing the document vector    
    temp2, normalized_doc_vector = [], []
    for docs in doc_vector:
        magni = 0
        for val in docs:
            magni += (val**2)
        magni = (magni**0.5)
        for val in docs:
            temp2.append(round(val/magni,3))
        normalized_doc_vector.append(temp2)
        temp2 = []
    return normalized_doc_vector

def query_vector(query,idf):
    query_terms = Query_preprocess(query)
    query_terms.sort()
    #query vector calculation and normalization
    query_vector = []
    for terms in query_terms:
        query_vector.append(idf[terms]*(query_terms.count(terms)))

#creating normalized query vector
    temp = 0
    normalized_query_vector = []
    for val in query_vector:
        temp += (val**2)

    try:
        temp = (temp**0.5)
        for val in query_vector:
            normalized_query_vector.append(round(val/temp,3))
    except ZeroDivisionError:
         final_result = []
         final_result.append("No Result Found")
         return final_result   	
    return normalized_query_vector 
    
def main():
    global path, dirs, files
    path, dirs, files = next(os.walk("./ku search"))
    terms_bag, postings = create_postings(files)
    terms_bag_sorted = sorted(terms_bag)
    #terms_bag_sorted = terms_bag_sorted.sort()
    print(terms_bag_sorted)
    idf = idf_data(postings)
    normalized_doc_vector = vector_and_normalize(files, terms_bag_sorted, idf)
    #normalized_query_vector = query_vector(query,idf)
    #store the distinct terms in pickle file
    file1 = open(r'pickel files/terms_bag.pkl', 'wb')
    pickle.dump(postings, file1)
    file1.close()
    
    
	#Store the dictionary structure in pickle file
    file2 = open(r'pickel files/postings.pkl', 'wb')
    pickle.dump(postings, file2)
    file2.close()
	#store the idf data 
    file3 = open(r'pickel files/idf.pkl', 'wb')
    pickle.dump(postings, file3)
    file3.close()
    
    #store the normalized vector data
    file4 = open(r'pickel files/normalized_doc_vector.pkl', 'wb')
    pickle.dump(postings, file4)
    file4.close()
        

if __name__ == "__main__":
	main()