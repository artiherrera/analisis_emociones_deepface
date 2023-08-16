def process_video(video_path, output_path):
    # Leer el video
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    
    # Estructura para almacenar las emociones
    emotions = []

    frame_number = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            # Procesar la imagen con DeepFace
            result = DeepFace.analyze(frame, actions=['emotion'])
            
            # Calcular el tiempo del frame actual
            time_seconds = frame_number / fps

            # Agregar las emociones al registro junto con el número de frame y el tiempo
            emotion_record = {'frame_number': frame_number, 'time_seconds': time_seconds, **result['emotion']}
            emotions.append(emotion_record)

            frame_number += 1
        else:
            break

    # Crear un DataFrame con las emociones y guardarlo como CSV
    emotions_df = pd.DataFrame(emotions)
    emotions_df.to_csv(output_path, index=False)

    cap.release()
    cv2.destroyAllWindows()