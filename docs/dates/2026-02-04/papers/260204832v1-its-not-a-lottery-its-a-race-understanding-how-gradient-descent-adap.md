---
layout: default
title: It's not a Lottery, it's a Race: Understanding How Gradient Descent Adapts the Network's Capacity to the Task
---

# It's not a Lottery, it's a Race: Understanding How Gradient Descent Adapts the Network's Capacity to the Task
**arXiv**：[2602.04832v1](https://arxiv.org/abs/2602.04832) · [PDF](https://arxiv.org/pdf/2602.04832.pdf)  
**作者**：Hannah Pinson  

**一句话要点**：提出梯度下降动态机制以解释神经网络有效容量适应任务的过程

**关键词**：梯度下降, 神经网络容量, 学习动态, 彩票票假设, 神经元分析

## 3 点简述
- 核心问题：梯度下降如何将神经网络理论容量降低为适应任务的有效容量
- 方法要点：分析单隐藏层ReLU网络中神经元学习动态，识别互对齐、解锁和竞争机制
- 实验或效果：解释彩票票假设，说明神经元初始条件如何影响权重范数

## 摘要（原文）

> Our theoretical understanding of neural networks is lagging behind their empirical success. One of the important unexplained phenomena is why and how, during the process of training with gradient descent, the theoretical capacity of neural networks is reduced to an effective capacity that fits the task. We here investigate the mechanism by which gradient descent achieves this through analyzing the learning dynamics at the level of individual neurons in single hidden layer ReLU networks. We identify three dynamical principles -- mutual alignment, unlocking and racing -- that together explain why we can often successfully reduce capacity after training through the merging of equivalent neurons or the pruning of low norm weights. We specifically explain the mechanism behind the lottery ticket conjecture, or why the specific, beneficial initial conditions of some neurons lead them to obtain higher weight norms.

