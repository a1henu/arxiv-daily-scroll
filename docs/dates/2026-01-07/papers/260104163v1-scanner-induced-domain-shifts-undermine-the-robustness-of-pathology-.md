---
layout: default
title: Scanner-Induced Domain Shifts Undermine the Robustness of Pathology Foundation Models
---

# Scanner-Induced Domain Shifts Undermine the Robustness of Pathology Foundation Models
**arXiv**：[2601.04163v1](https://arxiv.org/abs/2601.04163) · [PDF](https://arxiv.org/pdf/2601.04163.pdf)  
**作者**：Erik Thiringer, Fredrik K. Gustafsson, Kajsa Ledesma Eriksson, Mattias Rantalainen  

**一句话要点**：评估病理基础模型对扫描仪诱导域移的鲁棒性，揭示其临床可靠性风险

**关键词**：病理基础模型, 扫描仪诱导域移, 鲁棒性评估, 嵌入空间分析, 临床可靠性

## 3 点简述
- 核心问题：病理基础模型对全玻片扫描仪设备变异性的鲁棒性未知，可能影响临床应用的可靠性。
- 方法要点：使用多扫描仪数据集，通过无监督嵌入分析和监督预测任务，系统评估14个模型的鲁棒性。
- 实验或效果：模型嵌入空间存在显著扫描仪特异性变异，导致下游预测校准偏差，鲁棒性不随训练数据规模或模型大小而简单提升。

## 摘要（原文）

> Pathology foundation models (PFMs) have become central to computational pathology, aiming to offer general encoders for feature extraction from whole-slide images (WSIs). Despite strong benchmark performance, PFM robustness to real-world technical domain shifts, such as variability from whole-slide scanner devices, remains poorly understood. We systematically evaluated the robustness of 14 PFMs to scanner-induced variability, including state-of-the-art models, earlier self-supervised models, and a baseline trained on natural images. Using a multiscanner dataset of 384 breast cancer WSIs scanned on five devices, we isolated scanner effects independently from biological and laboratory confounders. Robustness is assessed via complementary unsupervised embedding analyses and a set of clinicopathological supervised prediction tasks. Our results demonstrate that current PFMs are not invariant to scanner-induced domain shifts. Most models encode pronounced scanner-specific variability in their embedding spaces. While AUC often remains stable, this masks a critical failure mode: scanner variability systematically alters the embedding space and impacts calibration of downstream model predictions, resulting in scanner-dependent bias that can impact reliability in clinical use cases. We further show that robustness is not a simple function of training data scale, model size, or model recency. None of the models provided reliable robustness against scanner-induced variability. While the models trained on the most diverse data, here represented by vision-language models, appear to have an advantage with respect to robustness, they underperformed on downstream supervised tasks. We conclude that development and evaluation of PFMs requires moving beyond accuracy-centric benchmarks toward explicit evaluation and optimisation of embedding stability and calibration under realistic acquisition variability.

