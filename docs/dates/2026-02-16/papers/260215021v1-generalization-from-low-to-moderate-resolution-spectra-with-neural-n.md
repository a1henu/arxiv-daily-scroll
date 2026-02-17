---
layout: default
title: Generalization from Low- to Moderate-Resolution Spectra with Neural Networks for Stellar Parameter Estimation: A Case Study with DESI
---

# Generalization from Low- to Moderate-Resolution Spectra with Neural Networks for Stellar Parameter Estimation: A Case Study with DESI
**arXiv**：[2602.15021v1](https://arxiv.org/abs/2602.15021) · [PDF](https://arxiv.org/pdf/2602.15021.pdf)  
**作者**：Xiaosheng Zhao, Yuan-Sen Ting, Rosemary F. G. Wyse, Alexander S. Szalay, Yang Huang, László Dobos, Tamás Budavári, Viska Wei  

**一句话要点**：研究预训练多层感知机从低分辨率到中分辨率光谱的跨调查泛化能力，用于恒星参数估计。

**关键词**：恒星光谱分析, 跨调查泛化, 多层感知机, 微调策略, 光谱嵌入, 恒星参数估计

## 3 点简述
- 核心问题：跨调查泛化挑战，特别是从低分辨率到中分辨率光谱的迁移。
- 方法要点：使用预训练多层感知机，比较直接训练光谱与基于嵌入的方法，评估不同微调策略。
- 实验或效果：预训练多层感知机在未微调时表现良好，微调后进一步提升；嵌入方法在富金属区有优势，但贫金属区表现较差。

## 摘要（原文）

> Cross-survey generalization is a critical challenge in stellar spectral analysis, particularly in cases such as transferring from low- to moderate-resolution surveys. We investigate this problem using pre-trained models, focusing on simple neural networks such as multilayer perceptrons (MLPs), with a case study transferring from LAMOST low-resolution spectra (LRS) to DESI medium-resolution spectra (MRS). Specifically, we pre-train MLPs on either LRS or their embeddings and fine-tune them for application to DESI stellar spectra. We compare MLPs trained directly on spectra with those trained on embeddings derived from transformer-based models (self-supervised foundation models pre-trained for multiple downstream tasks). We also evaluate different fine-tuning strategies, including residual-head adapters, LoRA, and full fine-tuning. We find that MLPs pre-trained on LAMOST LRS achieve strong performance, even without fine-tuning, and that modest fine-tuning with DESI spectra further improves the results. For iron abundance, embeddings from a transformer-based model yield advantages in the metal-rich ([Fe/H] > -1.0) regime, but underperform in the metal-poor regime compared to MLPs trained directly on LRS. We also show that the optimal fine-tuning strategy depends on the specific stellar parameter under consideration. These results highlight that simple pre-trained MLPs can provide competitive cross-survey generalization, while the role of spectral foundation models for cross-survey stellar parameter estimation requires further exploration.

