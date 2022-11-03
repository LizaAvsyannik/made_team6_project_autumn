#### Train Test Split
As we haven't yet decided on the approaches for the recsys, no train test split is performed for the time being. It will be corrected in the next sprint. As if we decide to go with the simplest approach of predicting the most popular autor in the tag, no training at all will be required and train test split will be unnecessary. If we go with something more advanced like representation learning, dataset will be transformed to sparse matrix and then splitted.

#### RecSys Metrics Analysis
***1. Precision@k and Recall @k*** <br>
Definition: 
Precision@k is the fraction of relevant items in the top k recommendations, and recall@k is the coverage of relevant times in the top k. <br>
Application to the problem: would work, seems like easy to compute, especially if we decide that the system always gives constant number of recommended authors.

***2. Mean Average Precision (MAP@k)*** <br>
Definition: 
MAP is the mean of Average Precision. If we have the AP (which is the area under the precision-recall curve) for each user, it is trivial just to average it over all users to calculate the MAP. <br>
Application to the problem: seems better than the previous one as we calculate for all the users, not just one.

***3. Normalized Discounted Cumulative Gain (NDCG)*** <br>
Definition: https://en.wikipedia.org/wiki/Discounted_cumulative_gain <br>
Application to the problem: will have to introduce some relevance score (for instance, cosine distance, or simply binary [0, 1], depending on the recsys model)
