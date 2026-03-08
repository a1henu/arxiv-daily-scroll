---
layout: default
title: Distribution-Conditioned Transport
---

# Distribution-Conditioned Transport
**arXiv**：[2603.04736v1](https://arxiv.org/abs/2603.04736) · [PDF](https://arxiv.org/pdf/2603.04736.pdf)  
**作者**：Nic Fishman, Gokul Gowri, Paolo L. B. Fischer, Marinka Zitnik, Omar Abudayyeh, Jonathan Gootenberg  

**一句话要点**：提出分布条件传输框架，以解决未见分布对的泛化问题，支持半监督学习。

**关键词**：分布条件传输, 泛化学习, 半监督学习, 传输模型, 生物学应用, 分布嵌入

## 3 点简述
- 核心问题：传统传输模型难以泛化到训练中未见的源和目标分布。
- 方法要点：通过条件化传输映射于学习到的分布嵌入，实现分布对泛化。
- 实验或效果：在合成基准和四个生物学应用中展示性能优势，如单细胞基因组学批效应转移。

## 摘要（原文）

> Learning a transport model that maps a source distribution to a target distribution is a canonical problem in machine learning, but scientific applications increasingly require models that can generalize to source and target distributions unseen during training. We introduce distribution-conditioned transport (DCT), a framework that conditions transport maps on learned embeddings of source and target distributions, enabling generalization to unseen distribution pairs. DCT also allows semi-supervised learning for distributional forecasting problems: because it learns from arbitrary distribution pairs, it can leverage distributions observed at only one condition to improve transport prediction. DCT is agnostic to the underlying transport mechanism, supporting models ranging from flow matching to distributional divergence-based models (e.g. Wasserstein, MMD). We demonstrate the practical performance benefits of DCT on synthetic benchmarks and four applications in biology: batch effect transfer in single-cell genomics, perturbation prediction from mass cytometry data, learning clonal transcriptional dynamics in hematopoiesis, and modeling T-cell receptor sequence evolution.

