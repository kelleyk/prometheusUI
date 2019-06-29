import math
import numpy as np
import time

normDCIconv = np.array([-0.44379, -0.45149, -0.45928, -0.46715, -0.47511, -0.48315, -0.49127, -0.49947, -0.50774, -0.51609, -0.52448, -0.53293, -0.54142, -0.54997, -0.55857, -0.56722, -0.57591, -0.58466, -0.59345, -0.60227, -0.61112, -0.61999, -0.62887, -0.63776, -0.64668, -0.6556, -0.66453, -0.67347, -0.68241, -0.69134, -0.70026, -0.70915, -0.71804, -0.72689, -0.73572, -0.7445, -0.75326, -0.76199, -0.77069, -0.77935, -0.78797, -0.79653, -0.80502, -0.81346, -0.82183, -0.83015, -0.83842, -0.84664, -0.85482, -0.86299, -0.87116, -0.87935, -0.88757, -0.89582, -0.90412, -0.91246, -0.92087, -0.92936, -0.93796, -0.94669, -0.95554, -0.96452, -0.97365, -0.98297, -0.99248, -0.99783, -0.9882, -0.97871, -0.96935, -0.96014, -0.95105, -0.94209, -0.93327, -0.92459, -0.91605, -0.90763, -0.89932, -0.89113, -0.88306, -0.87511, -0.86726, -0.85949, -0.85183, -0.84427, -0.8368, -0.82941, -0.8221, -0.81487, -0.80771, -0.80062, -0.79359, -0.78661, -0.77969, -0.77281, -0.76598, -0.75918, -0.75244, -0.74573, -0.73907, -0.73245, -0.72586, -0.71931, -0.7128, -0.70632, -0.69985, -0.69339, -0.68694, -0.68048, -0.67402, -0.66755, -0.66106, -0.65454, -0.64799, -0.6414, -0.63477, -0.62808, -0.62131, -0.61445, -0.6075, -0.60046, -0.59333, -0.58609, -0.57877, -0.57134, -0.56383, -0.55621, -0.54851, -0.54072, -0.53285, -0.52489, -0.51685, -0.50873, -0.50053, -0.49226, -0.48391, -0.47552, -0.46707, -0.45858, -0.45003, -0.44143, -0.43278, -0.42409, -0.41534, -0.40655, -0.39773, -0.38888, -0.38001, -0.37113, -0.36224, -0.35332, -0.3444, -0.33547, -0.32653, -0.31759, -0.30866, -0.29974, -0.29085, -0.28196, -0.27311, -0.26428, -0.2555, -0.24674, -0.23801, -0.22931, -0.22065, -0.21203, -0.20347, -0.19498, -0.18654, -0.17817, -0.16985, -0.16158, -0.15336, -0.14518, -0.13701, -0.12884, -0.12065, -0.11243, -0.10418, -0.095881, -0.087536, -0.079129, -0.070638, -0.062037, -0.053314, -0.044465, -0.035482, -0.026346, -0.01703, -0.0075244, 0.0021672, 0.011804, 0.021293, 0.030645, 0.039863, 0.048949, 0.05791, 0.066733, 0.075408, 0.083946, 0.092368, 0.10068, 0.10887, 0.11694, 0.12489, 0.13274, 0.14051, 0.14817, 0.15573, 0.1632, 0.17059, 0.1779, 0.18513, 0.19229, 0.19938, 0.20641, 0.21339, 0.22031, 0.22719, 0.23402, 0.24082, 0.24756, 0.25427, 0.26093, 0.26755, 0.27414, 0.28069, 0.2872, 0.29368, 0.30015, 0.30661, 0.31306, 0.31952, 0.32598, 0.33245, 0.33894, 0.34546, 0.35201, 0.3586, 0.36523, 0.37192, 0.37869, 0.38555, 0.3925, 0.39954, 0.40667, 0.41391, 0.42123, 0.42866, 0.43617, 0.44379, 0.45149, 0.45928, 0.46715, 0.47511, 0.48315, 0.49127, 0.49947, 0.50774, 0.51609, 0.52448, 0.53293, 0.54142, 0.54997, 0.55857, 0.56722, 0.57591, 0.58466, 0.59345, 0.60227, 0.61112, 0.61999, 0.62887, 0.63776, 0.64668, 0.6556, 0.66453, 0.67347, 0.68241, 0.69134, 0.70026, 0.70915, 0.71804, 0.72689, 0.73572, 0.7445, 0.75326, 0.76199, 0.77069, 0.77935, 0.78797, 0.79653, 0.80502, 0.81346, 0.82183, 0.83015, 0.83842, 0.84664, 0.85482, 0.86299, 0.87116, 0.87935, 0.88757, 0.89582, 0.90412, 0.91246, 0.92087, 0.92936, 0.93796, 0.94669, 0.95554, 0.96452, 0.97365, 0.98297, 0.99248, 0.99783, 0.9882, 0.97871, 0.96935, 0.96014, 0.95105, 0.94209, 0.93327, 0.92459, 0.91605, 0.90763, 0.89932, 0.89113, 0.88306, 0.87511, 0.86726, 0.85949, 0.85183, 0.84427, 0.8368, 0.82941, 0.8221, 0.81487, 0.80771, 0.80062, 0.79359, 0.78661, 0.77969, 0.77281, 0.76598, 0.75918, 0.75244, 0.74573, 0.73907, 0.73245, 0.72586, 0.71931, 0.7128, 0.70632, 0.69985, 0.69339, 0.68694, 0.68048, 0.67402, 0.66755, 0.66106, 0.65454, 0.64799, 0.6414, 0.63477, 0.62808, 0.62131, 0.61445, 0.6075, 0.60046, 0.59333, 0.58609, 0.57877, 0.57134, 0.56383, 0.55621, 0.54851, 0.54072, 0.53285, 0.52489, 0.51685, 0.50873, 0.50053, 0.49226, 0.48391, 0.47552, 0.46707, 0.45858, 0.45003, 0.44143, 0.43278, 0.42409, 0.41534, 0.40655, 0.39773, 0.38888, 0.38001, 0.37113, 0.36224, 0.35332, 0.3444, 0.33547, 0.32653, 0.31759, 0.30866, 0.29974, 0.29085, 0.28196, 0.27311, 0.26428, 0.2555, 0.24674, 0.23801, 0.22931, 0.22065, 0.21203, 0.20347, 0.19498, 0.18654, 0.17817, 0.16985, 0.16158, 0.15336, 0.14518, 0.13701, 0.12884, 0.12065, 0.11243, 0.10418, 0.095881, 0.087536, 0.079129, 0.070638, 0.062037, 0.053314, 0.044465, 0.035482, 0.026346, 0.01703, 0.0075244, -0.0021672, -0.011804, -0.021293, -0.030645, -0.039863, -0.048949, -0.05791, -0.066733, -0.075408, -0.083946, -0.092368, -0.10068, -0.10887, -0.11694, -0.12489, -0.13274, -0.14051, -0.14817, -0.15573, -0.1632, -0.17059, -0.1779, -0.18513, -0.19229, -0.19938, -0.20641, -0.21339, -0.22031, -0.22719, -0.23402, -0.24082, -0.24756, -0.25427, -0.26093, -0.26755, -0.27414, -0.28069, -0.2872, -0.29368, -0.30015, -0.30661, -0.31306, -0.31952, -0.32598, -0.33245, -0.33894, -0.34546, -0.35201, -0.3586, -0.36523, -0.37192, -0.37869, -0.38555, -0.3925, -0.39954, -0.40667, -0.41391, -0.42123, -0.42866, -0.43617, -0.44379])
normDCIconvshift = np.array([0.55621, 0.54851, 0.54072, 0.53285, 0.52489, 0.51685, 0.50873, 0.50053, 0.49226, 0.48391, 0.47552, 0.46707, 0.45858, 0.45003, 0.44143, 0.43278, 0.42409, 0.41534, 0.40655, 0.39773, 0.38888, 0.38001, 0.37113, 0.36224, 0.35332, 0.3444, 0.33547, 0.32653, 0.31759, 0.30866, 0.29974, 0.29085, 0.28196, 0.27311, 0.26428, 0.2555, 0.24674, 0.23801, 0.22931, 0.22065, 0.21203, 0.20347, 0.19498, 0.18654, 0.17817, 0.16985, 0.16158, 0.15336, 0.14518, 0.13701, 0.12884, 0.12065, 0.11243, 0.10418, 0.095881, 0.087536, 0.079129, 0.070638, 0.062037, 0.053314, 0.044465, 0.035482, 0.026346, 0.01703, 0.0075244, -0.0021672, -0.011804, -0.021293, -0.030645, -0.039863, -0.048949, -0.05791, -0.066733, -0.075408, -0.083946, -0.092368, -0.10068, -0.10887, -0.11694, -0.12489, -0.13274, -0.14051, -0.14817, -0.15573, -0.1632, -0.17059, -0.1779, -0.18513, -0.19229, -0.19938, -0.20641, -0.21339, -0.22031, -0.22719, -0.23402, -0.24082, -0.24756, -0.25427, -0.26093, -0.26755, -0.27414, -0.28069, -0.2872, -0.29368, -0.30015, -0.30661, -0.31306, -0.31952, -0.32598, -0.33245, -0.33894, -0.34546, -0.35201, -0.3586, -0.36523, -0.37192, -0.37869, -0.38555, -0.3925, -0.39954, -0.40667, -0.41391, -0.42123, -0.42866, -0.43617, -0.44379, -0.45149, -0.45928, -0.46715, -0.47511, -0.48315, -0.49127, -0.49947, -0.50774, -0.51609, -0.52448, -0.53293, -0.54142, -0.54997, -0.55857, -0.56722, -0.57591, -0.58466, -0.59345, -0.60227, -0.61112, -0.61999, -0.62887, -0.63776, -0.64668, -0.6556, -0.66453, -0.67347, -0.68241, -0.69134, -0.70026, -0.70915, -0.71804, -0.72689, -0.73572, -0.7445, -0.75326, -0.76199, -0.77069, -0.77935, -0.78797, -0.79653, -0.80502, -0.81346, -0.82183, -0.83015, -0.83842, -0.84664, -0.85482, -0.86299, -0.87116, -0.87935, -0.88757, -0.89582, -0.90412, -0.91246, -0.92087, -0.92936, -0.93796, -0.94669, -0.95554, -0.96452, -0.97365, -0.98297, -0.99248, -0.99783, -0.9882, -0.97871, -0.96935, -0.96014, -0.95105, -0.94209, -0.93327, -0.92459, -0.91605, -0.90763, -0.89932, -0.89113, -0.88306, -0.87511, -0.86726, -0.85949, -0.85183, -0.84427, -0.8368, -0.82941, -0.8221, -0.81487, -0.80771, -0.80062, -0.79359, -0.78661, -0.77969, -0.77281, -0.76598, -0.75918, -0.75244, -0.74573, -0.73907, -0.73245, -0.72586, -0.71931, -0.7128, -0.70632, -0.69985, -0.69339, -0.68694, -0.68048, -0.67402, -0.66755, -0.66106, -0.65454, -0.64799, -0.6414, -0.63477, -0.62808, -0.62131, -0.61445, -0.6075, -0.60046, -0.59333, -0.58609, -0.57877, -0.57134, -0.56383, -0.55621, -0.54851, -0.54072, -0.53285, -0.52489, -0.51685, -0.50873, -0.50053, -0.49226, -0.48391, -0.47552, -0.46707, -0.45858, -0.45003, -0.44143, -0.43278, -0.42409, -0.41534, -0.40655, -0.39773, -0.38888, -0.38001, -0.37113, -0.36224, -0.35332, -0.3444, -0.33547, -0.32653, -0.31759, -0.30866, -0.29974, -0.29085, -0.28196, -0.27311, -0.26428, -0.2555, -0.24674, -0.23801, -0.22931, -0.22065, -0.21203, -0.20347, -0.19498, -0.18654, -0.17817, -0.16985, -0.16158, -0.15336, -0.14518, -0.13701, -0.12884, -0.12065, -0.11243, -0.10418, -0.095881, -0.087536, -0.079129, -0.070638, -0.062037, -0.053314, -0.044465, -0.035482, -0.026346, -0.01703, -0.0075244, 0.0021672, 0.011804, 0.021293, 0.030645, 0.039863, 0.048949, 0.05791, 0.066733, 0.075408, 0.083946, 0.092368, 0.10068, 0.10887, 0.11694, 0.12489, 0.13274, 0.14051, 0.14817, 0.15573, 0.1632, 0.17059, 0.1779, 0.18513, 0.19229, 0.19938, 0.20641, 0.21339, 0.22031, 0.22719, 0.23402, 0.24082, 0.24756, 0.25427, 0.26093, 0.26755, 0.27414, 0.28069, 0.2872, 0.29368, 0.30015, 0.30661, 0.31306, 0.31952, 0.32598, 0.33245, 0.33894, 0.34546, 0.35201, 0.3586, 0.36523, 0.37192, 0.37869, 0.38555, 0.3925, 0.39954, 0.40667, 0.41391, 0.42123, 0.42866, 0.43617, 0.44379, 0.45149, 0.45928, 0.46715, 0.47511, 0.48315, 0.49127, 0.49947, 0.50774, 0.51609, 0.52448, 0.53293, 0.54142, 0.54997, 0.55857, 0.56722, 0.57591, 0.58466, 0.59345, 0.60227, 0.61112, 0.61999, 0.62887, 0.63776, 0.64668, 0.6556, 0.66453, 0.67347, 0.68241, 0.69134, 0.70026, 0.70915, 0.71804, 0.72689, 0.73572, 0.7445, 0.75326, 0.76199, 0.77069, 0.77935, 0.78797, 0.79653, 0.80502, 0.81346, 0.82183, 0.83015, 0.83842, 0.84664, 0.85482, 0.86299, 0.87116, 0.87935, 0.88757, 0.89582, 0.90412, 0.91246, 0.92087, 0.92936, 0.93796, 0.94669, 0.95554, 0.96452, 0.97365, 0.98297, 0.99248, 0.99783, 0.9882, 0.97871, 0.96935, 0.96014, 0.95105, 0.94209, 0.93327, 0.92459, 0.91605, 0.90763, 0.89932, 0.89113, 0.88306, 0.87511, 0.86726, 0.85949, 0.85183, 0.84427, 0.8368, 0.82941, 0.8221, 0.81487, 0.80771, 0.80062, 0.79359, 0.78661, 0.77969, 0.77281, 0.76598, 0.75918, 0.75244, 0.74573, 0.73907, 0.73245, 0.72586, 0.71931, 0.7128, 0.70632, 0.69985, 0.69339, 0.68694, 0.68048, 0.67402, 0.66755, 0.66106, 0.65454, 0.64799, 0.6414, 0.63477, 0.62808, 0.62131, 0.61445, 0.6075, 0.60046, 0.59333, 0.58609, 0.57877, 0.57134, 0.56383, 0.55621])
INDEX_OF_REFRACTION_SALT_WATER = 1.34
normConvBeg = normDCIconv[:len(normDCIconv)-1]
normConvEnd = normDCIconv[1:]
normConvShiftBeg = normDCIconvshift[:len(normDCIconvshift)-1]
normConvShiftEnd = normDCIconvshift[1:]
normDCIconvMax = np.amax(normDCIconv)
normDCIconvMin = np.amin(normDCIconv)
normDCIshiftMin = np.amin(normDCIconvshift)


def analyze(dcsData, freq):

	#dcsData is a 320x240x4 array
	dcs0 = dcsData[:,:,0].reshape(1,76800, order='C')[0]
	dcs1 = dcsData[:,:,1].reshape(1,76800, order='C')[0]
	dcs2 = dcsData[:,:,2].reshape(1,76800, order='C')[0]
	dcs3 = dcsData[:,:,3].reshape(1,76800, order='C')[0]

	a = time.time()

	#this is the mapping function mapping the each value of the dcs array through the dcsInverse function
	# f = lambda w,x,y,z: dcsInverse(freq, w,x,y,z)
	f = lambda w,x,y,z: inverseEstimate(w,x,y,z)
	vectf = np.vectorize(f)
	result = vectf(dcs0, dcs1, dcs2, dcs3)

	rmax = np.amax(result)
	rmin = np.amin(result)
	dif = rmax - rmin

	print("RESULT:", result[1])
	print(rmin)
	result -= rmin
	print("RESULT:", result[1])
	print(dif)
	result /= dif
	print("RESULT:", result[1])

	b = time.time()
	print("TIME: ", b-a)
	print("RESULT: ", result)
	# print("DONE ", result)
	return result.reshape(320,240, order='C')


def dcsInverse(freq, dcs0, dcs1, dcs2=None, dcs3=None):

	if type(dcs2) == type(dcs3) == float:
		dcs0 -= dcs2
		dcs1 -= dcs3
	wavelength = 300/(freq*4.0*INDEX_OF_REFRACTION_SALT_WATER)
	#300 = speedOfLight 3*10^8 / megahertz 10^6

	amplitude = float(abs(dcs0) + abs(dcs1))

	if math.isnan(dcs0) or math.isnan(dcs1):
		quality = 'NaN'
		phase = -1
	elif dcs0 == dcs1 == 0:
		phase = -1
		quality = 0
	else:
		quality = math.sqrt(dcs0**2 + dcs1**2)
		normDCS0 = dcs0/amplitude
		normDCS1 = dcs1/amplitude

		if normDCS0 >= normDCIconvMax:

			riseIndex = ((normConvShiftBeg <=normDCS1) & (normConvShiftEnd > normDCS1)).nonzero()[0][0]
			slope = float(normDCIconvshift[riseIndex] - normDCIconvshift[riseIndex-1])
			est = (normDCS1 - normDCIconvshift[riseIndex])/slope
			phase = ((riseIndex + est)/wavelength)%1.0
		elif normDCS0 <= normDCIconvMin:

			fallIndex = ((normConvShiftBeg >=normDCS1) & (normConvShiftEnd < normDCS1)).nonzero()[0][0]
			slope = float(normDCIconvshift[fallIndex] - normDCIconvshift[fallIndex-1])
			est = (normDCS1 - normDCIconvshift[fallIndex])/slope
			phase = ((riseIndex + est)/wavelength)%1.0
		else:

			riseIndex = ((normConvBeg <=normDCS0) & (normConvEnd > normDCS0)).nonzero()[0][0]
			fallIndex = ((normConvBeg >=normDCS0) & (normConvEnd < normDCS0)).nonzero()[0][0]
			if ((normDCS1 > min(normDCIconvshift[riseIndex], normDCIconvshift[riseIndex+1])) and (normDCS1 > max(normDCIconvshift[riseIndex], normDCIconvshift[riseIndex+1]))) or normDCS1 <= normDCIshiftMin:
				section = [riseIndex, riseIndex+1]
			else:
				section = [fallIndex, fallIndex+1]

			slope = normDCIconv[section[1]] - normDCIconv[section[0]]
			est = (normDCS0 - normDCIconv[section[0]])/slope

			phase = ((section[0] + est)/wavelength)%1.0

	return phase


PERIOD = 1.0
AMP = 1.0
slope_DCSconv = (max(normDCIconv) - min(normDCIconv))/(0.5*PERIOD)
slope_DCSconvshift = (max(normDCIconv) - min(normDCIconv))/(0.5*PERIOD)

def f_conv(x):
	if x <= (1.0/8)*PERIOD: 
		y = -slope_DCSconv*x - 0.5*AMP
	elif x >= (5.0/8)*PERIOD:
		y = -slope_DCSconv*x + 3.5*AMP
	else:
		y = slope_DCSconv*x - 1.5*AMP
	return y

def f_convshift(x):
	if x <= (3.0/8)*PERIOD:
		y = -slope_DCSconvshift*x + 0.5*AMP
	elif x >= (7.0/8)*PERIOD:
		y = -slope_DCSconvshift*x + 4.5*AMP
	else:
		y = slope_DCSconvshift*x - 2.5*AMP
	return y

def f_conv_inverse(y):

	if y < -0.5:
		fallingX = (y + (0.5*AMP))/(-slope_DCSconv)
	else:
		fallingX = (y - (3.5*AMP))/(-slope_DCSconv)
	
	risingX = (y + (1.5*AMP))/slope_DCSconv

	return (fallingX, risingX)

def f_convshift_inverse(y):
	if y > 0.5:
		x1 = (y - (4.5*AMP))/(-slope_DCSconvshift)
	else:
		x1 = (y - (0.5*AMP))/(-slope_DCSconvshift)

	x2 = (y + (2.5*AMP))/slope_DCSconvshift

	return (x1, x2)


def inverseEstimate(dcs0, dcs1, dcs2=None, dcs3=None):

	
	if type(dcs2) == type(dcs3) == float:
		dcs0 -= dcs2
		dcs1 -= dcs3

	amplitude = float(abs(dcs0) + abs(dcs1))

	if dcs0 == dcs1 == 0:
		print('AAAAAAAA')
		print(dcs0,dcs1,dcs2,dcs3)
		return 0.75
	else:
		normDCS0 = dcs0/amplitude
		normDCS1 = dcs1/amplitude

		falling, rising = f_conv_inverse(normDCS0)

		if normDCS1 > 0:
			return falling
		return rising
