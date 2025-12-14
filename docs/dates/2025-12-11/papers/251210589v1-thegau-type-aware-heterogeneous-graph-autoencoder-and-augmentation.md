---
layout: default
title: THeGAU: Type-Aware Heterogeneous Graph Autoencoder and Augmentation
---

# THeGAU: Type-Aware Heterogeneous Graph Autoencoder and Augmentation
**arXiv**：[2512.10589v1](https://arxiv.org/abs/2512.10589) · [PDF](https://arxiv.org/pdf/2512.10589.pdf)  
**作者**：Ming-Yi Hong, Miao-Chen Chiang, Youchen Teng, Yu-Hsiang Wang, Chih-Yu Wang, Che Lin  

**一句话要点**：提出THeGAU框架，通过类型感知图自编码器和引导图增强提升异构图节点分类性能。

**关键词**：异构图神经网络, 图自编码器, 图增强, 节点分类, 类型感知学习

## 3 点简述
- 核心问题：异构图神经网络存在类型信息丢失和结构噪声，影响表示保真度和泛化能力。
- 方法要点：结合类型感知图自编码器重建模式有效边以保留节点类型语义，并引入解码器驱动增强机制选择性优化噪声结构。
- 实验或效果：在IMDB、ACM和DBLP基准数据集上验证，THeGAU优于现有方法，实现最优性能并降低计算开销。

## 摘要（原文）

> Heterogeneous Graph Neural Networks (HGNNs) are effective for modeling Heterogeneous Information Networks (HINs), which encode complex multi-typed entities and relations. However, HGNNs often suffer from type information loss and structural noise, limiting their representational fidelity and generalization. We propose THeGAU, a model-agnostic framework that combines a type-aware graph autoencoder with guided graph augmentation to improve node classification. THeGAU reconstructs schema-valid edges as an auxiliary task to preserve node-type semantics and introduces a decoder-driven augmentation mechanism to selectively refine noisy structures. This joint design enhances robustness, accuracy, and efficiency while significantly reducing computational overhead. Extensive experiments on three benchmark HIN datasets (IMDB, ACM, and DBLP) demonstrate that THeGAU consistently outperforms existing HGNN methods, achieving state-of-the-art performance across multiple backbones.

