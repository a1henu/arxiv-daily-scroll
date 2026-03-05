---
layout: default
title: IPD: Boosting Sequential Policy with Imaginary Planning Distillation in Offline Reinforcement Learning
---

# IPD: Boosting Sequential Policy with Imaginary Planning Distillation in Offline Reinforcement Learning
**arXiv**：[2603.04289v1](https://arxiv.org/abs/2603.04289) · [PDF](https://arxiv.org/pdf/2603.04289.pdf)  
**作者**：Yihao Qin, Yuanfei Wang, Hang Zhou, Peiran Liu, Hao Dong, Yiding Ji  

**一句话要点**：提出IPD框架，通过想象规划蒸馏提升离线强化学习中序列策略的性能

**关键词**：离线强化学习, 序列策略, 想象规划, 蒸馏训练, 模型预测控制, 决策变换器

## 3 点简述
- 核心问题：基于决策变换器的序列策略在离线强化学习中受限于数据集质量和架构，难以整合次优经验并显式规划最优策略。
- 方法要点：IPD结合世界模型、准最优价值函数和模型预测控制，生成想象最优轨迹以增强数据，并训练序列策略进行蒸馏。
- 实验或效果：在D4RL基准测试中，IPD显著优于多种基于价值和变换器的离线强化学习方法，提升决策稳定性和性能。

## 摘要（原文）

> Decision transformer based sequential policies have emerged as a powerful paradigm in offline reinforcement learning (RL), yet their efficacy remains constrained by the quality of static datasets and inherent architectural limitations. Specifically, these models often struggle to effectively integrate suboptimal experiences and fail to explicitly plan for an optimal policy. To bridge this gap, we propose \textbf{Imaginary Planning Distillation (IPD)}, a novel framework that seamlessly incorporates offline planning into data generation, supervised training, and online inference. Our framework first learns a world model equipped with uncertainty measures and a quasi-optimal value function from the offline data. These components are utilized to identify suboptimal trajectories and augment them with reliable, imagined optimal rollouts generated via Model Predictive Control (MPC). A Transformer-based sequential policy is then trained on this enriched dataset, complemented by a value-guided objective that promotes the distillation of the optimal policy. By replacing the conventional, manually-tuned return-to-go with the learned quasi-optimal value function, IPD improves both decision-making stability and performance during inference. Empirical evaluations on the D4RL benchmark demonstrate that IPD significantly outperforms several state-of-the-art value-based and transformer-based offline RL methods across diverse tasks.

