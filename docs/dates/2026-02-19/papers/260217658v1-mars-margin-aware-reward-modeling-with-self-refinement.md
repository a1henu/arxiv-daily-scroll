---
layout: default
title: MARS: Margin-Aware Reward-Modeling with Self-Refinement
---

# MARS: Margin-Aware Reward-Modeling with Self-Refinement
**arXiv**：[2602.17658v1](https://arxiv.org/abs/2602.17658) · [PDF](https://arxiv.org/pdf/2602.17658.pdf)  
**作者**：Payel Bhattacharjee, Osvaldo Simeone, Ravi Tandon  

**一句话要点**：提出MARS框架，通过自适应边界感知增强与采样策略，提升奖励模型在偏好数据有限场景下的鲁棒性。

**关键词**：奖励建模, 数据增强, 自适应采样, 边界感知, 鲁棒性优化, 偏好学习

## 3 点简述
- 核心问题：奖励模型训练依赖昂贵人工偏好数据，现有增强方法忽略模型估计难度。
- 方法要点：针对低边界模糊偏好对进行自适应增强，迭代优化训练分布以聚焦失败模式。
- 实验或效果：理论证明增强信息与改善条件数，实证显示优于均匀增强的稳定增益。

## 摘要（原文）

> Reward modeling is a core component of modern alignment pipelines including RLHF and RLAIF, underpinning policy optimization methods including PPO and TRPO. However, training reliable reward models relies heavily on human-labeled preference data, which is costly and limited, motivating the use of data augmentation. Existing augmentation approaches typically operate at the representation or semantic level and remain agnostic to the reward model's estimation difficulty. In this paper, we propose MARS, an adaptive, margin-aware augmentation and sampling strategy that explicitly targets ambiguous and failure modes of the reward model. Our proposed framework, MARS, concentrates augmentation on low-margin (ambiguous) preference pairs where the reward model is most uncertain, and iteratively refines the training distribution via hard-sample augmentation. We provide theoretical guarantees showing that this strategy increases the average curvature of the loss function hence enhance information and improves conditioning, along with empirical results demonstrating consistent gains over uniform augmentation for robust reward modeling.

