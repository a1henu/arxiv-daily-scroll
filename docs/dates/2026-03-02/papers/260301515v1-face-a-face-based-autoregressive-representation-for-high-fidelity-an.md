---
layout: default
title: FACE: A Face-based Autoregressive Representation for High-Fidelity and Efficient Mesh Generation
---

# FACE: A Face-based Autoregressive Representation for High-Fidelity and Efficient Mesh Generation
**arXiv**：[2603.01515v1](https://arxiv.org/abs/2603.01515) · [PDF](https://arxiv.org/pdf/2603.01515.pdf)  
**作者**：Hanxiao Wang, Yuan-Chen Guo, Ying-Tian Liu, Zi-Xin Zou, Biao Zhang, Weize Quan, Ding Liang, Yan-Pei Cao, Dong-Ming Yan  

**一句话要点**：提出FACE框架，以面级自回归生成解决3D网格生成效率与质量瓶颈。

**关键词**：3D网格生成, 自回归模型, 面级表示, 自动编码器, 潜在扩散模型, 高保真几何合成

## 3 点简述
- 核心问题：传统自回归模型将网格展平为长顶点序列，导致计算成本高，阻碍高保真几何合成。
- 方法要点：采用面级自回归自动编码器，将每个三角形面作为单一令牌，序列长度减少九倍，压缩比达0.11。
- 实验或效果：在标准基准上实现最优重建质量，结合潜在扩散模型实现高保真单图像到网格生成。

## 摘要（原文）

> Autoregressive models for 3D mesh generation suffer from a fundamental limitation: they flatten meshes into long vertex-coordinate sequences. This results in prohibitive computational costs, hindering the efficient synthesis of high-fidelity geometry. We argue this bottleneck stems from operating at the wrong semantic level. We introduce FACE, a novel Autoregressive Autoencoder (ARAE) framework that reconceptualizes the task by generating meshes at the face level. Our one-face-one-token strategy treats each triangle face, the fundamental building block of a mesh, as a single, unified token. This simple yet powerful design reduces the sequence length by a factor of nine, leading to an unprecedented compression ratio of 0.11, halving the previous state-of-the-art. This dramatic efficiency gain does not compromise quality; by pairing our face-level decoder with a powerful VecSet encoder, FACE achieves state-of-the-art reconstruction quality on standard benchmarks. The versatility of the learned latent space is further demonstrated by training a latent diffusion model that achieves high-fidelity, single-image-to-mesh generation. FACE provides a simple, scalable, and powerful paradigm that lowers the barrier to high-quality structured 3D content creation.

