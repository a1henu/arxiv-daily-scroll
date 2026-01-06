---
layout: default
title: XAI-MeD: Explainable Knowledge Guided Neuro-Symbolic Framework for Domain Generalization and Rare Class Detection in Medical Imaging
---

# XAI-MeD: Explainable Knowledge Guided Neuro-Symbolic Framework for Domain Generalization and Rare Class Detection in Medical Imaging
**arXiv**：[2601.02008v1](https://arxiv.org/abs/2601.02008) · [PDF](https://arxiv.org/pdf/2601.02008.pdf)  
**作者**：Midhat Urooj, Ayan Banerjee, Sandeep Gupta  

**一句话要点**：提出XAI-MeD框架，通过神经符号架构整合临床知识，以解决医学影像中的领域泛化和罕见类别检测问题。

**关键词**：医学影像分析, 神经符号AI, 领域泛化, 罕见类别检测, 可解释AI, 临床知识整合

## 3 点简述
- 核心问题：医学AI在真实世界分布偏移下泛化能力差，且对罕见临床类别存在偏见。
- 方法要点：将临床知识编码为逻辑规则，通过加权特征满足分数进行符号推理，并与神经网络预测融合。
- 实验或效果：在多个任务上评估，领域泛化性能提升6%，罕见类别F1分数提高10%，优于现有基线。

## 摘要（原文）

> Explainability domain generalization and rare class reliability are critical challenges in medical AI where deep models often fail under real world distribution shifts and exhibit bias against infrequent clinical conditions This paper introduces XAIMeD an explainable medical AI framework that integrates clinically accurate expert knowledge into deep learning through a unified neuro symbolic architecture XAIMeD is designed to improve robustness under distribution shift enhance rare class sensitivity and deliver transparent clinically aligned interpretations The framework encodes clinical expertise as logical connectives over atomic medical propositions transforming them into machine checkable class specific rules Their diagnostic utility is quantified through weighted feature satisfaction scores enabling a symbolic reasoning branch that complements neural predictions A confidence weighted fusion integrates symbolic and deep outputs while a Hunt inspired adaptive routing mechanism guided by Entropy Imbalance Gain EIG and Rare Class Gini mitigates class imbalance high intra class variability and uncertainty We evaluate XAIMeD across diverse modalities on four challenging tasks i Seizure Onset Zone SOZ localization from rs fMRI ii Diabetic Retinopathy grading across 6 multicenter datasets demonstrate substantial performance improvements including 6 percent gains in cross domain generalization and a 10 percent improved rare class F1 score far outperforming state of the art deep learning baselines Ablation studies confirm that the clinically grounded symbolic components act as effective regularizers ensuring robustness to distribution shifts XAIMeD thus provides a principled clinically faithful and interpretable approach to multimodal medical AI.

