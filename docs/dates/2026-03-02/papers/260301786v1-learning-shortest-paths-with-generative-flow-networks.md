---
layout: default
title: Learning Shortest Paths with Generative Flow Networks
---

# Learning Shortest Paths with Generative Flow Networks
**arXiv**：[2603.01786v1](https://arxiv.org/abs/2603.01786) · [PDF](https://arxiv.org/pdf/2603.01786.pdf)  
**作者**：Nikita Morozov, Ian Maksimov, Daniil Tiapkin, Sergey Samsonov  

**一句话要点**：提出基于生成流网络的学习框架以解决图中最短路径问题

**关键词**：最短路径学习, 生成流网络, 图路径查找, 流正则化, 魔方求解

## 3 点简述
- 核心问题：在非循环图中学习最短路径，传统方法可能面临效率或泛化挑战
- 方法要点：利用生成流网络，通过最小化总流确保策略沿最短路径遍历，结合流正则化训练
- 实验或效果：在置换环境和魔方求解中验证，魔方求解在解长度上竞争先进方法，测试时搜索预算更小

## 摘要（原文）

> In this paper, we present a novel learning framework for finding shortest paths in graphs utilizing Generative Flow Networks (GFlowNets). First, we examine theoretical properties of GFlowNets in non-acyclic environments in relation to shortest paths. We prove that, if the total flow is minimized, forward and backward policies traverse the environment graph exclusively along shortest paths between the initial and terminal states. Building on this result, we show that the pathfinding problem in an arbitrary graph can be solved by training a non-acyclic GFlowNet with flow regularization. We experimentally demonstrate the performance of our method in pathfinding in permutation environments and in solving Rubik's Cubes. For the latter problem, our approach shows competitive results with state-of-the-art machine learning approaches designed specifically for this task in terms of the solution length, while requiring smaller search budget at test-time.

