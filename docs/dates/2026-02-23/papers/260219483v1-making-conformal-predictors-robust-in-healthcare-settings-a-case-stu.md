---
layout: default
title: Making Conformal Predictors Robust in Healthcare Settings: a Case Study on EEG Classification
---

# Making Conformal Predictors Robust in Healthcare Settings: a Case Study on EEG Classification
**arXiv**：[2602.19483v1](https://arxiv.org/abs/2602.19483) · [PDF](https://arxiv.org/pdf/2602.19483.pdf)  
**作者**：Arjun Chatterjee, Sayeed Sajjad Razin, John Wu, Siddhartha Laghuvarapu, Jathurshan Pradeepkumar, Jimeng Sun  

**一句话要点**：提出个性化校准策略以提升脑电图分类中保形预测的鲁棒性

**关键词**：保形预测, 脑电图分类, 分布偏移, 不确定性量化, 个性化校准, 医疗人工智能

## 3 点简述
- 核心问题：患者分布偏移违反标准保形预测的独立同分布假设，导致医疗场景下覆盖率下降
- 方法要点：评估多种保形预测方法，并引入个性化校准策略以应对分布偏移
- 实验或效果：在脑电图癫痫分类任务中，个性化校准使覆盖率提升超过20个百分点，同时保持预测集大小可比

## 摘要（原文）

> Quantifying uncertainty in clinical predictions is critical for high-stakes diagnosis tasks. Conformal prediction offers a principled approach by providing prediction sets with theoretical coverage guarantees. However, in practice, patient distribution shifts violate the i.i.d. assumptions underlying standard conformal methods, leading to poor coverage in healthcare settings. In this work, we evaluate several conformal prediction approaches on EEG seizure classification, a task with known distribution shift challenges and label uncertainty. We demonstrate that personalized calibration strategies can improve coverage by over 20 percentage points while maintaining comparable prediction set sizes. Our implementation is available via PyHealth, an open-source healthcare AI framework: https://github.com/sunlabuiuc/PyHealth.

