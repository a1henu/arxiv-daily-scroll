---
layout: default
title: Disentangling perception and reasoning for improving data efficiency in learning cloth manipulation without demonstrations
---

# Disentangling perception and reasoning for improving data efficiency in learning cloth manipulation without demonstrations
**arXiv**：[2601.21713v1](https://arxiv.org/abs/2601.21713) · [PDF](https://arxiv.org/pdf/2601.21713.pdf)  
**作者**：Donatien Delehelle, Fei Chen, Darwin Caldwell  

**一句话要点**：提出解耦感知与推理的模块化强化学习方法，以提升无演示布料操作的数据效率

**关键词**：布料操作, 强化学习, 数据效率, 模块化设计, 感知解耦, 仿真到现实迁移

## 3 点简述
- 核心问题：布料操作因高维状态空间、复杂动力学和自遮挡导致数据效率低、计算成本高
- 方法要点：通过解耦感知与推理，采用模块化设计减少模型大小和训练时间
- 实验或效果：在SoftGym基准测试中性能显著提升，模型更小且可迁移到现实世界

## 摘要（原文）

> Cloth manipulation is a ubiquitous task in everyday life, but it remains an open challenge for robotics. The difficulties in developing cloth manipulation policies are attributed to the high-dimensional state space, complex dynamics, and high propensity to self-occlusion exhibited by fabrics. As analytical methods have not been able to provide robust and general manipulation policies, reinforcement learning (RL) is considered a promising approach to these problems. However, to address the large state space and complex dynamics, data-based methods usually rely on large models and long training times. The resulting computational cost significantly hampers the development and adoption of these methods. Additionally, due to the challenge of robust state estimation, garment manipulation policies often adopt an end-to-end learning approach with workspace images as input. While this approach enables a conceptually straightforward sim-to-real transfer via real-world fine-tuning, it also incurs a significant computational cost by training agents on a highly lossy representation of the environment state. This paper questions this common design choice by exploring an efficient and modular approach to RL for cloth manipulation. We show that, through careful design choices, model size and training time can be significantly reduced when learning in simulation. Furthermore, we demonstrate how the resulting simulation-trained model can be transferred to the real world. We evaluate our approach on the SoftGym benchmark and achieve significant performance improvements over available baselines on our task, while using a substantially smaller model.

