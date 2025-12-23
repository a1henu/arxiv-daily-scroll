---
layout: default
title: Causal Heterogeneous Graph Learning Method for Chronic Obstructive Pulmonary Disease Prediction
---

# Causal Heterogeneous Graph Learning Method for Chronic Obstructive Pulmonary Disease Prediction
**arXiv**：[2512.19194v1](https://arxiv.org/abs/2512.19194) · [PDF](https://arxiv.org/pdf/2512.19194.pdf)  
**作者**：Leming Zhou, Zuo Wang, Zhigang Liu  

**一句话要点**：提出因果异构图学习方法以预测慢性阻塞性肺疾病共病风险

**关键词**：慢性阻塞性肺疾病预测, 因果异构图学习, 共病风险分析, 反事实推理, 图神经网络

## 3 点简述
- 核心问题：基层诊断能力不足导致慢性阻塞性肺疾病早期识别和急性加重预警存在缺陷，筛查率低。
- 方法要点：构建患者-疾病交互的异构图，结合因果推理与异构图学习，设计包含反事实推理和因果正则化的损失函数。
- 实验或效果：与强GNN基线比较，模型在检测准确性上表现优异。

## 摘要（原文）

> Due to the insufficient diagnosis and treatment capabilities at the grassroots level, there are still deficiencies in the early identification and early warning of acute exacerbation of Chronic obstructive pulmonary disease (COPD), often resulting in a high prevalence rate and high burden, but the screening rate is relatively low. In order to gradually improve this situation. In this paper, this study develop a Causal Heterogeneous Graph Representation Learning (CHGRL) method for COPD comorbidity risk prediction method that: a) constructing a heterogeneous Our dataset includes the interaction between patients and diseases; b) A cause-aware heterogeneous graph learning architecture has been constructed, combining causal inference mechanisms with heterogeneous graph learning, which can support heterogeneous graph causal learning for different types of relationships; and c) Incorporate the causal loss function in the model design, and add counterfactual reasoning learning loss and causal regularization loss on the basis of the cross-entropy classification loss. We evaluate our method and compare its performance with strong GNN baselines. Following experimental evaluation, the proposed model demonstrates high detection accuracy.

