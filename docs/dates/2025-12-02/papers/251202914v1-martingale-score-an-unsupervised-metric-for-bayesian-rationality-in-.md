---
layout: default
title: Martingale Score: An Unsupervised Metric for Bayesian Rationality in LLM Reasoning
---

# Martingale Score: An Unsupervised Metric for Bayesian Rationality in LLM Reasoning
**arXiv**：[2512.02914v1](https://arxiv.org/abs/2512.02914) · [PDF](https://arxiv.org/pdf/2512.02914.pdf)  
**作者**：Zhonghao He, Tianyi Qiu, Hirokazu Shirado, Maarten Sap  

**一句话要点**：提出无监督的鞅分数以评估大语言模型推理中的贝叶斯理性偏差

**关键词**：大语言模型推理, 信念固化, 贝叶斯理性, 无监督评估, 鞅性质, 回归分析

## 3 点简述
- 核心问题：迭代推理可能导致信念固化而非真相寻求，需系统评估。
- 方法要点：基于鞅性质，通过回归方法计算无监督的鞅分数来衡量偏差。
- 实验或效果：在多个开放域中发现偏差普遍，鞅分数可预测真实准确性。

## 摘要（原文）

> Recent advances in reasoning techniques have substantially improved the performance of large language models (LLMs), raising expectations for their ability to provide accurate, truthful, and reliable information. However, emerging evidence suggests that iterative reasoning may foster belief entrenchment and confirmation bias, rather than enhancing truth-seeking behavior. In this study, we propose a systematic evaluation framework for belief entrenchment in LLM reasoning by leveraging the Martingale property from Bayesian statistics. This property implies that, under rational belief updating, the expected value of future beliefs should remain equal to the current belief, i.e., belief updates are unpredictable from the current belief. We propose the unsupervised, regression-based Martingale Score to measure violations of this property, which signal deviation from the Bayesian ability of updating on new evidence. In open-ended problem domains including event forecasting, value-laden questions, and academic paper review, we find such violations to be widespread across models and setups, where the current belief positively predicts future belief updates, a phenomenon which we term belief entrenchment. We identify the models, reasoning techniques, and domains more prone to belief entrenchment. Finally, we validate the Martingale Score by showing that it predicts ground-truth accuracy on problem domains where ground truth labels are available. This indicates that, while designed as an unsupervised metric that operates even in domains without access to ground truth, the Martingale Score is a useful proxy of the truth-seeking ability of a reasoning process.

