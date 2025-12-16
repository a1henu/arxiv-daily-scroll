---
layout: default
title: PAC-Bayes Bounds for Multivariate Linear Regression and Linear Autoencoders
---

# PAC-Bayes Bounds for Multivariate Linear Regression and Linear Autoencoders
**arXiv**：[2512.12905v1](https://arxiv.org/abs/2512.12905) · [PDF](https://arxiv.org/pdf/2512.12905.pdf)  
**作者**：Ruixin Guo, Ruoming Jin, Xinyu Li, Yang Zhou  

**一句话要点**：提出多元线性回归与线性自编码器的PAC-Bayes泛化界，以增强推荐系统理论理解。

**关键词**：PAC-Bayes界, 多元线性回归, 线性自编码器, 泛化理论, 推荐系统, 统计学习

## 3 点简述
- 研究多元线性回归和线性自编码器的泛化性，填补理论空白。
- 扩展单输出线性回归的PAC-Bayes界，建立收敛条件并应用于线性自编码器。
- 实验显示界紧致，与召回率和NDCG等实用排名指标相关良好。

## 摘要（原文）

> Linear Autoencoders (LAEs) have shown strong performance in state-of-the-art recommender systems. However, this success remains largely empirical, with limited theoretical understanding. In this paper, we investigate the generalizability -- a theoretical measure of model performance in statistical learning -- of multivariate linear regression and LAEs. We first propose a PAC-Bayes bound for multivariate linear regression, extending the earlier bound for single-output linear regression by Shalaeva et al., and establish sufficient conditions for its convergence. We then show that LAEs, when evaluated under a relaxed mean squared error, can be interpreted as constrained multivariate linear regression models on bounded data, to which our bound adapts. Furthermore, we develop theoretical methods to improve the computational efficiency of optimizing the LAE bound, enabling its practical evaluation on large models and real-world datasets. Experimental results demonstrate that our bound is tight and correlates well with practical ranking metrics such as Recall@K and NDCG@K.

