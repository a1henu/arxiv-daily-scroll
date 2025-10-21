---
layout: default
title: Facial Expression-based Parkinson's Disease Severity Diagnosis via Feature Fusion and Adaptive Class Balancing
---

# Facial Expression-based Parkinson's Disease Severity Diagnosis via Feature Fusion and Adaptive Class Balancing
**arXiv**：[2510.17373v1](https://arxiv.org/abs/2510.17373) · [PDF](https://arxiv.org/pdf/2510.17373.pdf)  
**作者**：Yintao Zhou, Wei Huang, Zhengyu Li, Jing Huang, Meng Pang  

**一句话要点**：提出基于多表情特征融合与自适应类平衡的方法，用于帕金森病严重程度诊断。

**关键词**：帕金森病诊断, 面部表情分析, 特征融合, 类不平衡处理, 注意力机制, 多分类任务

## 3 点简述
- 核心问题：单表情诊断易误诊，类不平衡影响多阶段PD严重程度预测性能。
- 方法要点：采用注意力机制融合多表情特征，动态调整样本贡献以平衡类别。
- 实验或效果：实验显示方法在PD严重程度诊断中表现优异，验证了融合与平衡策略有效性。

## 摘要（原文）

> Parkinson's disease (PD) severity diagnosis is crucial for early detecting
> potential patients and adopting tailored interventions. Diagnosing PD based on
> facial expression is grounded in PD patients' "masked face" symptom and gains
> growing interest recently for its convenience and affordability. However,
> current facial expression-based approaches often rely on single type of
> expression which can lead to misdiagnosis, and ignore the class imbalance
> across different PD stages which degrades the prediction performance. Moreover,
> most existing methods focus on binary classification (i.e., PD / non-PD) rather
> than diagnosing the severity of PD. To address these issues, we propose a new
> facial expression-based method for PD severity diagnosis which integrates
> multiple facial expression features through attention-based feature fusion.
> Moreover, we mitigate the class imbalance problem via an adaptive class
> balancing strategy which dynamically adjusts the contribution of training
> samples based on their class distribution and classification difficulty.
> Experimental results demonstrate the promising performance of the proposed
> method for PD severity diagnosis, as well as the efficacy of attention-based
> feature fusion and adaptive class balancing.

