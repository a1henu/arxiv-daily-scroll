---
layout: default
title: ExpAlign: Expectation-Guided Vision-Language Alignment for Open-Vocabulary Grounding
---

# ExpAlign: Expectation-Guided Vision-Language Alignment for Open-Vocabulary Grounding
**arXiv**：[2601.22666v1](https://arxiv.org/abs/2601.22666) · [PDF](https://arxiv.org/pdf/2601.22666.pdf)  
**作者**：Junyi Hu, Tian Bai, Fengyi Wu, Wenyan Li, Zhenming Peng, Yi Zhang  

**一句话要点**：提出ExpAlign框架，通过期望对齐头和多尺度一致性正则化解决开放词汇定位中的弱监督视觉语言对齐问题。

**关键词**：开放词汇定位, 视觉语言对齐, 多实例学习, 弱监督学习, 长尾类别检测, 零样本实例分割

## 3 点简述
- 核心问题：开放词汇定位需在弱监督下实现细粒度视觉语言对齐，现有方法依赖全局嵌入或需显式监督。
- 方法要点：基于多实例学习，引入期望对齐头进行软MIL池化，并设计能量多尺度一致性正则化以稳定学习。
- 实验或效果：在LVIS等数据集上提升检测和分割性能，尤其在长尾类别，保持轻量高效。

## 摘要（原文）

> Open-vocabulary grounding requires accurate vision-language alignment under weak supervision, yet existing methods either rely on global sentence embeddings that lack fine-grained expressiveness or introduce token-level alignment with explicit supervision or heavy cross-attention designs. We propose ExpAlign, a theoretically grounded vision-language alignment framework built on a principled multiple instance learning formulation. ExpAlign introduces an Expectation Alignment Head that performs attention-based soft MIL pooling over token-region similarities, enabling implicit token and instance selection without additional annotations. To further stabilize alignment learning, we develop an energy-based multi-scale consistency regularization scheme, including a Top-K multi-positive contrastive objective and a Geometry-Aware Consistency Objective derived from a Lagrangian-constrained free-energy minimization. Extensive experiments show that ExpAlign consistently improves open-vocabulary detection and zero-shot instance segmentation, particularly on long-tail categories. Most notably, it achieves 36.2 AP$_r$ on the LVIS minival split, outperforming other state-of-the-art methods at comparable model scale, while remaining lightweight and inference-efficient.

