#!/usr/bin/env python
# coding: utf-8

# <center>
#     <img src='http://torus.uck.pk.edu.pl/~amarsz/images/mooc/naglowek_power2.png', alt="Logo: Fundusze Europejskie Wiedza Edukacja Rozwój, Politechnika Krakowska, Unia Europejska Europejski Fundusz Spełeczny">
# </center><br><br>
# <center>
#     <font size="10">Programowanie w języku Python
#     </font>
# </center><br>
# <br><center><small>
# Projekt „MOoC Kodowania” nr POWR.03.01.00-00-W004/18-00<br/> realizowany w ramach Programu Operacyjnego Wiedza Edukacja Rozwój 2014-2020<br/>
# współfinansowany ze środków Europejskiego Funduszu Społecznego  
#     </small>
# </center>

# Przed rozpoczęciem pracy z notatnikiem zmień jego nazwę zgodnie z wzorem: `NazwaUzytkownika_Zadania_2`.
# 
# Przed wysłaniem notatnika upewnij się, że rozwiązałeś wszystkie zadania/ćwiczenia, w szczególności, że uzupełniłeś wszystkie pola `YOUR CODE HERE` oraz `YOUR ANSWER HERE`.

# ## Zadanie 1 (2pkt.)
# Napisz program, który dla wprowadzonej liczby naturalnej `n` sprawdzi czy liczba ta jest parzysta i wyświetli napis `parzysta` dla liczby `n` parzystej albo `nieparzysta` dla liczby `n` nieparzystej albo `niepoprawna liczba` gdy podana liczba bęzie z poza dopuszczalnego zakresu.
# 
# #### Przykładowo:
# Dla `n=3` wyświetli `nieparzysta`, dla `n=4` wyświetli `parzysta`, dla `n=-1`lub `n=2.4` wyświetli `niepoprawna liczba`

# In[1]:


n=-1
if n>0 and isinstance(n, int):
    if n%2!=0:
        print('Nieparzysta')
    else:
        print('Parzysta')
else:
    print('Niepoprawna liczba')




# ## Zadanie 2 (2pkt.)
# Napisz program, który spośród trzch podanych liczb `a, b, c` wybierze i wyświetli największą z nich.
# 
# #### Przykładowo:
# Dla `a=2, b=10, c=5` wyświetli liczbę `10` 

# In[6]:


a=11
b=1421
c=7
temp=0
if a>b:
    temp =a
else:
    temp =b
if temp<c:
    temp=c
print(temp)


# ## Zadanie 3 (2pkt.)
# Napisz program, który na zmiennej `kolejka` typu `list` wykona poniższe operacje zgodnie z algorytmem `FIFO`:
# - dodaj element o wartości `2` do kolejki,
# - dodaj element o wartości `4` do kolejki,
# - pobierz element z kolejki,
# - dodaj element `6` do kolejki,
# - pobierz element z kolejki,
# - dodaj elemeny `7` do kolejki.
# 
# #### Przykładowo:
# Poczatkowa lista postaci `kolejka = [2,4,5]` po wykonaniu powyższych operacji będzie wyglądać następująco: `[5,2,4,6,7]`

# In[10]:


kolejka =[]
kolejka.append(2)
kolejka.append(4)
kolejka.pop(0)
kolejka.append(6)
kolejka.pop(0)
kolejka.append(7)
print(kolejka)


# ## Zadanie 4 (1pkt.)
# Napisz program, który dla podanej listy `L`, zwróci nową listę, której elementami będą elementy listy `L` ale tylko te z nieparzystych pozycji. Uwaga: index 0 to pozycja 1. 
# 
# #### Przykładowo:
# Dla listy `L=[2,4,3,4,5,5,2,3]` zwróci listę: `[2,3,5,2]`

# In[40]:


L=[2,4,3,4,5,5,2,3]
l=len(L)
temp=[]

for i in range(0,l,2):
    temp.append(L[i])
print(temp)


# ## Zadanie 5 (1pkt.)
# Napisz program, który dla podanej listy `L`, zwróci nową listę, której elementami będą elementy listy `L` ale tylko te z parzystych pozycji. Uwaga: index 0 to pozycja 1. 
# 
# #### Przykładowo:
# Dla listy `L=[2,4,3,4,5,5,2,3]` zwróci listę: `[4,4,5,3]`

# In[41]:


L=[2,4,3,4,5,5,2,3]
l=len(L)
temp=[]

for i in range(1,l,2):
    temp.append(L[i])
print(temp)


# ## Zadanie 6 (2pkt.)
# Dla liczb naturalnych z przedziału $[m, k], m<k$ znajdź średnią arytmetyczną tych liczb, które są podzielne pezez zadaną liczbę naturalną $p$.
# 
# #### Przykładowo:
# Dla $m=2, k=9, p=3$ zwróci średnią arytmetyczną równą $6.0$

# In[3]:


m=2
k=9
p=3
temp1=0
temp2=0
for i in range(m,k+1,1):
    if i % p ==0:
        temp1=temp1+i
        temp2=temp2+1
        
wynik=temp1/(temp2)
print(wynik)
    


# ## Zadanie 7 (2pkt.)
# Dany jest przedział $[p1, p2]$ liczb naturalnych oraz liczba naturalna $p$ z jego wnętrza. Utwórz sumę liczb naturalnych z przedziału $[p1, p]$ oraz lioczyn pozostałych liczb.
# 
# #### Przykładowo:
# Dla $p1=2, p2=9, p=5$ zwróci sumę równą $14$ i iloczyn równy $3024$

# In[11]:


p1=2
p2=9
p=5
suma=0
iloczyn=1
for i in range(m,p+1,1):
    suma=suma+i
print(suma)
for i in range(p+1,p2+1,1):
    iloczyn=iloczyn*i
print(iloczyn)
    
       


# ## Zadanie 8 (2pkt.)
# Napisz program, który z dwóch zadanych liczb naturalnych $a$ i $b$ utworzy listę zawiarającą elementy $c$ będące elementami ciągu Fibonacciego wg algorytmu:
# $$\begin{array}{c}c=a+b\\a=b\\b=c\end{array}$$
# dopóki $c$ nie przekroczy wartości $(a+b)^3$, a następnie zwróci sumę wszystkich elementów utworzonej listy.
# 
# #### Przykładowo:
# Dla $a=2, b=4$ zwróci listę postaci `[6, 10, 16, 26, 42, 68, 110, 178]` oraz sumę równą $456$

# In[10]:


a=2
b=4
c=a+b
fib=[a,b,c]
temp1=a
temp2=b
while c<(temp1+temp2)**3:
    c=a+b
    a=b
    b=c
    fib.append(c)
   
print(fib)
print(sum(fib))
    
    


    


# <div style="text-align: right">&copy; Politechnika Krakowska im. Tadeusza Kościuszki </div>

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




