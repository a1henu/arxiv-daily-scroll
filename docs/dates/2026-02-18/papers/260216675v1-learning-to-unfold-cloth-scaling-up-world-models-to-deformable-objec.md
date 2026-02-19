---
layout: default
title: Learning to unfold cloth: Scaling up world models to deformable object manipulation
---

# Learning to unfold cloth: Scaling up world models to deformable object manipulation
**arXiv**：[2602.16675v1](https://arxiv.org/abs/2602.16675) · [PDF](https://arxiv.org/pdf/2602.16675.pdf)  
**作者**：Jack Rome, Stephen James, Subramanian Ramamoorthy  

**一句话要点**：提出改进DreamerV2架构以解决机器人空中布料展开的泛化问题

**关键词**：布料操控, 可变形物体, 强化学习, 世界模型, 机器人部署

## 3 点简述
- 核心问题：布料作为可变形物体，其复杂物理特性使机器人操控面临泛化挑战。
- 方法要点：修改DreamerV2架构，引入表面法线输入，并优化回放缓冲和数据增强过程。
- 实验或效果：在仿真和零样本物理机器人部署中，成功展开多种布料，验证了架构的泛化优势。

## 摘要（原文）

> Learning to manipulate cloth is both a paradigmatic problem for robotic research and a problem of immediate relevance to a variety of applications ranging from assistive care to the service industry. The complex physics of the deformable object makes this problem of cloth manipulation nontrivial. In order to create a general manipulation strategy that addresses a variety of shapes, sizes, fold and wrinkle patterns, in addition to the usual problems of appearance variations, it becomes important to carefully consider model structure and their implications for generalisation performance. In this paper, we present an approach to in-air cloth manipulation that uses a variation of a recently proposed reinforcement learning architecture, DreamerV2. Our implementation modifies this architecture to utilise surface normals input, in addition to modiying the replay buffer and data augmentation procedures. Taken together these modifications represent an enhancement to the world model used by the robot, addressing the physical complexity of the object being manipulated by the robot. We present evaluations both in simulation and in a zero-shot deployment of the trained policies in a physical robot setup, performing in-air unfolding of a variety of different cloth types, demonstrating the generalisation benefits of our proposed architecture.

