---
layout: default
title: Composed Vision-Language Retrieval for Skin Cancer Case Search via Joint Alignment of Global and Local Representations
---

# Composed Vision-Language Retrieval for Skin Cancer Case Search via Joint Alignment of Global and Local Representations
**arXiv**：[2603.09108v1](https://arxiv.org/abs/2603.09108) · [PDF](https://arxiv.org/pdf/2603.09108.pdf)  
**作者**：Yuheng Wang, Yuji Lin, Dongrun Zhu, Jiayue Cai, Sunil Kalia, Harvey Lui, Chunqi Chang, Z. Jane Wang, Tim K. Lee  

**一句话要点**：提出基于Transformer的全局-局部联合对齐框架，以解决皮肤癌组合视觉-语言检索问题。

**关键词**：组合视觉-语言检索, 皮肤癌病例搜索, 全局-局部对齐, Transformer框架, 医学图像检索

## 3 点简述
- 核心问题：皮肤癌检索中，查询常结合图像与文本描述，需高效匹配活检确认的多类病例。
- 方法要点：学习层次化组合查询表示，通过空间注意力掩码聚合局部区域，并加权融合全局与局部对齐。
- 实验或效果：在Derm7pt数据集上优于现有方法，支持临床部署与医疗记录访问。

## 摘要（原文）

> Medical image retrieval aims to identify clinically relevant lesion cases to support diagnostic decision making, education, and quality control. In practice, retrieval queries often combine a reference lesion image with textual descriptors such as dermoscopic features. We study composed vision-language retrieval for skin cancer, where each query consists of an image to text pair and the database contains biopsy-confirmed, multi-class disease cases. We propose a transformer based framework that learns hierarchical composed query representations and performs joint global-local alignment between queries and candidate images. Local alignment aggregates discriminative regions via multiple spatial attention masks, while global alignment provides holistic semantic supervision. The final similarity is computed through a convex, domain-informed weighting that emphasizes clinically salient local evidence while preserving global consistency. Experiments on the public Derm7pt dataset demonstrate consistent improvements over state-of-the-art methods. The proposed framework enables efficient access to relevant medical records and supports practical clinical deployment.

