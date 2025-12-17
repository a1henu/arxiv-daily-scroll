---
layout: default
title: Weighted Conformal Prediction Provides Adaptive and Valid Mask-Conditional Coverage for General Missing Data Mechanisms
---

# Weighted Conformal Prediction Provides Adaptive and Valid Mask-Conditional Coverage for General Missing Data Mechanisms
**arXiv**：[2512.14221v1](https://arxiv.org/abs/2512.14221) · [PDF](https://arxiv.org/pdf/2512.14221.pdf)  
**作者**：Jiarong Fan, Juhyun Park. Thi Phuong Thuy Vo, Nicolas Brunel  

**一句话要点**：提出加权共形预测框架，为一般缺失数据机制提供自适应且有效的掩码条件覆盖

**关键词**：共形预测, 缺失数据处理, 不确定性量化, 掩码条件覆盖, 重加权方法, 插补校正

## 3 点简述
- 核心问题：共形预测在缺失协变量下无法保证覆盖，掩码条件有效性优于边际覆盖
- 方法要点：采用预插补-掩码-校正框架，通过重加权共形预测校正预测集，兼容标准插补流程
- 实验或效果：在合成和真实数据集上评估，显著减少预测区间宽度，同时保持目标保证

## 摘要（原文）

> Conformal prediction (CP) offers a principled framework for uncertainty quantification, but it fails to guarantee coverage when faced with missing covariates. In addressing the heterogeneity induced by various missing patterns, Mask-Conditional Valid (MCV) Coverage has emerged as a more desirable property than Marginal Coverage. In this work, we adapt split CP to handle missing values by proposing a preimpute-mask-then-correct framework that can offer valid coverage. We show that our method provides guaranteed Marginal Coverage and Mask-Conditional Validity for general missing data mechanisms. A key component of our approach is a reweighted conformal prediction procedure that corrects the prediction sets after distributional imputation (multiple imputation) of the calibration dataset, making our method compatible with standard imputation pipelines. We derive two algorithms, and we show that they are approximately marginally valid and MCV. We evaluate them on synthetic and real-world datasets. It reduces significantly the width of prediction intervals w.r.t standard MCV methods, while maintaining the target guarantees.

