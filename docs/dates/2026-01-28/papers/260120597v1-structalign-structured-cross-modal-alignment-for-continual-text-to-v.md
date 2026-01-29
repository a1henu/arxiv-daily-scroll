---
layout: default
title: StructAlign: Structured Cross-Modal Alignment for Continual Text-to-Video Retrieval
---

# StructAlign: Structured Cross-Modal Alignment for Continual Text-to-Video Retrieval
**arXiv**：[2601.20597v1](https://arxiv.org/abs/2601.20597) · [PDF](https://arxiv.org/pdf/2601.20597.pdf)  
**作者**：Shaokun Wang, Weili Guan, Jizhou Han, Jianlong Wu, Yupeng Hu, Liqiang Nie  

**一句话要点**：提出StructAlign方法，通过结构化跨模态对齐缓解持续文本-视频检索中的灾难性遗忘。

**关键词**：持续学习, 跨模态检索, 特征对齐, 灾难性遗忘, 文本-视频检索

## 3 点简述
- 核心问题：持续文本-视频检索面临模态内特征漂移和跨模态非合作漂移，导致灾难性遗忘。
- 方法要点：引入单纯形等角紧框架几何先验，设计跨模态ETF对齐损失和跨模态关系保持损失，联合抑制特征漂移。
- 实验或效果：在基准数据集上广泛实验，方法持续优于最先进的持续检索方法。

## 摘要（原文）

> Continual Text-to-Video Retrieval (CTVR) is a challenging multimodal continual learning setting, where models must incrementally learn new semantic categories while maintaining accurate text-video alignment for previously learned ones, thus making it particularly prone to catastrophic forgetting. A key challenge in CTVR is feature drift, which manifests in two forms: intra-modal feature drift caused by continual learning within each modality, and non-cooperative feature drift across modalities that leads to modality misalignment. To mitigate these issues, we propose StructAlign, a structured cross-modal alignment method for CTVR. First, StructAlign introduces a simplex Equiangular Tight Frame (ETF) geometry as a unified geometric prior to mitigate modality misalignment. Building upon this geometric prior, we design a cross-modal ETF alignment loss that aligns text and video features with category-level ETF prototypes, encouraging the learned representations to form an approximate simplex ETF geometry. In addition, to suppress intra-modal feature drift, we design a Cross-modal Relation Preserving loss, which leverages complementary modalities to preserve cross-modal similarity relations, providing stable relational supervision for feature updates. By jointly addressing non-cooperative feature drift across modalities and intra-modal feature drift, StructAlign effectively alleviates catastrophic forgetting in CTVR. Extensive experiments on benchmark datasets demonstrate that our method consistently outperforms state-of-the-art continual retrieval approaches.

