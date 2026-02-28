---
layout: default
title: Pix2Key: Controllable Open-Vocabulary Retrieval with Semantic Decomposition and Self-Supervised Visual Dictionary Learning
---

# Pix2Key: Controllable Open-Vocabulary Retrieval with Semantic Decomposition and Self-Supervised Visual Dictionary Learning
**arXiv**：[2602.22510v1](https://arxiv.org/abs/2602.22510) · [PDF](https://arxiv.org/pdf/2602.22510.pdf)  
**作者**：Guoyizhe Wei, Yang Jiao, Nan Xi, Zhishen Huang, Jingjing Meng, Rama Chellappa, Yan Gao  

**一句话要点**：提出Pix2Key方法，通过语义分解和自监督视觉词典学习，提升可控开放词汇检索的性能与多样性。

**关键词**：组合图像检索, 开放词汇检索, 视觉词典学习, 自监督预训练, 意图感知匹配, 多样性重排序

## 3 点简述
- 核心问题：组合图像检索中，传统方法易丢失细粒度线索或忽略用户隐含意图，导致结果重复。
- 方法要点：将查询和候选表示为开放词汇视觉词典，在统一嵌入空间实现意图感知约束匹配和多样性感知重排序。
- 实验或效果：在DFMM-Compose基准上，Pix2Key提升Recall@10达3.2点，自监督预训练组件V-Dict-AE额外增益2.3点，提高意图一致性和列表多样性。

## 摘要（原文）

> Composed Image Retrieval (CIR) uses a reference image plus a natural-language edit to retrieve images that apply the requested change while preserving other relevant visual content. Classic fusion pipelines typically rely on supervised triplets and can lose fine-grained cues, while recent zero-shot approaches often caption the reference image and merge the caption with the edit, which may miss implicit user intent and return repetitive results. We present Pix2Key, which represents both queries and candidates as open-vocabulary visual dictionaries, enabling intent-aware constraint matching and diversity-aware reranking in a unified embedding space. A self-supervised pretraining component, V-Dict-AE, further improves the dictionary representation using only images, strengthening fine-grained attribute understanding without CIR-specific supervision. On the DFMM-Compose benchmark, Pix2Key improves Recall@10 up to 3.2 points, and adding V-Dict-AE yields an additional 2.3-point gain while improving intent consistency and maintaining high list diversity.

