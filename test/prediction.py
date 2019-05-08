# 預測(prediction)

I = Image.open('D:/4.png') 
I=ImageOps.invert(I)
I_array = np.array(I)

reshapeI=I_array[:,:,1].ravel()
#plt.imshow(reshapeI)
#plt.show()
reshapeI=reshapeI.reshape(1,-1)
#print(reshapeI)

target=reshapeI
print(target.shape)
#deal with value
target=target/255

#print(target,target.shape)
predictions = model.predict_classes(target)
# get prediction result
print(predictions)
