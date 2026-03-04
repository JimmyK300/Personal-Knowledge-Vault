Overfitting happens when the model starts to memorize data using access capacity instead of generalizing
Large width does not instantly memorize because they starts of very general and only when they train enough do they settle into points in which memorization decrease loss
early stopping works because it stops the model before it can start memorization
double descent means that given enough parameters and enough data, the model will start to generalize again, as the number of parameter increase vastly, the model has the ability to not only model the data correctly (memo) but also use a curve that is even better. Why model resort to "nice" curves instead of "ugly" curves? I have seen the explanation, but still understand it only as it is a law of nature.

common failure: 
matrix size and row vs column differenciation
matrix derivation and backprop thing still not enough, still dont understand the backprop derivative correctly and why we tranpose what we transpose, what gets multiplied by what and so on.

lr>>not converge
epoch<< not learned
reinit: breaks learning (starting from zero)
small data + big Hidden = overfit

capacity defines the overall expressiveness of the model
optimization defines steps in which training is shortened
time defines the various states that the model is in during its training time.

