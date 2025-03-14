import cv2
import mediapipe as mp

# تحميل نموذج كشف الوجه والمعالم
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

# تشغيل الكاميرا
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # تحويل الصورة إلى RGB لأن Mediapipe يستخدم RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # استخراج معالم الوجه
    results = face_mesh.process(rgb_frame)
    
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            for idx, landmark in enumerate(face_landmarks.landmark):
                h, w, c = frame.shape
                x, y = int(landmark.x * w), int(landmark.y * h)
                
                # رسم النقاط على العين فقط (نقاط محددة للعين)
                if idx in [33, 133, 160, 144, 145, 153, 362, 263, 387, 373, 374, 380]:
                    cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)
    
    cv2.imshow('Eye Tracking', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
