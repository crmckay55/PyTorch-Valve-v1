import torch

# Pytorch install: https://pytorch.org/get-started/locally/


FILE_IN_PATH = 'F:/Python Projects/PyTorch-Valve-v1/model_pictures/originals_untagged/'
FILE_OUT_PATH = 'F:/Python Projects/PyTorch-Valve-v1/model_pictures/originals_modified/'
VALIDATE_SOURCE = '../model_test/source'
VALIDATE_PREDICTIONS = '../model_test/predictions'

TRAIN_DIR =  '/model_pictures/train'            # training images and XML files directory
MODEL_LOCATION = '../model_outputs/model100.pth'
VALID_DIR = '/model_pictures/test'              # validation images and XML files directory


COMPUTATION_DEVICE = 'cuda'
DEVICE = torch.device(COMPUTATION_DEVICE)

BATCH_SIZE = 9  # increase / decrease according to GPU memeory
RESIZE_TO = 640  # resize the image for training and transforms
NUM_EPOCHS = 100  # number of epochs to train for


# classes: 0 index is reserved for background
NUM_CLASSES = 3
CLASSES = ['background', 'valve', 'guage']


# whether to visualize images after crearing the data loaders
VISUALIZE_TRANSFORMED_IMAGES = False

# location to save model and plots
OUT_DIR = '/model_outputs/'
SAVE_PLOTS_EPOCH = 2 # save loss plots after these many epochs
SAVE_MODEL_EPOCH = 2  # save model after these many epochs