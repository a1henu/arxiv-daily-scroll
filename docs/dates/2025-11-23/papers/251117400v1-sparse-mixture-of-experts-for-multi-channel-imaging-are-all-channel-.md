---
layout: default
title: Sparse Mixture-of-Experts for Multi-Channel Imaging: Are All Channel Interactions Required?
---

# Sparse Mixture-of-Experts for Multi-Channel Imaging: Are All Channel Interactions Required?
**arXiv**：[2511.17400v1](https://arxiv.org/abs/2511.17400) · [PDF](https://arxiv.org/pdf/2511.17400.pdf)  
**作者**：Sukwon Yun, Heming Yao, Burkhard Hoeckendorf, David Richmond, Aviv Regev, Russell Littman  

**一句话要点**：提出MoE-ViT以解决多通道图像中注意力计算效率低的问题

**关键词**：稀疏混合专家, 多通道图像, 视觉Transformer, 注意力效率, 计算优化

## 3 点简述
- 多通道图像中通道交互建模导致注意力计算二次增长，效率低下
- 采用稀疏混合专家架构，将通道视为专家，轻量路由器选择相关专家
- 在JUMP-CP和So2Sat数据集上实现效率提升，性能未损失或增强

## 摘要（原文）

> Vision Transformers ($\text{ViTs}$) have become the backbone of vision foundation models, yet their optimization for multi-channel domains - such as cell painting or satellite imagery - remains underexplored. A key challenge in these domains is capturing interactions between channels, as each channel carries different information. While existing works have shown efficacy by treating each channel independently during tokenization, this approach naturally introduces a major computational bottleneck in the attention block - channel-wise comparisons leads to a quadratic growth in attention, resulting in excessive $\text{FLOPs}$ and high training cost. In this work, we shift focus from efficacy to the overlooked efficiency challenge in cross-channel attention and ask: "Is it necessary to model all channel interactions?". Inspired by the philosophy of Sparse Mixture-of-Experts ($\text{MoE}$), we propose MoE-ViT, a Mixture-of-Experts architecture for multi-channel images in $\text{ViTs}$, which treats each channel as an expert and employs a lightweight router to select only the most relevant experts per patch for attention. Proof-of-concept experiments on real-world datasets - JUMP-CP and So2Sat - demonstrate that $\text{MoE-ViT}$ achieves substantial efficiency gains without sacrificing, and in some cases enhancing, performance, making it a practical and attractive backbone for multi-channel imaging.

