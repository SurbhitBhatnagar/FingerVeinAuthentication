# Finger Veins Pattern Authentication-Project-
A Machine Learning and Computer Vision based Authentication system.
Unique Finger-vein pattern detection is taken as a biometric instead of fingerprint to ensure no forgery or theft of the biometric.
The repository consists of various codes implementing parts of the project.
The main code of the project which creates the feature sets is the ROI_InProgress/finalfeturemaker.py.

The finalfeturemaker.py follows the block diagram below:-
FingerVein Image Preprocessing -------> Region Of Interest Extraction -----------> Local Ternary Co-occurence Pattern Values Calculation -----> Histogram of LTCoP Values ------> Store in HD5F Datasets.

The testing/training of the datasets is done using KNN Algorithm in knnkamal1.py.
For more information regarding project please refer to:- http://ieeexplore-spotlight.ieee.org/article/finger-vein-authentication-biometric-security-system/
