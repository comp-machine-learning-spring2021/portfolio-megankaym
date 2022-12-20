# MNIST Covolutional Neural Network


The application of machine learning tools is vital for solving real world problems. This component of the portfolio explores the intersection between computer vision and machine learning, and is an extension of a project I worked on over the summer.


# ----Background----
The Modified National Institute of Standards and Technology, otherwise known as MNIST, database contains 60,000 training and 10,000 testing images of handwritten digits [1].

A neural network is a class of supervised (all data is labelled*) machine learning algorithms that can find complex patterns and relationships in data to solve complex problems (both classification and regression problems) and enable deep learning [2].

* A label is the thing a model is trying to predict. For this project, our label is what number is written in an image.

A Convolutional Neural Network, otherwise known as a “Convnet”, is built using neurons** and fully connected layers just like traditional neural networks, but they also have convolutional layers. Convolutional layers contain a set of filters/kernels, parameters of which are to be learned throughout the training. The size of the filters is usually smaller than the actual image. Each filters are applied to the images [2].

**Neurons are interconnected nodes in a layered structure that resembles the human brain.
 
The original code built a CNN model and performed an adversarial attack, and can be found in AE attack.ipynb

It may be helpful to review what an adversarial attack can look like. For example, the white-box attack is when attacker has complete access to the model’s function - i.e. the inputs, outputs, structure, and/or weights. The black-box attack is when the attacker has restricted access to the model, and only knows the inputs and outputs. Misclassification is when the attacker wants incorrect output classification, but disregards the resulting target class, whereas source/target misclassification is when the attacker wants to alter the input data so that the new, incorrect classification results in a specific target class.

In this project, a Fast Gradient Sign Attack (FGSM) was used. It was one of the very first adversarial attacks and is still incredibly common to this day because of it effectiveness. The Fast Gradient Sign Attack is designed to attack neural networks in a particular way, specifically how they learn. They attack a neural network’s gradients. The attack changes the input data based on the backpropagated gradients. In short, it uses gradient of the loss with reference to the input data, then adjusts the input data to maximize the loss [3].

The loss was calculated using the cross entropy loss function, which measures the performance of a classification model whose output is a probability value between 0 and 1. Cross-entropy loss increases as the predicted probability diverges from the actual label, which means a perfect model would have a loss of 0. [4, 6]
 
# ----Outline----

The goal of this component is to understand how the CNN was built in detail, as this was not the main focus of the summer project, and actually try to prevent the damage of the attack. Upon my own research, I discovered Pytorch transformations. These are commonly used to transform and alter data, specically images, to produce variability. These transformations could be used to allow for models to have better generalization. If a model is trained to predict the class of difficult or confusing images in addition to the original ones, it will likely perform better in general given that test data is completely new and could be variable [5].

Will transformations on the MNIST data improve the model's resilience to adversarial attacks?

1. Obtain the performance of a model that does not train/validate with Pytorch transformations
2. Evaluate the model's performace after an adversarial attack
3. Obtain the performance of a model that does train/validate with Pytorch transformations
4. Evaluate the model's performace after an adversarial attack to determine if Pytorch transformations can alleviate adversarial attacks.

# ----Results----

Please refer to the results.pdf file in this directory to see the evaluation.

# Resources
1. “MNIST Database.” Wikipedia, Wikimedia Foundation, 31 July 2022, https://en.wikipedia.org/wiki/MNIST_database. 
2. Saha, Sumit. “A Comprehensive Guide to Convolutional Neural Networks - the eli5 Way.” Medium, Towards Data Science, 17 Dec. 2018, https://towardsdatascience.com/a-comprehensive-guide-to-convolutional-neural-networks-the-eli5-way-3bd2b1164a53.
3. Inkawhich, Nathan. “Adversarial Example Generation.” Adversarial Example Generation - PyTorch Tutorials 1.12.0+cu102 Documentation, https://pytorch.org/tutorials/beginner/fgsm_tutorial.html.
4. Liusie, Adian. “Intuitively Understanding the Cross Entropy Loss.” YouTube, YouTube, 4 July 2021, https://www.youtube.com/watch?v=Pwgpl9mKars.
5. “Transforming and Augmenting Images¶.” Transforming and Augmenting Images - Torchvision Main Documentation, https://pytorch.org/vision/stable/transforms.html. 
6. https://ml-cheatsheet.readthedocs.io/en/latest/loss_functions.html
