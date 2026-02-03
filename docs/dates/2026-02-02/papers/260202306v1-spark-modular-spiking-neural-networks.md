---
layout: default
title: Spark: Modular Spiking Neural Networks
---

# Spark: Modular Spiking Neural Networks
**arXiv**：[2602.02306v1](https://arxiv.org/abs/2602.02306) · [PDF](https://arxiv.org/pdf/2602.02306.pdf)  
**作者**：Mario Franco, Carlos Gershenson  

**一句话要点**：提出Spark框架以构建模块化脉冲神经网络，提升数据与能源效率

**关键词**：脉冲神经网络, 模块化设计, 数据效率, 能源效率, 连续学习, 可塑性机制

## 3 点简述
- 核心问题：传统神经网络在数据和能源效率上不足，脉冲神经网络学习算法不成熟
- 方法要点：基于模块化设计，从简单组件到完整模型，支持连续无批次学习
- 实验或效果：通过简单可塑性机制解决稀疏奖励CartPole问题，展示框架实用性

## 摘要（原文）

> Nowadays, neural networks act as a synonym for artificial intelligence. Present neural network models, although remarkably powerful, are inefficient both in terms of data and energy. Several alternative forms of neural networks have been proposed to address some of these problems. Specifically, spiking neural networks are suitable for efficient hardware implementations. However, effective learning algorithms for spiking networks remain elusive, although it is suspected that effective plasticity mechanisms could alleviate the problem of data efficiency. Here, we present a new framework for spiking neural networks - Spark - built upon the idea of modular design, from simple components to entire models. The aim of this framework is to provide an efficient and streamlined pipeline for spiking neural networks. We showcase this framework by solving the sparse-reward cartpole problem with simple plasticity mechanisms. We hope that a framework compatible with traditional ML pipelines may accelerate research in the area, specifically for continuous and unbatched learning, akin to the one animals exhibit.

