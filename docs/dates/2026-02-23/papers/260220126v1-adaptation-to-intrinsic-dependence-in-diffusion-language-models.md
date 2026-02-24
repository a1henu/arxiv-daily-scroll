---
layout: default
title: Adaptation to Intrinsic Dependence in Diffusion Language Models
---

# Adaptation to Intrinsic Dependence in Diffusion Language Models
**arXiv**：[2602.20126v1](https://arxiv.org/abs/2602.20126) · [PDF](https://arxiv.org/pdf/2602.20126.pdf)  
**作者**：Yunxiao Zhao, Changxiao Cai  

**一句话要点**：提出自适应去掩码调度方法，以提升扩散语言模型的生成质量与效率。

**关键词**：扩散语言模型, 去掩码调度, 自适应采样, 并行生成, 理论分析

## 3 点简述
- 核心问题：去掩码调度对扩散语言模型生成质量的影响缺乏理论理解。
- 方法要点：引入分布无关的自适应去掩码调度，随机化每步揭示的令牌数量。
- 实验或效果：理论保证收敛速度与数据内在依赖结构相关，显著加速低复杂度分布的采样。

## 摘要（原文）

> Diffusion language models (DLMs) have recently emerged as a promising alternative to autoregressive (AR) approaches, enabling parallel token generation beyond a rigid left-to-right order. Despite growing empirical success, the theoretical understanding of how unmasking schedules -- which specify the order and size of unmasked tokens during sampling -- affect generation quality remains limited. In this work, we introduce a distribution-agnostic unmasking schedule for DLMs that adapts to the (unknown) dependence structure of the target data distribution, without requiring any prior knowledge or hyperparameter tuning. In contrast to prior deterministic procedures that fix unmasking sizes, our method randomizes the number of tokens revealed at each iteration. We show that, for two specific parameter choices, the sampling convergence guarantees -- measured by Kullback-Leibler (KL) divergence -- scale as $\widetilde O(\mathsf{TC}/K)$ and $\widetilde O(\mathsf{DTC}/K)$ respectively. Here, $K$ is the number of iterations, and $\mathsf{TC}$ and $\mathsf{DTC}$ are the total correlation and dual total correlation of the target distribution, capturing the intrinsic dependence structure underlying the data. Importantly, our guarantees hold in the practically relevant parallel-sampling regime $K<L$ where $L$ is the token sequence length. These results significantly improve upon prior convergence theories and yield substantial sampling acceleration for low-complexity distributions. Overall, our findings unveil the adaptivity of DLMs to intrinsic data structures and shed light on the benefit of randomized unmasking sizes in inference schedule design.

