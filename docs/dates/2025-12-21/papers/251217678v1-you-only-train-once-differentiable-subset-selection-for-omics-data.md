---
layout: default
title: You Only Train Once: Differentiable Subset Selection for Omics Data
---

# You Only Train Once: Differentiable Subset Selection for Omics Data
**arXiv**：[2512.17678v1](https://arxiv.org/abs/2512.17678) · [PDF](https://arxiv.org/pdf/2512.17678.pdf)  
**作者**：Daphné Chopard, Jorge da Silva Gonçalves, Irene Cannistraci, Thomas M. Sutter, Julia E. Vogt  

**一句话要点**：提出YOTO框架以解决单细胞转录组数据中基因子集选择与预测任务弱耦合的问题

**关键词**：单细胞转录组学, 基因子集选择, 端到端学习, 可微分架构, 多任务学习, 生物标志物发现

## 3 点简述
- 核心问题：现有特征选择方法多为多阶段流程或依赖事后特征归因，导致选择与预测弱耦合
- 方法要点：YOTO通过可微分架构联合识别离散基因子集并进行预测，实现端到端训练
- 实验或效果：在单细胞RNA-seq数据集上评估，YOTO优于现有基线，提升预测性能并生成紧凑基因子集

## 摘要（原文）

> Selecting compact and informative gene subsets from single-cell transcriptomic data is essential for biomarker discovery, improving interpretability, and cost-effective profiling. However, most existing feature selection approaches either operate as multi-stage pipelines or rely on post hoc feature attribution, making selection and prediction weakly coupled. In this work, we present YOTO (you only train once), an end-to-end framework that jointly identifies discrete gene subsets and performs prediction within a single differentiable architecture. In our model, the prediction task directly guides which genes are selected, while the learned subsets, in turn, shape the predictive representation. This closed feedback loop enables the model to iteratively refine both what it selects and how it predicts during training. Unlike existing approaches, YOTO enforces sparsity so that only the selected genes contribute to inference, eliminating the need to train additional downstream classifiers. Through a multi-task learning design, the model learns shared representations across related objectives, allowing partially labeled datasets to inform one another, and discovering gene subsets that generalize across tasks without additional training steps. We evaluate YOTO on two representative single-cell RNA-seq datasets, showing that it consistently outperforms state-of-the-art baselines. These results demonstrate that sparse, end-to-end, multi-task gene subset selection improves predictive performance and yields compact and meaningful gene subsets, advancing biomarker discovery and single-cell analysis.

