
import decoratorsLambda

# set up temporary directory

def setup_module():
    from testfixtures import TempDirectory
    d = TempDirectory()
    d.write('tmp.fasta',\
            b"""\
>TRINITY_DN21455_c0_g1_i1 len=291 path=[1:0-290] [-1, 1, -2]
GGGGAGACCAGTGTGGGCAGCGCTGGTAGGAGAGTCATCGCCAGATGTCACTACTGGCGC
GCTCTCGAGACAGCAGGAACGACCGTCCATCAAGGCACTGGCTTGCTACTTGCAGGGTGA
TACACCAAAACTGCAAGCGTACAACCACGCTGCACTGACGCTAACTCCCAGCAGCGCAGA
TCTGATCCAGAAAGCGAGCAACCGACCCAAACCAATCCGATCTAGCACAAGGCAGCTCCG
AACCCAGCAGACGAGTCCGTGAGCTGGAGGAAAATGGCAGGCGCGAGCGGC
>TRINITY_DN21442_c0_g1_i1 len=602 path=[1:0-601] [-1, 1, -2]
AACGGTTCTTCGGACCTTTGTCCATCTTCTTTGCATCGTCATGAACGATGAATCCAATGG
AGTCCTTGTAATCCAGAAATTCCTTCCACTGCTTCCCTATGCTTACCTGGGCAGCTTCAT
TGGCAGCATTTTTGGTCCAGATAGCTATTCTTTCCTGCTTACCACGTACACTAACGACTG
CTCCACAAATTTCATCACCATAGTCGAATTGTTCGCCAATCATTGCCAATAGAGTGTGCA
GCCACATTGTGTCAGATTTTCCTCTGCCACAGCTGATGGTCCATTTACCACCATTGGCAC
AAATAGGGTCTTCCCATTTTGGTTCAATCTTGTTCTTGAAACAATGGAAGTCTGCTCCCA
CAATCAACTTGCTAGGGTGGTGAATATTATTGTAAAGGCCCCAGAAGTCCTCGACGGTGG
AGAAGGTGTGGATGGGGCGGATGGAGCTCCCCCATGCGGCCTGCTTGGACTTTCCCTGCG
GGTTGTCGAACCAGAAGGTCCAGGAGTGCTCGAGCGGGTGCGTGGCGGGCTGGAGCGGCG
GTGCGGGGGCGGAGGAGTCGTCGGCGATCTCGCCCTCCTCCCTGTCGTCGCCGTCCGGCG
CG
>TRINITY_DN21422_c0_g1_i1 len=320 path=[298:0-319] [-1, 298, -2]
CACGACGTCTTCCGATCTTGTTTGCCCATGGAACCTGAATCAACAGCCATTACCGTCAGC
TCCGATTCACAGGGAAAATAATGGATCGTGCTCTGATTTTTTTGTACTGGTAAAAGAGAT
TTGGGACAGGCAATTGCAATCCAAATTCCACAACACAGTAGTATGTAGTAGTAGTAGTAG
AGAGACAAAGTGGGAGGGAGTCTGAAATTTTGGAGATTTGGAATTGAGCGGCAATGGCGA
TTGAAAACTTTTCGAATTCCCGCCTGGAGTGAAAATGGTGAAATCTCCAAAATTTCAGAG
ATCGGAAGAGCGTCGTGTAG
>TRINITY_DN21452_c0_g1_i1 len=244 path=[1:0-243] [-1, 1, -2]
TGAACATGCAAACTCTGCTTCTTGCACGCCGGCGCGGGGGCCCGGGCTCAGTGGCCGCCG
CCGCTGACGGCCCGGAACTGGCGCTTCGAGATCTTGGGCAGGAGGAAGAGGCCCACGATC
CCACCGATGAGGGCGAAGCCGGACGCCACGCCGAACGCCGGGATGTTCCCCTTGCCGAAC
AGCGCGTCCCACGGTCCCGCGCCCAGCGCGATGATCACCTGAGGGATGACAATGGAGATG
TTCA
>TRINITY_DN21478_c0_g1_i1 len=222 path=[200:0-221] [-1, 200, -2]
CAGCAAGATGTTGGTAATGATGGAGGTTTGGTCTCGGTATCACATTCTGGAAATGGAAAT
TTAACTCTCAATCTGAGGGAGGGTAATAACATCGAAACTGGTGTTGAGTTTGAGTATCGC
CTTAATTGAGTTGCTTTAGTTTTATCAATTATGTCCTTTTAGGAGTTCTGATTAAGCTTC
ATTTTGGTCCTCTTTTTTTTTACTACTGGTGTTGAGTTTGAG
>TRINITY_DN21477_c0_g1_i1 len=240 path=[218:0-239] [-1, 218, -2]
GTGACGGTGAAGTACGGCCAGACAACGCCGTCCGTCGACGACTGGATCGCCGTTTTCTCT
CCAGCTGATTTCATCTCGGGCACGTGCCCTAACCCTTCGAGATACCATGGAGAACCGCTG
CTCTGCACGGCGCCTATCAAGGTTACTTTGCAAGCATCAGACTCTAACCGTCGTGTTTGC
ACTCACTTAACCACGAAATATTACAGTCTGTAGATTTTTTTTTCTTACTGAAACTTGTTA
>TRINITY_DN21432_c0_g1_i1 len=203 path=[1:0-202] [-1, 1, -2]
AAATCTAACCAGAACAACAAGACCTGTTCGGAGAACAATGGCCAAATTACAGGTTTCATG
ACATATCTGCATTCCAAAGTAGGTAAGAATCAGAACTGTAGACCTTAGGGCAAGCATACT
CAGAGATTGAATGACCTAATAGTAAGAGGATCATCGCAGAAACCATGAAAAAAAAGGCAT
CGCAGCAGCCAAAAAAAAAAAAA
>TRINITY_DN21482_c0_g1_i1 len=367 path=[1:0-366] [-1, 1, -2]
AAGCAATTGGGGCTTGTCATTTCGCTTATATGCCCTCTTGAGCTGGAGCACAACACGAAC
AAGAAGCAACCGCCCAATCTCAGGAAACTTGGTATTCACAACCGCGACAAGTGCAGCAAA
AACATCGGTGAACCCAGGTGAGGCCATCTGTGACTTGATGCACGATTGGCAGAAGAGCCC
CCGCCCACGAACAAGGTTCTCCGCAAAGAGCTCCGGCACTATATTCTTGATATTGGTCGC
ATTGACCTTATTCACCAGCCCATTGATGCTCTTCTTGAGAGCATCCCAGGTGAGCCGCTG
GTACTCAGGGCTCGACTTGTCCTCCACCTCCCGCATCATCTGCGCCATGCGGAATGGCGG
GATGTAA
>TRINITY_DN21438_c0_g1_i1 len=254 path=[1:0-253] [-1, 1, -2]
ATACAATGTACGGTAGAAAAAAAATGGAATGCTTGTAACAAGCTCCTGCCTTGTTGGCTG
CAACATCAAGCTTCAATTAGAGAGGAAGTGCACCCGGGCGAGGGGGTACTCCTTCCCAGC
TACCCAAACGCCAGTCTGTGACCACTGCACGTCCTCCCATTCTAGGTTATCCTGCAACAC
CTCAAGTTGGTCTGCTGGTAGCGGGATACCGATGGAACGCATGGCACTTTCAGGCATGAG
ATCGGAAGAGCGGT
>TRINITY_DN21473_c0_g1_i1 len=255 path=[1:0-254] [-1, 1, -2]
GGTTTACATTCCTACACCAAAGAAAGGACTAACCTGGTGGTTCTTCCAGCTGCAAGCGGC
AAGCCTCTTGCTTTTGCTCTCCACCCAACCTGTGCATAACTCATGTACATACATACACTC
ATGCCTTTTGCTCTCTGGTCAGGGTATTTGTTAGATGTATTTGTTGCTTTTTGTTAGGCT
TTCGTTTGATTGATTGGTTCTTTCTTCAATCTTACCCCTTTTTTCTGGGGGAAGGGTCGT
CAATTCATATATTTT
>TRINITY_DN21434_c0_g1_i1 len=205 path=[1:0-204] [-1, 1, -2]
TCTAAGTAGAGCTACTTCCCCCTTCTCCTCTCCCTTTCTAGCCCAATACCAAAGAATAGT
ACGGAACACGAAAGCACCTTGACTTCCGCCTATAGAATGCGAAGTTGTTCACTCAATAAT
CGAGAAAGAACCAGGAAGAAATCGGCCAAAATCTACCTTCTATTCCCATGAGTACCAGCA
AGCTCCATCTTTGAGTGGATCGAAG
>TRINITY_DN21463_c0_g1_i1 len=202 path=[1:0-201] [-1, 1, -2]
TTCCGATCTCCTCGCGCGACTCTCCCTCCCCGCCGTCGCCGTCGACGCCGACGCCGGCCT
GCGCAACCTCGACCTCCTGCTCGGCCTCGAGAACCGCGTCCACCTCACCGCAGCCGACGT
CCTCGCCGGGGACTGCCGCCAGGGCCAGGCGCTCGTCCGACACCGCGCGCTCCAGGACCT
CCACCTCCTCTGCCTCTCCAAG
>TRINITY_DN21433_c0_g1_i1 len=264 path=[1:0-263] [-1, 1, -2]
GCTTGCGTCGTCGTCGGAGTGGCGCGACGGGAAGCCCGTGCTGCTCCACCATGGCTGGGC
TGGCATCGGCAAGGGTGCGGCGGAGGCCAGGCCGGAGCTCCACCTCAGGGTGAAGATGGA
GGCCGACCCCCGGTACATCTTCCAGTTCGACGACGAGGTCGCGCTCAACCCGCAGGTCGT
CCAGCTCCATGGCAGCTCCCGGCAGCCCATCTTCAGCTGCAAGTTCATCCGCGACCGCCG
CAGGCCGTCTCAGGGTGACGGGCG
>TRINITY_DN21483_c0_g1_i1 len=212 path=[190:0-211] [-1, 190, -2]
CGTGGAGTCGCGGCTCCTGCGGCTGCGGTCCTCCGACGACGCGGTCATCCGGGGGAGCGG
GTACCTCCACTTCGTCAGGCGGTGCGGCTTGAAGGAGGATGACGTGGTCGAGATCTGGGC
CCTTCAGGGGCACCTCGACTTCTTCAGGCTGTTTTAACGATTGCAGGGCCAGGTGTGGCG
GAAGCCATCTGCTGCACGTGCTGATCGCCAAG
>TRINITY_DN21419_c0_g1_i1 len=207 path=[1:0-206] [-1, 1, -2]
TTCACTGTAACCTCAATTAGGAAACCCCATGACACAACCAAAAGACAATAGCCGAGAATG
AAACTTCAAAGTATTCTAACAGAGCTGAAAATAAAGTAACAATGGATTGAGCACCACCAA
CATATTCTTTAGTATTCTTCATTCTTCAAGCTTCATGGTATGCGAATTTAACCAGAGGTA
CATACTCTAACCAATAATGTGAATTAG
>TRINITY_DN21454_c0_g1_i1 len=224 path=[1:0-223] [-1, 1, -2]
AGAGGATGTGGTCGTCCAGCCAGGCGAGCACGAGGGGCGTCGTCGAGATGGGGAGGGTGG
AGGCCGGGCCTTCCCATTTCCCCAAGAGGCCCGCGCCCCGTAATCCCACCAGGGTCAATC
TATCAAGGACACATGCAGTTAAACCTTGCTCAGCTGGCGACCGCGCAGGAATTTCAGTTA
AATGTAACTTGGGGTGGTCTTCTCAACCATCGCCCGACTTGAAG
>TRINITY_DN21498_c0_g1_i1 len=255 path=[233:0-254] [-1, 233, -2]
GCCAGTCAGATGCAGTTCTTTTCAGTGCCATATAGAGCTGTCCAGAGTCCAAGAGGAAGT
GACTCGATCATTCCCGGGAAGCAGCTTTGATTCTGATTAATTTTTTTGTGGGGAAAGGCT
TGTCTTTCCCCCATAGGTTCATTTAGATTTAAAGATAAATTCTAGTTCAGCAACATTTGG
GCATCTGTAGTAGACGGTGATAAGGGGATGGTCAACCTTTATGTTCATGTTGGAGCATGG
GTCTGTAACTTCAGG
>TRINITY_DN21405_c0_g1_i1 len=206 path=[1:0-205] [-1, 1, -2]
AGAATAGCGATCTGATCAAAAGTGTTAAAGAGTGCACGGATGATTTGCTAAAATGGGTAC
AAATTGATGAGGATATTGGACATCAACGAGCCAAGATCAACTGGCTCACTCTTGGTGATG
GAAACAACAACTTTTTTCATGCTACTATCAAAGAGAAAAATAAAAAAGTAGGCATGACTA
AGCTTGTTACCAGTTATGGAGTTACA
>TRINITY_DN21461_c0_g1_i1 len=213 path=[1:0-212] [-1, 1, -2]
GGAGGACTGGCGCGAGCTCTACGGCTCCCACCTGCAGCTAGAGGTGGAGCCGGCGGTGCA
CGACTCGCGCGACGAGGGCACCGCGGACGCGTGGATCGAGCGCAACCCGTCCCTCATCCG
GCTCACCGGCAAGCACCCGCTCAACTGCGAGCCGCCGCTGACGCGCCTGATGCACCACGG
CTTCATCACCCCGGCGCCGCTCCACTACGTGCG
>TRINITY_DN21435_c0_g1_i1 len=211 path=[1:0-210] [-1, 1, -2]
ATGGTTCCTATGGACAAGTTTTTCCAGGGTACCAGACAAAACAAGTTGGGCACTATCACA
AATGTATCTGGCGAAGAATGTAGTTATCTCCTATCGCGCTTATTAAATTCCCACGTGAAA
CATCAAATTGCCGTAACCTCATCCATAGTAACAATGCATCTTTTGCCGCGTAACACCTTG
ATAGTGGATAATGTTAAAAATCATCAAAAAG
>TRINITY_DN21441_c0_g1_i1 len=215 path=[1:0-214] [-1, 1, -2]
CTTATCGGCGGCCGGCTCCGGCTGGGGCTGGGCCTGCGCCGGAGTGAGCGCCTTCTTGAT
GGAGGCGGCGTGGATCTCCGCCATGTGCGGCGCCAGCGCCGTGTTCACCATCCGGTGCCG
CTCCAGCAGCCGCTTCCCCTCGAACTTCTCCGACACCACCTCGATCTCGTAGCTCGCACC
ACACCCTCCAGATGTATCCGTCACCATGAGATGGG
>TRINITY_DN21457_c0_g1_i1 len=286 path=[1:0-285] [-1, 1, -2]
GGCATTCCTGCTGAACCGCTCTTCCGATCTGCAAATGTTCCATTTGTTGGGACGTCGTCT
AAGGAATGCCAGCGTGCTTTTGACAAGCATAGCGCATCCCTCGAGCTTGATGTACAAGGT
TTCTTAACTGTGCCAAACTTTCTTGTGGAGAAGGACAAGTTGGCTAAGCAAGAGCTGGAG
GCATGGTTCCAAACCACAAATTTGAGCAAAGAAAATGGAAAAGTGATTGTCAAACCTACG
AGGGCTGGGTCAAGTATTGGTGTGGTTGTTGCTAGATCGGAAGAGC
>TRINITY_DN21481_c0_g1_i1 len=224 path=[202:0-223] [-1, 202, -2]
GTCAAATTTAACATAGGAATTCATTTTAGGAATCCTGCAACTAGTGGTCTTACCCAAACA
GAACTAGTATAAAGTACCAACTAACCTTCATGTGGACATTTGTAGCAACACTTCATTCTG
ACATAAGCATAATGATTAAGGACTCTCAACCACTCAGGCACTCACCACCAAAACTTACAA
AGACGTTTATATAAAGAGGTTTTCTAGAGGGGAACTAACAAAAT       
""")
    return d

def teardown_module():
    TempDirectory.cleanup_all()


def test_readFile():
    recs = decoratorsLambda.readFile('tmp.fasta')
    print(recs)
    print(len(recs))

setup_module()
test_readFile()
teardown_module()