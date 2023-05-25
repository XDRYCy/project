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

# Przed rozpoczęciem pracy z notatnikiem zmień jego nazwę zgodnie z wzorem: `NazwaUzytkownika_Zadania_1`.
# 
# Przed wysłaniem notatnika upewnij się, że rozwiązałeś wszystkie zadania/ćwiczenia, w szczególności, że uzupełniłeś wszystkie pola `YOUR CODE HERE` oraz `YOUR ANSWER HERE`.

# ## Zadanie 1 (2pkt.)
# Napisz program, który dla dwóch liczb rzeczywistych zapisanych w zmiennych `x` i `z` typu `float`, oraz dwóch liczb całkowitych zapisanych w zmiennych `i` i `j` typu `int` oblicz wartość następujących wyrażeń arytmetycznych i zapisze je do zmiennych `v` i `y`:
# $$v=\frac{\ln{x^2}+2x^2+z^{-2}}{(x+z)i}+\frac{i}{j}$$
# $$y=\frac{x\ln{(x^2+1)}}{2}\sin^2{(2x^2-1)}$$
# 
# #### Przykładowo:
# Dla $x=1.5, z=2.3, i=2, j=3$ wyrażenia te mają wartość:
# $v = 1.3903464210141043, y = 0.10877412656500485$

# In[30]:


import math
x,z=1.5,2.3
i,j=2,3
v=(math.log(x**2)+2*x**2+z**(-2))/((x+z)*i) +i/j
print(v)
y=(x*math.log(x**2+1)/2)*(math.sin(2*x**2-1))**2
print(y)


# ## Zadanie 2 (2pkt.)
# Napisz program, który zaokrągli podaną liczbę `x` w górę do podanej liczby miejsc po przecinku `n`.
# 
# #### Przykładowo:
# Dla $x=2.444$ i $n=2$ zwróci liczbę: $2.45$

# In[39]:


x=2.444
n=2
print(math.ceil(x *10**n) / 10**n)


# ## Zadanie 3 (1pkt.)
# Napisz program, który we wprowadzonym tekscie wyeliminuje pierwsze wystąpienie podanego znaku. Zakładamy, że podany znak na pewno występuje w tekscie.
# 
# #### Przykładowo:
# Dla tekstu `'przykładowy tekst'` i znaku `'y'` zwróci: `'przkładowy tekst'`

# In[7]:


znak='y'
tekst='przykładowy tekst'

index=tekst.index(znak)
nowy_tekst=tekst[:index]+tekst[index+1:]
print(nowy_tekst)


# ## Zadanie 4 (1pkt.)
# Napisz program, który we wprowadzonym tekscie wyeliminuje ostatnie wystąpienie podanego znaku. Zakładamy, że podany znak na pewno występuje w tekscie.
# 
# #### Przykładowo:
# Dla tekstu `'przykładowy tekst'` i znaku `'y'` zwróci: `'przykładow tekst'`

# In[8]:


znak='y'
tekst='przykładowy tekst'

index=tekst.rindex(znak)
nowy_tekst=tekst[:index]+tekst[index+1:]
print(nowy_tekst)


# ## Zadanie 5 (2pkt.)
# Dane są dwa teksty. Napisz program, który dołączy fragment tekstu pierwszego od znaku o podanej pozycji na koniec tekstu drugiego oraz poda liczbę słów w nowo utworzonym tekscie. Zakładamy, że słowa rozdziela spacja `(' ')`.
# 
# #### Przykładowo:
# Dla tekstów `t1 = 'przykładowy tekst 1'`, `t2 = 'przykładowy tekst 2'` i pozycji `4` zwróci tekst: `'przykładowy tekst 2kładowy tekst 1'` oraz liczbę słów `5`

# In[10]:


znak='y'
tekst1='przykładowy tekst1'
tekst2='przykładowy tekst2'

i=4

nowy_tekst=tekst1+tekst2[i:]
print(nowy_tekst)


# ## Zadanie 6 (2pkt.)
# Napisz program, który korzystając ze zmiennej `data`, w której przechowywana jest data w formacie `rrrr-mm-dd` (np. 2019-11-04), utworzy trzy nowe zmienne `rok`, `miesiac`, `dzien` i przypisze im odpowiednie wartości jako liczby całkowite.

# In[20]:


data='2023-04-4'
rok=int(data[:4])
miesiac=int(data[5:7])
dzien=int(data[8:])

print(data, rok, miesiac, dzien)


# <div style="text-align: right">&copy; Politechnika Krakowska im. Tadeusza Kościuszki </div>
