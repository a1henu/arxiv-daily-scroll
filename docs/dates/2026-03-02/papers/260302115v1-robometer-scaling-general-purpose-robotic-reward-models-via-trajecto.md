---
layout: default
title: Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons
---

# Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons
**arXiv**：[2603.02115v1](https://arxiv.org/abs/2603.02115) · [PDF](https://arxiv.org/pdf/2603.02115.pdf)  
**作者**：Anthony Liang, Yigit Korkmaz, Jiahui Zhang, Minyoung Hwang, Abrar Anwar, Sidhant Kaushik, Aditya Shah, Alex S. Huang, Luke Zettlemoyer, Dieter Fox, Yu Xiang, Anqi Li, Andreea Bobu, Abhishek Gupta, Stephen Tu, Erdem Biyik, Jesse Zhang  

**一句话要点**：提出Robometer框架，通过轨迹比较结合进度与偏好监督，以解决大规模机器人数据中奖励模型扩展性问题。

**关键词**：机器人奖励建模, 轨迹比较学习, 大规模数据集, 泛化性能, 进度监督, 偏好学习

## 3 点简述
- 核心问题：传统奖励模型依赖专家演示的绝对进度预测，在大规模含失败轨迹的数据中扩展性差且标签模糊。
- 方法要点：结合帧级进度损失与轨迹比较偏好损失，利用专家和失败轨迹进行双目标训练。
- 实验或效果：在基准和真实世界评估中，Robometer学习到更泛化的奖励函数，提升下游应用性能。

## 摘要（原文）

> General-purpose robot reward models are typically trained to predict absolute task progress from expert demonstrations, providing only local, frame-level supervision. While effective for expert demonstrations, this paradigm scales poorly to large-scale robotics datasets where failed and suboptimal trajectories are abundant and assigning dense progress labels is ambiguous. We introduce Robometer, a scalable reward modeling framework that combines intra-trajectory progress supervision with inter-trajectory preference supervision. Robometer is trained with a dual objective: a frame-level progress loss that anchors reward magnitude on expert data, and a trajectory-comparison preference loss that imposes global ordering constraints across trajectories of the same task, enabling effective learning from both real and augmented failed trajectories. To support this formulation at scale, we curate RBM-1M, a reward-learning dataset comprising over one million trajectories spanning diverse robot embodiments and tasks, including substantial suboptimal and failure data. Across benchmarks and real-world evaluations, Robometer learns more generalizable reward functions than prior methods and improves robot learning performance across a diverse set of downstream applications. Code, model weights, and videos at https://robometer.github.io/.

