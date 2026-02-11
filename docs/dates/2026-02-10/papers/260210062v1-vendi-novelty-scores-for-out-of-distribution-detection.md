---
layout: default
title: Vendi Novelty Scores for Out-of-Distribution Detection
---

# Vendi Novelty Scores for Out-of-Distribution Detection
**arXiv**：[2602.10062v1](https://arxiv.org/abs/2602.10062) · [PDF](https://arxiv.org/pdf/2602.10062.pdf)  
**作者**：Amey P. Pasarkar, Adji Bousso Dieng  

**一句话要点**：提出Vendi Novelty Score，基于多样性视角解决分布外检测问题。

**关键词**：分布外检测, 多样性度量, 非参数方法, 图像分类, 特征空间, 线性时间算法

## 3 点简述
- 核心问题：现有分布外检测方法依赖置信度或似然估计，受限于分布假设。
- 方法要点：利用Vendi Scores量化测试样本对特征集多样性的增加，无需密度建模。
- 实验或效果：在图像分类基准上实现最优性能，仅需1%训练数据保持效果。

## 摘要（原文）

> Out-of-distribution (OOD) detection is critical for the safe deployment of machine learning systems. Existing post-hoc detectors typically rely on model confidence scores or likelihood estimates in feature space, often under restrictive distributional assumptions. In this work, we introduce a third paradigm and formulate OOD detection from a diversity perspective. We propose the Vendi Novelty Score (VNS), an OOD detector based on the Vendi Scores (VS), a family of similarity-based diversity metrics. VNS quantifies how much a test sample increases the VS of the in-distribution feature set, providing a principled notion of novelty that does not require density modeling. VNS is linear-time, non-parametric, and naturally combines class-conditional (local) and dataset-level (global) novelty signals. Across multiple image classification benchmarks and network architectures, VNS achieves state-of-the-art OOD detection performance. Remarkably, VNS retains this performance when computed using only 1% of the training data, enabling deployment in memory- or access-constrained settings.

