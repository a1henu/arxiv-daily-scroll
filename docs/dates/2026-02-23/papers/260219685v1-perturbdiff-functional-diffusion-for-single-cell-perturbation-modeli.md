---
layout: default
title: PerturbDiff: Functional Diffusion for Single-Cell Perturbation Modeling
---

# PerturbDiff: Functional Diffusion for Single-Cell Perturbation Modeling
**arXiv**：[2602.19685v1](https://arxiv.org/abs/2602.19685) · [PDF](https://arxiv.org/pdf/2602.19685.pdf)  
**作者**：Xinyu Yuan, Xixian Liu, Ya Shi Zhang, Zuobai Zhang, Hongyu Guo, Jian Tang  

**一句话要点**：提出PerturbDiff以解决单细胞扰动建模中响应分布可变性问题

**关键词**：单细胞扰动建模, 分布嵌入, 扩散生成模型, 系统生物学, 虚拟细胞构建

## 3 点简述
- 核心问题：单细胞测序破坏性导致扰动前后细胞无法配对，且响应分布因隐藏因素可变
- 方法要点：在希尔伯特空间嵌入分布，基于扩散过程直接生成概率分布以捕获群体级响应变化
- 实验或效果：在基准数据集上实现最先进的预测性能，对未见扰动泛化能力显著提升

## 摘要（原文）

> Building Virtual Cells that can accurately simulate cellular responses to perturbations is a long-standing goal in systems biology. A fundamental challenge is that high-throughput single-cell sequencing is destructive: the same cell cannot be observed both before and after a perturbation. Thus, perturbation prediction requires mapping unpaired control and perturbed populations. Existing models address this by learning maps between distributions, but typically assume a single fixed response distribution when conditioned on observed cellular context (e.g., cell type) and the perturbation type. In reality, responses vary systematically due to unobservable latent factors such as microenvironmental fluctuations and complex batch effects, forming a manifold of possible distributions for the same observed conditions. To account for this variability, we introduce PerturbDiff, which shifts modeling from individual cells to entire distributions. By embedding distributions as points in a Hilbert space, we define a diffusion-based generative process operating directly over probability distributions. This allows PerturbDiff to capture population-level response shifts across hidden factors. Benchmarks on established datasets show that PerturbDiff achieves state-of-the-art performance in single-cell response prediction and generalizes substantially better to unseen perturbations. See our project page (https://katarinayuan.github.io/PerturbDiff-ProjectPage/), where code and data will be made publicly available (https://github.com/DeepGraphLearning/PerturbDiff).

