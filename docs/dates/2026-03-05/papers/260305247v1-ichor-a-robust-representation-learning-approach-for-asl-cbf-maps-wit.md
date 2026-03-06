---
layout: default
title: ICHOR: A Robust Representation Learning Approach for ASL CBF Maps with Self-Supervised Masked Autoencoders
---

# ICHOR: A Robust Representation Learning Approach for ASL CBF Maps with Self-Supervised Masked Autoencoders
**arXiv**：[2603.05247v1](https://arxiv.org/abs/2603.05247) · [PDF](https://arxiv.org/pdf/2603.05247.pdf)  
**作者**：Xavier Beltran-Urbano, Yiran Li, Xinglin Zeng, Katie R. Jobson, Manuel Taso, Christopher A. Brown, David A. Wolk, Corey T. McMillan, Ilya M. Nashrallah, Paul A. Yushkevich, Ze Wang, John A. Detre, Sudipto Dolui  

**一句话要点**：提出ICHOR自监督预训练方法，利用3D掩码自编码器学习ASL CBF图的鲁棒表示以解决跨站点泛化问题。

**关键词**：自监督学习, 掩码自编码器, ASL CBF图, 神经影像分析, 表示学习, Vision Transformer

## 3 点简述
- 核心问题：ASL CBF图存在图像质量差异、站点间协议不一致和标记数据有限，限制深度学习模型泛化能力。
- 方法要点：基于Vision Transformer的3D掩码自编码器进行自监督预训练，学习可迁移表示，作为下游任务通用编码器。
- 实验或效果：在11,405个ASL CBF扫描上预训练，在诊断分类和质量预测任务中优于现有神经影像自监督方法。

## 摘要（原文）

> Arterial spin labeling (ASL) perfusion MRI allows direct quantification of regional cerebral blood flow (CBF) without exogenous contrast, enabling noninvasive measurements that can be repeated without constraints imposed by contrast injection. ASL is increasingly acquired in research studies and clinical MRI protocols. Building on successes in structural imaging, recent efforts have implemented deep learning based methods to improve image quality, enable automated quality control, and derive robust quantitative and predictive biomarkers with ASL derived CBF. However, progress has been limited by variable image quality, substantial inter-site, vendor and protocol differences, and limited availability of labeled datasets needed to train models that generalize across cohorts. To address these challenges, we introduce ICHOR, a self supervised pre-training approach for ASL CBF maps that learns transferable representations using 3D masked autoencoders. ICHOR is pretrained via masked image modeling using a Vision Transformer backbone and can be used as a general-purpose encoder for downstream ASL tasks. For pre-training, we curated one of the largest ASL datasets to date, comprising 11,405 ASL CBF scans from 14 studies spanning multiple sites and acquisition protocols. We evaluated the pre-trained ICHOR encoder on three downstream diagnostic classification tasks and one ASL CBF map quality prediction regression task. Across all evaluations, ICHOR outperformed existing neuroimaging self-supervised pre-training methods adapted to ASL. Pre-trained weights and code will be made publicly available.

