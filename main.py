acid_table = [
             ["TTT", "TTC"], ["TTA", "TTG", "CTT", "CTC", "CTA", "CTG"], ["ATT", "ATC", "ATA"], ["ATG"], ["GTT", "GTC", "GTA", "GTG"],
             ["TCT", "TCC", "TCA", "TCG"], ["CCT", "CCC", "CCA", "CCG"], ["ACT", "ACC", "ACA", "ACG"], ["GCT", "GCC", "GCA", "GCG"],
             ["TAT", "TAC"], ["TAA", "TAG"], ["CAT", "CAC"], ["CAA", "CAG"], ["AAT", "AAC"], ["AAA", "AAG"], ["GAT", "GAC"], ["GAA", "GAG"],
             ["TGT", "TGC"], ["TGA"], ["TGG"], ["CGT", "CGC", "CGA", "CGG", "AGA", "AGG"], ["AGT", "AGC"], ["GGT", "GGC", "GGA", "GGG"]
             ]

OWN_DNA = False

with open("source/DNA.txt", "r") as DNA_fn:
    DNA_sam = DNA_fn.read()

with open("source/DNA_res_sam", "r") as DNA_res_sam_fn:
    DNA_resseq = DNA_res_sam_fn.read()



lst = []
i = 0

print("--- DNA Restrictive Sequence Hidder V.0 ---")
print("Please, provide us with the path to a file with DNA (if left blank, a DNA file in source/DNA.txt path will be used)")

usr1 = input()

if len(usr1) > 0:
    try:
        fn = open(usr1, 'r')
        DNA_sam = fn.read()
    except:
        print("The file does not exist. Try again")
        quit()



DNA_resseq = DNA_resseq.replace('\n', '')
DNA_resseq_lst = DNA_resseq.split(';')
DNA_resseq_lst.remove('')
DNA_sam = DNA_sam.replace('\n', '')

print("Here are default restrictive sequences: \n")
for seq in DNA_resseq_lst:
    print(seq)

print("\nDo you wish to add more? (y/n)")
usr2 = input() 

if usr2.lower() == 'y':
    print('Input sequences you want to add. Every sequence must be separate by ')

for i_resseq, resseq in enumerate(DNA_resseq_lst):
    while True:
        if i == 0:
            i = DNA_sam.find(resseq, 0)   
        else:
            i = DNA_sam.find(resseq, i + 1)

        if i == -1:
            break
        
        lst.append((i, i_resseq))

        if i == 0:
            i = 1
    
new_sam = list(DNA_sam)

for inx_dna, inx_resseq in lst:

    cod_start = inx_dna - (inx_dna % 3)
    resseq = DNA_resseq_lst[inx_resseq]
    inx_dnaend = len(resseq) + inx_dna - 1
    cod_end = inx_dnaend - (inx_dnaend % 3) + 2
    codons_str = DNA_sam[cod_start:cod_end + 1]
    
    codons_lst = []
    codon_temp = []
    for i_gen, gen in enumerate(codons_str):
        codon_temp.append(gen)
        if not (i_gen + 1) % 3:
            codons_lst.append(''.join(codon_temp))
            codon_temp = []

    
    codon_changed = False
    new_codons_lst = []

    for codon_i, codon in enumerate(codons_lst):
        new_codon = codon
        for acid in acid_table:
            if codon in acid:

                if len(acid) == 1 or codon_changed or not codon_i:
                    break
                
                temp_lst = acid.copy()
                temp_lst.remove(codon)
                new_codon = temp_lst[0]
                codon_changed = True

        new_codons_lst.append(new_codon) 

    new_codons = ''.join(new_codons_lst)

    new_sam[cod_start:cod_end + 1] = new_codons
    print("success")
    
    # print("inx_dna: {}, resseq: {}, inx_dnaend: {}, cod_start: {}, cod_end: {}, codons: {}, codons list: {}, new codons lst: {}, "
    #         .format(inx_dna, resseq, inx_dnaend, cod_start, cod_end, codons_str, codons_lst, new_codons, new_sam[cod_start:cod_end + 1]))

new_sam = ''.join(new_sam)

with open("results/DNA_results", "w") as res:
    res.write(new_sam)