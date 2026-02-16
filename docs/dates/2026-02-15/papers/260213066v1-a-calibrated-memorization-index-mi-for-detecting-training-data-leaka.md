---
layout: default
title: A Calibrated Memorization Index (MI) for Detecting Training Data Leakage in Generative MRI Models
---

# A Calibrated Memorization Index (MI) for Detecting Training Data Leakage in Generative MRI Models
**arXiv**：[2602.13066v1](https://arxiv.org/abs/2602.13066) · [PDF](https://arxiv.org/pdf/2602.13066.pdf)  
**作者**：Yash Deo, Yan Jia, Toni Lassila, Victoria J Hodge, Alejandro F Frang, Chenghao Qian, Siyuan Kang, Ibrahim Habli  

**一句话要点**：提出校准记忆指数以检测生成MRI模型中的训练数据泄露

**关键词**：训练数据泄露检测, 生成模型记忆性, MRI图像生成, 隐私保护, 校准指标

## 3 点简述
- 核心问题：生成模型可能复制训练图像，引发医疗隐私风险。
- 方法要点：基于MRI基础模型提取特征，聚合多层白化最近邻相似度，映射为有界指数。
- 实验或效果：在三个MRI数据集上，指标稳健检测复制，样本级检测接近完美。

## 摘要（原文）

> Image generative models are known to duplicate images from the training data as part of their outputs, which can lead to privacy concerns when used for medical image generation. We propose a calibrated per-sample metric for detecting memorization and duplication of training data. Our metric uses image features extracted using an MRI foundation model, aggregates multi-layer whitened nearest-neighbor similarities, and maps them to a bounded \emph{Overfit/Novelty Index} (ONI) and \emph{Memorization Index} (MI) scores. Across three MRI datasets with controlled duplication percentages and typical image augmentations, our metric robustly detects duplication and provides more consistent metric values across datasets. At the sample level, our metric achieves near-perfect detection of duplicates.

