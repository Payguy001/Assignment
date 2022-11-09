from seqbio.calculation.SeqCal import gcContent, countBasesDict
from seqbio.pattern.SeqPattern import enzTargetsScan
from seqbio.seqMan.dnaconvert import dna2protein, dna2rna, reverseComplementSeq
from seqbio.pattern.SeqPattern import cpgSearch
# print("in Main.py")

def argparserLocal():
    from argparse import ArgumentParser
    '''Argument parser for the commands'''
    parser = ArgumentParser(prog='myseq', description='Work with sequence')
    parser._optionals.title = 'optional arguments' #change the word title

    subparsers = parser.add_subparsers(
        title='commands', description='Please choose command below:',
        dest='command'
    )
    subparsers.required = True

    cgc_command = subparsers.add_parser('gcContent', help='Calculate GC content')
    cgc_command.add_argument("-s", "--seq", type=str, default=None, dest='seq',
                             help="Provide sequence")

    count_command = subparsers.add_parser('countBases', help='Count number of each base')
    count_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    count_command.add_argument("-r", "--revcomp", action = 'store_true',
                             help="Convet DNA to reverse-complementary")    

    # cgcserch_command = subparsers.add_parser('cpgScan', help='Search for CpG sequence')
    # cgcserch_command.add_argument("-s", "--seq", type=str, default=None,
    #                          help="Provide sequence")

    transcript_command = subparsers.add_parser('transcription', help='Convert DNA->RNA')
    transcript_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    transcript_command.add_argument("-r", "--revcomp", action = 'store_true',
                             help="Convet DNA to reverse-complementary")
       
    translate_command = subparsers.add_parser('translation', help='Convert DNA->Protein')
    translate_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    translate_command.add_argument("-r", "--revcomp", action = 'store_true',
                             help="Convet DNA to reverse-complementary")
    # parser.print_help()
    enzTargetsScan_command = subparsers.add_parser('enzTargetsScan', help='Find restriction enzyme')
    enzTargetsScan_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    enzTargetsScan_command.add_argument("-e", "--enz", type=str, default=None,
                             help="Enzyme name")    
    enzTargetsScan_command.add_argument("-r", "--revcomp", action = 'store_true',
                             help="Convet DNA to reverse-complementary")
    return parser

def test():
    # Input
    parser = argparserLocal()
    args = parser.parse_args(["cpgScan","-s","AAATTTCCCGGGCGGGGG"])
    print(args)
    print(cpgSearch(args.seq))
    
def main():
    parser = argparserLocal()
    args = parser.parse_args()
    # print(args)
    # print(args.cmd, args.seq)
    # print("Input",args.seq,"\nGC content =", gcContent(args.seq) )

    # if args.seq == None:
    #     print("------\nError: You do not provide -s or --seq\n------\n")
    # else:
    # seq = args.seq.upper()
    # # Input
    # # seq = 'ATGGGccGTAGAATTCTTGCaaGCCCGT'

    if args.command == 'gcContent':
        if args.seq == None:
            exit(parser.parse_args(['gcContent','-h']))
        seq = args.seq.upper()
        print("Input",args.seq,"\nGC content =", gcContent(seq) )

    elif args.command == 'countBases':
        if args.seq == None:
            exit(parser.parse_args(['countBases','-h']))
        if(args.revcomp): seq = reverseComplementSeq(args.seq.upper())
        else : seq = args.seq.upper()
        print("Input",args.seq,"\ncountBases =", countBasesDict(seq) )

    # elif args.command == 'cpgScan':
    #     if args.seq == None:
    #         exit(parser.parse_args(['cpgScan','-h']))
    #     seq = args.seq.upper()
    #     print("Input",args.seq,"\ncpgScan =", cpgSearch(seq) )    

    elif args.command == 'transcription':
        if args.seq == None:
            exit(parser.parse_args(['transcription','-h']))
        if(args.revcomp): seq = reverseComplementSeq(args.seq.upper())
        else : seq = args.seq.upper()
        print("Input",args.seq,"\nTranscription =", dna2rna(seq) )   

    elif args.command == 'translation':
        if args.seq == None:
            exit(parser.parse_args(['translation','-h']))
        if(args.revcomp): seq = reverseComplementSeq(args.seq.upper())
        else : seq = args.seq.upper()
        print("Input",args.seq,"\nTranslation =", dna2protein(seq) )
    
    elif args.command == 'enzTargetsScan':
        if args.seq == None:
            exit(parser.parse_args(['enzTargetsScan','-h']))
        
        if(args.revcomp): seq = reverseComplementSeq(args.seq.upper())
        else : seq = args.seq.upper()

        enz = args.enz
        print("Input",args.seq,"\n", enz, "sites =", enzTargetsScan(seq, enz))
            
# print(__name__)
if __name__ == "__main__":
    test()



