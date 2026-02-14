---
layout: default
title: Energy-Aware Spike Budgeting for Continual Learning in Spiking Neural Networks for Neuromorphic Vision
---

# Energy-Aware Spike Budgeting for Continual Learning in Spiking Neural Networks for Neuromorphic Vision
**arXiv**：[2602.12236v1](https://arxiv.org/abs/2602.12236) · [PDF](https://arxiv.org/pdf/2602.12236.pdf)  
**作者**：Anika Tabassum Meem, Muntasir Hossain Nadid, Md Zesun Ahmed Mia  

**一句话要点**：提出能量感知脉冲预算框架，以解决脉冲神经网络在神经形态视觉中持续学习的灾难性遗忘和能效优化问题。

**关键词**：脉冲神经网络, 持续学习, 神经形态视觉, 能量感知, 事件数据集, 脉冲预算

## 3 点简述
- 核心问题：脉冲神经网络在持续学习中面临灾难性遗忘，现有方法未联合优化准确性和能效，尤其在事件数据集上探索有限。
- 方法要点：集成经验回放、可学习神经元参数和自适应脉冲调度器，在训练中施加数据集特定的能量约束。
- 实验或效果：在帧数据集上提升准确性并降低脉冲率，在事件数据集上实现准确性增益，同时最小化动态功耗。

## 摘要（原文）

> Neuromorphic vision systems based on spiking neural networks (SNNs) offer ultra-low-power perception for event-based and frame-based cameras, yet catastrophic forgetting remains a critical barrier to deployment in continually evolving environments. Existing continual learning methods, developed primarily for artificial neural networks, seldom jointly optimize accuracy and energy efficiency, with particularly limited exploration on event-based datasets. We propose an energy-aware spike budgeting framework for continual SNN learning that integrates experience replay, learnable leaky integrate-and-fire neuron parameters, and an adaptive spike scheduler to enforce dataset-specific energy constraints during training. Our approach exhibits modality-dependent behavior: on frame-based datasets (MNIST, CIFAR-10), spike budgeting acts as a sparsity-inducing regularizer, improving accuracy while reducing spike rates by up to 47\%; on event-based datasets (DVS-Gesture, N-MNIST, CIFAR-10-DVS), controlled budget relaxation enables accuracy gains up to 17.45 percentage points with minimal computational overhead. Across five benchmarks spanning both modalities, our method demonstrates consistent performance improvements while minimizing dynamic power consumption, advancing the practical viability of continual learning in neuromorphic vision systems.

