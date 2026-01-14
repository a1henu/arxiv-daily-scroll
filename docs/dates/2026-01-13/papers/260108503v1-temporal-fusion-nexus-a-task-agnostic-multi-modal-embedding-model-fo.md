---
layout: default
title: Temporal Fusion Nexus: A task-agnostic multi-modal embedding model for clinical narratives and irregular time series in post-kidney transplant care
---

# Temporal Fusion Nexus: A task-agnostic multi-modal embedding model for clinical narratives and irregular time series in post-kidney transplant care
**arXiv**：[2601.08503v1](https://arxiv.org/abs/2601.08503) · [PDF](https://arxiv.org/pdf/2601.08503.pdf)  
**作者**：Aditya Kumar, Simon Rauch, Mario Cypko, Marcel Naik, Matthieu-P Schapranow, Aadil Rashid, Fabian Halleck, Bilgin Osmanodja, Roland Roller, Lars Pape, Klemens Budde, Mario Schiffer, Oliver Amft  

**一句话要点**：提出Temporal Fusion Nexus，一种任务无关的多模态嵌入模型，用于整合肾移植后护理中的不规则时间序列和临床叙述。

**关键词**：多模态嵌入, 不规则时间序列, 临床叙述, 肾移植护理, 任务无关模型, 可解释性分析

## 3 点简述
- 核心问题：肾移植后护理中，不规则时间序列和临床叙述等多模态数据整合困难。
- 方法要点：开发任务无关嵌入模型，融合不规则时间序列和临床文本，生成可解释的潜在因子。
- 实验或效果：在3382名患者队列中，TFN在移植物丢失和排斥预测上优于现有模型，AUC分别达0.96和0.84。

## 摘要（原文）

> We introduce Temporal Fusion Nexus (TFN), a multi-modal and task-agnostic embedding model to integrate irregular time series and unstructured clinical narratives. We analysed TFN in post-kidney transplant (KTx) care, with a retrospective cohort of 3382 patients, on three key outcomes: graft loss, graft rejection, and mortality. Compared to state-of-the-art model in post KTx care, TFN achieved higher performance for graft loss (AUC 0.96 vs. 0.94) and graft rejection (AUC 0.84 vs. 0.74). In mortality prediction, TFN yielded an AUC of 0.86. TFN outperformed unimodal baselines (approx 10% AUC improvement over time series only baseline, approx 5% AUC improvement over time series with static patient data). Integrating clinical text improved performance across all tasks. Disentanglement metrics confirmed robust and interpretable latent factors in the embedding space, and SHAP-based attributions confirmed alignment with clinical reasoning. TFN has potential application in clinical tasks beyond KTx, where heterogeneous data sources, irregular longitudinal data, and rich narrative documentation are available.

