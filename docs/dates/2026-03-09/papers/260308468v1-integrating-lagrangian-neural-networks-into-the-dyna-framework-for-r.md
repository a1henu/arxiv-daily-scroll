---
layout: default
title: Integrating Lagrangian Neural Networks into the Dyna Framework for Reinforcement Learning
---

# Integrating Lagrangian Neural Networks into the Dyna Framework for Reinforcement Learning
**arXiv**：[2603.08468v1](https://arxiv.org/abs/2603.08468) · [PDF](https://arxiv.org/pdf/2603.08468.pdf)  
**作者**：Shreya Das, Kundan Kumar, Muhammad Iqbal, Outi Savolainen, Dominik Baumann, Laura Ruotsalainen, Simo Särkkä  

**一句话要点**：提出基于拉格朗日神经网络的Dyna框架，以提升模型强化学习中动力学模型的物理一致性。

**关键词**：模型强化学习, 拉格朗日神经网络, Dyna框架, 动力学建模, 状态估计优化

## 3 点简述
- 核心问题：基于模型的强化学习依赖黑盒动力学模型，预测准确性差且不遵循物理定律。
- 方法要点：在Dyna框架中集成拉格朗日神经网络，通过拉格朗日结构约束模型训练，使用随机梯度和状态估计优化器学习权重。
- 实验或效果：状态估计优化器训练收敛更快，仿真结果验证了该框架在提升样本效率和预测准确性方面的有效性。

## 摘要（原文）

> Model-based reinforcement learning (MBRL) is sample-efficient but depends on the accuracy of the learned dynamics, which are often modeled using black-box methods that do not adhere to physical laws. Those methods tend to produce inaccurate predictions when presented with data that differ from the original training set. In this work, we employ Lagrangian neural networks (LNNs), which enforce an underlying Lagrangian structure to train the model within a Dyna-based MBRL framework. Furthermore, we train the LNN using stochastic gradient-based and state-estimation-based optimizers to learn the network's weights. The state-estimation-based method converges faster than the stochastic gradient-based method during neural network training. Simulation results are provided to illustrate the effectiveness of the proposed LNN-based Dyna framework for MBRL.

