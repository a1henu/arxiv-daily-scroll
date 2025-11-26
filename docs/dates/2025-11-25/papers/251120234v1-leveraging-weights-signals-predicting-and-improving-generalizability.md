---
layout: default
title: Leveraging weights signals - Predicting and improving generalizability in reinforcement learning
---

# Leveraging weights signals - Predicting and improving generalizability in reinforcement learning
**arXiv**：[2511.20234v1](https://arxiv.org/abs/2511.20234) · [PDF](https://arxiv.org/pdf/2511.20234.pdf)  
**作者**：Olivier Moulin, Vincent Francois-lavet, Paul Elbers, Mark Hoogendoorn  

**一句话要点**：提出基于权重信号预测和优化强化学习智能体泛化性的方法

**关键词**：强化学习, 泛化性预测, PPO算法, 神经网络权重, 过拟合问题, 损失函数优化

## 3 点简述
- 核心问题：强化学习智能体易过拟合训练环境，泛化能力不足。
- 方法要点：利用神经网络内部权重预测泛化分数，并改进PPO损失函数。
- 实验或效果：改进版PPO算法在实验中提升了智能体的泛化性能。

## 摘要（原文）

> Generalizability of Reinforcement Learning (RL) agents (ability to perform on environments different from the ones they have been trained on) is a key problem as agents have the tendency to overfit to their training environments. In order to address this problem and offer a solution to increase the generalizability of RL agents, we introduce a new methodology to predict the generalizability score of RL agents based on the internal weights of the agent's neural networks. Using this prediction capability, we propose some changes in the Proximal Policy Optimization (PPO) loss function to boost the generalization score of the agents trained with this upgraded version. Experimental results demonstrate that our improved PPO algorithm yields agents with stronger generalizability compared to the original version.

