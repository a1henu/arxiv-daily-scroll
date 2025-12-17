---
layout: default
title: Unleashing the Power of Image-Tabular Self-Supervised Learning via Breaking Cross-Tabular Barriers
---

# Unleashing the Power of Image-Tabular Self-Supervised Learning via Breaking Cross-Tabular Barriers
**arXiv**：[2512.14026v1](https://arxiv.org/abs/2512.14026) · [PDF](https://arxiv.org/pdf/2512.14026.pdf)  
**作者**：Yibing Fu, Yunpeng Zhao, Zhitao Zeng, Cheng Chen, Yueming Jin  

**一句话要点**：提出CITab框架以解决跨队列图像-表格自监督学习中的表格异构性障碍

**关键词**：多模态学习, 自监督学习, 医学图像分析, 表格数据处理, 跨队列学习, 阿尔茨海默病诊断

## 3 点简述
- 现有图像-表格自监督学习方法因表格建模机制僵化，难以处理异构表格数据，阻碍跨队列知识迁移。
- CITab通过语义感知的表格建模和原型引导的线性混合层，增强表格特征专业化和跨队列可扩展性。
- 在阿尔茨海默病诊断任务上，CITab在三个公开队列中超越现有方法，验证了其有效性。

## 摘要（原文）

> Multi-modal learning integrating medical images and tabular data has significantly advanced clinical decision-making in recent years. Self-Supervised Learning (SSL) has emerged as a powerful paradigm for pretraining these models on large-scale unlabeled image-tabular data, aiming to learn discriminative representations. However, existing SSL methods for image-tabular representation learning are often confined to specific data cohorts, mainly due to their rigid tabular modeling mechanisms when modeling heterogeneous tabular data. This inter-tabular barrier hinders the multi-modal SSL methods from effectively learning transferrable medical knowledge shared across diverse cohorts. In this paper, we propose a novel SSL framework, namely CITab, designed to learn powerful multi-modal feature representations in a cross-tabular manner. We design the tabular modeling mechanism from a semantic-awareness perspective by integrating column headers as semantic cues, which facilitates transferrable knowledge learning and the scalability in utilizing multiple data sources for pretraining. Additionally, we propose a prototype-guided mixture-of-linear layer (P-MoLin) module for tabular feature specialization, empowering the model to effectively handle the heterogeneity of tabular data and explore the underlying medical concepts. We conduct comprehensive evaluations on Alzheimer's disease diagnosis task across three publicly available data cohorts containing 4,461 subjects. Experimental results demonstrate that CITab outperforms state-of-the-art approaches, paving the way for effective and scalable cross-tabular multi-modal learning.

