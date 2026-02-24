---
layout: default
title: Tri-Subspaces Disentanglement for Multimodal Sentiment Analysis
---

# Tri-Subspaces Disentanglement for Multimodal Sentiment Analysis
**arXiv**：[2602.19585v1](https://arxiv.org/abs/2602.19585) · [PDF](https://arxiv.org/pdf/2602.19585.pdf)  
**作者**：Chunlei Meng, Jiabin Luo, Zhenglin Yan, Zhenyu Yu, Rong Fu, Zhongxue Gan, Chun Ouyang  

**一句话要点**：提出Tri-Subspace Disentanglement框架，通过三子空间解耦增强多模态情感分析表示能力。

**关键词**：多模态情感分析, 特征解耦, 子空间建模, 跨模态融合, 结构化正则化, 意图识别

## 3 点简述
- 问题：现有方法忽略仅部分模态共享的信号，限制多模态表示的表达力和判别力。
- 方法：将特征分解为全局共享、子模态共享和私有三子空间，引入解耦监督和结构化正则化保持独立性。
- 效果：在CMU-MOSI和CMU-MOSEI数据集上达到SOTA性能，并通过消融研究验证三子空间解耦与SACA模块的有效性。

## 摘要（原文）

> Multimodal Sentiment Analysis (MSA) integrates language, visual, and acoustic modalities to infer human sentiment. Most existing methods either focus on globally shared representations or modality-specific features, while overlooking signals that are shared only by certain modality pairs. This limits the expressiveness and discriminative power of multimodal representations. To address this limitation, we propose a Tri-Subspace Disentanglement (TSD) framework that explicitly factorizes features into three complementary subspaces: a common subspace capturing global consistency, submodally-shared subspaces modeling pairwise cross-modal synergies, and private subspaces preserving modality-specific cues. To keep these subspaces pure and independent, we introduce a decoupling supervisor together with structured regularization losses. We further design a Subspace-Aware Cross-Attention (SACA) fusion module that adaptively models and integrates information from the three subspaces to obtain richer and more robust representations. Experiments on CMU-MOSI and CMU-MOSEI demonstrate that TSD achieves state-of-the-art performance across all key metrics, reaching 0.691 MAE on CMU-MOSI and 54.9% ACC-7 on CMU-MOSEI, and also transfers well to multimodal intent recognition tasks. Ablation studies confirm that tri-subspace disentanglement and SACA jointly enhance the modeling of multi-granular cross-modal sentiment cues.

