---
layout: default
title: Communication-Efficient Learning for Satellite Constellations
---

# Communication-Efficient Learning for Satellite Constellations
**arXiv**：[2511.20220v1](https://arxiv.org/abs/2511.20220) · [PDF](https://arxiv.org/pdf/2511.20220.pdf)  
**作者**：Ruxandra-Stefania Tudose, Moritz H. W. Grüss, Grace Ra Kim, Karl H. Johansson, Nicola Bastianello  

**一句话要点**：提出通信高效联邦学习算法以优化卫星星座模型训练

**关键词**：卫星星座, 联邦学习, 通信效率, 误差反馈, 模型压缩, 收敛分析

## 3 点简述
- 核心问题：卫星星座联邦学习中通信开销大，影响模型训练效率。
- 方法要点：采用本地训练、压缩和误差反馈机制减少通信量与提升精度。
- 实验或效果：在真实空间场景模拟中，算法收敛性优于现有方法。

## 摘要（原文）

> Satellite constellations in low-Earth orbit are now widespread, enabling positioning, Earth imaging, and communications. In this paper we address the solution of learning problems using these satellite constellations. In particular, we focus on a federated approach, where satellites collect and locally process data, with the ground station aggregating local models. We focus on designing a novel, communication-efficient algorithm that still yields accurate trained models. To this end, we employ several mechanisms to reduce the number of communications with the ground station (local training) and their size (compression). We then propose an error feedback mechanism that enhances accuracy, which yields, as a byproduct, an algorithm-agnostic error feedback scheme that can be more broadly applied. We analyze the convergence of the resulting algorithm, and compare it with the state of the art through simulations in a realistic space scenario, showcasing superior performance.

