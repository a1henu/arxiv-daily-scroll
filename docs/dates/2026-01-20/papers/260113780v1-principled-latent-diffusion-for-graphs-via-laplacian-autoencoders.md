---
layout: default
title: Principled Latent Diffusion for Graphs via Laplacian Autoencoders
---

# Principled Latent Diffusion for Graphs via Laplacian Autoencoders
**arXiv**：[2601.13780v1](https://arxiv.org/abs/2601.13780) · [PDF](https://arxiv.org/pdf/2601.13780.pdf)  
**作者**：Antoine Siraudin, Christopher Morris  

**一句话要点**：提出LG-Flow框架，通过拉普拉斯自编码器实现图数据的潜在扩散生成，解决二次复杂度与无损重建挑战。

**关键词**：图生成, 潜在扩散, 拉普拉斯自编码器, 扩散变换器, 流匹配, 置换等变性

## 3 点简述
- 图扩散模型在生成中面临二次复杂度瓶颈，且稀疏图中大量容量浪费于建模无连接边。
- LG-Flow使用置换等变自编码器将节点映射到固定维嵌入，实现近无损重建，并在潜在空间训练扩散变换器。
- 实验显示，该方法在保持竞争力的同时，实现高达1000倍的加速，适用于无向图和有向无环图。

## 摘要（原文）

> Graph diffusion models achieve state-of-the-art performance in graph generation but suffer from quadratic complexity in the number of nodes -- and much of their capacity is wasted modeling the absence of edges in sparse graphs. Inspired by latent diffusion in other modalities, a natural idea is to compress graphs into a low-dimensional latent space and perform diffusion there. However, unlike images or text, graph generation requires nearly lossless reconstruction, as even a single error in decoding an adjacency matrix can render the entire sample invalid. This challenge has remained largely unaddressed. We propose LG-Flow, a latent graph diffusion framework that directly overcomes these obstacles. A permutation-equivariant autoencoder maps each node into a fixed-dimensional embedding from which the full adjacency is provably recoverable, enabling near-lossless reconstruction for both undirected graphs and DAGs. The dimensionality of this latent representation scales linearly with the number of nodes, eliminating the quadratic bottleneck and making it feasible to train larger and more expressive models. In this latent space, we train a Diffusion Transformer with flow matching, enabling efficient and expressive graph generation. Our approach achieves competitive results against state-of-the-art graph diffusion models, while achieving up to $1000\times$ speed-up.

