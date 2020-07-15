"""

File for decorators and lambda


1. write a function that parses fasta
2. write a function that filters fasta based on length
3. Return list

"""
def readFile(handle):
    """

    :param handle: fasta file
    :return: file accessions
    """
    """
    A large part of bioinformatics is just reformating. We are using fasta parsing as a
    trivial example. However, reading file definitions, and using these definitions for parsing 
    could easily end up as large part of your job as a researcher. We will keep it fairly simple here.
    """
    #read in file
    with open(handle) as f:
       recs = f.read().rstrip().split('>') # read the entire file in and strip and split the the
                                           # text. The split should be based on the header!
    print(len(recs))
    return recs










if __name__ == '__main__':
    pass
