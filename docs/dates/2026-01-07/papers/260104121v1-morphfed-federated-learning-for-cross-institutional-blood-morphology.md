---
layout: default
title: MORPHFED: Federated Learning for Cross-institutional Blood Morphology Analysis
---

# MORPHFED: Federated Learning for Cross-institutional Blood Morphology Analysis
**arXiv**：[2601.04121v1](https://arxiv.org/abs/2601.04121) · [PDF](https://arxiv.org/pdf/2601.04121.pdf)  
**作者**：Gabriel Ansah, Eden Ruffell, Delmiro Fernandez-Reyes, Petru Manescu  

**一句话要点**：提出联邦学习框架MORPHFED，用于跨机构血细胞形态分析以解决数据隐私和泛化问题。

**关键词**：联邦学习, 血细胞形态分析, 医学影像AI, 数据隐私, 跨机构协作

## 3 点简述
- 核心问题：血细胞形态分析在低收入和中等收入国家受数据集偏移影响，且集中式数据收集因隐私限制不可行。
- 方法要点：采用联邦学习，在不交换训练数据的情况下实现跨机构协作训练，学习鲁棒、领域不变的表示。
- 实验或效果：评估显示联邦模型在跨站点性能和泛化到未见机构方面优于集中式训练。

## 摘要（原文）

> Automated blood morphology analysis can support hematological diagnostics in low- and middle-income countries (LMICs) but remains sensitive to dataset shifts from staining variability, imaging differences, and rare morphologies. Building centralized datasets to capture this diversity is often infeasible due to privacy regulations and data-sharing restrictions. We introduce a federated learning framework for white blood cell morphology analysis that enables collaborative training across institutions without exchanging training data. Using blood films from multiple clinical sites, our federated models learn robust, domain-invariant representations while preserving complete data privacy. Evaluations across convolutional and transformer-based architectures show that federated training achieves strong cross-site performance and improved generalization to unseen institutions compared to centralized training. These findings highlight federated learning as a practical and privacy-preserving approach for developing equitable, scalable, and generalizable medical imaging AI in resource-limited healthcare environments.

