---
layout: default
title: Learning Tangent Bundles and Characteristic Classes with Autoencoder Atlases
---

# Learning Tangent Bundles and Characteristic Classes with Autoencoder Atlases
**arXiv**：[2602.22873v1](https://arxiv.org/abs/2602.22873) · [PDF](https://arxiv.org/pdf/2602.22873.pdf)  
**作者**：Eduardo Paluzo-Hidalgo, Yuichi Ike  

**一句话要点**：提出多图自编码器框架，连接流形学习与向量丛理论以计算特征类。

**关键词**：流形学习, 自编码器, 向量丛, 特征类, 可定向性检测, 多图表示

## 3 点简述
- 核心问题：传统自编码器缺乏微分拓扑不变量的直接计算能力。
- 方法要点：将局部编码器-解码器对视为学习图册，线性化转移映射定义向量丛。
- 实验或效果：应用于低维和高维数据集，检测可定向性并确定最小图册数。

## 摘要（原文）

> We introduce a theoretical framework that connects multi-chart autoencoders in manifold learning with the classical theory of vector bundles and characteristic classes. Rather than viewing autoencoders as producing a single global Euclidean embedding, we treat a collection of locally trained encoder-decoder pairs as a learned atlas on a manifold. We show that any reconstruction-consistent autoencoder atlas canonically defines transition maps satisfying the cocycle condition, and that linearising these transition maps yields a vector bundle coinciding with the tangent bundle when the latent dimension matches the intrinsic dimension of the manifold. This construction provides direct access to differential-topological invariants of the data. In particular, we show that the first Stiefel-Whitney class can be computed from the signs of the Jacobians of learned transition maps, yielding an algorithmic criterion for detecting orientability. We also show that non-trivial characteristic classes provide obstructions to single-chart representations, and that the minimum number of autoencoder charts is determined by the good cover structure of the manifold. Finally, we apply our methodology to low-dimensional orientable and non-orientable manifolds, as well as to a non-orientable high-dimensional image dataset.

