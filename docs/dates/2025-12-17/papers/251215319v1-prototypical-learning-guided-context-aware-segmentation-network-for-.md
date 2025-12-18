---
layout: default
title: Prototypical Learning Guided Context-Aware Segmentation Network for Few-Shot Anomaly Detection
---

# Prototypical Learning Guided Context-Aware Segmentation Network for Few-Shot Anomaly Detection
**arXiv**：[2512.15319v1](https://arxiv.org/abs/2512.15319) · [PDF](https://arxiv.org/pdf/2512.15319.pdf)  
**作者**：Yuxin Jiang, Yunkang Cao, Weiming Shen  

**一句话要点**：提出原型学习引导的上下文感知分割网络以解决少样本异常检测中的领域差距问题。

**关键词**：少样本异常检测, 原型学习, 上下文感知分割, 领域适应, 像素级定位

## 3 点简述
- 核心问题：现有方法依赖预训练特征，但忽视与目标场景的领域差距，影响异常检测性能。
- 方法要点：设计原型特征适应子网络增强正常数据紧凑性，并引入上下文感知分割子网络进行像素级定位。
- 实验或效果：在MVTec和MPDD数据集上，8-shot场景下图像级AUROC分别达94.9%和80.2%，实际应用验证有效性。

## 摘要（原文）

> Few-shot anomaly detection (FSAD) denotes the identification of anomalies within a target category with a limited number of normal samples. Existing FSAD methods largely rely on pre-trained feature representations to detect anomalies, but the inherent domain gap between pre-trained representations and target FSAD scenarios is often overlooked. This study proposes a Prototypical Learning Guided Context-Aware Segmentation Network (PCSNet) to address the domain gap, thereby improving feature descriptiveness in target scenarios and enhancing FSAD performance. In particular, PCSNet comprises a prototypical feature adaption (PFA) sub-network and a context-aware segmentation (CAS) sub-network. PFA extracts prototypical features as guidance to ensure better feature compactness for normal data while distinct separation from anomalies. A pixel-level disparity classification loss is also designed to make subtle anomalies more distinguishable. Then a CAS sub-network is introduced for pixel-level anomaly localization, where pseudo anomalies are exploited to facilitate the training process. Experimental results on MVTec and MPDD demonstrate the superior FSAD performance of PCSNet, with 94.9% and 80.2% image-level AUROC in an 8-shot scenario, respectively. Real-world applications on automotive plastic part inspection further demonstrate that PCSNet can achieve promising results with limited training samples. Code is available at https://github.com/yuxin-jiang/PCSNet.

