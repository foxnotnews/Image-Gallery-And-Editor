import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

class Image():
    #img_data: numpy array of the pixel values
    #met_data
    def __init__(self):
        print("to be done")
    def loadImage(self, path):
        self.data = np.array(Image.open(path))
        #to be added here: reading metadata
    def BilinearUpscaleImage(self, scale_factor):
        #Bilinear upscaler. first scales the x direction by the scale_factor, then scales the y direction by the scale_factor. 
        #Inpurts:
        #   scale_factor: an integer that states by how much each axis is supposed to get scaled.
        #   self: obviously this class and all its variables.
        #
        #Output:
        #   overwrites self.data: overwrites the image with the upscaled array containing the new pixel data.
        if(len(np.shape(self.data)) == 3):
            upscaled_image = np.zeros((int(self.data.shape[0] *1.5), int(self.data.shape[1] *1.5), self.data.shape[2]), dtype = "int")
            for j in range(3):
                xupscaled_channel = []
                for i in self.data[:,:,j]:
                    upscaled_vector = self.__interp_1D(i, scale_factor)
                    upscaled_vector = upscaled_vector.astype(int)
                    xupscaled_channel.append(upscaled_vector)
                xupscaled_channel = np.array(xupscaled_channel)
                xupscaled_channel = np.transpose(xupscaled_channel)
                upscaled_channel = []
                for i in xupscaled_channel:
                    upscaled_vector = self.__interp_1D(i, scale_factor)
                    upscaled_vector = upscaled_vector.astype(int)
                    upscaled_channel.append(upscaled_vector)
                for i in range(len(upscaled_channel)):
                    upscaled_image[:, i, j] = upscaled_channel[i]
        else:
            upscaled_image = np.zeros((int(self.data.shape[0] *1.5), int(self.data.shape[1] *1.5)), dtype = "int")
            xupscaled_channel = []
            for i in self.data[:,:]:
                upscaled_vector = self.__interp_1D(i, scale_factor)
                upscaled_vector = upscaled_vector.astype(int)
                xupscaled_channel.append(upscaled_vector)
            xupscaled_channel = np.array(xupscaled_channel)
            xupscaled_channel = np.transpose(xupscaled_channel)
            upscaled_channel = []
            for i in xupscaled_channel:
                upscaled_vector = self.__interp_1D(i, scale_factor)
                upscaled_vector = upscaled_vector.astype(int)
                upscaled_channel.append(upscaled_vector)
            for i in range(len(upscaled_channel)):
                upscaled_image[:, i] = upscaled_channel[i]
            self.data = upscaled_image
    def __interp_1D(self, signal, scale_factor):
    # Linearly interpolates one dimensional signal by a given saling fcator
    #
    # Inputs:
    #   signal: A one dimensional signal to be samples from, numpy array
    #   scale_factor: scaling factor, float
    #
    # Outputs:
    #   y_new: Interpolated 1D signal, numpy array
        x_vals = np.linspace(1,len(signal),len(signal))
        x_new = np.linspace(1,len(signal), int(len(signal)*scale_factor))
        y_new = np.zeros(len(x_new))
        for i in range(len(x_new)):
            if (x_new[i] <= x_vals[0]):
                y_new[i] = signal[0]
            elif (x_new[i] >= x_vals[len(x_vals)-1]):
                y_new[i] = signal[len(signal)-1]
            elif (x_new[i]-np.floor(x_new[i]) < 0.00000001):
                y_new[i] = signal[x_vals == int(x_new[i])]
            else:
                x0 = int(np.floor(x_new[i])) 
                x1 = int(np.ceil(x_new[i])) 
                fx0 = signal[x0-1]
                fx1 = signal[x1-1]
                y_new[i] = fx0 *(1- (x_new[i] - x0) / (x1 - x0)) + fx1 * (x_new[i] - x0) / (x1 - x0)
        return y_new
    



    def BilinearUpscaleImage_Carla(self,scale_factor):
        original_img=self.data
        img=np.apply_along_axis(self.__interp_1D_Carla, scale_factor=scale_factor, axis=1, arr=original_img)
        img=np.apply_along_axis(self.__interp_1D_Carla, scale_factor=scale_factor, axis=0, arr=img)
        return img

    def __interp_1D_Carla(signal,scale_factor):
        # Computes interpolation at the given abscissas
        #
        # Inputs:
        #   scale factor:
        #   Signal: Given input ordinates, numpy array
        
        #
        # Outputs:
        #   y_new: Interpolated values, numpy array
        x_new=np.linspace(1,len(signal), int(len(signal)*scale_factor),dtype=np.float32)
        x_vals=np.arange(len(signal))+1
        signal = signal.astype(np.float32)

        y_new=np.full_like(x_new,0, dtype=np.float32)
        for i,val in enumerate(x_new):
            
            #check if x_new is smaller or equal than the first value in x
            if val<=x_vals[0]:
                y_new[i]=signal[0]
            #check if x_new is bigger  or equal than the last value in x
            elif val>=x_vals[-1]:
                y_new[i]=signal[-1]
            
            else:
                #the closer 2 points (x0,x1) are the smallest  difference between val and x_vals. sort and get their inital index 
                indices=np.argsort(abs(val - x_vals))[:2]
                x0,x1=x_vals[indices]
                y0,y1=signal[indices]
                y_new[i]=y0 + (val - x0) * (y1 - y0) / (x1 - x0)

        return y_new




