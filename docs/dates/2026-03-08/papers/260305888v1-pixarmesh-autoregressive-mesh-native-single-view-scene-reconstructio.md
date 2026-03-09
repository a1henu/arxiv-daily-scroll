---
layout: default
title: PixARMesh: Autoregressive Mesh-Native Single-View Scene Reconstruction
---

# PixARMesh: Autoregressive Mesh-Native Single-View Scene Reconstruction
**arXiv**：[2603.05888v1](https://arxiv.org/abs/2603.05888) · [PDF](https://arxiv.org/pdf/2603.05888.pdf)  
**作者**：Xiang Zhang, Sohyun Yoo, Hongrui Wu, Chuan Li, Jianwen Xie, Zhuowen Tu  

**一句话要点**：提出PixARMesh以从单张RGB图像自回归重建完整3D室内场景网格

**关键词**：单视图场景重建, 自回归网格生成, 3D室内场景, 像素对齐特征, 交叉注意力, 轻量级网格

## 3 点简述
- 核心问题：从单视图RGB图像重建完整3D室内场景网格，避免依赖隐式场和后处理优化
- 方法要点：结合点云编码器与像素对齐特征，通过交叉注意力联合预测布局和几何，自回归生成统一令牌流
- 实验或效果：在合成和真实数据集上实现最先进重建质量，生成轻量级高质量网格，适用于下游应用

## 摘要（原文）

> We introduce PixARMesh, a method to autoregressively reconstruct complete 3D indoor scene meshes directly from a single RGB image. Unlike prior methods that rely on implicit signed distance fields and post-hoc layout optimization, PixARMesh jointly predicts object layout and geometry within a unified model, producing coherent and artist-ready meshes in a single forward pass. Building on recent advances in mesh generative models, we augment a point-cloud encoder with pixel-aligned image features and global scene context via cross-attention, enabling accurate spatial reasoning from a single image. Scenes are generated autoregressively from a unified token stream containing context, pose, and mesh, yielding compact meshes with high-fidelity geometry. Experiments on synthetic and real-world datasets show that PixARMesh achieves state-of-the-art reconstruction quality while producing lightweight, high-quality meshes ready for downstream applications.

