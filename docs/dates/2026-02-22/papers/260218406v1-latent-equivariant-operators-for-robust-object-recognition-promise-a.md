---
layout: default
title: Latent Equivariant Operators for Robust Object Recognition: Promise and Challenges
---

# Latent Equivariant Operators for Robust Object Recognition: Promise and Challenges
**arXiv**：[2602.18406v1](https://arxiv.org/abs/2602.18406) · [PDF](https://arxiv.org/pdf/2602.18406.pdf)  
**作者**：Minh Dinh, Stéphane Deny  

**一句话要点**：提出潜在等变算子架构，以解决对称变换下物体识别的分布外泛化问题。

**关键词**：等变神经网络, 潜在空间学习, 分布外泛化, 对称变换, 物体识别

## 3 点简述
- 核心问题：深度学习在训练中罕见对称变换（如姿态、尺度）时物体识别困难。
- 方法要点：从对称变换示例学习潜在空间等变算子，无需先验知识。
- 实验或效果：在旋转平移噪声MNIST数据集上实现分布外分类，克服传统和等变网络局限。

## 摘要（原文）

> Despite the successes of deep learning in computer vision, difficulties persist in recognizing objects that have undergone group-symmetric transformations rarely seen during training-for example objects seen in unusual poses, scales, positions, or combinations thereof. Equivariant neural networks are a solution to the problem of generalizing across symmetric transformations, but require knowledge of transformations a priori. An alternative family of architectures proposes to earn equivariant operators in a latent space from examples of symmetric transformations. Here, using simple datasets of rotated and translated noisy MNIST, we illustrate how such architectures can successfully be harnessed for out-of-distribution classification, thus overcoming the limitations of both traditional and equivariant networks. While conceptually enticing, we discuss challenges ahead on the path of scaling these architectures to more complex datasets.

