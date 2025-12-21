---
layout: default
title: TreeNet: A Light Weight Model for Low Bitrate Image Compression
---

# TreeNet: A Light Weight Model for Low Bitrate Image Compression
**arXiv**：[2512.16743v1](https://arxiv.org/abs/2512.16743) · [PDF](https://arxiv.org/pdf/2512.16743.pdf)  
**作者**：Mahadev Prasad Panda, Purnachandra Rao Makkena, Srivatsa Prativadibhayankaram, Siegfried Fößel, André Kaup  

**一句话要点**：提出TreeNet以解决学习型图像压缩的计算复杂度高问题，适用于低比特率场景。

**关键词**：图像压缩, 低复杂度模型, 二叉树结构, 注意力机制, 低比特率, BD-rate评估

## 3 点简述
- 核心问题：学习型图像压缩的计算复杂度高，阻碍广泛应用。
- 方法要点：采用二叉树结构编码器-解码器架构和注意力特征融合机制。
- 实验或效果：在低比特率下，BD-rate比JPEG AI平均提升4.83%，模型复杂度降低87.82%。

## 摘要（原文）

> Reducing computational complexity remains a critical challenge for the widespread adoption of learning-based image compression techniques. In this work, we propose TreeNet, a novel low-complexity image compression model that leverages a binary tree-structured encoder-decoder architecture to achieve efficient representation and reconstruction. We employ attentional feature fusion mechanism to effectively integrate features from multiple branches. We evaluate TreeNet on three widely used benchmark datasets and compare its performance against competing methods including JPEG AI, a recent standard in learning-based image compression. At low bitrates, TreeNet achieves an average improvement of 4.83% in BD-rate over JPEG AI, while reducing model complexity by 87.82%. Furthermore, we conduct extensive ablation studies to investigate the influence of various latent representations within TreeNet, offering deeper insights into the factors contributing to reconstruction.

