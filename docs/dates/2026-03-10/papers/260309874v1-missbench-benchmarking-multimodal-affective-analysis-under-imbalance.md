---
layout: default
title: MissBench: Benchmarking Multimodal Affective Analysis under Imbalanced Missing Modalities
---

# MissBench: Benchmarking Multimodal Affective Analysis under Imbalanced Missing Modalities
**arXiv**：[2603.09874v1](https://arxiv.org/abs/2603.09874) · [PDF](https://arxiv.org/pdf/2603.09874.pdf)  
**作者**：Tien Anh Pham, Phuong-Anh Nguyen, Duc-Trong Le, Cam-Van Thi Nguyen  

**一句话要点**：提出MissBench基准与框架，以评估不平衡缺失模态下的多模态情感分析模型性能。

**关键词**：多模态情感分析, 缺失模态基准, 模态公平指数, 模态学习指数, 不平衡缺失率, 情感计算

## 3 点简述
- 核心问题：现实应用中多模态数据存在不平衡缺失，导致训练偏差，标准评估方法无法充分揭示。
- 方法要点：定义共享和不平衡缺失率协议，引入模态公平指数和模态学习指数作为诊断指标。
- 实验或效果：在四个数据集上测试，显示模型在不平衡条件下可能表现出模态不公平和优化失衡。

## 摘要（原文）

> Multimodal affective computing underpins key tasks such as sentiment analysis and emotion recognition. Standard evaluations, however, often assume that textual, acoustic, and visual modalities are equally available. In real applications, some modalities are systematically more fragile or expensive, creating imbalanced missing rates and training biases that task-level metrics alone do not reveal. We introduce MissBench, a benchmark and framework for multimodal affective tasks that standardizes both shared and imbalanced missing-rate protocols on four widely used sentiment and emotion datasets. MissBench also defines two diagnostic metrics. The Modality Equity Index (MEI) measures how fairly different modalities contribute across missing-modality configurations. The Modality Learning Index (MLI) quantifies optimization imbalance by comparing modality-specific gradient norms during training, aggregated across modality-related modules. Experiments on representative method families show that models that appear robust under shared missing rates can still exhibit marked modality inequity and optimization imbalance under imbalanced conditions. These findings position MissBench, together with MEI and MLI, as practical tools for stress-testing and analyzing multimodal affective models in realistic incomplete-modality settings.For reproducibility, we release our code at: https://anonymous.4open.science/r/MissBench-4098/

