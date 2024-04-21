def getImageComponents(inputImage):
    os.makedirs("Image Components", exist_ok=True)
    colors = ["Reds","Greens","Blues"]
    for i in range(3):
        plt.figure(figsize=(14, 6))
        plt.imshow(inputImage[:,:,2-i],cmap=colors[i])
        plt.axis("off")
        plt.colorbar()
        plt.savefig(f"Image Components/a_{colors[i][:-1].lower()}.png")
inputImageArray = cv2.imread("image1.png")
getImageComponents(inputImageArray)