# Personal Projects
A collection of personal projects, mostly odds and ends that are too small for their own repository.

## EMNIST_Balanced_CNN
*Because MNIST is too easy*
```
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d (Conv2D)              (None, 28, 28, 28)        140       
_________________________________________________________________
batch_normalization (BatchNo (None, 28, 28, 28)        112       
_________________________________________________________________
activation (Activation)      (None, 28, 28, 28)        0         
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 28, 28, 28)        3164      
_________________________________________________________________
batch_normalization_1 (Batch (None, 28, 28, 28)        112       
_________________________________________________________________
activation_1 (Activation)    (None, 28, 28, 28)        0         
_________________________________________________________________
max_pooling2d (MaxPooling2D) (None, 14, 14, 28)        0         
_________________________________________________________________
batch_normalization_2 (Batch (None, 14, 14, 28)        112       
_________________________________________________________________
dropout (Dropout)            (None, 14, 14, 28)        0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 14, 14, 56)        6328      
_________________________________________________________________
batch_normalization_3 (Batch (None, 14, 14, 56)        224       
_________________________________________________________________
activation_2 (Activation)    (None, 14, 14, 56)        0         
_________________________________________________________________
conv2d_3 (Conv2D)            (None, 14, 14, 56)        12600     
_________________________________________________________________
batch_normalization_4 (Batch (None, 14, 14, 56)        224       
_________________________________________________________________
activation_3 (Activation)    (None, 14, 14, 56)        0         
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 7, 7, 56)          0         
_________________________________________________________________
batch_normalization_5 (Batch (None, 7, 7, 56)          224       
_________________________________________________________________
activation_4 (Activation)    (None, 7, 7, 56)          0         
_________________________________________________________________
dropout_1 (Dropout)          (None, 7, 7, 56)          0         
_________________________________________________________________
conv2d_4 (Conv2D)            (None, 7, 7, 112)         25200     
_________________________________________________________________
batch_normalization_6 (Batch (None, 7, 7, 112)         448       
_________________________________________________________________
activation_5 (Activation)    (None, 7, 7, 112)         0         
_________________________________________________________________
conv2d_5 (Conv2D)            (None, 7, 7, 112)         50288     
_________________________________________________________________
batch_normalization_7 (Batch (None, 7, 7, 112)         448       
_________________________________________________________________
activation_6 (Activation)    (None, 7, 7, 112)         0         
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 3, 3, 112)         0         
_________________________________________________________________
batch_normalization_8 (Batch (None, 3, 3, 112)         448       
_________________________________________________________________
dropout_2 (Dropout)          (None, 3, 3, 112)         0         
_________________________________________________________________
flatten (Flatten)            (None, 1008)              0         
_________________________________________________________________
dense (Dense)                (None, 128)               129152    
_________________________________________________________________
batch_normalization_9 (Batch (None, 128)               512       
_________________________________________________________________
alpha_dropout (AlphaDropout) (None, 128)               0         
_________________________________________________________________
activation_7 (Activation)    (None, 128)               0         
_________________________________________________________________
dense_1 (Dense)              (None, 128)               16512     
_________________________________________________________________
batch_normalization_10 (Batc (None, 128)               512       
_________________________________________________________________
alpha_dropout_1 (AlphaDropou (None, 128)               0         
_________________________________________________________________
activation_8 (Activation)    (None, 128)               0         
_________________________________________________________________
dense_2 (Dense)              (None, 47)                6063      
=================================================================
Total params: 252,823
Trainable params: 251,135
Non-trainable params: 1,688
_________________________________________________________________
```
Some notes: Even the best networks seem to top out at 90-ish% on the EMNIST Balanced dataset and when we look at our confusion matrix we may feel a little forgiving towards the network. It's struggling to classify 0 vs O, capital F vs lowercase f, confusing Ls Is and 1s... all in all it tends to make very human mistakes. In a setting where you're trying to use the network to automatically process handwritten text one could use the context of the word or number a character is situated in to help disambiguate it.

## Curse of Strahd Tarokka Deck
Implemented a python class to create the tarokka deck from the d&d 5e Curse of Strahd module. Automates the Tarot reading that determines the location of key items and characters. Used as an opportunity to get more familiar with dunder methods.
```
deck = TarokkaDeck()
deck.five_card_spread()
```

## Pong
Not much to say, it's standard pong (though the ball gets faster with each rebound). Coded in python with turtle module instead of pygame. The game performance is far too variable from machine to machine and would require a near complete recode in a proper engine for any sort of distribution.

## Serebii Scraper Prototype Ver 0.0
Built a scraper using beautiful soup and regular expressions that pulls data from serebii's gen 1 dex pages. Outputs data to pandas dataframe for further analysis. Future plans include automating the population of a SQL database with the data from these pages among others, implementing a pokemon class that can be used with the data to automatically generate pokemon objects with attacks etc to significantly reduce the work of creating a pokemon clone game.

## Special Relativity Calculator
Created a calculator in python that can convert the spacetime coordinates of an event from one observer to another. Can also calculate length contraction and time dilation effects. Currently working on implementing the ability to draw equivalent Minkowski diagrams for observers using matplotlib and relativistic dynamics calculations as well as adding functionality to handle non-inertial reference frames.

## Wordle Cheat Engine
Takes and validates user input for green, yellow, and gray letters, formats the input into regular expressions and searches the wordle dictionary (sourced from github.com/a-vanderheiden) for potential matches and returns a list of matches. Refactored for code readability and added handling of double letter edge cases in a way that doesn't impede on the user experience. Comments may be on the verbose side but I'd rather have overexplained code than underexplained code.

## Advanced Evolutionary Algorithms HW
Assignment for my bootcamp (committed a few months late but c'est la vie) implementing genetic algorithms from scratch in order to solve the knapsack problem.

## NLTK Practice
Just a small notebook where I played around with NLTK and followed the official documentation to learn the ropes. Did some analysis on classic books like Frankenstein.

## AAPL Stock Forecasting
Attempts to apply time series analysis techniques to AAPL stock. Horrific failure but fun nonetheless

## CIFAR 100
Attempts at extending a CIFAR10 classifier to CIFAR100 (superclasses) was only able to achieve ~60% accuracy on the test set without transfer learning but keep in mind since there are 20 superclasses random guessing would mean 5% accuracy and the confusion matrix shows a rather successful classifier with some weaknesses.

## Tarot
Similar to the tarokka implementation (was actually the base program for the tarokka program) allows you to draw tarot cards from a deck with an orientation (reversed/upright). Coult implement spreads but my mind is on other projects right now.
