diccionario={'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7,'Maite': 5}
lista=[]
for i in diccionario:
    lista.append(diccionario[i])
    x=list(set(lista))
print(x)