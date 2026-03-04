---
layout: default
title: CMoE: Contrastive Mixture of Experts for Motion Control and Terrain Adaptation of Humanoid Robots
---

# CMoE: Contrastive Mixture of Experts for Motion Control and Terrain Adaptation of Humanoid Robots
**arXiv**：[2603.03067v1](https://arxiv.org/abs/2603.03067) · [PDF](https://arxiv.org/pdf/2603.03067.pdf)  
**作者**：Shihao Ma, Hongjin Chen, Zijun Xu, Yi Zhao, Ke Wu, Ruichen Yang, Leyao Zou, Zhongxue Gan, Wenchao Ding  

**一句话要点**：提出CMoE框架，通过对比学习优化专家激活分布，提升人形机器人复杂地形适应能力。

**关键词**：人形机器人控制, 混合专家模型, 对比学习, 地形适应, 强化学习, 运动控制

## 3 点简述
- 核心问题：传统混合专家框架中门控网络激活分布均匀，削弱专家专业化，限制模型表达能力。
- 方法要点：引入对比学习约束，最大化同地形内专家激活一致性，最小化跨地形相似性，促进专家专业化。
- 实验或效果：在Unitree G1机器人上验证，能跨越20厘米高台阶和80厘米宽间隙，在混合地形中实现稳健自然步态。

## 摘要（原文）

> For effective deployment in real-world environments, humanoid robots must autonomously navigate a diverse range of complex terrains with abrupt transitions. While the Vanilla mixture of experts (MoE) framework is theoretically capable of modeling diverse terrain features, in practice, the gating network exhibits nearly uniform expert activations across different terrains, weakening the expert specialization and limiting the model's expressive power. To address this limitation, we introduce CMoE, a novel single-stage reinforcement learning framework that integrates contrastive learning to refine expert activation distributions. By imposing contrastive constraints, CMoE maximizes the consistency of expert activations within the same terrain while minimizing their similarity across different terrains, thereby encouraging experts to specialize in distinct terrain types. We validated our approach on the Unitree G1 humanoid robot through a series of challenging experiments. Results demonstrate that CMoE enables the robot to traverse continuous steps up to 20 cm high and gaps up to 80 cm wide, while achieving robust and natural gait across diverse mixed terrains, surpassing the limits of existing methods. To support further research and foster community development, we release our code publicly.

