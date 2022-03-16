import os
import inquirer
import hashlib
# Creado por sebastian Nicolas
print("Creando el hash de un archivo")
CurrentDir = os.listdir('.')

elegirArchivo = [
    inquirer.List('archivoElegido',
        message="Elige el archivo",
        choices= CurrentDir,
        ),
]
elArchivo = inquirer.prompt(elegirArchivo)['archivoElegido']
print(elArchivo)

TipoDeHash = [ 
        inquirer.List('tipos',
            message="Que hash desea?",
            choices=['md5','sha1','sha512'],
            ),
        ]
hashElegido = inquirer.prompt(TipoDeHash)['tipos']


print(f'El {hashElegido} del archivo es:')
## workplace now
print(f'El hash que se a escogido y contatenado es {hashElegido}')

#toPrintInFile = hashlib.md5(answers["theFile"].encode('UTF-8')).hexdigest()
#la opcion multiple aparece
#toPrintInFile = hashlib.md5(open(elArchivo,'rb').read()).hexdigest()
#ejempplo ^
if hashElegido == 'md5':
    global toPrintInFile
    toPrintInFile = hashlib.md5(open(elArchivo,'rb').read()).hexdigest()
elif hashElegido == 'sha1':
    toPrintInFile = hashlib.sha1(open(elArchivo,'rb').read()).hexdigest()
elif hashElegido == 'sha512':
    toPrintInFile = hashlib.sha512(open(elArchivo,'rb').read()).hexdigest()

print(toPrintInFile)



#la opcion multiple acaba
guardar = [ 
        inquirer.List('sino',
            message='Deseas guardar?',
            choices=['Sip','No guardes'],
            ),
        ]
seGuardara = inquirer.prompt(guardar)
if seGuardara["sino"] == 'Sip':
    print("Guardando Archivo")

    askNombreDelArchivo = [
        inquirer.Text('name', message="Cual sera el nombre del archivo (agregar al final .txt)"),
    ]

    elNombreDelArchivo = inquirer.prompt(askNombreDelArchivo)
    print(elNombreDelArchivo["name"])
    
    # Aqui empieza la creacion del archivo
    # elNombreDelArchivo["name"]
    # toPrintInFile es lo que debes escribir
    file = open(elNombreDelArchivo["name"], "w")
    file.write(toPrintInFile)
    file.close
else:
    print(f'ok, no se guardara el {hashElegido}')
