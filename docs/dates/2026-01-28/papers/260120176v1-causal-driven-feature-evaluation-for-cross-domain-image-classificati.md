---
layout: default
title: Causal-Driven Feature Evaluation for Cross-Domain Image Classification
---

# Causal-Driven Feature Evaluation for Cross-Domain Image Classification
**arXiv**：[2601.20176v1](https://arxiv.org/abs/2601.20176) · [PDF](https://arxiv.org/pdf/2601.20176.pdf)  
**作者**：Chen Cheng, Ang Li  

**一句话要点**：提出因果驱动特征评估框架以提升跨域图像分类的分布外泛化能力

**关键词**：跨域图像分类, 分布外泛化, 因果评估, 特征有效性, 域偏移, 鲁棒泛化

## 3 点简述
- 核心问题：分布外泛化中，跨域不变特征未必因果有效，导致现有方法不可靠
- 方法要点：从因果视角评估特征的必要性和充分性，直接测量跨域因果有效性
- 实验或效果：在多域基准测试中，尤其在挑战性域偏移下，OOD性能持续提升

## 摘要（原文）

> Out-of-distribution (OOD) generalization remains a fundamental challenge in real-world classification, where test distributions often differ substantially from training data. Most existing approaches pursue domain-invariant representations, implicitly assuming that invariance implies reliability. However, features that are invariant across domains are not necessarily causally effective for prediction.
>   In this work, we revisit OOD classification from a causal perspective and propose to evaluate learned representations based on their necessity and sufficiency under distribution shift. We introduce an explicit segment-level framework that directly measures causal effectiveness across domains, providing a more faithful criterion than invariance alone.
>   Experiments on multi-domain benchmarks demonstrate consistent improvements in OOD performance, particularly under challenging domain shifts, highlighting the value of causal evaluation for robust generalization.

