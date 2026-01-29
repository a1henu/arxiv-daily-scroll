---
layout: default
title: PatchFormer: A Patch-Based Time Series Foundation Model with Hierarchical Masked Reconstruction and Cross-Domain Transfer Learning for Zero-Shot Multi-Horizon Forecasting
---

# PatchFormer: A Patch-Based Time Series Foundation Model with Hierarchical Masked Reconstruction and Cross-Domain Transfer Learning for Zero-Shot Multi-Horizon Forecasting
**arXiv**：[2601.20845v1](https://arxiv.org/abs/2601.20845) · [PDF](https://arxiv.org/pdf/2601.20845.pdf)  
**作者**：Olaf Yunus Laitinen Imanov, Derya Umut Kulali, Taner Yilmaz  

**一句话要点**：提出PatchFormer，基于分块的时间序列基础模型，通过分层掩码重建和跨域迁移学习实现零样本多步预测。

**关键词**：时间序列预测, 基础模型, 自监督学习, 跨域迁移, 零样本学习, 多步预测

## 3 点简述
- 核心问题：时间序列预测常需领域特定特征工程和大量标注数据，限制了泛化能力。
- 方法要点：将时间序列分块，使用分层掩码重建进行自监督预训练，结合跨域知识蒸馏和轻量适配器。
- 实验或效果：在24个基准数据集上实现最先进的零样本多步预测，MSE降低27.3%，任务特定训练数据减少94%。

## 摘要（原文）

> Time series forecasting is a fundamental problem with applications in climate, energy, healthcare, and finance. Many existing approaches require domain-specific feature engineering and substantial labeled data for each task. We introduce PatchFormer, a patch-based time series foundation model that uses hierarchical masked reconstruction for self-supervised pretraining and lightweight adapters for efficient transfer. PatchFormer segments time series into patches and learns multiscale temporal representations with learnable aggregation across temporal scales. Pretraining uses masked patch reconstruction with dynamic masking and objectives that encourage both local accuracy and global consistency, followed by cross-domain knowledge distillation. Experiments on 24 benchmark datasets spanning weather, energy, traffic, finance, and healthcare demonstrate state-of-the-art zero-shot multi-horizon forecasting, reducing mean squared error by 27.3 percent relative to strong baselines while requiring 94 percent less task-specific training data. The model exhibits near log-linear scaling with more pretraining data up to 100 billion points and processes length-512 sequences 3.8x faster than full-sequence transformers.

