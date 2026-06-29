N= int(input(" "))
c1=N//100
N=N%100
c2=N//50
N=N%50
c3=N//20
N=N%20
c4=N//10
N=N%10
c5=N//5
N=N%5
c6=N//2
N=N%2
c7=N//1
N=N%1
sum=c1+c2+c3+c4+c5+c6+c7
print(sum)

