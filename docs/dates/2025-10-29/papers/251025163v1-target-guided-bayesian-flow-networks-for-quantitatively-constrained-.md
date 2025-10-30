---
layout: default
title: Target-Guided Bayesian Flow Networks for Quantitatively Constrained CAD Generation
---

# Target-Guided Bayesian Flow Networks for Quantitatively Constrained CAD Generation
**arXiv**：[2510.25163v1](https://arxiv.org/abs/2510.25163) · [PDF](https://arxiv.org/pdf/2510.25163.pdf)  
**作者**：Wenhao Zheng, Chenwei Sun, Wenbo Zhang, Jiancheng Lv, Xianggen Liu  

**一句话要点**：提出目标引导贝叶斯流网络以解决定量约束CAD生成问题

**关键词**：CAD生成, 贝叶斯流网络, 多模态数据, 参数约束, 生成模型

## 3 点简述
- 核心问题：多模态CAD序列生成面临长范围约束和参数敏感性挑战
- 方法要点：在统一连续可微参数空间处理离散命令和连续参数
- 实验或效果：在单条件和多条件约束任务中实现最先进性能

## 摘要（原文）

> Deep generative models, such as diffusion models, have shown promising
> progress in image generation and audio generation via simplified continuity
> assumptions. However, the development of generative modeling techniques for
> generating multi-modal data, such as parametric CAD sequences, still lags
> behind due to the challenges in addressing long-range constraints and parameter
> sensitivity. In this work, we propose a novel framework for quantitatively
> constrained CAD generation, termed Target-Guided Bayesian Flow Network (TGBFN).
> For the first time, TGBFN handles the multi-modality of CAD sequences (i.e.,
> discrete commands and continuous parameters) in a unified continuous and
> differentiable parameter space rather than in the discrete data space. In
> addition, TGBFN penetrates the parameter update kernel and introduces a guided
> Bayesian flow to control the CAD properties. To evaluate TGBFN, we construct a
> new dataset for quantitatively constrained CAD generation. Extensive
> comparisons across single-condition and multi-condition constrained generation
> tasks demonstrate that TGBFN achieves state-of-the-art performance in
> generating high-fidelity, condition-aware CAD sequences. The code is available
> at https://github.com/scu-zwh/TGBFN.

