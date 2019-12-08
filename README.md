# EC601_miniproject3_DSP

# Create a low pass filter using python
## matplotlib library
Matplotlib is a Python 2D plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms. Matplotlib can be used in Python scripts, the Python and IPython shells, the Jupyter notebook, web application servers, and four graphical user interface toolkits.

![image](https://matplotlib.org/_images/sphx_glr_histogram_thumb.png)
## Step1: Create the signal
* create a signal with frequency of 100Hz **signala = np.sin(2*np.pi*100*t)**
![image](https://github.com/Miketan1/EC601_miniproject3_DSP/blob/master/a.png)
* create a signal with frequency of 20Hz **signalb = np.sin(2*np.pi*20*t)**
![image](https://github.com/Miketan1/EC601_miniproject3_DSP/blob/master/b.png)
* Add signal a and b
![image](https://github.com/Miketan1/EC601_miniproject3_DSP/blob/master/c.png)
## Step2: Using low pass filter
* Pass the signal frequency less than 30Hz
![image](https://github.com/Miketan1/EC601_miniproject3_DSP/blob/master/Figure_1.png)
## Reference
[1] https://matplotlib.org/
