# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 14:09:35 2018

@author: acb16ua
"""

import math
import numpy as np

class Retrieve:
    # Create new Retrieve object storing index and termWeighting scheme
    def __init__(self,index, termWeighting):
        self.index = index
        self.termWeighting = termWeighting
        
        
        self.docCounter = []
        self.x = []
        for term in index:
            for docid in index[term]:
                if docid not in self.docCounter:
                    self.x.append(docid)
                    self.docCounter.append(docid)
        self.totalDocs = len(self.x)
        
        
        self.dfw = {}
        for term in index:
            self.dfw[term] = len(index[term])
        
        self.idf = {}
        for term in index:
            self.idf[term] = math.log(self.totalDocs/self.dfw[term])
            
            
#           
##            
#        self.tf = {}
#        for i in range(1, self.totalDocs + 1):
#            self.tf[i] = {}
#            for term in self.index:
#                if i in self.index[term]:
#                    self.tf[i][term] = self.index[term][i]
#                else:
#                    self.tf[i][term] = 0
#                    
#        print(self.tf)
#                    
        
#        self.docBinary = {}
#        for i in range(1, self.totalDocs + 1):
#            self.docBinary[i] = {}
#            
##        print(self.docBinary)
#                
#        for docid in self.docBinary:
#            for term in self.index:
#                for docd in self.index[term]:
##                    print(self.index[term][docd])
#                    if docd == docid:
###                if self.index[term] == docid:
#                        self.docBinary[docid][term] = 1
                
        
#        for term in self.index:
#            for docid in self.index[term]:
#                if term in
#                self.docBinary[docid][term] += 1
                    
#        print(self.docBinary)           
                    
                    
#                    
#        self.binaryD = {}
#        for i in range(1, self.totalDocs + 1):
#            self.binaryD[i] = 0
#        
#        for term in self.index:
#            for docid in self.index[term]:    
#                self.binaryD[docid] += 1
#                
#        self.binaryDSum = sum(self.binaryD.values())            
#        print(self.binaryDSum)           
                
            
#        self.tfidf = {}
#        self.counter = 0
#        for i in range(1, self.totalDocs+1):
#            for term in index:
#                for docid in index[term]:
#                    if docid == i:
#                        self.tfidf[term] = self.idf[term] * index[term][docid]
            
        #print(self.tfidf)
        
            
    # Method performing retrieval for specified query
    def forQuery(self, query):
        
        
        
        self.qtf = {}
        for i in range(1, self.totalDocs + 1):
            self.qtf[i] = {}
            for term in query:
                if term in self.index:
                    if i in self.index[term]:
                        self.qtf[i][term] = self.index[term][i]
                    else:
                        self.qtf[i][term] = 0
                else:
                    self.qtf[i][term] = 0
                    
        print(self.qtf)            
            
        
        self.qdfw = {}
        for term in query:
            if term in self.index:
                self.qdfw[term] = len(self.index[term])

        self.qidf = {}
        for term in query:
            if term in self.index:
                self.qidf[term] = math.log(self.totalDocs/self.qdfw[term])

#        if self.termWeighting == 'tf':
#            document_scores = dict()
#            for index_word in self.index:
#                #print("index word", index_word)
#                for document_number in self.index[index_word]:
#                    #print("doc nr", document_number)
#                    for query_word in query:
#                        if query_word == index_word:
#                            if document_number in document_scores:
#                                document_scores[document_number] += 1
#                            else:
#                                document_scores[document_number] = 1
#                                
#            sortedVal = sorted(document_scores, key=lambda v:document_scores[v], reverse=True)
#            self.candDocs = sortedVal[:10]                
    #             
#            return self.candDocs
#
        cosDict = {}         
#        qdList = []
#        qLen = len(query)         
        for term in query:
            if term in self.index:
                for docid in self.index[term]:
                    if self.termWeighting == 'tf':
                        if docid in cosDict:
                            cosDict[docid] += 1
                        else:
                            cosDict[docid] = 1
                    if self.termWeighting == 'tfidf':
                        
#                        return 2
#                    if self.termWeighting == 'binary':
#                        qd = 1
#                        qdList.append(qd)
#                        qdSum = sum(qdList)
#                        print(qLen)
#                        dVals = list(self.docBinary[docid].values())
#                        dValsSq = map(lambda x: x ** 2, dVals)
#                        docBinarySum = sum(dVals)
#                        dTotal = math.sqrt(docBinarySum)
#                        cosine = qLen/dTotal
#                        cosDict[docid] = cosine
                        
#                        
        sortedVal = sorted(cosDict, key=lambda v:cosDict[v], reverse=True)
#        print(sortedVal) 
        self.candDocs = sortedVal[:10]                
#        print(self.candDocs)      
        return self.candDocs        