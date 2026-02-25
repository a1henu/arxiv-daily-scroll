---
layout: default
title: Ski Rental with Distributional Predictions of Unknown Quality
---

# Ski Rental with Distributional Predictions of Unknown Quality
**arXiv**：[2602.21104v1](https://arxiv.org/abs/2602.21104) · [PDF](https://arxiv.org/pdf/2602.21104.pdf)  
**作者**：Qiming Cui, Michael Dinitz  

**一句话要点**：提出基于分布预测的滑雪租赁算法，以未知质量的预测优化在线决策成本。

**关键词**：滑雪租赁问题, 分布预测, 在线算法, Wasserstein距离, 一致性鲁棒性

## 3 点简述
- 研究滑雪租赁在线问题，引入分布预测而非点预测以增强模型适应性。
- 算法成本上限为OPT加O(min(max(η,1)*√b, b log b))，η为预测分布与真实分布的Wasserstein-1距离。
- 无需预测误差先验，在预测准确时一致性为O(√b)，误差大时鲁棒性为O(b log b)。

## 摘要（原文）

> We revisit the central online problem of ski rental in the "algorithms with predictions" framework from the point of view of distributional predictions. Ski rental was one of the first problems to be studied with predictions, where a natural prediction is simply the number of ski days. But it is both more natural and potentially more powerful to think of a prediction as a distribution p-hat over the ski days. If the true number of ski days is drawn from some true (but unknown) distribution p, then we show as our main result that there is an algorithm with expected cost at most OPT + O(min(max({eta}, 1) * sqrt(b), b log b)), where OPT is the expected cost of the optimal policy for the true distribution p, b is the cost of buying, and {eta} is the Earth Mover's (Wasserstein-1) distance between p and p-hat. Note that when {eta} < o(sqrt(b)) this gives additive loss less than b (the trivial bound), and when {eta} is arbitrarily large (corresponding to an extremely inaccurate prediction) we still do not pay more than O(b log b) additive loss. An implication of these bounds is that our algorithm has consistency O(sqrt(b)) (additive loss when the prediction error is 0) and robustness O(b log b) (additive loss when the prediction error is arbitrarily large). Moreover, we do not need to assume that we know (or have any bound on) the prediction error {eta}, in contrast with previous work in robust optimization which assumes that we know this error.
>   We complement this upper bound with a variety of lower bounds showing that it is essentially tight: not only can the consistency/robustness tradeoff not be improved, but our particular loss function cannot be meaningfully improved.

