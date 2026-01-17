---
layout: default
title: Adjusted Similarity Measures and a Violation of Expectations
---

# Adjusted Similarity Measures and a Violation of Expectations
**arXiv**：[2601.10641v1](https://arxiv.org/abs/2601.10641) · [PDF](https://arxiv.org/pdf/2601.10641.pdf)  
**作者**：William L. Lippitt, Edward J. Bedrick, Nichole E. Carlson  

**一句话要点**：研究调整相似性度量的通用化与充分条件，以解决期望属性违反问题

**关键词**：调整相似性度量, 零模型, 统计标准化, 期望属性, 聚类比较, 度量评估

## 3 点简述
- 核心问题：调整相似性度量在通用零模型下可能违反期望属性，如均值非零或确定性为零
- 方法要点：推广调整算子至通用零模型和统计标准化，并识别确保期望属性的充分条件
- 实验或效果：展示违反条件可导致度量崩溃，如传统调整产生非正值或统计标准化下确定性为零

## 摘要（原文）

> Adjusted similarity measures, such as Cohen's kappa for inter-rater reliability and the adjusted Rand index used to compare clustering algorithms, are a vital tool for comparing discrete labellings. These measures are intended to have the property of 0 expectation under a null distribution and maximum value 1 under maximal similarity to aid in interpretation. Measures are frequently adjusted with respect to the permutation distribution for historic and analytic reasons. There is currently renewed interest in considering other null models more appropriate for context, such as clustering ensembles permitting a random number of identified clusters. The purpose of this work is two -- fold: (1) to generalize the study of the adjustment operator to general null models and to a more general procedure which includes statistical standardization as a special case and (2) to identify sufficient conditions for the adjustment operator to produce the intended properties, where sufficient conditions are related to whether and how observed data are incorporated into null distributions. We demonstrate how violations of the sufficient conditions may lead to substantial breakdown, such as by producing a non-positive measure under traditional adjustment rather than one with mean 0, or by producing a measure which is deterministically 0 under statistical standardization.

