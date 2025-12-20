---
layout: default
title: Few-Shot Specific Emitter Identification via Integrated Complex Variational Mode Decomposition and Spatial Attention Transfer
---

# Few-Shot Specific Emitter Identification via Integrated Complex Variational Mode Decomposition and Spatial Attention Transfer
**arXiv**：[2512.16786v1](https://arxiv.org/abs/2512.16786) · [PDF](https://arxiv.org/pdf/2512.16786.pdf)  
**作者**：Chenyu Zhu, Zeyang Li, Ziyi Xie, Jie Zhang  

**一句话要点**：提出集成复变分模态分解与空间注意力迁移方法，以解决少样本特定发射器识别问题。

**关键词**：特定发射器识别, 少样本学习, 复变分模态分解, 空间注意力机制, 时序卷积网络

## 3 点简述
- 核心问题：基于深度学习的特定发射器识别依赖大量数据或先验信息，在少样本场景中面临挑战。
- 方法要点：集成复变分模态分解算法重构复值信号，结合时序卷积网络和空间注意力机制增强特征提取与识别性能。
- 实验或效果：在公开数据集上，仅用10个符号无需先验知识，达到96%的准确率，验证了模型组件的有效性。

## 摘要（原文）

> Specific emitter identification (SEI) utilizes passive hardware characteristics to authenticate transmitters, providing a robust physical-layer security solution. However, most deep-learning-based methods rely on extensive data or require prior information, which poses challenges in real-world scenarios with limited labeled data. We propose an integrated complex variational mode decomposition algorithm that decomposes and reconstructs complex-valued signals to approximate the original transmitted signals, thereby enabling more accurate feature extraction. We further utilize a temporal convolutional network to effectively model the sequential signal characteristics, and introduce a spatial attention mechanism to adaptively weight informative signal segments, significantly enhancing identification performance. Additionally, the branch network allows leveraging pre-trained weights from other data while reducing the need for auxiliary datasets. Ablation experiments on the simulated data demonstrate the effectiveness of each component of the model. An accuracy comparison on a public dataset reveals that our method achieves 96% accuracy using only 10 symbols without requiring any prior knowledge.

