# coding: utf-8

#####################################################################################
# This configuration file sets various parameters for generation of training
# set & evalutation of DeepLabCut
#####################################################################################

# myconfig.py:

########################################
# Step 1: Selecting Frames from videos
########################################

Task = 'reaching'

# Filename and path to behavioral video:
vidpath = '.'
filename = 'reachingvideo1.avi'

cropping = True

# ROI dimensions / bounding box (only used if cropping == True)
# x1,y1 indicates the top left corner and
# x2,y2 is the lower right corner of the croped region.

x1 = 0
x2 = 640
y1 = 277
y2 = 624

# Portion of the video to sample from in step 1. Set to 1 by default.
portion = 1

########################################
# Step 2: Converting frames to pandas array 
########################################

bodyparts = ["Current_pelletBottom","Current_pelletSide","Current_pelletTop","middle_knuckleBottom","middle_knuckleSide","middle_knuckleTop","middle_tipBottom","middle_tipSide","middle_tipTop","palmBottom","palmSide","palmTop","pinky_knuckleBottom","pinky_knuckleSide","pinky_knuckleTop","pinky_tipBottom","pinky_tipSide","pinky_tipTop","pointer_knuckleBottom","pointer_knuckleSide","pointer_knuckleTop","pointer_tipBottom","pointer_tipSide","pointer_tipTop","ring_knuckleBottom","ring_knuckleSide","ring_knuckleTop","ring_tipBottom","ring_tipSide","ring_tipTop","thumb_knuckleBottom","thumb_knuckleSide","thumb_knuckleTop","thumb_tipBottom","thumb_tipSide","thumb_tipTop","wristBottom","wristSide","wristTop"]  # Exact sequence of labels as were put by
# annotator in *.csv file
Scorers = ['Marci']  # who is labeling?

# Set this true if the data was sequentially labeled and if there is one file per folder (you can set the name of this file below, i.e. multibodypartsfilename)
# Otherwise there should be individual files per bodypart, i.e. in our demo case hand.csv, Finger1.csv etc.
# If true then those files will be generated from Results.txt
multibodypartsfile=False 
multibodypartsfilename="Results.csv"

# When importing the images and the labels in the csv/xls files should be in the same order!
# During labeling in Fiji one can thus (for occluded body parts) click in the origin of the image 
#(i.e. top left corner (close to 0,0)), these "false" labels will then be removed. To do so set the following variable:
#set this to 0 if no labels should be removed!

invisibleboundary=10 # If labels are closer to origin than this number they are set to NaN (not a number). Please adjust to your situation. Units in pixel.
 
imagetype=".png" # image type of labeled frames

########################################
# Step 3: Check labels / makes plots
########################################

colormap = 'cool' #set color map, i.e. viridis, cool, hsv
scale = 1  # for plotting
msize=10   #size of labels
alphavalue =.6 #transparency of labels

########################################
# Step 4: Generate Training Files 
########################################

date = 'Jun21'
scorer = 'Marci'

# Userparameters for training set. Other parameters can be set in pose_cfg.yaml
Shuffles = [1]  # Ids for shuffles, i.e. range(5) for 5 shuffles
TrainingFraction = [0.95]  # Fraction of labeled images used for training

# Which resnet to use
# (these are parameters reflected in the pose_cfg.yaml file)
resnet = 50

# For Evaluation/ Analyzing videos
# To evaluate the last model that was trained most set this to: -1 
# To evaluate all models (training stages) set this to: "all"  (as string!)

snapshotindex = -1 #"all"
shuffleindex = 0
pcutoff=.1 # likelihood. RMSE will be reported for all pairs and pairs with larger likelihood than pcutoff (see paper). This cutoff will also be used in plots.
plotting=True #If true will plot train & test images including DeepLabCut labels next to human labels. Note that this will be plotted for all snapshots as indicated by snapshotindex
