---
layout: default
title: Relative Geometry of Neural Forecasters: Linking Accuracy and Alignment in Learned Latent Geometry
---

# Relative Geometry of Neural Forecasters: Linking Accuracy and Alignment in Learned Latent Geometry
**arXiv**：[2602.15676v1](https://arxiv.org/abs/2602.15676) · [PDF](https://arxiv.org/pdf/2602.15676.pdf)  
**作者**：Deniz Kucukahmetler, Maximilian Jean Hemmann, Julian Mosig von Aehrenfeld, Maximilian Amthor, Christian Deubel, Nico Scherf, Diaaeldin Taha  

**一句话要点**：提出基于锚点的相对嵌入方法，以比较神经网络在七类动力系统中的表示对齐与预测精度关系。

**关键词**：神经网络预测, 表示对齐, 相对几何, 动力系统, 潜在空间, 模型比较

## 3 点简述
- 研究神经网络如何内部表示复杂动力系统的潜在几何结构，揭示表示对齐问题。
- 引入几何无关的相对嵌入，消除潜在空间中的旋转和缩放模糊性，实现模型间可比性。
- 在七类动力系统上实验，发现对齐与预测精度相关，但高精度可伴随低对齐，提供可复现的几何基础。

## 摘要（原文）

> Neural networks can accurately forecast complex dynamical systems, yet how they internally represent underlying latent geometry remains poorly understood. We study neural forecasters through the lens of representational alignment, introducing anchor-based, geometry-agnostic relative embeddings that remove rotational and scaling ambiguities in latent spaces. Applying this framework across seven canonical dynamical systems - ranging from periodic to chaotic - we reveal reproducible family-level structure: multilayer perceptrons align with other MLPs, recurrent networks with RNNs, while transformers and echo-state networks achieve strong forecasts despite weaker alignment. Alignment generally correlates with forecasting accuracy, yet high accuracy can coexist with low alignment. Relative geometry thus provides a simple, reproducible foundation for comparing how model families internalize and represent dynamical structure.

