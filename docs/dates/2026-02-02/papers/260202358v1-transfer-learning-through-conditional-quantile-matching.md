---
layout: default
title: Transfer Learning Through Conditional Quantile Matching
---

# Transfer Learning Through Conditional Quantile Matching
**arXiv**：[2602.02358v1](https://arxiv.org/abs/2602.02358) · [PDF](https://arxiv.org/pdf/2602.02358.pdf)  
**作者**：Yikun Zhang, Steven Wilkins-Reeves, Wesley Lee, Aude Hofleitner  

**一句话要点**：提出基于条件分位数匹配的迁移学习框架，以提升数据稀缺目标域的回归预测性能。

**关键词**：迁移学习, 条件分位数匹配, 数据增强, 回归预测, 异构源域, 风险界限

## 3 点简述
- 核心问题：数据稀缺目标域中回归预测性能受限，需利用异构源域进行迁移学习。
- 方法要点：为每个源域学习条件生成模型，通过条件分位数匹配校准响应分布至目标域。
- 实验或效果：理论证明增强数据集训练的风险界限更紧，实验显示预测准确性优于基准方法。

## 摘要（原文）

> We introduce a transfer learning framework for regression that leverages heterogeneous source domains to improve predictive performance in a data-scarce target domain. Our approach learns a conditional generative model separately for each source domain and calibrates the generated responses to the target domain via conditional quantile matching. This distributional alignment step corrects general discrepancies between source and target domains without imposing restrictive assumptions such as covariate or label shift. The resulting framework provides a principled and flexible approach to high-quality data augmentation for downstream learning tasks in the target domain. From a theoretical perspective, we show that an empirical risk minimizer (ERM) trained on the augmented dataset achieves a tighter excess risk bound than the target-only ERM under mild conditions. In particular, we establish new convergence rates for the quantile matching estimator that governs the transfer bias-variance tradeoff. From a practical perspective, extensive simulations and real data applications demonstrate that the proposed method consistently improves prediction accuracy over target-only learning and competing transfer learning methods.

