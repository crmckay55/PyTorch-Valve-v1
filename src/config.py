import torch

# Pytorch install: https://pytorch.org/get-started/locally/


# TODO: get proper representation in the test set
# TODO: tag valve and guage only (don't classify further)
# TODO: finish random permutaion of pictures to increase sample size

BATCH_SIZE = 9  # increase / decrease according to GPU memeory
RESIZE_TO = 640  # resize the image for training and transforms
NUM_EPOCHS = 100  # number of epochs to train for
DEVICE = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
# training images and XML files directory
TRAIN_DIR = '/model_pictures/train'
# validation images and XML files directory
VALID_DIR = '/model_pictures/test'
# classes: 0 index is reserved for background
CLASSES = [
    'background', 'valve', 'guage'
]
NUM_CLASSES = 3
# whether to visualize images after crearing the data loaders
VISUALIZE_TRANSFORMED_IMAGES = False
# location to save model and plots
OUT_DIR = '/model_outputs/'
SAVE_PLOTS_EPOCH = 2 # save loss plots after these many epochs
SAVE_MODEL_EPOCH = 2  # save model after these many epochs