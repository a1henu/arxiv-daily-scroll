---
layout: default
title: Count Bridges enable Modeling and Deconvolving Transcriptomic Data
---

# Count Bridges enable Modeling and Deconvolving Transcriptomic Data
**arXiv**：[2603.04730v1](https://arxiv.org/abs/2603.04730) · [PDF](https://arxiv.org/pdf/2603.04730.pdf)  
**作者**：Nic Fishman, Gokul Gowri, Tanush Kumar, Jiaqi Lu, Valentin de Bortoli, Jonathan S. Gootenberg, Omar Abudayyeh  

**一句话要点**：提出Count Bridges以建模和解卷积生物计数数据

**关键词**：计数数据建模, 随机桥过程, 解卷积方法, 生物信息学, 生成模型, RNA测序

## 3 点简述
- 核心问题：生物计数数据（如RNA测序）常为聚合观测，需建模整数分布和解卷积。
- 方法要点：引入整数上的随机桥过程，提供精确可处理的扩散式模型，支持EM训练。
- 实验或效果：在整数分布匹配基准上表现优异，应用于单细胞基因表达和空间转录组解卷积。

## 摘要（原文）

> Many modern biological assays, including RNA sequencing, yield integer-valued counts that reflect the number of molecules detected. These measurements are often not at the desired resolution: while the unit of interest is typically a single cell, many measurement technologies produce counts aggregated over sets of cells. Although recent generative frameworks such as diffusion and flow matching have been extended to non-Euclidean and discrete settings, it remains unclear how best to model integer-valued data or how to systematically deconvolve aggregated observations. We introduce Count Bridges, a stochastic bridge process on the integers that provides an exact, tractable analogue of diffusion-style models for count data, with closed-form conditionals for efficient training and sampling. We extend this framework to enable direct training from aggregated measurements via an Expectation-Maximization-style approach that treats unit-level counts as latent variables. We demonstrate state-of-the-art performance on integer distribution matching benchmarks, comparing against flow matching and discrete flow matching baselines across various metrics. We then apply Count Bridges to two large-scale problems in biology: modeling single-cell gene expression data at the nucleotide resolution, with applications to deconvolving bulk RNA-seq, and resolving multicellular spatial transcriptomic spots into single-cell count profiles. Our methods offer a principled foundation for generative modeling and deconvolution of biological count data across scales and modalities.

