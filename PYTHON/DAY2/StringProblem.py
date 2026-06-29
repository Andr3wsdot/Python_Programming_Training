n=input(" ")
se=len(n)//2
firstpart=n[:se] 
secondpart=n[se:]
revf=firstpart[::-1]
revs=secondpart[::-1]
print(revf+revs)
