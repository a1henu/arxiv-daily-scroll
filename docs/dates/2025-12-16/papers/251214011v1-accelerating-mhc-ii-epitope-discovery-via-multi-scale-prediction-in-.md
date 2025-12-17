---
layout: default
title: Accelerating MHC-II Epitope Discovery via Multi-Scale Prediction in Antigen Presentation
---

# Accelerating MHC-II Epitope Discovery via Multi-Scale Prediction in Antigen Presentation
**arXiv**：[2512.14011v1](https://arxiv.org/abs/2512.14011) · [PDF](https://arxiv.org/pdf/2512.14011.pdf)  
**作者**：Yue Wan, Jiayi Yuan, Zhiwei Feng, Xiaowei Jia  

**一句话要点**：提出多尺度预测框架以加速MHC-II抗原呈递中的表位发现

**关键词**：MHC-II表位预测, 抗原呈递, 机器学习任务, 多尺度评估, 数据集标准化, 计算免疫疗法

## 3 点简述
- 核心问题：MHC-II表位预测因结合特异性复杂和数据集小而不如MHC-I成熟。
- 方法要点：构建标准化数据集并定义肽结合、呈递和抗原呈递三个机器学习任务。
- 实验或效果：通过多尺度评估框架基准测试现有模型，分析建模设计以提供资源基础。

## 摘要（原文）

> Antigenic epitope presented by major histocompatibility complex II (MHC-II) proteins plays an essential role in immunotherapy. However, compared to the more widely studied MHC-I in computational immunotherapy, the study of MHC-II antigenic epitope poses significantly more challenges due to its complex binding specificity and ambiguous motif patterns. Consequently, existing datasets for MHC-II interactions are smaller and less standardized than those available for MHC-I. To address these challenges, we present a well-curated dataset derived from the Immune Epitope Database (IEDB) and other public sources. It not only extends and standardizes existing peptide-MHC-II datasets, but also introduces a novel antigen-MHC-II dataset with richer biological context. Leveraging this dataset, we formulate three major machine learning (ML) tasks of peptide binding, peptide presentation, and antigen presentation, which progressively capture the broader biological processes within the MHC-II antigen presentation pathway. We further employ a multi-scale evaluation framework to benchmark existing models, along with a comprehensive analysis over various modeling designs to this problem with a modular framework. Overall, this work serves as a valuable resource for advancing computational immunotherapy, providing a foundation for future research in ML guided epitope discovery and predictive modeling of immune responses.

