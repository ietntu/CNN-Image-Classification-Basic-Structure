from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator

model_basic = load_model('C:/Users/Luo Jinqi/Desktop/IET IC Workshop/result_parameters.h5')

datagen_test = ImageDataGenerator(rescale=1. / 255)

test_data = datagen_test.flow_from_directory (
    directory = 'C:/Users/Luo Jinqi/Desktop/IET IC Workshop/Your own images/BabyShirt',
    target_size = (150, 150),
    class_mode = None,
    shuffle = False,
    batch_size = 200)

print(test_data.class_indices)
print(test_data.filenames)

scores = model_basic.predict_generator(test_data)
y_pred = [round(score[0]) for score in scores]
print(y_pred)
