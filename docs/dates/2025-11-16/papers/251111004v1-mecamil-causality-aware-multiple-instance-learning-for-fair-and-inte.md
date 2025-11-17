---
layout: default
title: MeCaMIL: Causality-Aware Multiple Instance Learning for Fair and Interpretable Whole Slide Image Diagnosis
---

# MeCaMIL: Causality-Aware Multiple Instance Learning for Fair and Interpretable Whole Slide Image Diagnosis
**arXiv**：[2511.11004v1](https://arxiv.org/abs/2511.11004) · [PDF](https://arxiv.org/pdf/2511.11004.pdf)  
**作者**：Yiran Song, Yikai Zhang, Shuang Zhou, Guojun Xiong, Xiaofeng Yang, Nian Wang, Fenglong Ma, Rui Zhang, Mingquan Lin  

**一句话要点**：提出MeCaMIL因果感知多示例学习框架，解决全切片图像诊断中的公平性和可解释性问题

**关键词**：多示例学习, 因果推断, 全切片图像分析, 公平性, 可解释AI, 数字病理学

## 3 点简述
- 现有MIL方法缺乏因果可解释性，且未整合人口统计学数据，导致公平性问题
- MeCaMIL通过结构化因果图建模人口统计学混杂因素，使用因果推断分离疾病信号
- 在多个基准测试中实现高精度和公平性，公平性方差平均降低超65%

## 摘要（原文）

> Multiple instance learning (MIL) has emerged as the dominant paradigm for whole slide image (WSI) analysis in computational pathology, achieving strong diagnostic performance through patch-level feature aggregation. However, existing MIL methods face critical limitations: (1) they rely on attention mechanisms that lack causal interpretability, and (2) they fail to integrate patient demographics (age, gender, race), leading to fairness concerns across diverse populations. These shortcomings hinder clinical translation, where algorithmic bias can exacerbate health disparities. We introduce \textbf{MeCaMIL}, a causality-aware MIL framework that explicitly models demographic confounders through structured causal graphs. Unlike prior approaches treating demographics as auxiliary features, MeCaMIL employs principled causal inference -- leveraging do-calculus and collider structures -- to disentangle disease-relevant signals from spurious demographic correlations. Extensive evaluation on three benchmarks demonstrates state-of-the-art performance across CAMELYON16 (ACC/AUC/F1: 0.939/0.983/0.946), TCGA-Lung (0.935/0.979/0.931), and TCGA-Multi (0.977/0.993/0.970, five cancer types). Critically, MeCaMIL achieves superior fairness -- demographic disparity variance drops by over 65% relative reduction on average across attributes, with notable improvements for underserved populations. The framework generalizes to survival prediction (mean C-index: 0.653, +0.017 over best baseline across five cancer types). Ablation studies confirm causal graph structure is essential -- alternative designs yield 0.048 lower accuracy and 4.2x times worse fairness. These results establish MeCaMIL as a principled framework for fair, interpretable, and clinically actionable AI in digital pathology. Code will be released upon acceptance.

