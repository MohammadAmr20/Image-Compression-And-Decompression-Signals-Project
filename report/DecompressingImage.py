def decompressImage(compressedImage,m):
    blocksShape = (compressedImage.shape[0]//m,compressedImage.shape[1]//m)
    decompressedImage = np.zeros((8*blocksShape[0],8*blocksShape[1],3))
    for channel in range(3):
        for row in range(blocksShape[0]):
            for col in range(blocksShape[1]):
                processedBlock = np.zeros((8,8))
                processedBlock[:m,:m] = compressedImage[m*row:m*(row+1),m*col:m*(col+1),channel]
                idctBlock = IDCT(processedBlock)
                decompressedImage[8*row:8*(row+1),8*col:8*(col+1),channel] = idctBlock
    return decompressedImage