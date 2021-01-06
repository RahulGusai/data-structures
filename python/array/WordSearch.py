class Solution:
    def exist(self,board,word):
        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                if word[0]==board[i][j]:
                    if len(word)==1:
                        return True
                    
                    indicesL  = [(i,j)]
                    ret = self.checkIndex(board,word,0,i,j,len(board),len(board[0]),indicesL)
                    if ret == True:
                        return ret
       
        return False
    
        
    def checkIndex(self,board,word,wordIndex,i,j,rows,columns,indicesL):
        if wordIndex==4:
            print("START")

        if wordIndex==4:
            print("CHECKING")
        if (j-1)>=0 and not((i,j-1) in indicesL):
            if word[wordIndex+1]==board[i][j-1]:
                print("1st Block")
                if (wordIndex+1)==len(word)-1:
                    return True
                else:
                    copy = indicesL.copy()
                    copy.append((i,j-1))
                    ret = self.checkIndex(board,word,wordIndex+1,i,j-1,rows,columns,copy)
                    if ret == True:
                        return ret        
                
        if wordIndex==4:
            print("CHECKING")        
        if (j+1)<columns and not((i,j+1) in indicesL):
            if word[wordIndex+1]==board[i][j+1]:'[  A   '
                print("2nd Block")
                if (wordIndex+1)==len(word)-1:
                    return True
                else:
                    copy = indicesL.copy()
                    copy.append((i,j-1))
                    ret = self.checkIndex(board,word,wordIndex+1,i,j+1,rows,columns,copy)
                    if ret == True:
                        return ret
            
        if wordIndex==4:
            print("CHECKING")    
        if (i-1)>=0 and not((i-1,j) in indicesL):
            if word[wordIndex+1]==board[i-1][j]:
                print("3rd Block")
                if (wordIndex+1)==len(word)-1:
                    return True
                else:
                    copy = indicesL.copy()
                    copy.append((i,j-1))
                    ret = self.checkIndex(board,word,wordIndex+1,i-1,j,rows,columns,copy)
                    if ret == True:
                        return ret
                    
        if wordIndex==4:
            print("CHECKING") 
            print(indicesL)           
        if (i+1)<rows and not((i+1,j) in indicesL):
            if word[wordIndex+1]==board[i+1][j]:
                print("4th Block")
                if (wordIndex+1)==len(word)-1:
                    return True
                else:
                    copy = indicesL.copy()
                    copy.append((i,j-1))
                    ret = self.checkIndex(board,word,wordIndex+1,i+1,j,rows,columns,copy)
                    if ret == True:
                        return ret    
                
        if wordIndex==4:
            print("END")
                
        return False
    

obj = Solution()
print(obj.exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]] , "ABCESEEEFS"))