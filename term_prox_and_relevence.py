import os
import copy
import pickle
from pre_process import file_preprocess,Query_preprocess
from newindexfile import create_postings,idf_data,vector_and_normalize,query_vector

doc_files = next(os.walk("./ku search"))

#Collecting doc url info
file0 = open(r'pickel files/doc_urls.pkl', 'rb')
doc_urls = pickle.load(file0)
file0.close()
#collecting word list using pickle
file1 = open(r'pickel files/terms_bag.pkl', 'rb')
terms_bag = pickle.load(file1)
file1.close()
#print(tokens_list_word)

#Collecting dictionary structure (specifically postings) using pickle
file2 = open(r'pickel files/postings.pkl', 'rb')
postings = pickle.load(file2)
file2.close()

#Collecting the idf data
file3 = open(r'pickel files/idf.pkl', 'rb')
idf = pickle.load(file3)
file3.close()

#Collecting dictionary structure (specifically posting_dict) using pickle
file4 = open(r'pickel files/normalized_doc_vector.pkl', 'rb')
normalized_doc_vector = pickle.load(file4)
file4.close()



def term_proximity(cos_similarity,query):
    cosine_similarity = copy.deepcopy(cos_similarity)
    sorted_cosine_similarity= cosine_similarity.sort(reverse = True)
    changed_result,cos_value_list = [],[]
    value_track = (val for val in sorted_cosine_similarity if val > 0)									
    for val in value_track:
        doc_index = cos_similarity.index(val)
    #after getting the doc index from the cos_similarity it tries to locate the term
        if val in cos_value_list:																			
            counter_index = 0
            counter_index = cos_value_list.count(val)
            while(counter_index != 0):
                doc_index = cos_similarity.index(val, doc_index +1)
                counter_index -= 1
    cos_value_list.append(val)
    #here it starts looking for each query term into the document and tries to calculate the index 
    #and frequecy of term in the doc                
    count, freq, query_index = 0 ,0, 0
    while(query_index < len(query) - 1 ):															 
        term_index = -1
        try:#find the first occurance of the query term pair in the document
            count = term_index + 1
            check = 1
            freq = 0
        #look for pairs of query terms for the entire length of query
        #look through the entire documents for each pair of query terms
            while(count < len(doc_files[doc_index])):												
                if(doc_files[doc_index][count] != query[query_index]):
                    if(doc_files[doc_index][count] == query[query_index + 1]):
                    #inreament the frquency after finding more occurences
                        freq += 1																	
                        term_index = -1
                        try:
                            term_index = doc_files[doc_index].index(query[query_index], count + 1)
                            count = term_index + 1
                        except ValueError:
                            break
                    elif (check > 3):																
                        term_index = -1
                        try:
                            term_index = doc_files[doc_index].index(query[query_index], count + 1)
                            count = term_index + 1
                        except ValueError:
                            break
                    else:																			
                        check += 1
                        count += 1

                else:
                    count += 1

        except ValueError:
            query_index += 1

        query_index += 1

        
    #create a list with freq of the pair of query terms and the document no.   
    changed_result.append([doc_index, freq])
    freq = 0
    
#sorting the the list with descending freq    
    changed_result = {val[0]:val[1] for val in changed_result}
    changed_result = sorted(changed_result, key=changed_result.get, reverse = True)

#return the final result reading the url and documents name based on the above ranking
    result = []
    count = 0
    for val in changed_result:
        if(count > 15):
            break
        else:   
            result.append(doc_urls[2*val])
            result.append(doc_urls[(2*val) + 1])
            count +=1
                
            return result
        
def Relevance_feedback(doc_name):
    for i in doc_name:
        
        doc_index = doc_urls.index(i)
        
        newquery = []
        counter = 0
        for value in normalized_doc_vector[doc_index]:
            newquery.append(normalized_query_vector[counter] + 0.5*value)
            counter += 1
            
        temp = 0
        normalized_newquery = []
        for val in newquery:
            temp += (val**2)

        temp = (temp**0.5)
        for val in newquery:
            normalized_newquery.append(round(val/temp,3))

        #newsorted similarity cosine for ongoing query using Rochio's Algorithm    
        new_similarity_cosine = []
        for doc in normalized_doc_vector:
            counter, value = 0, 0
            while counter < len(doc):
                value += round(doc[counter]*normalized_newquery[counter],3)
                counter += 1
            new_similarity_cosine.append(value)


        sorted_new_similarity_cosine = copy.deepcopy(new_similarity_cosine)
        sorted_new_similarity_cosine.sort(reverse = True)   
            
         #two documents with similar cosine values should be ordered accordingly
        improved_result = []
        count = 1
        value_list = []
        flag = False
        value_track = (val for val in sorted_new_similarity_cosine if val > 0)
        for val in value_track:
            if count > 10:
                break
            else:
                document_index = new_similarity_cosine.index(val)
                if val in value_list:
                    counter_index = 0
                    counter_index = value_list.count(val)
                    while (counter_index != 0):
                        try:
                            document_index = new_similarity_cosine.index(val, document_index + 1)
                            counter_index -= 1
                        except ValueError:
                            flag = True
                            break
                value_list.append(val)

                #return the final list reading the link and document name according to the above rank
                if(flag == False):               
                    improved_result.append(doc_urls[2*document_index])
                    improved_result.append(doc_urls[(2*document_index) + 1])
                    count += 1

        return improved_result   
            
            

    
#qurey preprocess and vector creation
def main_func(query):
    global normalized_query_vector 
    try:
        normalized_query_vector = query_vector(query,idf)
        #cosine similarity calculations
        cos_similarity = []
        for doc in normalized_doc_vector:
            counter, total = 0, 0
            while counter < len(doc):
                total += round(doc[counter]*normalized_query_vector[counter],3)
                counter += 1
            cos_similarity.append(total)
        return term_proximity(cos_similarity,query)
    except (TypeError,ValueError):
        pass


    
    
    
	#Initializing term length to frequency
	##term_length_to_freq()
	#Initializing Euclidean length
	##euclid_length_docs()
	#get_res the query from the user
	##enter_query_user(query)