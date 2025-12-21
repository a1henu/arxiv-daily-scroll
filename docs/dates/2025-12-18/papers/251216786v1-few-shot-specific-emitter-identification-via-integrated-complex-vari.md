---
layout: default
title: Few-Shot Specific Emitter Identification via Integrated Complex Variational Mode Decomposition and Spatial Attention Transfer
---

# Few-Shot Specific Emitter Identification via Integrated Complex Variational Mode Decomposition and Spatial Attention Transfer
**arXiv**：[2512.16786v1](https://arxiv.org/abs/2512.16786) · [PDF](https://arxiv.org/pdf/2512.16786.pdf)  
**作者**：Chenyu Zhu, Zeyang Li, Ziyi Xie, Jie Zhang  

**一句话要点**：提出集成复数变分模态分解与空间注意力迁移方法，以解决少样本特定发射器识别问题。

**关键词**：特定发射器识别, 少样本学习, 复数变分模态分解, 时序卷积网络, 空间注意力机制, 物理层安全

## 3 点简述
- 核心问题：基于深度学习的特定发射器识别在现实场景中面临标记数据有限和依赖先验信息的挑战。
- 方法要点：集成复数变分模态分解算法重构信号，结合时序卷积网络建模序列特征，并引入空间注意力机制加权信息段。
- 实验或效果：在公开数据集上，仅用10个符号无需先验知识，达到96%的识别准确率。

## 摘要（原文）

> Specific emitter identification (SEI) utilizes passive hardware characteristics to authenticate transmitters, providing a robust physical-layer security solution. However, most deep-learning-based methods rely on extensive data or require prior information, which poses challenges in real-world scenarios with limited labeled data. We propose an integrated complex variational mode decomposition algorithm that decomposes and reconstructs complex-valued signals to approximate the original transmitted signals, thereby enabling more accurate feature extraction. We further utilize a temporal convolutional network to effectively model the sequential signal characteristics, and introduce a spatial attention mechanism to adaptively weight informative signal segments, significantly enhancing identification performance. Additionally, the branch network allows leveraging pre-trained weights from other data while reducing the need for auxiliary datasets. Ablation experiments on the simulated data demonstrate the effectiveness of each component of the model. An accuracy comparison on a public dataset reveals that our method achieves 96% accuracy using only 10 symbols without requiring any prior knowledge.

