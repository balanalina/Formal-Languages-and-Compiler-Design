# implementation for pif using a 2*2 matrix
class PIF:
    def __init__(self):
        self.table = []
        self.size = 0

    # adds the pair [token, index] as anew list at the end of the matrix
    # return the position on which it was added
    def insert(self,token,index):
        # make sure that the token is a string
        str(token)
        self.size += 1
        self.table.append([token,index])
        return self.size

    def get_length(self):
        return self.size

    def pretty_print(self):
        result = ''
        for row in self.table:
            result += (row[0] + "\t" + str(row[1])+'\n')
        return result






