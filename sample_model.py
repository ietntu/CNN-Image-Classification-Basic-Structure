
###################################################################

# coding: utf-8
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Conv1D, MaxPooling1D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img


datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

###################################################################

batch_size = 128

# this is the augmentation configuration we will use for training
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.12,
        zoom_range=0.12,
        horizontal_flip=True
        )

# this is the augmentation configuration we will use for testing:
test_datagen = ImageDataGenerator(rescale=1./255)

###################################################################

# Below is a generator that will read pictures found in
# subfolers of 'Training_Images', and indefinitely generate
# batches of augmented image data. Each batch is of size 128.
train_generator = train_datagen.flow_from_directory(
        "C:/Users/xxx/Desktop/IET IC Workshop/Training Images",  # this is the target directory
        target_size=(100, 100),  # all images will be resized to 100x100
        batch_size=batch_size,
        class_mode='categorical')  

# this is a similar flow-in, for validation data
validation_generator = test_datagen.flow_from_directory(
        'C:/Users/xxx/Desktop/IET IC Workshop/Validation Images',
        target_size=(100, 100),
        batch_size=batch_size,
        class_mode='categorical')

###################################################################

model = Sequential()

model.add(Conv2D(100, (3, 3), input_shape=(100, 100, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(3, 3)))

model.add(Conv2D(100, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(200, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
model.add(Dense(64))

model.add(Activation('relu'))

model.add(Dropout(0.5))
model.add(Dense(3)) #3 types of images

model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

###################################################################

bacth_size = 128

model.fit_generator(
        train_generator,
        steps_per_epoch=30000// batch_size,
        epochs=3,
        validation_data=validation_generator,
        validation_steps=30000 // batch_size)
model.save_weights('result_parameters.h5')




