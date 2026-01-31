---
layout: default
title: Investigating Batch Inference in a Sequential Monte Carlo Framework for Neural Networks
---

# Investigating Batch Inference in a Sequential Monte Carlo Framework for Neural Networks
**arXiv**：[2601.21983v1](https://arxiv.org/abs/2601.21983) · [PDF](https://arxiv.org/pdf/2601.21983.pdf)  
**作者**：Andrew Millard, Joshua Murphy, Peter Green, Simon Maskell  

**一句话要点**：提出数据退火方法以加速神经网络中的序列蒙特卡洛采样训练

**关键词**：贝叶斯推断, 序列蒙特卡洛, 神经网络训练, 数据退火, 计算效率, 图像分类

## 3 点简述
- 核心问题：序列蒙特卡洛采样在神经网络贝叶斯推断中计算成本高，因需全批量数据评估似然和梯度。
- 方法要点：探索数据退火策略，逐步引入小批量数据到SMC采样器的似然和梯度评估中。
- 实验或效果：在基准图像分类任务上实现高达6倍训练加速，且精度损失最小。

## 摘要（原文）

> Bayesian inference allows us to define a posterior distribution over the weights of a generic neural network (NN). Exact posteriors are usually intractable, in which case approximations can be employed. One such approximation - variational inference - is computationally efficient when using mini-batch stochastic gradient descent as subsets of the data are used for likelihood and gradient evaluations, though the approach relies on the selection of a variational distribution which sufficiently matches the form of the posterior. Particle-based methods such as Markov chain Monte Carlo and Sequential Monte Carlo (SMC) do not assume a parametric family for the posterior by typically require higher computational cost. These sampling methods typically use the full-batch of data for likelihood and gradient evaluations, which contributes to this computational expense. We explore several methods of gradually introducing more mini-batches of data (data annealing) into likelihood and gradient evaluations of an SMC sampler. We find that we can achieve up to $6\times$ faster training with minimal loss in accuracy on benchmark image classification problems using NNs.

