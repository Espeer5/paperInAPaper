# Entitlement Justice and Measures of Algorithmic Fairness

## Introduction

### Algorithmic Decision Makers
 - Use of algorithmic decision making is on the rise
   - Adopted in fields including criminal justice, college admissions, job hiring, bank loans.
 - Include ML models, decision trees, and other "block box" solutions

### Concerns
 - There are growing concerns about the fairness of these decision makers
   - Conerns about due process
   - Concerns about bias/discrimination
   - Concerns about the "algorithmic leviathon"
 - In response to these concerns, a large literature has developed surrounding algorithmic fairness measures
   - These measures aim to quantify the fairness of algorithmic decision makers
    - They are used to evaluate the fairness of a decision maker, and to guide the development of new decision makers

### Types of Justice:
 - If one seeks to quantify fairness, one must first define what is meant by "fairness"
 - There are many attempts to define justice in the literature, with contemporary efforts relating back to the Rawls/Nozick liberal vs. libertarian debate
 - In the field of algorithmic fairness, measures rely on Rawlsian justice to the exclusive of entitlement theories of justice
   
### Argument
 - Entitlement justice is important in algorithmic fairness, but historically neglected in discussions of fairness measures
 - Some counterfactuals measures can be considered as emphasizing entitlement justice
    - This paper will explore the implications of entitlement justice for algorithmic fairness measures, the ways in which counterfactual fairness measures can be seen as capturing entitlement justice, and why this is important for the development of algorithmic decision makers.

## Algorithmic Fairness Measures

### Statistical Parity Measures
 - Measures of statistical parity dominate the literature and are the most commonly used measures of algorithmic fairness
 - Seek to maximize some distributional measure of fairness
   - i.e, the proportion of individuals in a protected class who are positively classified, or the egality of false positive rates across classes
 - These measures are criticized for overlooking individual differences between members of protected classes
   - i.e - consider the case where only one man applied to a predominantly female college. A measure of parity would require that he be admitted, even if underqualified. Though the group of males in general may not be underqualified, this individual is - but the measure fails to take this into consideration.

### Counterfactual Fairness
 - (presentation of concept)
 - Counterfactual fairness addresses the issues of conventional measures by considering causal reasoning
   - It asks whether the protected attribute of an individual is the cause of the decision - if so, the decision is considered unfair
 - Notice though, that we must aggregate over counterfactuals to determine fairness, we don't get a direct measure on every individual
 - Limited by ability to define socially constructed variables
   - i.e, we cannot simply flip the "race" variable of an individual in a hiring case, we must flip the neighborhood they grew up in, their education, etc. - and exactly how we should account for these is unclear.

## End-state and Entitlement Theories of Justice

### End-state Theories
 - (presentation of Rawls' theory)
 - End-state theories are associated with welfare economics
    - They aim to maximize the welfare of the least well-off in society
    - They are often associated with redistributive policies
 - Present conventional Wilt Chamberlain example of a challenge to end-state theories

### Entitlement Theories
 - (Presentation of Nozick's Theory)
 - Entitlement theories are associated with libertarianism
    - They aim to protect the property rights of individuals
    - They are often associated with non-redistributive policies - theories in which the accumulation of holdings is governed but redistribution policies such as welfare and taxation are not considered just
 - These theories are historic - a distribution of resources is just if the history of acquisitions and transfers of holdings is just according to the principles of the society
 - These theories are more focused on the treatments of individuals - each individual is treated according to the holdings they are subject to
   - This means no individual will lose property unwillingly to the benefit of another


## Emphasis on End-state Theories in Algorithmic Fairness
 - Statistical parity measures are clearly associated with end-state theories
   - These measures consider the outcome distribution of the decision maker, and try to ensure that groups receive end-state outcomes that are equal
 - Present formally how several statistical parity measures do this

## Entitlement Justice and Counterfactual Fairness
 - Counterfactual fairness can be seen as emphasizing entitlement justice
   - If we can see that the protected attributes of an individual (and indeed any attributes which should not be considered in the decision in question) are flipped, and the decision does not change, then the person receiving the decision is entitled to that decision
 - This hinges on a particular theory of property rights which enable an individual to consider the object of a decision a holding before the decision has been made
   - (Present this account more formally)

## Implications

## Conclusion

## Aknowledgements

## References
