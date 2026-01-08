---
layout: default
title: Causal Data Augmentation for Robust Fine-Tuning of Tabular Foundation Models
---

# Causal Data Augmentation for Robust Fine-Tuning of Tabular Foundation Models
**arXiv**：[2601.04110v1](https://arxiv.org/abs/2601.04110) · [PDF](https://arxiv.org/pdf/2601.04110.pdf)  
**作者**：Magnus Bühler, Lennart Purucker, Frank Hutter  

**一句话要点**：提出CausalMixFT方法，通过因果数据增强提升表格基础模型在数据稀缺下的微调鲁棒性。

**关键词**：表格基础模型, 因果数据增强, 微调鲁棒性, 数据稀缺, 结构因果模型, 早期停止

## 3 点简述
- 核心问题：数据稀缺下微调表格基础模型时，验证集性能难以反映真实泛化能力，导致早期停止不可靠。
- 方法要点：利用结构因果模型生成结构一致的合成样本，增强训练数据，保持特征依赖关系并增加多样性。
- 实验或效果：在33个分类数据集上评估，CausalMixFT将中位归一化ROC-AUC从0.10提升至0.12，优于统计生成方法，并缩小验证-测试性能相关性差距。

## 摘要（原文）

> Fine-tuning tabular foundation models (TFMs) under data scarcity is challenging, as early stopping on even scarcer validation data often fails to capture true generalization performance. We propose CausalMixFT, a method that enhances fine-tuning robustness and downstream performance by generating structurally consistent synthetic samples using Structural Causal Models (SCMs) fitted on the target dataset. This approach augments limited real data with causally informed synthetic examples, preserving feature dependencies while expanding training diversity. Evaluated across 33 classification datasets from TabArena and over 2300 fine-tuning runs, our CausalMixFT method consistently improves median normalized ROC-AUC from 0.10 (standard fine-tuning) to 0.12, outperforming purely statistical generators such as CTGAN (-0.01), TabEBM (-0.04), and TableAugment (-0.09). Moreover, it narrows the median validation-test performance correlation gap from 0.67 to 0.30, enabling more reliable validation-based early stopping, a key step toward improving fine-tuning stability under data scarcity. These results demonstrate that incorporating causal structure into data augmentation provides an effective and principled route to fine-tuning tabular foundation models in low-data regimes.

