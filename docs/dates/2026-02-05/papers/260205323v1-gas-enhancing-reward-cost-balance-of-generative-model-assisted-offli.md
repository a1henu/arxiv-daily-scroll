---
layout: default
title: GAS: Enhancing Reward-Cost Balance of Generative Model-assisted Offline Safe RL
---

# GAS: Enhancing Reward-Cost Balance of Generative Model-assisted Offline Safe RL
**arXiv**：[2602.05323v1](https://arxiv.org/abs/2602.05323) · [PDF](https://arxiv.org/pdf/2602.05323.pdf)  
**作者**：Zifan Liu, Xinran Li, Shibo Chen, Jun Zhang  

**一句话要点**：提出GAS算法以增强离线安全强化学习中生成模型的奖励-成本平衡与轨迹拼接能力

**关键词**：离线安全强化学习, 生成模型, 奖励-成本平衡, 轨迹拼接, 目标函数, 数据增强

## 3 点简述
- 核心问题：生成模型辅助方法在离线安全强化学习中缺乏轨迹拼接能力且难以平衡冲突的奖励与成本目标
- 方法要点：通过数据增强与重标注提升轨迹拼接，引入目标函数估计最优奖励与成本目标以指导策略训练
- 实验或效果：实证结果显示GAS在奖励最大化与约束满足的平衡上优于现有方法

## 摘要（原文）

> Offline Safe Reinforcement Learning (OSRL) aims to learn a policy to achieve high performance in sequential decision-making while satisfying constraints, using only pre-collected datasets. Recent works, inspired by the strong capabilities of Generative Models (GMs), reformulate decision-making in OSRL as a conditional generative process, where GMs generate desirable actions conditioned on predefined reward and cost values. However, GM-assisted methods face two major challenges in OSRL: (1) lacking the ability to "stitch" optimal transitions from suboptimal trajectories within the dataset, and (2) struggling to balance reward targets with cost targets, particularly when they are conflict. To address these issues, we propose Goal-Assisted Stitching (GAS), a novel algorithm designed to enhance stitching capabilities while effectively balancing reward maximization and constraint satisfaction. To enhance the stitching ability, GAS first augments and relabels the dataset at the transition level, enabling the construction of high-quality trajectories from suboptimal ones. GAS also introduces novel goal functions, which estimate the optimal achievable reward and cost goals from the dataset. These goal functions, trained using expectile regression on the relabeled and augmented dataset, allow GAS to accommodate a broader range of reward-cost return pairs and achieve a better tradeoff between reward maximization and constraint satisfaction compared to human-specified values. The estimated goals then guide policy training, ensuring robust performance under constrained settings. Furthermore, to improve training stability and efficiency, we reshape the dataset to achieve a more uniform reward-cost return distribution. Empirical results validate the effectiveness of GAS, demonstrating superior performance in balancing reward maximization and constraint satisfaction compared to existing methods.

