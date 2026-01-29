---
layout: default
title: MMSF: Multitask and Multimodal Supervised Framework for WSI Classification and Survival Analysis
---

# MMSF: Multitask and Multimodal Supervised Framework for WSI Classification and Survival Analysis
**arXiv**：[2601.20347v1](https://arxiv.org/abs/2601.20347) · [PDF](https://arxiv.org/pdf/2601.20347.pdf)  
**作者**：Chengying She, Chengwei Chen, Xinran Zhang, Ben Wang, Lizhuang Liu, Chengwei Shao, Yun Bian  

**一句话要点**：提出MMSF框架，通过多任务多模态监督解决全切片图像分类与生存分析中的异质信号融合挑战。

**关键词**：多模态学习, 全切片图像分类, 生存分析, 多任务学习, 特征融合, 计算病理学

## 3 点简述
- 核心问题：全切片图像与临床数据特征空间统计和尺度差异大，异质信号融合困难。
- 方法要点：基于线性复杂度MIL骨干，分解并融合跨模态信息，包括图特征提取、临床数据嵌入和特征对齐模块。
- 实验或效果：在CAMELYON16和TCGA-NSCLC上提升准确率和AUC，在TCGA生存队列中C-index优于单模态和多模态基线。

## 摘要（原文）

> Multimodal evidence is critical in computational pathology: gigapixel whole slide images capture tumor morphology, while patient-level clinical descriptors preserve complementary context for prognosis. Integrating such heterogeneous signals remains challenging because feature spaces exhibit distinct statistics and scales. We introduce MMSF, a multitask and multimodal supervised framework built on a linear-complexity MIL backbone that explicitly decomposes and fuses cross-modal information. MMSF comprises a graph feature extraction module embedding tissue topology at the patch level, a clinical data embedding module standardizing patient attributes, a feature fusion module aligning modality-shared and modality-specific representations, and a Mamba-based MIL encoder with multitask prediction heads. Experiments on CAMELYON16 and TCGA-NSCLC demonstrate 2.1--6.6\% accuracy and 2.2--6.9\% AUC improvements over competitive baselines, while evaluations on five TCGA survival cohorts yield 7.1--9.8\% C-index improvements compared with unimodal methods and 5.6--7.1\% over multimodal alternatives.

