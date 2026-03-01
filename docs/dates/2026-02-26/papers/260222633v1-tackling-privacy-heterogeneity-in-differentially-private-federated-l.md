---
layout: default
title: Tackling Privacy Heterogeneity in Differentially Private Federated Learning
---

# Tackling Privacy Heterogeneity in Differentially Private Federated Learning
**arXiv**：[2602.22633v1](https://arxiv.org/abs/2602.22633) · [PDF](https://arxiv.org/pdf/2602.22633.pdf)  
**作者**：Ruichen Xu, Ying-Jun Angela Zhang, Jianwei Huang  

**一句话要点**：提出隐私感知客户端选择策略以解决差分隐私联邦学习中的隐私异质性问题

**关键词**：差分隐私联邦学习, 隐私异质性, 客户端选择, 收敛分析, 凸优化

## 3 点简述
- 核心问题：现有差分隐私联邦学习假设统一隐私预算，忽略实际中隐私需求的异质性，影响模型训练效果。
- 方法要点：基于收敛分析建立理论框架，通过凸优化自适应调整客户端选择概率以最小化训练误差。
- 实验或效果：在基准数据集上测试，相比基线方法，CIFAR-10测试准确率提升最高达10%。

## 摘要（原文）

> Differentially private federated learning (DP-FL) enables clients to collaboratively train machine learning models while preserving the privacy of their local data. However, most existing DP-FL approaches assume that all clients share a uniform privacy budget, an assumption that does not hold in real-world scenarios where privacy requirements vary widely. This privacy heterogeneity poses a significant challenge: conventional client selection strategies, which typically rely on data quantity, cannot distinguish between clients providing high-quality updates and those introducing substantial noise due to strict privacy constraints. To address this gap, we present the first systematic study of privacy-aware client selection in DP-FL. We establish a theoretical foundation by deriving a convergence analysis that quantifies the impact of privacy heterogeneity on training error. Building on this analysis, we propose a privacy-aware client selection strategy, formulated as a convex optimization problem, that adaptively adjusts selection probabilities to minimize training error. Extensive experiments on benchmark datasets demonstrate that our approach achieves up to a 10% improvement in test accuracy on CIFAR-10 compared to existing baselines under heterogeneous privacy budgets. These results highlight the importance of incorporating privacy heterogeneity into client selection for practical and effective federated learning.

