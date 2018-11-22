
class Retrieve:
    # Create new Retrieve object storing index and termWeighting scheme
    def __init__(self,index, termWeighting):
        self.index = index
        self.termWeighting = termWeighting
        

    # Method performing retrieval for specified query
    def forQuery(self, query):
        
        if self.termWeighting == 'binary':
            return self.binaryWeighting(self.index, query)
            #return range(1,5)
            
        elif self.termWeighting == 'tf':
            return self.tfWeighting(self.index, query)
            #return range(1,2)
            
        elif self.termWeighting == 'tfidf':
            return self.tfidfWeighting(self.index, query)
            #return range(1,31)

    def binaryWeighting(self, index, query):
        return range(1,11)
        
        
    def tfWeighting(self, index, query):
        return range(11,21)
        
        
    def tfidfWeighting(self, index, query):
        return range(21,31)    
    
    
    self.index["a"][11]
    
    for term in self.index:
            # for all elems in index
            for doc in term:
                # your code here ;))))))
                self.index[term][doc]
                
                