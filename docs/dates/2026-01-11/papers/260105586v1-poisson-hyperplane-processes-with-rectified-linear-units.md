---
layout: default
title: Poisson Hyperplane Processes with Rectified Linear Units
---

# Poisson Hyperplane Processes with Rectified Linear Units
**arXiv**：[2601.05586v1](https://arxiv.org/abs/2601.05586) · [PDF](https://arxiv.org/pdf/2601.05586.pdf)  
**作者**：Shufei Ge, Shijia Wang, Lloyd Elliott  

**一句话要点**：提出基于泊松超平面过程的两层ReLU神经网络概率表示，以提升大规模问题的可扩展性和性能。

**关键词**：泊松超平面过程, ReLU神经网络, 概率表示, 贝叶斯推断, 可扩展性, 退火顺序蒙特卡洛

## 3 点简述
- 核心问题：连接泊松超平面过程与两层ReLU神经网络，提供替代概率表示。
- 方法要点：利用高斯先验和分解命题，实现模型在大规模问题中的可扩展性。
- 实验或效果：通过退火顺序蒙特卡洛算法进行贝叶斯推断，实验显示性能优于经典两层ReLU网络。

## 摘要（原文）

> Neural networks have shown state-of-the-art performances in various classification and regression tasks. Rectified linear units (ReLU) are often used as activation functions for the hidden layers in a neural network model. In this article, we establish the connection between the Poisson hyperplane processes (PHP) and two-layer ReLU neural networks. We show that the PHP with a Gaussian prior is an alternative probabilistic representation to a two-layer ReLU neural network. In addition, we show that a two-layer neural network constructed by PHP is scalable to large-scale problems via the decomposition propositions. Finally, we propose an annealed sequential Monte Carlo algorithm for Bayesian inference. Our numerical experiments demonstrate that our proposed method outperforms the classic two-layer ReLU neural network. The implementation of our proposed model is available at https://github.com/ShufeiGe/Pois_Relu.git.

