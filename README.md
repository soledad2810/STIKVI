# STIKVI: A Smart Stick to Improve Navigation of Visually Impaired People
----------------------------------------------------------------------------------------------------------------------------------------------------
## Información del grupo
1. Equipo:

    * Soledad Zarai Fernandez Arbieto
    * Kiara Micaela Rodriguez Bautista
----------------------------------------------------------------------------------------------------------------------------------------------------
## Creación del dataset de semáforos peatonales
1. Recopilación de 285 imágenes de semáforos peatonales usando [Google Maps](https://www.google.com/maps/).
2. Etiquetado de la data recopilada en dos clases (verde-rojo) usando la aplicación labelImag. 
3. Incremento de la cantidad de imágenes a 528, usando distintas técnicas de preprocesamiento en la plataforma de [Roboflow](https://roboflow.com/).

Dataset de Semáforos peatonales: [Pedestrian Light Detector](https://app.roboflow.com/project/pedestrian-light-detector/)

----------------------------------------------------------------------------------------------------------------------------------------------------
## Entrenamiento del modelo de detección de semáforos peatonales usando YOLOv4-tiny

1. Entrenamiento con el dataset customizado usando el modelo de detección de objetos: [tiny-yolov4](https://colab.research.google.com/drive/15yqB8ZAWhU3Fr8VAyBKz_ulPvkPD-aUL?authuser=2#scrollTo=IO5LMU5wCPJB).

2. El script en mención nos devolverá dos archicos importante:

    * custom-yolov4-tiny-detector.cfg
    * custom-yolov4-tiny-detector_best.weights

   Los cuales se encuentran en la carpeta [Acuraccy92.13_](https://github.com/soledad2810/STIKVI/tree/main/Acuraccy%2092.13_).
   El archivo .cfg contiene la estructura de la red de entrenamiento, por otro lado, el archivo archivo .weights contiene los nuevos pesos del modelo.
   
   Ambos archicos son importantes para desarrollar el script de detección de semáforos peatonales en tiempo real en OpenCV.

