---
layout: default
title: Hyperdimensional Cross-Modal Alignment of Frozen Language and Image Models for Efficient Image Captioning
---

# Hyperdimensional Cross-Modal Alignment of Frozen Language and Image Models for Efficient Image Captioning
**arXiv**：[2602.23588v1](https://arxiv.org/abs/2602.23588) · [PDF](https://arxiv.org/pdf/2602.23588.pdf)  
**作者**：Abhishek Dalvi, Vasant Honavar  

**一句话要点**：提出HDFLIM框架，通过超维计算对齐冻结语言与图像模型，实现高效图像描述生成

**关键词**：跨模态对齐, 超维计算, 冻结模型, 图像描述生成, 符号操作, 高效计算

## 3 点简述
- 核心问题：跨模态对齐通常需计算密集型微调，可能扰动预训练表示
- 方法要点：将单模态嵌入投影到共享超维空间，利用轻量符号操作构建关联表示
- 实验或效果：性能媲美端到端训练方法，生成描述比零样本基线更语义接地

## 摘要（原文）

> Large unimodal foundation models for vision and language encode rich semantic structures, yet aligning them typically requires computationally intensive multimodal fine-tuning. Such approaches depend on large-scale parameter updates, are resource intensive, and can perturb pretrained representations. Emerging evidence suggests, however, that independently trained foundation models may already exhibit latent semantic compatibility, reflecting shared structures in the data they model. This raises a fundamental question: can cross-modal alignment be achieved without modifying the models themselves? Here we introduce HDFLIM (HyperDimensional computing with Frozen Language and Image Models), a framework that establishes cross-modal mappings while keeping pretrained vision and language models fully frozen. HDFLIM projects unimodal embeddings into a shared hyperdimensional space and leverages lightweight symbolic operations -- binding, bundling, and similarity-based retrieval to construct associative cross-modal representations in a single pass over the data. Caption generation emerges from high-dimensional memory retrieval rather than iterative gradient-based optimization. We show that HDFLIM achieves performance comparable to end-to-end vision-language training methods and produces captions that are more semantically grounded than zero-shot baselines. By decoupling alignment from parameter tuning, our results suggest that semantic mapping across foundation models can be realized through symbolic operations on hyperdimensional encodings of the respective embeddings. More broadly, this work points toward an alternative paradigm for foundation model alignment in which frozen models are integrated through structured representational mappings rather than through large-scale retraining. The codebase for our implementation can be found at https://github.com/Abhishek-Dalvi410/HDFLIM.

