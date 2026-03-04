---
layout: default
title: DreamFlow: Local Navigation Beyond Observation via Conditional Flow Matching in the Latent Space
---

# DreamFlow: Local Navigation Beyond Observation via Conditional Flow Matching in the Latent Space
**arXiv**：[2603.02976v1](https://arxiv.org/abs/2603.02976) · [PDF](https://arxiv.org/pdf/2603.02976.pdf)  
**作者**：Jiwon Park, Dongkyu Lee, I Made Aswin Nahrendra, Jaeyoung Lim, Hyun Myung  

**一句话要点**：提出DreamFlow，通过条件流匹配在潜在空间中扩展感知范围以解决局部导航中的局部极小值问题。

**关键词**：局部导航, 条件流匹配, 潜在空间预测, 深度强化学习, 四足机器人

## 3 点简述
- 核心问题：局部导航在密集障碍环境中因感知受限易陷入局部极小值。
- 方法要点：基于条件流匹配学习局部高度图与导航上下文的空间表示映射。
- 实验或效果：在仿真和真实四足机器人实验中，预测精度和导航性能优于现有方法。

## 摘要（原文）

> Local navigation in cluttered environments often suffers from dense obstacles and frequent local minima. Conventional local planners rely on heuristics and are prone to failure, while deep reinforcement learning(DRL)based approaches provide adaptability but are constrained by limited onboard sensing. These limitations lead to navigation failures because the robot cannot perceive structures outside its field of view. In this paper, we propose DreamFlow, a DRL-based local navigation framework that extends the robot's perceptual horizon through conditional flow matching(CFM). The proposed CFM based prediction module learns probabilistic mapping between local height map latent representation and broader spatial representation conditioned on navigation context. This enables the navigation policy to predict unobserved environmental features and proactively avoid potential local minima. Experimental results demonstrate that DreamFlow outperforms existing methods in terms of latent prediction accuracy and navigation performance in simulation. The proposed method was further validated in cluttered real world environments with a quadrupedal robot. The project page is available at https://dreamflow-icra.github.io.

