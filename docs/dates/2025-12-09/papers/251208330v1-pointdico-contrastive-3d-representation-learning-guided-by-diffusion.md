---
layout: default
title: PointDico: Contrastive 3D Representation Learning Guided by Diffusion Models
---

# PointDico: Contrastive 3D Representation Learning Guided by Diffusion Models
**arXiv**：[2512.08330v1](https://arxiv.org/abs/2512.08330) · [PDF](https://arxiv.org/pdf/2512.08330.pdf)  
**作者**：Pengbo Li, Yiding Sun, Haozhe Cheng  

**一句话要点**：提出PointDico模型，通过扩散模型引导对比学习以解决3D点云表示学习中的过拟合和无序性问题。

**关键词**：3D表示学习, 点云处理, 扩散模型, 对比学习, 知识蒸馏, 多尺度特征提取

## 3 点简述
- 核心问题：现有对比方法易过拟合，生成方法难处理无序点云，阻碍3D表示学习。
- 方法要点：结合扩散模型和对比学习，通过知识蒸馏实现多尺度特征提取与局部全局信息融合。
- 实验或效果：在ScanObjectNN和ShapeNetPart上达到新SOTA，准确率分别为94.32%和86.5% mIoU。

## 摘要（原文）

> Self-supervised representation learning has shown significant improvement in Natural Language Processing and 2D Computer Vision. However, existing methods face difficulties in representing 3D data because of its unordered and uneven density. Through an in-depth analysis of mainstream contrastive and generative approaches, we find that contrastive models tend to suffer from overfitting, while 3D Mask Autoencoders struggle to handle unordered point clouds. This motivates us to learn 3D representations by sharing the merits of diffusion and contrast models, which is non-trivial due to the pattern difference between the two paradigms. In this paper, we propose \textit{PointDico}, a novel model that seamlessly integrates these methods. \textit{PointDico} learns from both denoising generative modeling and cross-modal contrastive learning through knowledge distillation, where the diffusion model serves as a guide for the contrastive model. We introduce a hierarchical pyramid conditional generator for multi-scale geometric feature extraction and employ a dual-channel design to effectively integrate local and global contextual information. \textit{PointDico} achieves a new state-of-the-art in 3D representation learning, \textit{e.g.}, \textbf{94.32\%} accuracy on ScanObjectNN, \textbf{86.5\%} Inst. mIoU on ShapeNetPart.

