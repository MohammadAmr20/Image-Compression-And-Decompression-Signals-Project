def calculatePSNR(inputImage,decompressedImage):
    SE = (inputImage-decompressedImage)**2
    MSE = np.mean(SE)
    peak = 255
    PSNR = 10*log10(peak**2/MSE)
    return PSNR