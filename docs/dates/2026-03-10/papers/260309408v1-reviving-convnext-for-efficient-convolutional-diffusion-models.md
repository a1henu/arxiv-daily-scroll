---
layout: default
title: Reviving ConvNeXt for Efficient Convolutional Diffusion Models
---

# Reviving ConvNeXt for Efficient Convolutional Diffusion Models
**arXiv**：[2603.09408v1](https://arxiv.org/abs/2603.09408) · [PDF](https://arxiv.org/pdf/2603.09408.pdf)  
**作者**：Taesung Kwon, Lorenzo Bianchi, Lennart Wittke, Felix Watine, Fabio Carrara, Jong Chul Ye, Romann Weber, Vinicius Azevedo  

**一句话要点**：提出全卷积扩散模型以替代Transformer，实现高效扩散建模

**关键词**：扩散模型, 卷积神经网络, 高效训练, 生成建模, ConvNeXt, 参数效率

## 3 点简述
- 问题：扩散模型多采用Transformer，卷积网络在生成建模中效率优势未充分探索
- 方法：设计基于ConvNeXt的全卷积扩散模型，优化参数效率与硬件友好性
- 效果：在256×256和512×512分辨率下，以更少训练步骤和计算量达到竞争性能

## 摘要（原文）

> Recent diffusion models increasingly favor Transformer backbones, motivated by the remarkable scalability of fully attentional architectures. Yet the locality bias, parameter efficiency, and hardware friendliness--the attributes that established ConvNets as the efficient vision backbone--have seen limited exploration in modern generative modeling. Here we introduce the fully convolutional diffusion model (FCDM), a model having a backbone similar to ConvNeXt, but designed for conditional diffusion modeling. We find that using only 50% of the FLOPs of DiT-XL/2, FCDM-XL achieves competitive performance with 7$\times$ and 7.5$\times$ fewer training steps at 256$\times$256 and 512$\times$512 resolutions, respectively. Remarkably, FCDM-XL can be trained on a 4-GPU system, highlighting the exceptional training efficiency of our architecture. Our results demonstrate that modern convolutional designs provide a competitive and highly efficient alternative for scaling diffusion models, reviving ConvNeXt as a simple yet powerful building block for efficient generative modeling.

