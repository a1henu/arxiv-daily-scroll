---
layout: default
title: Real-time Motion Segmentation with Event-based Normal Flow
---

# Real-time Motion Segmentation with Event-based Normal Flow
**arXiv**：[2602.20790v1](https://arxiv.org/abs/2602.20790) · [PDF](https://arxiv.org/pdf/2602.20790.pdf)  
**作者**：Sheng Zhong, Zhongyang Ren, Xiya Zhu, Dehao Yuan, Cornelia Fermuller, Yi Zhou  

**一句话要点**：提出基于法向流的实时运动分割框架，以解决事件相机在动态场景理解中的效率问题。

**关键词**：事件相机, 法向流, 运动分割, 实时处理, 图割优化, 动态场景理解

## 3 点简述
- 核心问题：事件相机原始数据稀疏，直接处理效率低，限制实时运动分割应用。
- 方法要点：利用事件邻域学习密集法向流，通过图割能量最小化和迭代聚类拟合实现分割。
- 实验或效果：在多个公开数据集上验证，相比现有方法实现近800倍加速，确保实时性能。

## 摘要（原文）

> Event-based cameras are bio-inspired sensors with pixels that independently and asynchronously respond to brightness changes at microsecond resolution, offering the potential to handle visual tasks in challenging scenarios. However, due to the sparse information content in individual events, directly processing the raw event data to solve vision tasks is highly inefficient, which severely limits the applicability of state-of-the-art methods in real-time tasks, such as motion segmentation, a fundamental task for dynamic scene understanding. Incorporating normal flow as an intermediate representation to compress motion information from event clusters within a localized region provides a more effective solution. In this work, we propose a normal flow-based motion segmentation framework for event-based vision. Leveraging the dense normal flow directly learned from event neighborhoods as input, we formulate the motion segmentation task as an energy minimization problem solved via graph cuts, and optimize it iteratively with normal flow clustering and motion model fitting. By using a normal flow-based motion model initialization and fitting method, the proposed system is able to efficiently estimate the motion models of independently moving objects with only a limited number of candidate models, which significantly reduces the computational complexity and ensures real-time performance, achieving nearly a 800x speedup in comparison to the open-source state-of-the-art method. Extensive evaluations on multiple public datasets fully demonstrate the accuracy and efficiency of our framework.

