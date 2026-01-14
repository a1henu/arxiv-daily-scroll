---
layout: default
title: One-Shot Identification with Different Neural Network Approaches
---

# One-Shot Identification with Different Neural Network Approaches
**arXiv**：[2601.08278v1](https://arxiv.org/abs/2601.08278) · [PDF](https://arxiv.org/pdf/2601.08278.pdf)  
**作者**：Janis Mohr, Jörg Frochte  

**一句话要点**：提出使用胶囊网络和堆叠图像技术，以提升工业应用和人脸识别中的单次识别性能。

**关键词**：单次学习, 胶囊网络, 堆叠图像, 人脸识别, 工业应用, 孪生网络

## 3 点简述
- 核心问题：单次学习场景下数据稀缺，传统卷积神经网络难以有效学习特征。
- 方法要点：采用堆叠图像技术和孪生胶囊网络架构，增强模型在有限数据下的泛化能力。
- 实验或效果：胶囊网络方法在多个数据集上表现优异，超越其他技术，且易于使用和优化。

## 摘要（原文）

> Convolutional neural networks (CNNs) have been widely used in the computer vision community, significantly improving the state-of-the-art. But learning good features often is computationally expensive in machine learning settings and is especially difficult when there is a lack of data. One-shot learning is one such area where only limited data is available. In one-shot learning, predictions have to be made after seeing only one example from one class, which requires special techniques. In this paper we explore different approaches to one-shot identification tasks in different domains including an industrial application and face recognition. We use a special technique with stacked images and use siamese capsule networks. It is encouraging to see that the approach using capsule architecture achieves strong results and exceeds other techniques on a wide range of datasets from industrial application to face recognition benchmarks while being easy to use and optimise.

