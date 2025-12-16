---
layout: default
title: PvP: Data-Efficient Humanoid Robot Learning with Proprioceptive-Privileged Contrastive Representations
---

# PvP: Data-Efficient Humanoid Robot Learning with Proprioceptive-Privileged Contrastive Representations
**arXiv**：[2512.13093v1](https://arxiv.org/abs/2512.13093) · [PDF](https://arxiv.org/pdf/2512.13093.pdf)  
**作者**：Mingqi Yuan, Tao Yu, Haolin Song, Bo Li, Xin Jin, Hua Chen, Wenjun Zeng  

**一句话要点**：提出PvP框架，利用本体感知与特权状态互补性，提升人形机器人强化学习的数据效率。

**关键词**：人形机器人控制, 对比学习, 状态表示学习, 数据效率, 强化学习, 本体感知

## 3 点简述
- 核心问题：人形机器人强化学习样本效率低，源于复杂动力学和部分可观测性。
- 方法要点：PvP通过对比学习学习紧凑任务相关表示，无需手工数据增强。
- 实验或效果：在LimX Oli机器人上，PvP在速度跟踪和运动模仿任务中显著优于基线方法。

## 摘要（原文）

> Achieving efficient and robust whole-body control (WBC) is essential for enabling humanoid robots to perform complex tasks in dynamic environments. Despite the success of reinforcement learning (RL) in this domain, its sample inefficiency remains a significant challenge due to the intricate dynamics and partial observability of humanoid robots. To address this limitation, we propose PvP, a Proprioceptive-Privileged contrastive learning framework that leverages the intrinsic complementarity between proprioceptive and privileged states. PvP learns compact and task-relevant latent representations without requiring hand-crafted data augmentations, enabling faster and more stable policy learning. To support systematic evaluation, we develop SRL4Humanoid, the first unified and modular framework that provides high-quality implementations of representative state representation learning (SRL) methods for humanoid robot learning. Extensive experiments on the LimX Oli robot across velocity tracking and motion imitation tasks demonstrate that PvP significantly improves sample efficiency and final performance compared to baseline SRL methods. Our study further provides practical insights into integrating SRL with RL for humanoid WBC, offering valuable guidance for data-efficient humanoid robot learning.

