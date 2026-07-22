class PrefixTree:

    def __init__(self):
        self.trie = [dict(), False]

    def insert(self, word: str) -> None:
        dictObj = self.trie
        
        i = 0
        while i < len(word):
            if word[i] not in dictObj[0]:
                dictObj[0][word[i]] = [dict(), False]
            if i == len(word) - 1:
                dictObj[0][word[i]][1] = True
            dictObj = dictObj[0][word[i]]
            i += 1


    def search(self, word: str) -> bool:
        i = 0
        dictObj = self.trie
        while i < len(word):
            if word[i] in dictObj[0]:
                dictObj = dictObj[0][word[i]]
            else:
                return False
            
            if i == len(word) - 1 and dictObj[1] == False:
                return False
            i += 1
        return True
        

    def startsWith(self, prefix: str) -> bool:
        i = 0
        dictObj = self.trie
        while i < len(prefix):
            if prefix[i] in dictObj[0]:
                dictObj = dictObj[0][prefix[i]]
            else:
                return False
            i += 1
        return True

        
        