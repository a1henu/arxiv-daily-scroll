---
layout: default
title: Detecting Structural Heart Disease from Electrocardiograms via a Generalized Additive Model of Interpretable Foundation-Model Predictors
---

# Detecting Structural Heart Disease from Electrocardiograms via a Generalized Additive Model of Interpretable Foundation-Model Predictors
**arXiv**：[2603.02616v1](https://arxiv.org/abs/2603.02616) · [PDF](https://arxiv.org/pdf/2603.02616.pdf)  
**作者**：Ya Zhou, Zhaohong Sun, Tianxiang Hao, Xiangjie Li  

**一句话要点**：提出基于可解释基础模型预测器的广义可加模型，用于从心电图检测结构性心脏病。

**关键词**：结构性心脏病检测, 心电图分析, 可解释人工智能, 广义可加模型, 基础模型预测器

## 3 点简述
- 核心问题：现有AI心电图分析模型为黑箱，缺乏可解释性，限制临床采用。
- 方法要点：整合临床有意义的心电图基础模型预测器至广义可加模型，实现透明风险归因。
- 实验或效果：在超8万对数据上，AUROC、AUPRC和F1分数相对提升约1%，训练数据仅需30%时性能略优。

## 摘要（原文）

> Structural heart disease (SHD) is a prevalent condition with many undiagnosed cases, and early detection is often limited by the high cost and accessibility constraints of echocardiography (ECHO). Recent studies show that artificial intelligence (AI)-based analysis of electrocardiograms (ECGs) can detect SHD, offering a scalable alternative. However, existing methods are fully black-box models, limiting interpretability and clinical adoption. To address these challenges, we propose an interpretable and effective framework that integrates clinically meaningful ECG foundation-model predictors within a generalized additive model, enabling transparent risk attribution while maintaining strong predictive performance. Using the EchoNext benchmark of over 80,000 ECG-ECHO pairs, the method demonstrates relative improvements of +0.98% in AUROC, +1.01% in AUPRC, and +1.41% in F1 score over the latest state-of-the-art deep-learning baseline, while achieving slightly better performance even with only 30% of the training data. Subgroup analyses confirm robust performance across heterogeneous populations, and the estimated entry-wise functions provide interpretable insights into the relationships between risks of traditional ECG diagnoses and SHD. This work illustrates a complementary paradigm between classical statistical modeling and modern AI, offering a pathway to interpretable, high-performing, and clinically actionable ECG-based SHD screening.

