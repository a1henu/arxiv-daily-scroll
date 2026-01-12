---
layout: default
title: Learning Reconstructive Embeddings in Reproducing Kernel Hilbert Spaces via the Representer Theorem
---

# Learning Reconstructive Embeddings in Reproducing Kernel Hilbert Spaces via the Representer Theorem
**arXiv**：[2601.05811v1](https://arxiv.org/abs/2601.05811) · [PDF](https://arxiv.org/pdf/2601.05811.pdf)  
**作者**：Enrique Feito-Casares, Francisco M. Melgarejo-Meseguer, José-Luis Rojo-Álvarez  

**一句话要点**：提出基于表示定理的RKHS重构嵌入算法，用于高维数据的表示学习与降维。

**关键词**：表示学习, 再生核希尔伯特空间, 表示定理, 自表示, 核对齐, 降维

## 3 点简述
- 核心问题：高维数据中潜在结构的表示学习，需在RKHS中实现重构与降维。
- 方法要点：利用表示定理优化自表示，通过算子值核扩展至向量值数据，并进行核对齐投影。
- 实验或效果：在模拟和真实数据集上验证了方法的有效性，包括癌症分子活动和物联网入侵检测。

## 摘要（原文）

> Motivated by the growing interest in representation learning approaches that uncover the latent structure of high-dimensional data, this work proposes new algorithms for reconstruction-based manifold learning within Reproducing-Kernel Hilbert Spaces (RKHS). Each observation is first reconstructed as a linear combination of the other samples in the RKHS, by optimizing a vector form of the Representer Theorem for their autorepresentation property. A separable operator-valued kernel extends the formulation to vector-valued data while retaining the simplicity of a single scalar similarity function. A subsequent kernel-alignment task projects the data into a lower-dimensional latent space whose Gram matrix aims to match the high-dimensional reconstruction kernel, thus transferring the auto-reconstruction geometry of the RKHS to the embedding. Therefore, the proposed algorithms represent an extended approach to the autorepresentation property, exhibited by many natural data, by using and adapting well-known results of Kernel Learning Theory. Numerical experiments on both simulated (concentric circles and swiss-roll) and real (cancer molecular activity and IoT network intrusions) datasets provide empirical evidence of the practical effectiveness of the proposed approach.

