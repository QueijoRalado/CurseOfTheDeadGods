import os
import subprocess
import cv2

def recortar_e_converter(input_path, output_path, largura_crop=500, altura_crop=500):
    cap = cv2.VideoCapture(input_path)

    if not cap.isOpened():
        print(f"Erro ao abrir o vídeo: {input_path}")
        return

    largura_total = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    altura_total = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    x_inicio = (largura_total - largura_crop) // 2
    y_inicio = (altura_total - altura_crop) // 2 - 50

    # Salvar temporariamente antes de converter
    temp_output = output_path.replace(".mp4", "_temp.mp4")
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(temp_output, fourcc, fps, (largura_crop, altura_crop))

    for _ in range(total_frames):
        ret, frame = cap.read()
        if not ret:
            break
        crop = frame[y_inicio:y_inicio + altura_crop, x_inicio:x_inicio + largura_crop]
        out.write(crop)

    cap.release()
    out.release()

    # Agora converte usando ffmpeg para formato compatível com web
    final_output = output_path
    comando = [
        "ffmpeg",
        "-y",
        "-i", temp_output,
        "-vcodec", "libx264",
        "-acodec", "aac",
        "-movflags", "+faststart",
        final_output
    ]

    try:
        subprocess.run(comando, check=True)
        os.remove(temp_output)  # Remove o arquivo temporário
        print(f"✔️ {os.path.basename(final_output)} salvo e convertido com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao converter vídeo com FFmpeg: {e}")

def processar_pasta(caminho_pasta, largura_crop=500, altura_crop=500):
    saida_dir = os.path.join(caminho_pasta, "recortados")
    os.makedirs(saida_dir, exist_ok=True)

    for nome_arquivo in os.listdir(caminho_pasta):
        if nome_arquivo.lower().endswith((".mp4", ".mov", ".avi", ".mkv")):
            caminho_video = os.path.join(caminho_pasta, nome_arquivo)
            caminho_saida = os.path.join(saida_dir, f"recortado_{nome_arquivo}")
            recortar_e_converter(caminho_video, caminho_saida, largura_crop, altura_crop)

if __name__ == "__main__":
    pasta_dos_videos = "./videos"
    processar_pasta(pasta_dos_videos)
