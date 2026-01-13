---
layout: default
title: Towards Automated Diagnosis of Inherited Arrhythmias: Combined Arrhythmia Classification Using Lead-Aware Spatial Attention Networks
---

# Towards Automated Diagnosis of Inherited Arrhythmias: Combined Arrhythmia Classification Using Lead-Aware Spatial Attention Networks
**arXiv**：[2601.07124v1](https://arxiv.org/abs/2601.07124) · [PDF](https://arxiv.org/pdf/2601.07124.pdf)  
**作者**：Sophie Sigfstead, River Jiang, Brianna Davies, Zachary W. M. Laksman, Julia Cadrin-Tourigny, Rafik Tadros, Habib Khan, Joseph Atallah, Christian Steinberg, Shubhayan Sanatani, Mario Talajic, Rahul Krishnan, Andrew D. Krahn, Christopher C. Cheung  

**一句话要点**：提出导联感知空间注意力网络以提升遗传性心律失常的自动诊断性能

**关键词**：遗传性心律失常分类, 导联感知注意力, ECG基础模型, 微调策略, 临床可解释性, 多中心验证

## 3 点简述
- 核心问题：遗传性心律失常如ARVC和LQTS的分类缺乏临床可解释的深度学习模型
- 方法要点：结合导联感知空间注意力网络与ECG基础模型，通过微调优化集成策略
- 实验或效果：在13中心队列中实现近天花板性能，导联掩蔽验证了生理合理性

## 摘要（原文）

> Arrhythmogenic right ventricular cardiomyopathy (ARVC) and long QT syndrome (LQTS) are inherited arrhythmia syndromes associated with sudden cardiac death. Deep learning shows promise for ECG interpretation, but multi-class inherited arrhythmia classification with clinically grounded interpretability remains underdeveloped. Our objective was to develop and validate a lead-aware deep learning framework for multi-class (ARVC vs LQTS vs control) and binary inherited arrhythmia classification, and to determine optimal strategies for integrating ECG foundation models within arrhythmia screening tools. We assembled a 13-center Canadian cohort (645 patients; 1,344 ECGs). We evaluated four ECG foundation models using three transfer learning approaches: linear probing, fine-tuning, and combined strategies. We developed lead-aware spatial attention networks (LASAN) and assessed integration strategies combining LASAN with foundation models. Performance was compared against the established foundation model baselines. Lead-group masking quantified disease-specific lead dependence. Fine-tuning outperformed linear probing and combined strategies across all foundation models (mean macro-AUROC 0.904 vs 0.825). The best lead-aware integrations achieved near-ceiling performance (HuBERT-ECG hybrid: macro-AUROC 0.990; ARVC vs control AUROC 0.999; LQTS vs control AUROC 0.994). Lead masking demonstrated physiologic plausibility: V1-V3 were most critical for ARVC detection (4.54% AUROC reduction), while lateral leads were preferentially important for LQTS (2.60% drop). Lead-aware architectures achieved state-of-the-art performance for inherited arrhythmia classification, outperforming all existing published models on both binary and multi-class tasks while demonstrating clinically aligned lead dependence. These findings support potential utility for automated ECG screening pending validation.

