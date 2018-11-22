import math

class Retrieve:
    # Create new Retrieve object storing index and termWeighting scheme
    def __init__(self,index, termWeighting):
        self.index = index
        self.termWeighting = termWeighting
        ######################################
        docCounter = []
#        self.totalDocs = []
        x = []
        for term in index:
            for docid in index[term]:
                if docid not in docCounter:
                    x.append(docid)
                    docCounter.append(docid)
                self.tf = index[term][docid]
            print(index[term][docid])
        self.totalDocs = len(x)             
        ######################################            
        #for term in index:
            #for docid in index[term]:
#        self.tf = index[term][docid]
        ######################################  
#        self.docIdSum = 0
        self.sumva = []
        for term in index:
            self.dfw = len(index[term])
            self.idf = math.log(self.totalDocs / self.dfw)
            self.tfidf = self.idf * self.tf
#            self.docIdSum += self.tfidf
            self.sumva.append(self.tfidf)
            
        self.docIdSum = sum(self.sumva)
        
            
    # Method performing retrieval for specified query
    def forQuery(self, query):   
        ######################################
        for term in query:
            if term in self.index:
                self.qfw = len(self.index[term])
                for docid in self.index[term]:
                    self.qTf = self.index[term][docid]
        ######################################
        #for term in query:
        self.qidf = math.log(self.totalDocs / self.qfw)
        ######################################
        self.qIdSum = 0
        #for term in query:
        self.qtfidf = self.qidf * self.qTf
        self.qIdSum += self.qtfidf
        ######################################
        
        qDSum = []
        fullList = {}
        
        for term in query:
            if term in self.index:
                for docid in self.index[term]:
                    if self.termWeighting == 'tfidf':
                        qDSum.append(self.qtfidf * self.tfidf)
                        
                    elif self.termWeighting == 'tf':
                        qDSum.append(self.tf * self.qTf)
                        
                    elif self.termWeighting == 'binary':
                        if term in self.index:
                            self.qBinScore = 1
                        else:
                            self.qBinScore = 0
                        qDSum.append(self.qBinScore)
#                    print(self.tf, self.qTf)
                    upper = sum(qDSum)/(self.docIdSum * self.qIdSum)
                    fullList[docid] = upper
                    
                    
        sortedVal = sorted(fullList, key=lambda v:fullList[v], reverse=True)
        self.candDocs = sortedVal[:10]

        return self.candDocs