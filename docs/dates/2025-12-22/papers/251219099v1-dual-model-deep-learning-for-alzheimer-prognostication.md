---
layout: default
title: Dual Model Deep Learning for Alzheimer Prognostication
---

# Dual Model Deep Learning for Alzheimer Prognostication
**arXiv**：[2512.19099v1](https://arxiv.org/abs/2512.19099) · [PDF](https://arxiv.org/pdf/2512.19099.pdf)  
**作者**：Alireza Moayedikia, Sara Fin, Uffe Kock Wiil  

**一句话要点**：提出PROGRESS双模型深度学习框架，基于单次脑脊液生物标志物评估预测阿尔茨海默病进展，支持首次就诊决策。

**关键词**：阿尔茨海默病预测, 深度学习框架, 生存分析, 不确定性量化, 脑脊液生物标志物, 临床决策支持

## 3 点简述
- 核心问题：阿尔茨海默病治疗需精准时机，但现有模型依赖纵向数据且无不确定性量化，不适用于首次就诊决策。
- 方法要点：PROGRESS框架包含概率轨迹网络预测认知衰退（带校准不确定性）和深度生存模型估计轻度认知障碍向痴呆转化时间。
- 实验或效果：在NACC数据库超3000名参与者数据上，PROGRESS在生存预测上显著优于传统方法，风险分层识别转化率七倍差异组，留一中心验证显示强泛化性。

## 摘要（原文）

> Disease modifying therapies for Alzheimer's disease demand precise timing decisions, yet current predictive models require longitudinal observations and provide no uncertainty quantification, rendering them impractical at the critical first visit when treatment decisions must be made. We developed PROGRESS (PRognostic Generalization from REsting Static Signatures), a dual-model deep learning framework that transforms a single baseline cerebrospinal fluid biomarker assessment into actionable prognostic estimates without requiring prior clinical history. The framework addresses two complementary clinical questions: a probabilistic trajectory network predicts individualized cognitive decline with calibrated uncertainty bounds achieving near-nominal coverage, enabling honest prognostic communication; and a deep survival model estimates time to conversion from mild cognitive impairment to dementia. Using data from over 3,000 participants across 43 Alzheimer's Disease Research Centers in the National Alzheimer's Coordinating Center database, PROGRESS substantially outperforms Cox proportional hazards, Random Survival Forests, and gradient boosting methods for survival prediction. Risk stratification identifies patient groups with seven-fold differences in conversion rates, enabling clinically meaningful treatment prioritization. Leave-one-center-out validation demonstrates robust generalizability, with survival discrimination remaining strong across held-out sites despite heterogeneous measurement conditions spanning four decades of assay technologies. By combining superior survival prediction with trustworthy trajectory uncertainty quantification, PROGRESS bridges the gap between biomarker measurement and personalized clinical decision-making.

