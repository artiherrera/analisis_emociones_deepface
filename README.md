# Análisis de Emociones en Videos

Este proyecto utiliza DeepFace para analizar las emociones en un video. El script procesa un video y guarda los resultados en un archivo CSV, incluyendo información como el número de fotograma, los segundos en el tiempo, y las emociones detectadas.

## Requisitos

- Python 3.7 o superior
- Bibliotecas: \`tkinter\`, \`cv2\`, \`pandas\`, \`DeepFace\`

Puedes instalar las bibliotecas requeridas utilizando el siguiente comando:

\`\`\`bash
pip install opencv-python pandas deepface
\`\`\`

## Cómo Ejecutar

1. **Clonar el Repositorio:** Clona este repositorio en tu máquina local utilizando \`git clone <URL_DEL_REPOSITORIO>\`.

2. **Navegar al Directorio:** Navega al directorio donde se encuentra el script en la terminal.

3. **Ejecutar el Script:** Ejecuta el siguiente comando para iniciar el script:

   \`\`\`bash
   python nombre_del_script.py
   \`\`\`

4. **Seleccionar el Video:** Se abrirá una ventana para que selecciones el video que deseas analizar.

5. **Guardar los Resultados:** Se abrirá otra ventana para que selecciones dónde guardar el archivo CSV con los resultados.

6. **Revisar los Resultados:** Una vez que el script haya terminado de ejecutar, encontrarás el archivo CSV en la ubicación seleccionada.

## Información Adicional

- **ID del Usuario y del Video:** El script te pedirá que ingreses un ID de usuario y un ID de video que se guardarán junto con los resultados.

- **Emociones Analizadas:** Las emociones analizadas incluyen felicidad, tristeza, sorpresa, miedo, disgusto, ira y neutralidad.

- **Limitaciones:** Solo se puede analizar un video en el que se muestre una sola cara. 

