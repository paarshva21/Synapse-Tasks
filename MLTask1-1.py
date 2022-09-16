modern_family = ["CLaiRe_DunPhY", "PHiL_dUnpHY", "GLoRiA_PriTCheTt", "CaMErOn_TuCKEr","StELLa"]
indices,characters=[],[]
for index,value in enumerate(modern_family):
    value=value.replace("_","-")
    indices.append(index)
    characters.append(value.lower())
f=lambda x: len(x)
temp=list(map(f,characters))
indices=list(zip(temp,indices))
for i in range(len(indices)):
    indices[i]=sum(indices[i])
indices.sort()
indices.reverse()
Phew_finally={}
for j in range(len(indices)):
   Phew_finally[indices[j]]=[characters[j]]
print(Phew_finally)