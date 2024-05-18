from deepface import DeepFace

def analyzeWithAll():
    try:
            backends = [
                'opencv', 
                'ssd', 
                'mtcnn', 
                'fastmtcnn',
                'retinaface', 
                'mediapipe',
                'yolov8',
                'yunet',
                'centerface',
            ]
            results = []
            for backend in backends:
                demography = DeepFace.analyze("image.jpg",detector_backend=backend)
                results.append({backend: demography})

            return print(results)
    except Exception as e:
        print(str(e))

analyzeWithAll()