---
layout: default
title: Learning on the Manifold: Unlocking Standard Diffusion Transformers with Representation Encoders
---

# Learning on the Manifold: Unlocking Standard Diffusion Transformers with Representation Encoders
**arXiv**：[2602.10099v1](https://arxiv.org/abs/2602.10099) · [PDF](https://arxiv.org/pdf/2602.10099.pdf)  
**作者**：Amandeep Kumar, Vishal M. Patel  

**一句话要点**：提出黎曼流匹配与雅可比正则化以解决标准扩散变换器在表示编码器上的几何干扰问题

**关键词**：扩散变换器, 表示编码器, 流形学习, 黎曼流匹配, 几何干扰, 生成建模

## 3 点简述
- 核心问题：标准扩散变换器在表示编码器上不收敛，源于欧几里得流匹配导致概率路径偏离流形表面
- 方法要点：引入黎曼流匹配约束生成过程沿流形测地线，并添加雅可比正则化校正曲率误差传播
- 实验或效果：标准DiT-B架构（1.31亿参数）有效收敛，FID达3.37，优于先前方法

## 摘要（原文）

> Leveraging representation encoders for generative modeling offers a path for efficient, high-fidelity synthesis. However, standard diffusion transformers fail to converge on these representations directly. While recent work attributes this to a capacity bottleneck proposing computationally expensive width scaling of diffusion transformers we demonstrate that the failure is fundamentally geometric. We identify Geometric Interference as the root cause: standard Euclidean flow matching forces probability paths through the low-density interior of the hyperspherical feature space of representation encoders, rather than following the manifold surface. To resolve this, we propose Riemannian Flow Matching with Jacobi Regularization (RJF). By constraining the generative process to the manifold geodesics and correcting for curvature-induced error propagation, RJF enables standard Diffusion Transformer architectures to converge without width scaling. Our method RJF enables the standard DiT-B architecture (131M parameters) to converge effectively, achieving an FID of 3.37 where prior methods fail to converge. Code: https://github.com/amandpkr/RJF

