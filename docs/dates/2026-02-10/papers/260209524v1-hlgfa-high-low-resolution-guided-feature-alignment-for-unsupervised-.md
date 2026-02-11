---
layout: default
title: HLGFA: High-Low Resolution Guided Feature Alignment for Unsupervised Anomaly Detection
---

# HLGFA: High-Low Resolution Guided Feature Alignment for Unsupervised Anomaly Detection
**arXiv**：[2602.09524v1](https://arxiv.org/abs/2602.09524) · [PDF](https://arxiv.org/pdf/2602.09524.pdf)  
**作者**：Han Zhou, Yuxuan Gao, Yinchao Du, Xuezhe Zheng  

**一句话要点**：提出HLGFA框架，通过高低分辨率特征对齐解决工业异常检测中缺陷样本稀缺问题。

**关键词**：无监督异常检测, 特征对齐, 工业检测, 多分辨率学习, 噪声抑制

## 3 点简述
- 核心问题：工业异常检测中缺陷样本稀缺，需无监督方法确保可靠检测。
- 方法要点：利用高低分辨率特征一致性建模正常性，通过条件调制和门控残差校正细化特征。
- 实验或效果：在MVTec AD数据集上达到97.9%像素级AUROC，优于现有方法。

## 摘要（原文）

> Unsupervised industrial anomaly detection (UAD) is essential for modern manufacturing inspection, where defect samples are scarce and reliable detection is required. In this paper, we propose HLGFA, a high-low resolution guided feature alignment framework that learns normality by modeling cross-resolution feature consistency between high-resolution and low-resolution representations of normal samples, instead of relying on pixel-level reconstruction. Dual-resolution inputs are processed by a shared frozen backbone to extract multi-level features, and high-resolution representations are decomposed into structure and detail priors to guide the refinement of low-resolution features through conditional modulation and gated residual correction. During inference, anomalies are naturally identified as regions where cross-resolution alignment breaks down. In addition, a noise-aware data augmentation strategy is introduced to suppress nuisance-induced responses commonly observed in industrial environments. Extensive experiments on standard benchmarks demonstrate the effectiveness of HLGFA, achieving 97.9% pixel-level AUROC and 97.5% image-level AUROC on the MVTec AD dataset, outperforming representative reconstruction-based and feature-based methods.

