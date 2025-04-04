import cv2
import os

def recortar_video(input_path, output_path, largura_crop=500, altura_crop=500):
    cap = cv2.VideoCapture(input_path)

    if not cap.isOpened():
        print(f"Erro ao abrir o vídeo: {input_path}")
        return

    largura_total = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    altura_total = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Coordenadas para centralizar o recorte
    x_inicio = (largura_total - largura_crop) // 2
    y_inicio = (altura_total - altura_crop) // 2 - 50

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (largura_crop, altura_crop))

    for _ in range(total_frames):
        ret, frame = cap.read()
        if not ret:
            break
        crop = frame[y_inicio:y_inicio + altura_crop, x_inicio:x_inicio + largura_crop]
        out.write(crop)

    cap.release()
    out.release()
    print(f"✔️ {os.path.basename(output_path)} salvo com sucesso!")

def processar_pasta(caminho_pasta, largura_crop=500, altura_crop=500):
    saida_dir = os.path.join(caminho_pasta, "recortados")
    os.makedirs(saida_dir, exist_ok=True)

    for nome_arquivo in os.listdir(caminho_pasta):
        if nome_arquivo.lower().endswith((".mp4", ".mov", ".avi", ".mkv")):
            caminho_video = os.path.join(caminho_pasta, nome_arquivo)
            caminho_saida = os.path.join(saida_dir, f"recortado_{nome_arquivo}")
            recortar_video(caminho_video, caminho_saida, largura_crop, altura_crop)

if __name__ == "__main__":
    # Substitua pelo caminho onde seus vídeos estão salvos
    pasta_dos_videos = "./videos"
    processar_pasta(pasta_dos_videos)