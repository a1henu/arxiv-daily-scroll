---
layout: default
title: ViCLIP-OT: The First Foundation Vision-Language Model for Vietnamese Image-Text Retrieval with Optimal Transport
---

# ViCLIP-OT: The First Foundation Vision-Language Model for Vietnamese Image-Text Retrieval with Optimal Transport
**arXiv**：[2602.22678v1](https://arxiv.org/abs/2602.22678) · [PDF](https://arxiv.org/pdf/2602.22678.pdf)  
**作者**：Quoc-Khang Tran, Minh-Thien Nguyen, Nguyen-Khang Pham  

**一句话要点**：提出ViCLIP-OT，首个越南语图文检索基础模型，结合最优传输提升跨模态一致性。

**关键词**：越南语图文检索, 视觉语言模型, 最优传输, 低资源语言, 跨模态对齐

## 3 点简述
- 核心问题：现有视觉语言模型对越南语等低资源语言图文检索效果不佳。
- 方法要点：集成CLIP对比学习与SIGROT损失，增强全局一致性并减少模态间隙。
- 实验或效果：在三个越南语基准测试中超越CLIP和SigLIP，零-shot性能提升显著。

## 摘要（原文）

> Image-text retrieval has become a fundamental component in intelligent multimedia systems; however, most existing vision-language models are optimized for highresource languages and remain suboptimal for low-resource settings such as Vietnamese. This work introduces ViCLIP-OT, a foundation vision-language model specifically designed for Vietnamese image-text retrieval. The proposed framework integrates CLIP-style contrastive learning with a Similarity-Graph Regularized Optimal Transport (SIGROT) loss to enhance global cross-modal consistency and mitigate modality gap issues. Extensive experiments on three Vietnamese benchmarks (UITOpenViIC, KTVIC, and Crossmodal-3600) demonstrate that ViCLIP-OT consistently outperforms CLIP and SigLIP baselines in both in-domain and zero-shot settings. On UIT-OpenViIC, the model achieves an average Recall@K of 67.34%, improving upon CLIP by 5.75 percentage points. In zero-shot evaluation on Crossmodal-3600, ViCLIPOT surpasses CLIP by 11.72 percentage points. Embedding-space analysis further confirms improved alignment and reduced modality gap. The results indicate that integrating SIGROT provides an effective and scalable strategy for cross-modal retrieval in low-resource languages, offering practical implications for intelligent multimedia retrieval systems in Vietnamese and other underrepresented linguistic contexts.

