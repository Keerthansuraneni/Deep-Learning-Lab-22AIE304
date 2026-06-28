from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

X=np.array([[0,0],[0,1],[1,0],[1,1]])
y=np.array([0,1,1,0])
model=Sequential([
    Dense(8,activation="relu",input_shape=(2,)),
    Dense(1,activation="sigmoid")
])
model.compile(optimizer="adam",loss="binary_crossentropy",metrics=["accuracy"])
model.fit(X,y,epochs=200,verbose=0)
print(model.predict(X))
