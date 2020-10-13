import submission
import util
from collections import defaultdict

# Read in examples
trainExamples = util.readExamples('names.train')
devExampels = util.readExamples('names.dev')


def featureExtractor(x):
    pass


# Learn a predictor
weights = submit.learnPredictor(trainExamples,)
