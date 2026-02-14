---
layout: default
title: Hi-SAM: A Hierarchical Structure-Aware Multi-modal Framework for Large-Scale Recommendation
---

# Hi-SAM: A Hierarchical Structure-Aware Multi-modal Framework for Large-Scale Recommendation
**arXiv**：[2602.11799v1](https://arxiv.org/abs/2602.11799) · [PDF](https://arxiv.org/pdf/2602.11799.pdf)  
**作者**：Pingjun Pan, Tingting Zhou, Peiyao Lu, Tingting Fei, Hongxiang Chen, Chuanjiang Luo  

**一句话要点**：提出Hi-SAM框架，通过解耦语义分词器和分层记忆锚点Transformer解决多模态推荐中的语义冗余与架构不匹配问题。

**关键词**：多模态推荐, 语义ID, 分层Transformer, 解耦学习, 冷启动优化, 大规模部署

## 3 点简述
- 核心问题：现有方法在语义ID生成中存在跨模态语义与模态细节未解耦，以及Transformer架构忽略用户交互和物品的层次结构。
- 方法要点：设计解耦语义分词器统一多模态信息并量化，采用分层记忆锚点Transformer恢复层次结构并压缩物品表示。
- 实验或效果：在真实数据集上优于现有方法，冷启动场景表现突出，大规模部署实现核心指标提升6.55%。

## 摘要（原文）

> Multi-modal recommendation has gained traction as items possess rich attributes like text and images. Semantic ID-based approaches effectively discretize this information into compact tokens. However, two challenges persist: (1) Suboptimal Tokenization: existing methods (e.g., RQ-VAE) lack disentanglement between shared cross-modal semantics and modality-specific details, causing redundancy or collapse; (2) Architecture-Data Mismatch: vanilla Transformers treat semantic IDs as flat streams, ignoring the hierarchy of user interactions, items, and tokens. Expanding items into multiple tokens amplifies length and noise, biasing attention toward local details over holistic semantics. We propose Hi-SAM, a Hierarchical Structure-Aware Multi-modal framework with two designs: (1) Disentangled Semantic Tokenizer (DST): unifies modalities via geometry-aware alignment and quantizes them via a coarse-to-fine strategy. Shared codebooks distill consensus while modality-specific ones recover nuances from residuals, enforced by mutual information minimization; (2) Hierarchical Memory-Anchor Transformer (HMAT): splits positional encoding into inter- and intra-item subspaces via Hierarchical RoPE to restore hierarchy. It inserts Anchor Tokens to condense items into compact memory, retaining details for the current item while accessing history only through compressed summaries. Experiments on real-world datasets show consistent improvements over SOTA baselines, especially in cold-start scenarios. Deployed on a large-scale social platform serving millions of users, Hi-SAM achieved a 6.55% gain in the core online metric.

