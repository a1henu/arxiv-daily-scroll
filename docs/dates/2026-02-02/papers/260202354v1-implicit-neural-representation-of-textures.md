---
layout: default
title: Implicit neural representation of textures
---

# Implicit neural representation of textures
**arXiv**：[2602.02354v1](https://arxiv.org/abs/2602.02354) · [PDF](https://arxiv.org/pdf/2602.02354.pdf)  
**作者**：Albert Kwok, Zheyuan Hu, Dounia Hammou  

**一句话要点**：提出隐式神经表示纹理模型，在连续UV坐标空间实现高效纹理表示与渲染。

**关键词**：隐式神经表示, 纹理建模, 连续坐标空间, 实时渲染, 内存效率

## 3 点简述
- 核心问题：传统纹理表示基于离散采样，在连续空间应用中存在限制。
- 方法要点：设计神经网络作为隐式纹理表示，直接映射UV坐标到纹理值。
- 实验或效果：评估图像质量、内存使用和渲染时间，分析平衡并探索实时渲染应用。

## 摘要（原文）

> Implicit neural representation (INR) has proven to be accurate and efficient in various domains. In this work, we explore how different neural networks can be designed as a new texture INR, which operates in a continuous manner rather than a discrete one over the input UV coordinate space. Through thorough experiments, we demonstrate that these INRs perform well in terms of image quality, with considerable memory usage and rendering inference time. We analyze the balance between these objectives. In addition, we investigate various related applications in real-time rendering and down-stream tasks, e.g. mipmap fitting and INR-space generation.

