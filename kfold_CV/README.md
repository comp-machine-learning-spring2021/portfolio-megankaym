# k-fold Cross Validation

k-fold Cross Validation is a evaluation method that allows the programmer to see the error made b. Inspiration to use a decision tree method in this k-foldCV code actually came from a website post I found whilst trying to debug my old k-foldCV [1]. This coding component contains far more than 50% new material compared to the previous assignment it is based on.

*It should be noted that this coding component is meant to be run with terminal, python hw5.py or pytest -v. the notebook just shows thought process and brainstorming


# Results
There were 7 different tests run with the functions created for this coding component. First, I tested single inputs and then later tested different combinations of input variables. Interestingly, all tests resulted in the same computed error, 200 when k=5. When k=10, these tests all returned an error of 100. When k=200, the error output was 5 for all of them. It seems like the errors are inversely proportional to the chosen k. 

1. neuroticism
2. performance
3. job
4. neuroticism & performance
5. neuroticism & job
6. performance & job
7. neuroticism & performance & job

# Resources
1. razeal113, et al. “Cross Validation + Decision Trees in Sklearn.” Stack Overflow, 1 Mar. 1963, https://stackoverflow.com/questions/35097003/cross-validation-decision-trees-in-sklearn.
