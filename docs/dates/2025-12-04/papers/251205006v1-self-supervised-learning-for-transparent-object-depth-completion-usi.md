---
layout: default
title: Self-Supervised Learning for Transparent Object Depth Completion Using Depth from Non-Transparent Objects
---

# Self-Supervised Learning for Transparent Object Depth Completion Using Depth from Non-Transparent Objects
**arXiv**：[2512.05006v1](https://arxiv.org/abs/2512.05006) · [PDF](https://arxiv.org/pdf/2512.05006.pdf)  
**作者**：Xianghui Fan, Zhaoyu Chen, Mengyang Pan, Anping Deng, Hang Yang  

**一句话要点**：提出自监督深度补全方法，利用非透明区域模拟透明物体深度缺失以降低标注成本

**关键词**：透明物体感知, 深度补全, 自监督学习, 深度传感器, 计算机视觉, 模拟训练

## 3 点简述
- 核心问题：透明物体因光折射反射导致深度传感器难以准确感知，传统方法依赖昂贵标注数据
- 方法要点：在非透明区域模拟透明物体的深度缺失，使用原始深度图作为监督信号进行自监督训练
- 实验或效果：方法性能接近监督方法，小样本下预训练可提升模型表现

## 摘要（原文）

> The perception of transparent objects is one of the well-known challenges in computer vision. Conventional depth sensors have difficulty in sensing the depth of transparent objects due to refraction and reflection of light. Previous research has typically train a neural network to complete the depth acquired by the sensor, and this method can quickly and accurately acquire accurate depth maps of transparent objects. However, previous training relies on a large amount of annotation data for supervision, and the labeling of depth maps is costly. To tackle this challenge, we propose a new self-supervised method for training depth completion networks. Our method simulates the depth deficits of transparent objects within non-transparent regions and utilizes the original depth map as ground truth for supervision. Experiments demonstrate that our method achieves performance comparable to supervised approach, and pre-training with our method can improve the model performance when the training samples are small.

