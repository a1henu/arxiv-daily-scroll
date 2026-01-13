---
layout: default
title: Covariance-Driven Regression Trees: Reducing Overfitting in CART
---

# Covariance-Driven Regression Trees: Reducing Overfitting in CART
**arXiv**：[2601.07281v1](https://arxiv.org/abs/2601.07281) · [PDF](https://arxiv.org/pdf/2601.07281.pdf)  
**作者**：Likun Zhang, Wei Ma  

**一句话要点**：提出协方差驱动回归树以解决CART过拟合问题

**关键词**：决策树, 过拟合, 回归树, 协方差驱动, 分裂准则, 预测精度

## 3 点简述
- CART决策树易过拟合，尤其在深度大或样本少时
- 引入协方差驱动分裂准则，生成更平衡稳定的分裂
- 在模拟和真实任务中预测精度优于CART

## 摘要（原文）

> Decision trees are powerful machine learning algorithms, widely used in fields such as economics and medicine for their simplicity and interpretability. However, decision trees such as CART are prone to overfitting, especially when grown deep or the sample size is small. Conventional methods to reduce overfitting include pre-pruning and post-pruning, which constrain the growth of uninformative branches. In this paper, we propose a complementary approach by introducing a covariance-driven splitting criterion for regression trees (CovRT). This method is more robust to overfitting than the empirical risk minimization criterion used in CART, as it produces more balanced and stable splits and more effectively identifies covariates with true signals. We establish an oracle inequality of CovRT and prove that its predictive accuracy is comparable to that of CART in high-dimensional settings. We find that CovRT achieves superior prediction accuracy compared to CART in both simulations and real-world tasks.

