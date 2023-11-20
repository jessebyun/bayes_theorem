<h2>Using Bayes' Theorem in AI Decision-Making</h2>

Bayes' Theorem is a principle in probability theory that describes how to update the probabilities of hypotheses when given new evidence. It calculates the probability of an event based on prior knowledge of conditions that might be related to the event. In its basic form, the theorem states:

<img src="https://i.imgur.com/GUai4n5.png" alt="image"/>

Where:
- \( P(A|B) \) is the probability of event A given that B is true (posterior probability).
- \( P(B|A) \) is the probability of event B given that A is true.
- \( P(A) \) is the probability of event A (prior probability).
- \( P(B) \) is the probability of event B.

In simple terms, it allows us to update our initial understanding or belief about an event (A) in light of new evidence or information (B), resulting in a revised belief or probability. Bayes' Theorem is widely used in various fields, including statistics, finance, medicine, and artificial intelligence, to make predictions and informed decisions under uncertainty.

---------------------------------------------------------------------

Suppose someone has a box of role-playing game dice, precisely one each of 4, 6, 8, 12, and 20 sides. Each die has its sides numbered 1 through n, where n is the number of sides: the 4-sided die has sides numbered 1 - 4, the 6-sided die has sides numbered 1 - 6, etc., up through the 20-sided die, which has sides numbered 1 - 20.

Someone picks one die at random without seeing which die was selected, the person rolls it a few times and tells you the results. Based on the outcome of the rolls, you have to guess which die was picked. 

To start, need to find the probability of each of the die being selected. Having 5 die the chances are 1/5 = 0.2
<br/>
<img src="https://i.imgur.com/l5lbG7k.png" alt="image"/>

If someone rolled a 6. A 6-sided die has 1/6 chance, or 0.1666667; An 8-sided die has probability of 1/8, or 0.125, etc. As the die has more sides the probability keeps going down; each value on the 20-sided die has a probability of only 1/20 or 0.05
<br/>
<img src="https://i.imgur.com/04OMvDt.png" alt="image"/>
<br/>


However, you can't just enter those probabilities in this table, as it would be wrong. Not only because the probabilities don't add up to 1, but we need the probability of each die given that it has rolled a number, expressed in terms of conditional probability as P(die k | roll=6). This is where Bayes' Theorem comes into play. Then, we need to calculate the posterior probability for each die. 

First, we need to find the likelihood of each die rolling a given number by multiplying the chances of choosing that die with the probability of that die rolling a given number. The sum of the all the likelihoods is the total probability of rolling that given number. Then, to calculate the posterior probability for each die, we divide the likeihood of each die rolling a given number by the total probability. The sum of all the posterior probabilities is 1. 
<br/>
<img src="https://i.imgur.com/3Adx6RF.png" alt="image"/>
<br/>

Now we have the posterior probabilities for each die.
<br/>
<img src="https://i.imgur.com/DdSRCU3.png" alt="image"/>
<br/>

<h3>Collecting more evidence</h3>

So rolling a 6 we see that there is approx 39% chance it was from a 6-sided die and we have some basis for making an informed guess. However, to improve the odds of making a correct guess, we should gather more evidence. If the die is rolled again and this time it is a 5, we can calculate new values for the probabilities.
<br/>
<img src="https://i.imgur.com/YjTcW6t.png" alt="image"/>
<br/>

Now we can be more confident that a 6-sided die was rolled. However chance of being right is still around 50%
<br/>
<img src="https://i.imgur.com/DWmXpiC.png" alt="image"/>
<br/>

We can gather more evidence by with another roll of the die, this time the value returns 8. 
<br/>
<img src="https://i.imgur.com/o1OFseg.png" alt="image"/>
<br/>

Now we see that the probability has dramatically changed due to this roll. We see that the probability that the 8-sided die was chosen is 73%. Although guess might be wrong, the odds are strongly in your favor. 
<br/>
<img src="https://i.imgur.com/JyqrtCC.png" alt="image"/>
<br/>

This python code will take inputs on the number of times the die was rolled and the value of the die from each roll. The program will then return the posterior probabilities of each die on if it was the one that was likely chosen.  
<img src="https://i.imgur.com/zBFs4LN.jpg" alt="image"/>
