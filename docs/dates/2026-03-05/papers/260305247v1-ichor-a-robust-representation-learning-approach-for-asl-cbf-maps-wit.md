---
layout: default
title: ICHOR: A Robust Representation Learning Approach for ASL CBF Maps with Self-Supervised Masked Autoencoders
---

# ICHOR: A Robust Representation Learning Approach for ASL CBF Maps with Self-Supervised Masked Autoencoders
**arXiv**：[2603.05247v1](https://arxiv.org/abs/2603.05247) · [PDF](https://arxiv.org/pdf/2603.05247.pdf)  
**作者**：Xavier Beltran-Urbano, Yiran Li, Xinglin Zeng, Katie R. Jobson, Manuel Taso, Christopher A. Brown, David A. Wolk, Corey T. McMillan, Ilya M. Nashrallah, Paul A. Yushkevich, Ze Wang, John A. Detre, Sudipto Dolui  

**一句话要点**：提出ICHOR自监督预训练方法，利用3D掩码自编码器学习ASL CBF图的鲁棒表示以解决跨站点泛化挑战。

**关键词**：自监督学习, 掩码自编码器, ASL CBF图, Vision Transformer, 跨站点泛化, 医学影像分析

## 3 点简述
- ASL CBF图分析面临图像质量差异、跨站点协议不一致和标注数据有限等泛化问题。
- ICHOR基于Vision Transformer，通过掩码图像建模自监督预训练，学习可迁移的通用编码器表示。
- 在包含11,405次扫描的大规模数据集上预训练，并在下游分类和回归任务中优于现有方法。

## 摘要（原文）

> Arterial spin labeling (ASL) perfusion MRI allows direct quantification of regional cerebral blood flow (CBF) without exogenous contrast, enabling noninvasive measurements that can be repeated without constraints imposed by contrast injection. ASL is increasingly acquired in research studies and clinical MRI protocols. Building on successes in structural imaging, recent efforts have implemented deep learning based methods to improve image quality, enable automated quality control, and derive robust quantitative and predictive biomarkers with ASL derived CBF. However, progress has been limited by variable image quality, substantial inter-site, vendor and protocol differences, and limited availability of labeled datasets needed to train models that generalize across cohorts. To address these challenges, we introduce ICHOR, a self supervised pre-training approach for ASL CBF maps that learns transferable representations using 3D masked autoencoders. ICHOR is pretrained via masked image modeling using a Vision Transformer backbone and can be used as a general-purpose encoder for downstream ASL tasks. For pre-training, we curated one of the largest ASL datasets to date, comprising 11,405 ASL CBF scans from 14 studies spanning multiple sites and acquisition protocols. We evaluated the pre-trained ICHOR encoder on three downstream diagnostic classification tasks and one ASL CBF map quality prediction regression task. Across all evaluations, ICHOR outperformed existing neuroimaging self-supervised pre-training methods adapted to ASL. Pre-trained weights and code will be made publicly available.

