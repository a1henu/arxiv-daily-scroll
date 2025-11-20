---
layout: default
title: Multi-Text Guided Few-Shot Semantic Segmentation
---

# Multi-Text Guided Few-Shot Semantic Segmentation
**arXiv**：[2511.15515v1](https://arxiv.org/abs/2511.15515) · [PDF](https://arxiv.org/pdf/2511.15515.pdf)  
**作者**：Qiang Jiao, Bin Yan, Yi Yang, Mengrui Shi, Qiang Zhang  

**一句话要点**：提出MTGNet以解决少样本语义分割中文本先验不足和跨模态交互弱的问题

**关键词**：少样本语义分割, 跨模态交互, 多文本引导, 视觉先验优化, 语义一致性

## 3 点简述
- 核心问题：单文本提示无法覆盖复杂类别语义多样性，导致目标区域激活不完整和噪声干扰
- 方法要点：设计多文本先验精炼和文本锚点特征融合模块，增强跨模态交互和语义一致性
- 实验或效果：在PASCAL-5i和COCO-20i基准上取得高mIoU，显著提升类内变化大的场景

## 摘要（原文）

> Recent CLIP-based few-shot semantic segmentation methods introduce class-level textual priors to assist segmentation by typically using a single prompt (e.g., a photo of class). However, these approaches often result in incomplete activation of target regions, as a single textual description cannot fully capture the semantic diversity of complex categories. Moreover, they lack explicit cross-modal interaction and are vulnerable to noisy support features, further degrading visual prior quality. To address these issues, we propose the Multi-Text Guided Few-Shot Semantic Segmentation Network (MTGNet), a dual-branch framework that enhances segmentation performance by fusing diverse textual prompts to refine textual priors and guide the cross-modal optimization of visual priors. Specifically, we design a Multi-Textual Prior Refinement (MTPR) module that suppresses interference and aggregates complementary semantic cues to enhance foreground activation and expand semantic coverage for structurally complex objects. We introduce a Text Anchor Feature Fusion (TAFF) module, which leverages multi-text embeddings as semantic anchors to facilitate the transfer of discriminative local prototypes from support images to query images, thereby improving semantic consistency and alleviating intra-class variations. Furthermore, a Foreground Confidence-Weighted Attention (FCWA) module is presented to enhance visual prior robustness by leveraging internal self-similarity within support foreground features. It adaptively down-weights inconsistent regions and effectively suppresses interference in the query segmentation process. Extensive experiments on standard FSS benchmarks validate the effectiveness of MTGNet. In the 1-shot setting, it achieves 76.8% mIoU on PASCAL-5i and 57.4% on COCO-20i, with notable improvements in folds exhibiting high intra-class variations.

