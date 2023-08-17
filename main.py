import tkinter as tk
from tkinter import filedialog
from deepface import DeepFace
import cv2
import pandas as pd

def process_video(video_path, output_path, id_usuario, id_video):
    print("Procesando video:", video_path)

    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    emotions = []
    frame_number = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            result = DeepFace.analyze(frame, actions=['emotion'])
            time_seconds = frame_number / fps
            emotion_data = result[0]['emotion']
            emotion_record = {'id_usuario': id_usuario, 'id_video': id_video, 'frame_number': frame_number, 'time_seconds': time_seconds, **emotion_data}
            emotions.append(emotion_record)
            frame_number += 1
        else:
            break

    emotions_df = pd.DataFrame(emotions)
    emotions_df.to_csv(output_path, index=False)

    cap.release()
    cv2.destroyAllWindows()

    print("Procesamiento completo. Resultados guardados en:", output_path)

def select_and_process_video():
    print("Iniciando la selección de video...")

    root = tk.Tk()
    root.withdraw()
    video_path = filedialog.askopenfilename(title="Selecciona el video")
    print("Video seleccionado:", video_path)

    output_path = filedialog.asksaveasfilename(title="Guardar como", defaultextension=".csv", filetypes=[("Archivos CSV", "*.csv")])

    id_usuario = input("Por favor, ingrese el ID de usuario que desea asignar: ") # Pide al usuario el ID de usuario
    id_video = input("Por favor, ingrese el ID de video que desea asignar: ") # Pide al usuario el ID de video

    if video_path and output_path:
        process_video(video_path, output_path, id_usuario, id_video)
    else:
        print("Operación cancelada.")

if __name__ == "__main__":
    select_and_process_video()
