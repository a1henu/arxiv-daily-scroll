---
layout: default
title: TreeGrad-Ranker: Feature Ranking via $O(L)$-Time Gradients for Decision Trees
---

# TreeGrad-Ranker: Feature Ranking via $O(L)$-Time Gradients for Decision Trees
**arXiv**：[2602.11623v1](https://arxiv.org/abs/2602.11623) · [PDF](https://arxiv.org/pdf/2602.11623.pdf)  
**作者**：Weida Li, Yaoliang Yu, Bryan Kian Hsiang Low  

**一句话要点**：提出TreeGrad-Ranker，通过O(L)时间梯度优化特征排序以解释决策树预测。

**关键词**：特征排序, 决策树解释, 梯度优化, 概率值, Shapley值, 数值稳定性

## 3 点简述
- 核心问题：概率值（如Shapley值）在优化插入和删除指标时不可靠，无法有效解决特征子集选择问题。
- 方法要点：基于TreeGrad计算联合目标的多线性扩展梯度，在O(L)时间内实现高效特征排序，并满足概率值公理（除线性外）。
- 实验或效果：TreeGrad-Ranker在插入和删除指标上显著优于基线，TreeGrad-Shap计算Shapley值的数值误差远低于Linear TreeShap。

## 摘要（原文）

> We revisit the use of probabilistic values, which include the well-known Shapley and Banzhaf values, to rank features for explaining the local predicted values of decision trees. The quality of feature rankings is typically assessed with the insertion and deletion metrics. Empirically, we observe that co-optimizing these two metrics is closely related to a joint optimization that selects a subset of features to maximize the local predicted value while minimizing it for the complement. However, we theoretically show that probabilistic values are generally unreliable for solving this joint optimization. Therefore, we explore deriving feature rankings by directly optimizing the joint objective. As the backbone, we propose TreeGrad, which computes the gradients of the multilinear extension of the joint objective in $O(L)$ time for decision trees with $L$ leaves; these gradients include weighted Banzhaf values. Building upon TreeGrad, we introduce TreeGrad-Ranker, which aggregates the gradients while optimizing the joint objective to produce feature rankings, and TreeGrad-Shap, a numerically stable algorithm for computing Beta Shapley values with integral parameters. In particular, the feature scores computed by TreeGrad-Ranker satisfy all the axioms uniquely characterizing probabilistic values, except for linearity, which itself leads to the established unreliability. Empirically, we demonstrate that the numerical error of Linear TreeShap can be up to $10^{15}$ times larger than that of TreeGrad-Shap when computing the Shapley value. As a by-product, we also develop TreeProb, which generalizes Linear TreeShap to support all probabilistic values. In our experiments, TreeGrad-Ranker performs significantly better on both insertion and deletion metrics. Our code is available at https://github.com/watml/TreeGrad.

