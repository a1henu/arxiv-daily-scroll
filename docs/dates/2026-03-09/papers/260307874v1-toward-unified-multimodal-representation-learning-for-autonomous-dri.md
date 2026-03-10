---
layout: default
title: Toward Unified Multimodal Representation Learning for Autonomous Driving
---

# Toward Unified Multimodal Representation Learning for Autonomous Driving
**arXiv**：[2603.07874v1](https://arxiv.org/abs/2603.07874) · [PDF](https://arxiv.org/pdf/2603.07874.pdf)  
**作者**：Ximeng Tao, Dimitar Filev, Gaurav Pandey  

**一句话要点**：提出对比张量预训练框架以统一多模态对齐，提升自动驾驶场景理解。

**关键词**：多模态表示学习, 自动驾驶, 对比学习, 张量对齐, 点云理解

## 3 点简述
- 核心问题：现有方法仅对齐成对模态，未能确保多模态空间的一致统一对齐。
- 方法要点：扩展2D相似度矩阵为多模态相似度张量，引入张量损失进行联合对比学习。
- 实验或效果：构建文本-图像-点云三元数据集，验证框架在预训练和从头训练中均表现良好。

## 摘要（原文）

> Contrastive Language-Image Pre-training (CLIP) has shown impressive performance in aligning visual and textual representations. Recent studies have extended this paradigm to 3D vision to improve scene understanding for autonomous driving. A common strategy is to employ pairwise cosine similarity between modalities to guide the training of a 3D encoder. However, considering the similarity between individual modality pairs rather than all modalities jointly fails to ensure consistent and unified alignment across the entire multimodal space. In this paper, we propose a Contrastive Tensor Pre-training (CTP) framework that simultaneously aligns multiple modalities in a unified embedding space to enhance end-to-end autonomous driving. Compared with pairwise cosine similarity alignment, our method extends the 2D similarity matrix into a multimodal similarity tensor. Furthermore, we introduce a tensor loss to enable joint contrastive learning across all modalities. For experimental validation of our framework, we construct a text-image-point cloud triplet dataset derived from existing autonomous driving datasets. The results show that our proposed unified multimodal alignment framework achieves favorable performance for both scenarios: (i) aligning a 3D encoder with pretrained CLIP encoders, and (ii) pretraining all encoders from scratch.

