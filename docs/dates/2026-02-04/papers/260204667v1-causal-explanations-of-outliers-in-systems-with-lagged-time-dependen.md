---
layout: default
title: Causal explanations of outliers in systems with lagged time-dependencies
---

# Causal explanations of outliers in systems with lagged time-dependencies
**arXiv**：[2602.04667v1](https://arxiv.org/abs/2602.04667) · [PDF](https://arxiv.org/pdf/2602.04667.pdf)  
**作者**：Philipp Alexander Schwarz, Johannes Oberpriller, Sven Klaassen  

**一句话要点**：扩展因果根因分析方法以处理具有滞后时间依赖性的系统

**关键词**：因果根因分析, 时间依赖系统, 滞后效应, 能源系统, 截断方法

## 3 点简述
- 针对具有瞬时和延迟效应的系统（如能源系统）的根因分析挑战
- 提出两种截断方法处理无限依赖图，保持或近似因果机制
- 在工厂能源管理场景中验证方法能定位特征和时间域根因

## 摘要（原文）

> Root-cause analysis in controlled time dependent systems poses a major challenge in applications. Especially energy systems are difficult to handle as they exhibit instantaneous as well as delayed effects and if equipped with storage, do have a memory. In this paper we adapt the causal root-cause analysis method of Budhathoki et al. [2022] to general time-dependent systems, as it can be regarded as a strictly causal definition of the term "root-cause". Particularly, we discuss two truncation approaches to handle the infinite dependency graphs present in time-dependent systems. While one leaves the causal mechanisms intact, the other approximates the mechanisms at the start nodes. The effectiveness of the different approaches is benchmarked using a challenging data generation process inspired by a problem in factory energy management: the avoidance of peaks in the power consumption. We show that given enough lags our extension is able to localize the root-causes in the feature and time domain. Further the effect of mechanism approximation is discussed.

