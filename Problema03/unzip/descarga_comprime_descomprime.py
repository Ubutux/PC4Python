import requests
import os
import zipfile

os.chdir('/workspaces/PC4Python/Problema03/')
url = 'https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'

response = requests.get(url)
with open('imagen.jpg', 'wb') as f:
    f.write(response.content)
    pass

# creando un archivo zipeado
directory = '/workspaces/PC4Python/Problema03/'
files = os.listdir(directory)

with zipfile.ZipFile('archivos.zip', 'w') as zip:
    for file in files:
        file_path = os.path.join(directory, file)

        if os.path.isfile(file_path):
            zip.write(file_path
                      ,  os.path.basename(file_path) # para evitar subcarpetas
                      )
if not os.path.isdir('./unzip'): 
    os.mkdir('./unzip') 


# extración de archivos
with zipfile.ZipFile('archivos.zip', 'r') as zip_ref:
    zip_ref.extractall(path='./unzip')