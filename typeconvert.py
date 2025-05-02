"""Converssão de tipos imutáveis e primitivos"""

print(int('1'),type(int('1')))
print(int('1')+int('1'))
print(type(int('1')+float('1')))
print(type(int('1')+1))

"""O mesmo  se aplica para concatenar STR com INT
basta converter INT em STR"""
print(str(11)+ 'B')

"""Em converssão do type bool, o  vazio é TRUE e a ausência
de caracter ou espaço é resultante em FALSE"""
print(bool(' ')) #=TRUE
print(bool('')) #=FALSE
print(bool('X')) #=TRUE
