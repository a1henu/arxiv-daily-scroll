---
layout: default
title: Self-Augmented Mixture-of-Experts for QoS Prediction
---

# Self-Augmented Mixture-of-Experts for QoS Prediction
**arXiv**：[2601.11036v1](https://arxiv.org/abs/2601.11036) · [PDF](https://arxiv.org/pdf/2601.11036.pdf)  
**作者**：Kecheng Cai, Chao Peng, Chenyang Xu, Xia Chen  

**一句话要点**：提出自增强专家混合模型以解决QoS预测中的交互稀疏性问题

**关键词**：QoS预测, 自增强学习, 专家混合模型, 稀疏交互, 服务计算, 个性化推荐

## 3 点简述
- 核心问题：QoS预测中用户-服务交互稀疏，仅少量反馈值可观测。
- 方法要点：设计自增强策略，利用模型预测迭代优化，结合专家混合架构实现专家间协作。
- 实验或效果：在基准数据集上超越现有基线，取得竞争性结果。

## 摘要（原文）

> Quality of Service (QoS) prediction is one of the most fundamental problems in service computing and personalized recommendation. In the problem, there is a set of users and services, each associated with a set of descriptive features. Interactions between users and services produce feedback values, typically represented as numerical QoS metrics such as response time or availability. Given the observed feedback for a subset of user-service pairs, the goal is to predict the QoS values for the remaining pairs.
>   A key challenge in QoS prediction is the inherent sparsity of user-service interactions, as only a small subset of feedback values is typically observed. To address this, we propose a self-augmented strategy that leverages a model's own predictions for iterative refinement. In particular, we partially mask the predicted values and feed them back into the model to predict again. Building on this idea, we design a self-augmented mixture-of-experts model, where multiple expert networks iteratively and collaboratively estimate QoS values. We find that the iterative augmentation process naturally aligns with the MoE architecture by enabling inter-expert communication: in the second round, each expert receives the first-round predictions and refines its output accordingly. Experiments on benchmark datasets show that our method outperforms existing baselines and achieves competitive results.

