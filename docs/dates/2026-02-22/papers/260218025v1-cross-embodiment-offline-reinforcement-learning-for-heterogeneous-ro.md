---
layout: default
title: Cross-Embodiment Offline Reinforcement Learning for Heterogeneous Robot Datasets
---

# Cross-Embodiment Offline Reinforcement Learning for Heterogeneous Robot Datasets
**arXiv**：[2602.18025v1](https://arxiv.org/abs/2602.18025) · [PDF](https://arxiv.org/pdf/2602.18025.pdf)  
**作者**：Haruki Abe, Takayuki Osa, Yusuke Mukuta, Tatsuya Harada  

**一句话要点**：提出跨具身离线强化学习，利用异构机器人数据集预训练通用控制策略

**关键词**：离线强化学习, 跨具身学习, 机器人控制, 异构数据集, 策略预训练

## 3 点简述
- 核心问题：机器人策略预训练成本高，需跨不同形态平台收集高质量数据。
- 方法要点：结合离线强化学习和跨具身学习，聚合异构轨迹以获取通用控制先验。
- 实验效果：在16个机器人数据集上验证，优于行为克隆，但数据冲突需分组策略缓解。

## 摘要（原文）

> Scalable robot policy pre-training has been hindered by the high cost of collecting high-quality demonstrations for each platform. In this study, we address this issue by uniting offline reinforcement learning (offline RL) with cross-embodiment learning. Offline RL leverages both expert and abundant suboptimal data, and cross-embodiment learning aggregates heterogeneous robot trajectories across diverse morphologies to acquire universal control priors. We perform a systematic analysis of this offline RL and cross-embodiment paradigm, providing a principled understanding of its strengths and limitations. To evaluate this offline RL and cross-embodiment paradigm, we construct a suite of locomotion datasets spanning 16 distinct robot platforms. Our experiments confirm that this combined approach excels at pre-training with datasets rich in suboptimal trajectories, outperforming pure behavior cloning. However, as the proportion of suboptimal data and the number of robot types increase, we observe that conflicting gradients across morphologies begin to impede learning. To mitigate this, we introduce an embodiment-based grouping strategy in which robots are clustered by morphological similarity and the model is updated with a group gradient. This simple, static grouping substantially reduces inter-robot conflicts and outperforms existing conflict-resolution methods.

