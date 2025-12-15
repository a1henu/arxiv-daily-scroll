---
layout: default
title: Back to the Baseline: Examining Baseline Effects on Explainability Metrics
---

# Back to the Baseline: Examining Baseline Effects on Explainability Metrics
**arXiv**：[2512.11433v1](https://arxiv.org/abs/2512.11433) · [PDF](https://arxiv.org/pdf/2512.11433.pdf)  
**作者**：Agustin Martin Picard, Thibaut Boissin, Varshini Subhash, Rémi Cadène, Thomas Fel  

**一句话要点**：提出模型依赖基线以解决可解释性评估中基线选择偏差问题

**关键词**：可解释人工智能, 归因方法, 基线选择, 评估指标, 特征可视化

## 3 点简述
- 揭示基线选择对归因方法评估的偏差影响，导致不同基线得出矛盾最优方法
- 提出基线应具备移除信息且不过度偏离分布的双重属性，但现有基线存在权衡
- 引入基于特征可视化的模型依赖基线，在移除信息与分布偏移间取得更好平衡

## 摘要（原文）

> Attribution methods are among the most prevalent techniques in Explainable Artificial Intelligence (XAI) and are usually evaluated and compared using Fidelity metrics, with Insertion and Deletion being the most popular. These metrics rely on a baseline function to alter the pixels of the input image that the attribution map deems most important. In this work, we highlight a critical problem with these metrics: the choice of a given baseline will inevitably favour certain attribution methods over others. More concerningly, even a simple linear model with commonly used baselines contradicts itself by designating different optimal methods. A question then arises: which baseline should we use? We propose to study this problem through two desirable properties of a baseline: (i) that it removes information and (ii) that it does not produce overly out-of-distribution (OOD) images. We first show that none of the tested baselines satisfy both criteria, and there appears to be a trade-off among current baselines: either they remove information or they produce a sequence of OOD images. Finally, we introduce a novel baseline by leveraging recent work in feature visualisation to artificially produce a model-dependent baseline that removes information without being overly OOD, thus improving on the trade-off when compared to other existing baselines. Our code is available at https://github.com/deel-ai-papers/Back-to-the-Baseline

