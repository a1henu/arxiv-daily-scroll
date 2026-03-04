---
layout: default
title: SGMA: Semantic-Guided Modality-Aware Segmentation for Remote Sensing with Incomplete Multimodal Data
---

# SGMA: Semantic-Guided Modality-Aware Segmentation for Remote Sensing with Incomplete Multimodal Data
**arXiv**：[2603.02505v1](https://arxiv.org/abs/2603.02505) · [PDF](https://arxiv.org/pdf/2603.02505.pdf)  
**作者**：Lekang Wen, Liang Liao, Jing Xiao, Mi Wang  

**一句话要点**：提出SGMA框架以解决遥感多模态语义分割中的模态缺失问题

**关键词**：遥感语义分割, 多模态学习, 模态缺失处理, 语义引导融合, 模态感知采样, 类内变化减少

## 3 点简述
- 核心问题：遥感多模态语义分割面临模态缺失、模态不平衡、类内变化和跨模态异质性挑战
- 方法要点：SGMA通过语义引导融合和模态感知采样模块，平衡多模态学习并减少不一致性
- 实验或效果：在多个数据集和骨干网络上验证，SGMA优于现有方法，尤其在脆弱模态上提升显著

## 摘要（原文）

> Multimodal semantic segmentation integrates complementary information from diverse sensors for remote sensing Earth observation. However, practical systems often encounter missing modalities due to sensor failures or incomplete coverage, termed Incomplete Multimodal Semantic Segmentation (IMSS). IMSS faces three key challenges: (1) multimodal imbalance, where dominant modalities suppress fragile ones; (2) intra-class variation in scale, shape, and orientation across modalities; and (3) cross-modal heterogeneity with conflicting cues producing inconsistent semantic responses. Existing methods rely on contrastive learning or joint optimization, which risk over-alignment, discarding modality-specific cues or imbalanced training, favoring robust modalities, while largely overlooking intra-class variation and cross-modal heterogeneity. To address these limitations, we propose the Semantic-Guided Modality-Aware (SGMA) framework, which ensures balanced multimodal learning while reducing intra-class variation and reconciling cross-modal inconsistencies through semantic guidance. SGMA introduces two complementary plug-and-play modules: (1) Semantic-Guided Fusion (SGF) module extracts multi-scale, class-wise semantic prototypes that capture consistent categorical representations across modalities, estimates per-modality robustness based on prototype-feature alignment, and performs adaptive fusion weighted by robustness scores to mitigate intra-class variation and cross-modal heterogeneity; (2) Modality-Aware Sampling (MAS) module leverages robustness estimations from SGF to dynamically reweight training samples, prioritizing challenging samples from fragile modalities to address modality imbalance. Extensive experiments across multiple datasets and backbones demonstrate that SGMA consistently outperforms state-of-the-art methods, with particularly significant improvements in fragile modalities.

