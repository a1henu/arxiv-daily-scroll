---
layout: default
title: MoRE: Batch-Robust Multi-Omics Representations from Frozen Pre-trained Transformers
---

# MoRE: Batch-Robust Multi-Omics Representations from Frozen Pre-trained Transformers
**arXiv**：[2511.20382v1](https://arxiv.org/abs/2511.20382) · [PDF](https://arxiv.org/pdf/2511.20382.pdf)  
**作者**：Audrey Pei-Hsuan Chen  

**一句话要点**：提出MoRE框架，利用冻结预训练Transformer解决多组学数据集成中的批次效应问题

**关键词**：多组学表示学习, 参数高效微调, 批次效应校正, Transformer模型, 模态融合

## 3 点简述
- 多组学数据集成面临高维、模态异质性和批次效应等挑战
- 采用冻结预训练Transformer，结合轻量适配器和融合层进行参数高效微调
- 实验显示MoRE在批次鲁棒性和生物学保守性上表现优异，参数显著减少

## 摘要（原文）

> Representation learning on multi-omics data is challenging due to extreme dimensionality, modality heterogeneity, and cohort-specific batch effects. While pre-trained transformer backbones have shown broad generalization capabilities in biological sequence modeling, their application to multi-omics integration remains underexplored. We present MoRE (Multi-Omics Representation Embedding), a framework that repurposes frozen pre-trained transformers to align heterogeneous assays into a shared latent space. Unlike purely generative approaches, MoRE employs a parameter-efficient fine-tuning (PEFT) strategy, prioritizing cross-sample and cross-modality alignment over simple sequence reconstruction. Specifically, MoRE attaches lightweight, modality-specific adapters and a task-adaptive fusion layer to the frozen backbone. It optimizes a masked modeling objective jointly with supervised contrastive and batch-invariant alignment losses, yielding structure-preserving embeddings that generalize across unseen cell types and platforms. We benchmark MoRE against established baselines, including scGPT, scVI, and Harmony with scArches, evaluating integration fidelity, rare population detection, and modality transfer. Our results demonstrate that MoRE achieves competitive batch robustness and biological conservation while significantly reducing trainable parameters compared to fully fine-tuned models. This work positions MoRE as a practical step toward general-purpose omics foundation models.

