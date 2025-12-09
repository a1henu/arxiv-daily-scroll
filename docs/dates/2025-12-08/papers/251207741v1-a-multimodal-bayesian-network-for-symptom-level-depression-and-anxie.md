---
layout: default
title: A multimodal Bayesian Network for symptom-level depression and anxiety prediction from voice and speech data
---

# A multimodal Bayesian Network for symptom-level depression and anxiety prediction from voice and speech data
**arXiv**：[2512.07741v1](https://arxiv.org/abs/2512.07741) · [PDF](https://arxiv.org/pdf/2512.07741.pdf)  
**作者**：Agnes Norbury, George Fairs, Alexandra L. Georgescu, Matthew M. Nour, Emilia Molimpakis, Stefano Goria  

**一句话要点**：提出基于贝叶斯网络的多模态模型，从语音数据预测抑郁和焦虑症状，以支持临床评估。

**关键词**：贝叶斯网络, 多模态预测, 语音分析, 精神症状评估, 临床支持工具

## 3 点简述
- 核心问题：临床评估中整合非语言信息（如语音特征）预测精神症状的挑战。
- 方法要点：使用贝叶斯网络建模，分析大规模语音数据集（30,135名说话者），评估症状级预测。
- 实验或效果：模型在抑郁和焦虑预测上ROC-AUC达0.842和0.831，并探讨了公平性和临床实用性。

## 摘要（原文）

> During psychiatric assessment, clinicians observe not only what patients report, but important nonverbal signs such as tone, speech rate, fluency, responsiveness, and body language. Weighing and integrating these different information sources is a challenging task and a good candidate for support by intelligence-driven tools - however this is yet to be realized in the clinic. Here, we argue that several important barriers to adoption can be addressed using Bayesian network modelling. To demonstrate this, we evaluate a model for depression and anxiety symptom prediction from voice and speech features in large-scale datasets (30,135 unique speakers). Alongside performance for conditions and symptoms (for depression, anxiety ROC-AUC=0.842,0.831 ECE=0.018,0.015; core individual symptom ROC-AUC>0.74), we assess demographic fairness and investigate integration across and redundancy between different input modality types. Clinical usefulness metrics and acceptability to mental health service users are explored. When provided with sufficiently rich and large-scale multimodal data streams and specified to represent common mental conditions at the symptom rather than disorder level, such models are a principled approach for building robust assessment support tools: providing clinically-relevant outputs in a transparent and explainable format that is directly amenable to expert clinical supervision.

