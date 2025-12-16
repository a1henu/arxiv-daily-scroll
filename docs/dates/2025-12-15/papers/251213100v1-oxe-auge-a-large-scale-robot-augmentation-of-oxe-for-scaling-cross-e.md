---
layout: default
title: OXE-AugE: A Large-Scale Robot Augmentation of OXE for Scaling Cross-Embodiment Policy Learning
---

# OXE-AugE: A Large-Scale Robot Augmentation of OXE for Scaling Cross-Embodiment Policy Learning
**arXiv**：[2512.13100v1](https://arxiv.org/abs/2512.13100) · [PDF](https://arxiv.org/pdf/2512.13100.pdf)  
**作者**：Guanhua Ji, Harsha Polavaram, Lawrence Yunliang Chen, Sandeep Bajamahal, Zehan Ma, Simeon Adebola, Chenfeng Xu, Ken Goldberg  

**一句话要点**：提出OXE-AugE数据集与AugE-Toolkit流水线，通过机器人增强解决跨具身策略学习的数据不平衡问题。

**关键词**：跨具身策略学习, 机器人数据增强, 大规模数据集, 通用机器人策略, 分布偏移

## 3 点简述
- 核心问题：Open X-Embodiment数据集高度不平衡，前四种机器人类型占真实数据超85%，可能导致过拟合。
- 方法要点：开发AugE-Toolkit流水线，生成OXE-AugE数据集，增强9种机器人具身，轨迹数超440万。
- 实验或效果：增强提升策略性能，包括未见机器人；微调OpenVLA和π_0在真实任务中成功率提高24-45%。

## 摘要（原文）

> Large and diverse datasets are needed for training generalist robot policies that have potential to control a variety of robot embodiments -- robot arm and gripper combinations -- across diverse tasks and environments. As re-collecting demonstrations and retraining for each new hardware platform are prohibitively costly, we show that existing robot data can be augmented for transfer and generalization. The Open X-Embodiment (OXE) dataset, which aggregates demonstrations from over 60 robot datasets, has been widely used as the foundation for training generalist policies. However, it is highly imbalanced: the top four robot types account for over 85\% of its real data, which risks overfitting to robot--scene combinations. We present AugE-Toolkit, a scalable robot augmentation pipeline, and OXE-AugE, a high-quality open-source dataset that augments OXE with 9 different robot embodiments. OXE-AugE provides over 4.4 million trajectories, more than triple the size of the original OXE. We conduct a systematic study of how scaling robot augmentation impacts cross-embodiment learning. Results suggest that augmenting datasets with diverse arms and grippers improves policy performance not only on the augmented robots, but also on unseen robots and even the original robots under distribution shifts. In physical experiments, we demonstrate that state-of-the-art generalist policies such as OpenVLA and $π_0$ benefit from fine-tuning on OXE-AugE, improving success rates by 24-45% on previously unseen robot--gripper combinations across four real-world manipulation tasks. Project website: https://OXE-AugE.github.io/.

