---
layout: default
title: A Semi-supervised Molecular Learning Framework for Activity Cliff Estimation
---

# A Semi-supervised Molecular Learning Framework for Activity Cliff Estimation
**arXiv**：[2601.04507v1](https://arxiv.org/abs/2601.04507) · [PDF](https://arxiv.org/pdf/2601.04507.pdf)  
**作者**：Fang Wu  

**一句话要点**：提出SemiMol半监督学习框架以解决低数据场景下分子活性悬崖估计问题

**关键词**：分子性质预测, 半监督学习, 活性悬崖估计, 图神经网络, 伪标签方法, 课程学习

## 3 点简述
- 核心问题：活性悬崖挑战分子相似性假设，导致基于图的机器学习算法性能下降
- 方法要点：引入教师模型评估伪标签可信度，并设计自适应课程学习算法逐步处理难样本
- 实验或效果：在30个数据集上验证，显著提升图基架构性能，超越现有预训练和半监督基线

## 摘要（原文）

> Machine learning (ML) enables accurate and fast molecular property predictions, which are of interest in drug discovery and material design. Their success is based on the principle of similarity at its heart, assuming that similar molecules exhibit close properties. However, activity cliffs challenge this principle, and their presence leads to a sharp decline in the performance of existing ML algorithms, particularly graph-based methods. To overcome this obstacle under a low-data scenario, we propose a novel semi-supervised learning (SSL) method dubbed SemiMol, which employs predictions on numerous unannotated data as pseudo-signals for subsequent training. Specifically, we introduce an additional instructor model to evaluate the accuracy and trustworthiness of proxy labels because existing pseudo-labeling approaches require probabilistic outputs to reveal the model's confidence and fail to be applied in regression tasks. Moreover, we design a self-adaptive curriculum learning algorithm to progressively move the target model toward hard samples at a controllable pace. Extensive experiments on 30 activity cliff datasets demonstrate that SemiMol significantly enhances graph-based ML architectures and outpasses state-of-the-art pretraining and SSL baselines.

