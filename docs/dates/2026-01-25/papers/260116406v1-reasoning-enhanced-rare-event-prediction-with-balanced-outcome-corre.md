---
layout: default
title: Reasoning-Enhanced Rare-Event Prediction with Balanced Outcome Correction
---

# Reasoning-Enhanced Rare-Event Prediction with Balanced Outcome Correction
**arXiv**：[2601.16406v1](https://arxiv.org/abs/2601.16406) · [PDF](https://arxiv.org/pdf/2601.16406.pdf)  
**作者**：Vitaly Bulgakov, Alexander Turchin  

**一句话要点**：提出LPCORP框架，结合推理增强预测与置信度校正，解决稀有事件预测中的类别不平衡问题。

**关键词**：稀有事件预测, 类别不平衡, 推理增强, 置信度校正, 成本分析

## 3 点简述
- 核心问题：稀有事件预测中极端类别不平衡导致模型偏向多数类，影响召回率、校准和实用性。
- 方法要点：两阶段框架，先通过推理模型从叙事输入生成增强预测，再用逻辑回归分类器基于置信度选择性校正输出。
- 实验或效果：在医疗和消费服务数据集上评估，显著提升性能，特别是精确度，并实现成本降低超过50%。

## 摘要（原文）

> Rare-event prediction is critical in domains such as healthcare, finance, reliability engineering, customer support, aviation safety, where positive outcomes are infrequent yet potentially catastrophic. Extreme class imbalance biases conventional models toward majority-class predictions, limiting recall, calibration, and operational usefulness. We propose LPCORP (Low-Prevalence CORrector for Prediction)*, a two-stage framework that combines reasoningenhanced prediction with confidence-based outcome correction. A reasoning model first produces enriched predictions from narrative inputs, after which a lightweight logistic-regression classifier evaluates and selectively corrects these outputs to mitigate prevalence-driven bias. We evaluate LPCORP on real-world datasets from medical and consumer service domains. The results show that this method transforms a highly imbalanced setting into a well-balanced one while preserving the original number of samples and without applying any resampling strategies. Test-set evaluation demonstrates substantially improved performance, particularly in precision, which is a known weakness in low-prevalence data. We further provide a costreduction analysis comparing the expenses associated with rare-event damage control without preventive measures to those incurred when low-cost, prediction-based preventive interventions are applied that showed more than 50% reduction in some cases. * Patent pending: U.S. Provisional 63/933,518, filed 8 December 2025.

