---
layout: default
title: Smooth Operator: Smooth Verifiable Reward Activates Spatial Reasoning Ability of Vision-Language Model
---

# Smooth Operator: Smooth Verifiable Reward Activates Spatial Reasoning Ability of Vision-Language Model
**arXiv**：[2601.07695v1](https://arxiv.org/abs/2601.07695) · [PDF](https://arxiv.org/pdf/2601.07695.pdf)  
**作者**：Siwen Jiao, Tianxiong Lv, Kangan Qian, Chenxu Zhao, Xiuyuan Zhu, Tianlun Li, Xiaolong Cheng, Jinyu Li, Zhihao Liao, Yang Cai  

**一句话要点**：提出平滑数值奖励激活算子和绝对保持GRPO框架，以解决视觉语言模型在3D场景理解中的数值预测瓶颈。

**关键词**：视觉语言模型, 3D场景理解, 强化学习, 奖励设计, 数值预测, 数据效率

## 3 点简述
- 核心问题：传统强化学习在3D场景理解中因奖励稀疏和梯度不稳定，无法有效利用物理约束信号。
- 方法要点：引入平滑数值奖励激活算子，将反馈转换为连续奖励，并结合绝对保持GRPO框架保留数值信息。
- 实验或效果：在构建的Numerical3D-50k数据集上，AP-GRPO实现与大规模监督方法相当性能，数据效率更高。

## 摘要（原文）

> Vision-Language Models (VLMs) face a critical bottleneck in achieving precise numerical prediction for 3D scene understanding. Traditional reinforcement learning (RL) approaches, primarily based on relative ranking, often suffer from severe reward sparsity and gradient instability, failing to effectively exploit the verifiable signals provided by 3D physical constraints. Notably, in standard GRPO frameworks, relative normalization causes "near-miss" samples (characterized by small but non-zero errors) to suffer from advantage collapse. This leads to a severe data utilization bottleneck where valuable boundary samples are discarded during optimization. To address this, we introduce the Smooth Numerical Reward Activation (SNRA) operator and the Absolute-Preserving GRPO (AP-GRPO) framework. SNRA employs a dynamically parameterized Sigmoid function to transform raw feedback into a dense, continuous reward continuum. Concurrently, AP-GRPO integrates absolute scalar gradients to mitigate the numerical information loss inherent in conventional relative-ranking mechanisms. By leveraging this approach, we constructed Numerical3D-50k, a dataset comprising 50,000 verifiable 3D subtasks. Empirical results indicate that AP-GRPO achieves performance parity with large-scale supervised methods while maintaining higher data efficiency, effectively activating latent 3D reasoning in VLMs without requiring architectural modifications.

