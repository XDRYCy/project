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

# Przed rozpoczęciem pracy z notatnikiem zmień jego nazwę zgodnie z wzorem: `NazwaUzytkownika_Zadania_3`.
# 
# Przed wysłaniem notatnika upewnij się, że rozwiązałeś wszystkie zadania/ćwiczenia, w szczególności, że uzupełniłeś wszystkie pola `YOUR CODE HERE` oraz `YOUR ANSWER HERE`.

# ## Zadanie 1 (2pkt.)
# Napisz program, który dla dwóch zbiorów danych $s_1=\{1,2,3,4\}$ oraz $s_2=\{3,4,5,6\}$ wyświetli:
# 
# - elementy obu zbiorów (bez powtórzeń),
# - elementy wspólne dla obu zbiorów,
# - elementy zbioru $s_1$ nie będące elementami zbioru $s_2$,
# - elementy zbioru $s_2$ nie będące elementami zbioru $s_1$.

# In[21]:


s1={1,2,3,4}
s2={3,4,5,6}
suma=s1|s2
iloczyn=s1&s2
roznica1=s1-s2
roznica2=s2-s1

print("suma:", suma)
print("iloczyn:", iloczyn)
print("roznica1:", roznica1)
print("roznica2:", roznica2)


# # Zadanie 2 (3pkt.)
# Wykorzystując słownik napisz translator tekstu na alfabet Mors'a.
# Szczegółowe informacje znajdzisze pod linkiem: http://alfabetmorsa.pl/.
# Przetłumacz poniższy tekst. Załóżmy, że znakiem rozdzielającym słowa w alfabecie Morse'a jest znak `/`.

# In[33]:


litery = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U',
          'V','W','X','Y','Z',' ']
mors = ['•-','-•••','-•-•','-••','•','••-•','--•','••••','••','•---','-•-','•-••','--','-•',
        '---','•--•','--•-','•-•','•••','-','••-','•••-','•--','-••-','-•--','--••','/']
tekst = 'Matematyka i informatyka jest super'

tlumacz={
    
    'a': '•-', 
    'b': '-•••', 
    'c': '-•-•', 
    'd': '-••', 
    'e': '•', 
    'f': '••-•', 
    'g': '--•', 
    'h': '••••', 
    'i': '••', 
    'j': '•---', 
    'k': '-•-', 
    'l': '•-••', 
    'm': '--', 
    'n': '-•', 
    'o': '---', 
    'p': '•--•', 
    'q': '--•-', 
    'r': '•-•', 
    's': '•••', 
    't': '-', 
    'u': '••-', 
    'v': '•••-', 
    'w': '•--', 
    'x': '-••-', 
    'y': '-•--', 
    'z': '--••',
    ' ': '/'
    
}
kod=''

for k in tekst.lower():
        kod +=tlumacz[k]
print(kod)
        


# ## Zadanie 3 (3pkt.)
# Uzupełnij poniższy program, tak aby wypisywał tekstowy komunikat o wyniku dzielenia liczb `x` i `y` lub o ewentualnym błędzie (z informacją o szczegółach błędu). Program powinien być odporny na błędy niezależnie od przekazanych argumentów. Jeśli nie będzie błedów w dzieleniu, wybisz `brak błędów`. Skorzytaj z mechanizmu obsługi wyjątków i klauzuli `try`.

# In[4]:


while True:
    try:
        x = float(input("Podaj liczbę x "))
    except ValueError:
        print("Błędna wartość")
    except Exception as e:
        print("Błąd",e._class_)
        
    else:
        break
while True:    
    try:
        y = float(input("Podaj liczbę y "))
        z=x/y
    except ValueError:
        print("Błędna wartość")
    except ZeroDivisionError:
        print("Nie dziel przez zero")
    except Exception as e:
        print("Błąd",e._class_)   
    else:
        break
    
print("Brak błędów w dzieleniu")
print(z)


# <div style="text-align: right">&copy; Politechnika Krakowska im. Tadeusza Kościuszki </div>

# In[ ]:




