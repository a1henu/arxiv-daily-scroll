---
layout: default
title: SubspaceAD: Training-Free Few-Shot Anomaly Detection via Subspace Modeling
---

# SubspaceAD: Training-Free Few-Shot Anomaly Detection via Subspace Modeling
**arXiv**：[2602.23013v1](https://arxiv.org/abs/2602.23013) · [PDF](https://arxiv.org/pdf/2602.23013.pdf)  
**作者**：Camile Lendering, Erkut Akdag, Egor Bondarev  

**一句话要点**：提出SubspaceAD，通过子空间建模实现无需训练的小样本异常检测

**关键词**：小样本异常检测, 子空间建模, 训练免费方法, 工业视觉检测, DINOv2特征, PCA分析

## 3 点简述
- 核心问题：工业检测中仅需少量正常图像的小样本异常检测，现有方法依赖复杂组件如记忆库或多模态调优。
- 方法要点：使用冻结DINOv2提取特征，PCA拟合正常变化子空间，基于重构残差检测异常，无需训练或额外数据。
- 实验或效果：在MVTec-AD和VisA数据集上，单样本设置下图像级和像素级AUROC达98.0%/97.6%和93.3%/98.3%，超越先前最优结果。

## 摘要（原文）

> Detecting visual anomalies in industrial inspection often requires training with only a few normal images per category. Recent few-shot methods achieve strong results employing foundation-model features, but typically rely on memory banks, auxiliary datasets, or multi-modal tuning of vision-language models. We therefore question whether such complexity is necessary given the feature representations of vision foundation models. To answer this question, we introduce SubspaceAD, a training-free method, that operates in two simple stages. First, patch-level features are extracted from a small set of normal images by a frozen DINOv2 backbone. Second, a Principal Component Analysis (PCA) model is fit to these features to estimate the low-dimensional subspace of normal variations. At inference, anomalies are detected via the reconstruction residual with respect to this subspace, producing interpretable and statistically grounded anomaly scores. Despite its simplicity, SubspaceAD achieves state-of-the-art performance across one-shot and few-shot settings without training, prompt tuning, or memory banks. In the one-shot anomaly detection setting, SubspaceAD achieves image-level and pixel-level AUROC of 98.0% and 97.6% on the MVTec-AD dataset, and 93.3% and 98.3% on the VisA dataset, respectively, surpassing prior state-of-the-art results. Code and demo are available at https://github.com/CLendering/SubspaceAD.

