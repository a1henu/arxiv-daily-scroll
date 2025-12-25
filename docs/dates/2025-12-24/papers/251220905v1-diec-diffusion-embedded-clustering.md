---
layout: default
title: DiEC: Diffusion Embedded Clustering
---

# DiEC: Diffusion Embedded Clustering
**arXiv**：[2512.20905v1](https://arxiv.org/abs/2512.20905) · [PDF](https://arxiv.org/pdf/2512.20905.pdf)  
**作者**：Haidong Hu  

**一句话要点**：提出DiEC方法，利用预训练扩散模型的内部激活进行无监督聚类

**关键词**：扩散模型, 无监督聚类, 表示学习, U-Net激活, 自训练优化, 图正则化

## 3 点简述
- 核心问题：传统深度聚类使用单一编码器忽略扩散模型在不同层次和噪声时间步的表示轨迹，其中聚类友好性差异大
- 方法要点：通过层×时间步二维搜索选择表示，分解为固定瓶颈层和最优时间步搜索，结合KL自训练、自适应图正则化和熵正则化优化聚类
- 实验或效果：在多个标准基准测试中实现竞争性聚类性能，验证了方法的有效性

## 摘要（原文）

> Deep clustering hinges on learning representations that are inherently clusterable. However, using a single encoder to produce a fixed embedding ignores the representation trajectory formed by a pretrained diffusion model across network hierarchies and noise timesteps, where clusterability varies substantially. We propose DiEC (Diffusion Embedded Clustering), which performs unsupervised clustering by directly reading internal activations from a pretrained diffusion U-Net.
>   DiEC formulates representation selection as a two-dimensional search over layer x timestep, and exploits a weak-coupling property to decompose it into two stages. Specifically, we first fix the U-Net bottleneck layer as the Clustering-friendly Middle Layer (CML), and then use Optimal Timestep Search (OTS) to identify the clustering-optimal timestep (t*). During training, we extract bottleneck features at the fixed t* and obtain clustering representations via a lightweight residual mapping. We optimize a DEC-style KL self-training objective, augmented with adaptive graph regularization and entropy regularization to strengthen cluster structures. In parallel, we introduce a denoising-consistency branch at random timesteps to stabilize the representations and preserve generative consistency. Experiments show that DiEC achieves competitive clustering performance on multiple standard benchmarks.

