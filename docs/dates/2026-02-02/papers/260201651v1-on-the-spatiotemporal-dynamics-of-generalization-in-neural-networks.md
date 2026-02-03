---
layout: default
title: On the Spatiotemporal Dynamics of Generalization in Neural Networks
---

# On the Spatiotemporal Dynamics of Generalization in Neural Networks
**arXiv**：[2602.01651v1](https://arxiv.org/abs/2602.01651) · [PDF](https://arxiv.org/pdf/2602.01651.pdf)  
**作者**：Zichao Wei  

**一句话要点**：提出SEAD架构以解决神经网络长度泛化问题，基于物理约束推导计算模型。

**关键词**：长度泛化, 神经元胞自动机, 物理约束, 计算稳定性, 迭代推理

## 3 点简述
- 核心问题：神经网络在加法等任务中无法从短序列泛化到长序列，违反物理规律。
- 方法要点：从局部性、对称性和稳定性约束推导SEAD架构，采用神经元胞自动机实现迭代计算。
- 实验效果：在奇偶性、加法和Rule 110任务中实现完美长度泛化，准确率达100%。

## 摘要（原文）

> Why do neural networks fail to generalize addition from 16-digit to 32-digit numbers, while a child who learns the rule can apply it to arbitrarily long sequences? We argue that this failure is not an engineering problem but a violation of physical postulates. Drawing inspiration from physics, we identify three constraints that any generalizing system must satisfy: (1) Locality -- information propagates at finite speed; (2) Symmetry -- the laws of computation are invariant across space and time; (3) Stability -- the system converges to discrete attractors that resist noise accumulation. From these postulates, we derive -- rather than design -- the Spatiotemporal Evolution with Attractor Dynamics (SEAD) architecture: a neural cellular automaton where local convolutional rules are iterated until convergence. Experiments on three tasks validate our theory: (1) Parity -- demonstrating perfect length generalization via light-cone propagation; (2) Addition -- achieving scale-invariant inference from L=16 to L=1 million with 100% accuracy, exhibiting input-adaptive computation; (3) Rule 110 -- learning a Turing-complete cellular automaton without trajectory divergence. Our results suggest that the gap between statistical learning and logical reasoning can be bridged -- not by scaling parameters, but by respecting the physics of computation.

