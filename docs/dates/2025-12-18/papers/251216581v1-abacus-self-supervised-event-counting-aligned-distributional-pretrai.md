---
layout: default
title: Abacus: Self-Supervised Event Counting-Aligned Distributional Pretraining for Sequential User Modeling
---

# Abacus: Self-Supervised Event Counting-Aligned Distributional Pretraining for Sequential User Modeling
**arXiv**：[2512.16581v1](https://arxiv.org/abs/2512.16581) · [PDF](https://arxiv.org/pdf/2512.16581.pdf)  
**作者**：Sullivan Castro, Artem Betlei, Thomas Di Martino, Nadir El Manouzi  

**一句话要点**：提出Abacus自监督预训练方法，结合事件计数分布预测与序列建模，以提升展示广告中的用户购买行为预测性能。

**关键词**：自监督预训练, 序列用户建模, 事件计数分布, 展示广告, 混合学习目标, 用户行为预测

## 3 点简述
- 核心问题：用户购买行为建模面临事件稀疏、类别不平衡和时序不规则挑战，传统方法依赖手工特征，忽略用户意图的细粒度演化。
- 方法要点：引入Abacus预测用户事件的经验频率分布，结合自监督预训练与序列学习目标，融合聚合统计的稳定性和序列建模的敏感性。
- 实验或效果：在真实数据集上，Abacus预训练加速下游任务收敛，混合方法相比基线提升高达6.1% AUC。

## 摘要（原文）

> Modeling user purchase behavior is a critical challenge in display advertising systems, necessary for real-time bidding. The difficulty arises from the sparsity of positive user events and the stochasticity of user actions, leading to severe class imbalance and irregular event timing. Predictive systems usually rely on hand-crafted "counter" features, overlooking the fine-grained temporal evolution of user intent. Meanwhile, current sequential models extract direct sequential signal, missing useful event-counting statistics. We enhance deep sequential models with self-supervised pretraining strategies for display advertising. Especially, we introduce Abacus, a novel approach of predicting the empirical frequency distribution of user events. We further propose a hybrid objective unifying Abacus with sequential learning objectives, combining stability of aggregated statistics with the sequence modeling sensitivity. Experiments on two real-world datasets show that Abacus pretraining outperforms existing methods accelerating downstream task convergence, while hybrid approach yields up to +6.1% AUC compared to the baselines.

