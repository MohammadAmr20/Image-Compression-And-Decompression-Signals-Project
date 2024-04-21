def compressImage(inputImage,m):
    blocksShape = (inputImage.shape[0]//8,inputImage.shape[1]//8)
    compressedImage = np.zeros((m*blocksShape[0],m*blocksShape[1],3))
    for channel in range(3):
        for row in range(blocksShape[0]):
            for col in range(blocksShape[1]):
                processedBlock = inputImage[8*row:8*(row+1),8*col:8*(col+1),channel]
                dctBlock = DCT(processedBlock)
                dctRetainedBlock = dctBlock[:m,:m]
                compressedImage[m*row:m*(row+1),m*col:m*(col+1),channel] = dctRetainedBlock
    return compressedImage