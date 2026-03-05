---
layout: default
title: From Misclassifications to Outliers: Joint Reliability Assessment in Classification
---

# From Misclassifications to Outliers: Joint Reliability Assessment in Classification
**arXiv**：[2603.03903v1](https://arxiv.org/abs/2603.03903) · [PDF](https://arxiv.org/pdf/2603.03903.pdf)  
**作者**：Yang Li, Youyang Sha, Yinzhi Wang, Timothy Hospedales, Xi Shen, Shell Xu Hu, Xuanlong Yu  

**一句话要点**：提出联合评估框架与SURE+方法以提升分类器在分布内外样本的可靠性

**关键词**：可靠性评估, OOD检测, 失败预测, 双评分函数, 分类器鲁棒性, 机器学习部署

## 3 点简述
- 核心问题：传统方法将OOD检测与失败预测分离，忽略其紧密联系，影响分类器可靠性
- 方法要点：引入统一评估框架，使用双评分函数和新指标DS-F1/DS-AURC，并扩展SURE为SURE+方法
- 实验或效果：在OpenOOD基准上，双评分函数显著提升可靠性，SURE+在多种场景下表现优异

## 摘要（原文）

> Building reliable classifiers is a fundamental challenge for deploying machine learning in real-world applications. A reliable system should not only detect out-of-distribution (OOD) inputs but also anticipate in-distribution (ID) errors by assigning low confidence to potentially misclassified samples. Yet, most prior work treats OOD detection and failure prediction as separated problems, overlooking their closed connection. We argue that reliability requires evaluating them jointly. To this end, we propose a unified evaluation framework that integrates OOD detection and failure prediction, quantified by our new metrics DS-F1 and DS-AURC, where DS denotes double scoring functions. Experiments on the OpenOOD benchmark show that double scoring functions yield classifiers that are substantially more reliable than traditional single scoring approaches. Our analysis further reveals that OOD-based approaches provide notable gains under simple or far-OOD shifts, but only marginal benefits under more challenging near-OOD conditions. Beyond evaluation, we extend the reliable classifier SURE and introduce SURE+, a new approach that significantly improves reliability across diverse scenarios. Together, our framework, metrics, and method establish a new benchmark for trustworthy classification and offer practical guidance for deploying robust models in real-world settings. The source code is publicly available at https://github.com/Intellindust-AI-Lab/SUREPlus.

