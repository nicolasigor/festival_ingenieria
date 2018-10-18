Al ejecutar el script super_interface.py, se abre una pequeña ventana que permite abrir las demos. Cuando otra demo se abre, el programa automáticamente cierra los procesos anteriormente ejecutados. Ocupa python 3.


INSTRUCCIONES:

Para configurar el super_interface, hay que editar el archivo 'config_demos.json'

El valor de "python_path" debe ser el path de python dentro del ambiente virtual de anaconda a utilizar (fijarse en el ejemplo en mi computador). Este será el python utilizado cada vez que se ejecute "python" en los comandos (no hay que escribir "source activate my_env" en los comandos).

El valor de "wait_seconds_between_commands" debe ser igual al número de segundos que se debe esperar antes de ejecutar el siguiente comando cuando la lista de comandos tiene más de un elemento (el caso de Glow). Dejé este parámetro por si es importante que se espere un tiempo. Si no es importante se puede configurar en 0.

"demos" es la lista de demos a utilizar. Ya tiene 3 elementos con sus respectivos nombres (el valor de "name"). Para cada demo hay que especificar la lista de comandos que se deben ejecutar (o sea, una lista de 3 para Glow, y una lista de 1 para los otros dos). El programa trae unas demos sintéticas para ejemplificar su uso. Los path son relativos a la carpeta desde la que se ejecuta super_interface.py.