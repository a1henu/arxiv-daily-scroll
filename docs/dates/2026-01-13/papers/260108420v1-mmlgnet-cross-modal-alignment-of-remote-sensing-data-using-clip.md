---
layout: default
title: MMLGNet: Cross-Modal Alignment of Remote Sensing Data using CLIP
---

# MMLGNet: Cross-Modal Alignment of Remote Sensing Data using CLIP
**arXiv**：[2601.08420v1](https://arxiv.org/abs/2601.08420) · [PDF](https://arxiv.org/pdf/2601.08420.pdf)  
**作者**：Aditya Chaudhary, Sneha Barman, Mainak Singha, Ankit Jha, Girish Mishra, Biplab Banerjee  

**一句话要点**：提出MMLGNet，利用CLIP对齐遥感多模态数据与自然语言语义

**关键词**：遥感多模态对齐, CLIP应用, 双向对比学习, 语言监督, 高光谱成像, 激光雷达

## 3 点简述
- 核心问题：遥感多模态数据（如高光谱成像和激光雷达）与语言语义对齐困难，需融合光谱、空间和几何信息。
- 方法要点：采用模态特定编码器，通过双向对比学习在共享潜在空间对齐视觉特征与手工文本嵌入。
- 实验或效果：在基准数据集上超越多种多模态视觉方法，展示语言监督的显著优势，代码已开源。

## 摘要（原文）

> In this paper, we propose a novel multimodal framework, Multimodal Language-Guided Network (MMLGNet), to align heterogeneous remote sensing modalities like Hyperspectral Imaging (HSI) and LiDAR with natural language semantics using vision-language models such as CLIP. With the increasing availability of multimodal Earth observation data, there is a growing need for methods that effectively fuse spectral, spatial, and geometric information while enabling semantic-level understanding. MMLGNet employs modality-specific encoders and aligns visual features with handcrafted textual embeddings in a shared latent space via bi-directional contrastive learning. Inspired by CLIP's training paradigm, our approach bridges the gap between high-dimensional remote sensing data and language-guided interpretation. Notably, MMLGNet achieves strong performance with simple CNN-based encoders, outperforming several established multimodal visual-only methods on two benchmark datasets, demonstrating the significant benefit of language supervision. Codes are available at https://github.com/AdityaChaudhary2913/CLIP_HSI.

