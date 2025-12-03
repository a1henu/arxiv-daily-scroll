---
layout: default
title: COPE: Chain-Of-Thought Prediction Engine for Open-Source Large Language Model Based Stroke Outcome Prediction from Clinical Notes
---

# COPE: Chain-Of-Thought Prediction Engine for Open-Source Large Language Model Based Stroke Outcome Prediction from Clinical Notes
**arXiv**：[2512.02499v1](https://arxiv.org/abs/2512.02499) · [PDF](https://arxiv.org/pdf/2512.02499.pdf)  
**作者**：Yongkai Liu, Helena Feng, Bin Jiang, Yixin Wang, Max Wintermark, David S. Liebeskind, Michael Moseley, Maarten Lansberg, Gregory Albers, Jeremy Heit, Greg Zaharchuk  

**一句话要点**：提出链式思维预测引擎COPE，基于开源大语言模型从临床笔记预测急性缺血性卒中90天功能结局。

**关键词**：急性缺血性卒中, 临床笔记分析, 链式思维推理, 开源大语言模型, 结局预测

## 3 点简述
- 核心问题：临床笔记非结构化限制传统模型预测急性缺血性卒中结局。
- 方法要点：采用两步链式思维框架，首步生成临床推理，次步输出改良Rankin量表预测。
- 实验或效果：COPE性能媲美GPT-4.1，优于ClinicalBERT、临床机器学习模型和单步大语言模型。

## 摘要（原文）

> Predicting outcomes in acute ischemic stroke (AIS) guides clinical decision-making, patient counseling, and resource allocation. Clinical notes contain rich contextual information, but their unstructured nature limits their use in traditional predictive models. We developed and evaluated the Chain-of-Thought (CoT) Outcome Prediction Engine (COPE), a reasoning-enhanced large language model framework, for predicting 90-day functional outcomes after AIS from unstructured clinical notes. This study included 464 AIS patients with discharge summaries and 90-day modified Rankin Scale (mRS) scores. COPE uses a two-step CoT framework based on sequential open-source LLaMA-3-8B models: the first generates clinical reasoning, and the second outputs an mRS prediction. We compared COPE with GPT-4.1, ClinicalBERT, a structured variable-based machine learning model (Clinical ML), and a single-step LLM without CoT. Performance was evaluated using mean absolute error (MAE), accuracy within +/-1 mRS point, and exact accuracy. COPE achieved an MAE of 1.01 (95% CI 0.92-1.11), +/-1 accuracy of 74.4% (69.9, 78.8%), and exact accuracy of 32.8% (28.0, 37.6%), comparable to GPT-4.1 and superior to ClinicalBERT [MAE 1.24 (1.13-1.36)], Clinical ML [1.28 (1.18-1.39)], and the single-step LLM [1.20 (1.09-1.33)]. Subgroup analyses showed consistent performance across sex and age, with slightly higher error among older patients, those undergoing thrombectomy, and those with longer summaries. These findings demonstrate that COPE, a lightweight, interpretable, and privacy-preserving open-source framework, provides an accurate and practical solution for outcome prediction from unstructured clinical text.

