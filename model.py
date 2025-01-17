from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

def get_class(model, labels, image):
  np.set_printoptions(suppress=True)
  model = load_model(model, compile=False)
  class_names = open(labels, "r").readlines()

  data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

  image = Image.open(image).convert("RGB")

  size = (224, 224)
  image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

  image_array = np.asarray(image)

  normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

  data[0] = normalized_image_array


  prediction = model.predict(data)
  index = np.argmax(prediction)
  class_name = class_names[index]
  confidence_score = prediction[0][index]


  bird = class_name[2:].strip()
  msg2 = "Wykryto obiekt z dokładnością: " + confidence_score
  if bird == 'Sparrows':
        msg = 'Oto co możesz podać gołębiom: ciecierzyca, pszenica, jęczmień, nasiona, kasza gryczana, proso, groch, soczewica i inne zboża w suchej postaci.'

  elif bird == 'Pigeons':
        msg = "Oto, co możesz dać wróblom: popękaną kukurydzę, ziarna zbóż, owies, pszenicę, ryż i suszone owady."

  return(msg,msg2)