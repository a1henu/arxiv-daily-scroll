---
layout: default
title: Mem-MLP: Real-Time 3D Human Motion Generation from Sparse Inputs
---

# Mem-MLP: Real-Time 3D Human Motion Generation from Sparse Inputs
**arXiv**：[2511.16264v1](https://arxiv.org/abs/2511.16264) · [PDF](https://arxiv.org/pdf/2511.16264.pdf)  
**作者**：Sinan Mutlu, Georgios F. Angelis, Savas Ozkan, Paul Wisbey, Anastasios Drosou, Mete Ozay  

**一句话要点**：提出Mem-MLP方法，从稀疏输入实时生成3D人体运动，提升AR/VR沉浸感。

**关键词**：3D人体运动生成, 稀疏输入处理, 实时推理, 多任务学习, AR/VR应用

## 3 点简述
- 核心问题：AR/VR中仅跟踪头手导致3D全身运动重建不完整。
- 方法要点：使用MLP骨干，结合残差连接和Memory-Block处理缺失数据。
- 实验效果：预测误差显著降低，在移动HMD上达到72 FPS。

## 摘要（原文）

> Realistic and smooth full-body tracking is crucial for immersive AR/VR applications. Existing systems primarily track head and hands via Head Mounted Devices (HMDs) and controllers, making the 3D full-body reconstruction in-complete. One potential approach is to generate the full-body motions from sparse inputs collected from limited sensors using a Neural Network (NN) model. In this paper, we propose a novel method based on a multi-layer perceptron (MLP) backbone that is enhanced with residual connections and a novel NN-component called Memory-Block. In particular, Memory-Block represents missing sensor data with trainable code-vectors, which are combined with the sparse signals from previous time instances to improve the temporal consistency. Furthermore, we formulate our solution as a multi-task learning problem, allowing our MLP-backbone to learn robust representations that boost accuracy. Our experiments show that our method outperforms state-of-the-art baselines by substantially reducing prediction errors. Moreover, it achieves 72 FPS on mobile HMDs that ultimately improves the accuracy-running time tradeoff.

