---
layout: default
title: CLIP-Map: Structured Matrix Mapping for Parameter-Efficient CLIP Compression
---

# CLIP-Map: Structured Matrix Mapping for Parameter-Efficient CLIP Compression
**arXiv**：[2602.05909v1](https://arxiv.org/abs/2602.05909) · [PDF](https://arxiv.org/pdf/2602.05909.pdf)  
**作者**：Kangjie Zhang, Wenxuan Huang, Xin Zhou, Boxiang Zhou, Dejia Song, Yuan Xie, Baochang Zhang, Lizhuang Ma, Nemo Chen, Xu Tang, Yao Hu, Shaohui Lin  

**一句话要点**：提出CLIP-Map框架，通过结构化矩阵映射实现参数高效压缩，以解决CLIP模型在资源受限场景下的高成本问题。

**关键词**：CLIP压缩, 参数高效学习, 结构化矩阵映射, Kronecker分解, 模型优化, 资源受限应用

## 3 点简述
- 核心问题：CLIP模型因高内存和计算成本，难以应用于资源受限场景，现有基于选择的压缩方法在极端压缩下会损害特征表示能力。
- 方法要点：采用基于映射的压缩框架，利用可学习矩阵通过全映射与Kronecker分解来映射和组合预训练权重，并引入对角继承初始化以缓解优化挑战。
- 实验或效果：在多种压缩比下优于基于选择的方法，尤其在高压縮设置下表现显著提升。

## 摘要（原文）

> Contrastive Language-Image Pre-training (CLIP) has achieved widely applications in various computer vision tasks, e.g., text-to-image generation, Image-Text retrieval and Image captioning. However, CLIP suffers from high memory and computation cost, which prohibits its usage to the resource-limited application scenarios. Existing CLIP compression methods typically reduce the size of pre-trained CLIP weights by selecting their subset as weight inheritance for further retraining via mask optimization or important weight measurement. However, these select-based weight inheritance often compromises the feature presentation ability, especially on the extreme compression. In this paper, we propose a novel mapping-based CLIP compression framework, CLIP-Map. It leverages learnable matrices to map and combine pretrained weights by Full-Mapping with Kronecker Factorization, aiming to preserve as much information from the original weights as possible. To mitigate the optimization challenges introduced by the learnable mapping, we propose Diagonal Inheritance Initialization to reduce the distribution shifting problem for efficient and effective mapping learning. Extensive experimental results demonstrate that the proposed CLIP-Map outperforms select-based frameworks across various compression ratios, with particularly significant gains observed under high compression settings.

