---
layout: default
title: Learning Geometric Invariance for Gait Recognition
---

# Learning Geometric Invariance for Gait Recognition
**arXiv**：[2601.05604v1](https://arxiv.org/abs/2601.05604) · [PDF](https://arxiv.org/pdf/2601.05604.pdf)  
**作者**：Zengbin Wang, Junjie Li, Saihui Hou, Xu Liu, Chunshui Cao, Yongzhen Huang, Muyi Sun, Siye Wang, Man Zhang  

**一句话要点**：提出RRS-Gait框架，通过几何不变性学习解决步态识别中的跨视角和跨服装问题。

**关键词**：步态识别, 几何不变性, 特征等变性, 跨视角识别, 跨服装识别, 卷积神经网络

## 3 点简述
- 核心问题：步态识别需提取身份不变特征，但现有方法较少显式探索不同步态条件间的内在关系。
- 方法要点：将步态变化建模为几何变换组合，设计反射-旋转-缩放不变性学习框架，通过调整卷积核实现特征等变性。
- 实验或效果：在Gait3D等四个数据集上验证，在各种步态条件下表现优异。

## 摘要（原文）

> The goal of gait recognition is to extract identity-invariant features of an individual under various gait conditions, e.g., cross-view and cross-clothing. Most gait models strive to implicitly learn the common traits across different gait conditions in a data-driven manner to pull different gait conditions closer for recognition. However, relatively few studies have explicitly explored the inherent relations between different gait conditions. For this purpose, we attempt to establish connections among different gait conditions and propose a new perspective to achieve gait recognition: variations in different gait conditions can be approximately viewed as a combination of geometric transformations. In this case, all we need is to determine the types of geometric transformations and achieve geometric invariance, then identity invariance naturally follows. As an initial attempt, we explore three common geometric transformations (i.e., Reflect, Rotate, and Scale) and design a $\mathcal{R}$eflect-$\mathcal{R}$otate-$\mathcal{S}$cale invariance learning framework, named ${\mathcal{RRS}}$-Gait. Specifically, it first flexibly adjusts the convolution kernel based on the specific geometric transformations to achieve approximate feature equivariance. Then these three equivariant-aware features are respectively fed into a global pooling operation for final invariance-aware learning. Extensive experiments on four popular gait datasets (Gait3D, GREW, CCPG, SUSTech1K) show superior performance across various gait conditions.

