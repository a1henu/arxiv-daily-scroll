---
layout: default
title: Hierarchical Transformers for Unsupervised 3D Shape Abstraction
---

# Hierarchical Transformers for Unsupervised 3D Shape Abstraction
**arXiv**：[2510.27088v1](https://arxiv.org/abs/2510.27088) · [PDF](https://arxiv.org/pdf/2510.27088.pdf)  
**作者**：Aditya Vora, Lily Goli, Andrea Tagliasacchi, Hao Zhang  

**一句话要点**：提出分层变换器HiT，用于无监督3D形状抽象，学习通用层次结构。

**关键词**：分层变换器, 无监督学习, 3D形状抽象, 神经场表示, 形状分割

## 3 点简述
- 核心问题：无监督学习3D形状的通用层次结构，避免固定结构限制。
- 方法要点：使用分层变换器和压缩码本，自动识别跨类别的子结构关系。
- 实验效果：在ShapeNet 55类上实现多粒度形状分割，验证有效性。

## 摘要（原文）

> We introduce HiT, a novel hierarchical neural field representation for 3D
> shapes that learns general hierarchies in a coarse-to-fine manner across
> different shape categories in an unsupervised setting. Our key contribution is
> a hierarchical transformer (HiT), where each level learns parent-child
> relationships of the tree hierarchy using a compressed codebook. This codebook
> enables the network to automatically identify common substructures across
> potentially diverse shape categories. Unlike previous works that constrain the
> task to a fixed hierarchical structure (e.g., binary), we impose no such
> restriction, except for limiting the total number of nodes at each tree level.
> This flexibility allows our method to infer the hierarchical structure directly
> from data, over multiple shape categories, and representing more general and
> complex hierarchies than prior approaches. When trained at scale with a
> reconstruction loss, our model captures meaningful containment relationships
> between parent and child nodes. We demonstrate its effectiveness through an
> unsupervised shape segmentation task over all 55 ShapeNet categories, where our
> method successfully segments shapes into multiple levels of granularity.

