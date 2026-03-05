---
layout: default
title: Motion Manipulation via Unsupervised Keypoint Positioning in Face Animation
---

# Motion Manipulation via Unsupervised Keypoint Positioning in Face Animation
**arXiv**：[2603.04302v1](https://arxiv.org/abs/2603.04302) · [PDF](https://arxiv.org/pdf/2603.04302.pdf)  
**作者**：Hong Li, Boyu Liu, Xuhui Liu, Baochang Zhang  

**一句话要点**：提出MMFA方法，通过无监督关键点定位实现人脸动画中的运动操控

**关键词**：人脸动画, 无监督关键点定位, 运动操控, 表情解耦, 变分自编码器, 自监督学习

## 3 点简述
- 核心问题：现有无监督关键点分解方法无法完全解耦身份语义与交织的运动信息，导致可控人脸生成困难。
- 方法要点：引入自监督表示学习编码解码表情，设计新关键点计算方式以实现任意运动控制，并构建变分自编码器映射表情特征到连续分布。
- 实验或效果：在公开数据集上验证MMFA有效性，显示其在生成真实动画和操控人脸运动方面优于先前方法。

## 摘要（原文）

> Face animation deals with controlling and generating facial features with a wide range of applications. The methods based on unsupervised keypoint positioning can produce realistic and detailed virtual portraits. However, they cannot achieve controllable face generation since the existing keypoint decomposition pipelines fail to fully decouple identity semantics and intertwined motion information (e.g., rotation, translation, and expression). To address these issues, we present a new method, Motion Manipulation via unsupervised keypoint positioning in Face Animation (MMFA). We first introduce self-supervised representation learning to encode and decode expressions in the latent feature space and decouple them from other motion information. Secondly, we propose a new way to compute keypoints aiming to achieve arbitrary motion control. Moreover, we design a variational autoencoder to map expression features to a continuous Gaussian distribution, allowing us for the first time to interpolate facial expressions in an unsupervised framework. We have conducted extensive experiments on publicly available datasets to validate the effectiveness of MMFA, which show that MMFA offers pronounced advantages over prior arts in creating realistic animation and manipulating face motion.

