---
layout: default
title: Probabilistic Label Spreading: Efficient and Consistent Estimation of Soft Labels with Epistemic Uncertainty on Graphs
---

# Probabilistic Label Spreading: Efficient and Consistent Estimation of Soft Labels with Epistemic Uncertainty on Graphs
**arXiv**：[2602.04574v1](https://arxiv.org/abs/2602.04574) · [PDF](https://arxiv.org/pdf/2602.04574.pdf)  
**作者**：Jonathan Klees, Tobias Riedlinger, Peter Stehr, Bennet Böddecker, Daniel Kondermann, Matthias Rottmann  

**一句话要点**：提出概率标签传播方法，以高效估计图数据中标签的认知不确定性，减少标注成本。

**关键词**：概率标签传播, 认知不确定性估计, 图扩散方法, 标注效率提升, 数据中心图像分类

## 3 点简述
- 核心问题：感知任务中高质量标注数据稀缺，且标注存在认知和随机不确定性，通常被忽略。
- 方法要点：基于图扩散传播单标注，假设特征空间标签平滑性，证明方法在标注数趋零时仍提供一致概率估计。
- 实验或效果：在常见图像数据集上显著降低标注预算，在Data-Centric Image Classification基准上达到新最优性能。

## 摘要（原文）

> Safe artificial intelligence for perception tasks remains a major challenge, partly due to the lack of data with high-quality labels. Annotations themselves are subject to aleatoric and epistemic uncertainty, which is typically ignored during annotation and evaluation. While crowdsourcing enables collecting multiple annotations per image to estimate these uncertainties, this approach is impractical at scale due to the required annotation effort. We introduce a probabilistic label spreading method that provides reliable estimates of aleatoric and epistemic uncertainty of labels. Assuming label smoothness over the feature space, we propagate single annotations using a graph-based diffusion method. We prove that label spreading yields consistent probability estimators even when the number of annotations per data point converges to zero. We present and analyze a scalable implementation of our method. Experimental results indicate that, compared to baselines, our approach substantially reduces the annotation budget required to achieve a desired label quality on common image datasets and achieves a new state of the art on the Data-Centric Image Classification benchmark.

