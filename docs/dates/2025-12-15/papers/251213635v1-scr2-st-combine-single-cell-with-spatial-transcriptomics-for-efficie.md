---
layout: default
title: SCR2-ST: Combine Single Cell with Spatial Transcriptomics for Efficient Active Sampling via Reinforcement Learning
---

# SCR2-ST: Combine Single Cell with Spatial Transcriptomics for Efficient Active Sampling via Reinforcement Learning
**arXiv**：[2512.13635v1](https://arxiv.org/abs/2512.13635) · [PDF](https://arxiv.org/pdf/2512.13635.pdf)  
**作者**：Junchao Zhu, Ruining Deng, Junlin Guo, Tianyuan Yao, Chongyu Qu, Juming Xiong, Siqi Lu, Zhengyi Lu, Yanfan Zhu, Marilyn Lionts, Yuechen Yang, Yalin Zheng, Yu Wang, Shilin Zhao, Haichun Yang, Yuankai Huo  

**一句话要点**：提出SCR2-ST框架，结合单细胞与空间转录组学，通过强化学习实现高效主动采样与表达预测。

**关键词**：空间转录组学, 单细胞测序, 强化学习, 主动采样, 表达预测, 混合网络

## 3 点简述
- 核心问题：空间转录组学数据获取昂贵，固定网格采样导致冗余，限制方法发展。
- 方法要点：利用单细胞先验知识，通过强化学习指导采样，结合回归-检索网络进行预测。
- 实验或效果：在三个公共数据集上验证，在低预算场景下实现采样效率和预测准确性的SOTA性能。

## 摘要（原文）

> Spatial transcriptomics (ST) is an emerging technology that enables researchers to investigate the molecular relationships underlying tissue morphology. However, acquiring ST data remains prohibitively expensive, and traditional fixed-grid sampling strategies lead to redundant measurements of morphologically similar or biologically uninformative regions, thus resulting in scarce data that constrain current methods. The well-established single-cell sequencing field, however, could provide rich biological data as an effective auxiliary source to mitigate this limitation. To bridge these gaps, we introduce SCR2-ST, a unified framework that leverages single-cell prior knowledge to guide efficient data acquisition and accurate expression prediction. SCR2-ST integrates a single-cell guided reinforcement learning-based (SCRL) active sampling and a hybrid regression-retrieval prediction network SCR2Net. SCRL combines single-cell foundation model embeddings with spatial density information to construct biologically grounded reward signals, enabling selective acquisition of informative tissue regions under constrained sequencing budgets. SCR2Net then leverages the actively sampled data through a hybrid architecture combining regression-based modeling with retrieval-augmented inference, where a majority cell-type filtering mechanism suppresses noisy matches and retrieved expression profiles serve as soft labels for auxiliary supervision. We evaluated SCR2-ST on three public ST datasets, demonstrating SOTA performance in both sampling efficiency and prediction accuracy, particularly under low-budget scenarios. Code is publicly available at: https://github.com/hrlblab/SCR2ST

