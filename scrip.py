

from os import lseek


with open("source/DNA_sam", "r") as DNA_fn:
    DNA_sam = DNA_fn.read()

with open("source/DNA_res_sam", "r") as DNA_res_sam_fn:
    DNA_resseq = DNA_res_sam_fn.read()

i = 0
lst = []

DNA_resseq = DNA_resseq.replace('\n', '')
DNA_resseq_lst = DNA_resseq.split(';')
DNA_resseq_lst.remove('')



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
    
print(lst)