---
layout: default
title: Score-Based Turbo Message Passing for Plug-and-Play Compressive Imaging
---

# Score-Based Turbo Message Passing for Plug-and-Play Compressive Imaging
**arXiv**：[2512.14435v1](https://arxiv.org/abs/2512.14435) · [PDF](https://arxiv.org/pdf/2512.14435.pdf)  
**作者**：Chang Cai, Hao Jiang, Xiaojun Yuan, Ying-Jun Angela Zhang  

**一句话要点**：提出基于分数的Turbo消息传递算法，用于即插即用压缩成像

**关键词**：压缩成像, 消息传递算法, 分数生成模型, 即插即用方法, 量化测量

## 3 点简述
- 传统即插即用方法依赖通用先验，在高度欠定压缩成像中重建效果不佳
- 结合分数生成模型与消息传递，设计最小均方误差去噪器以提升性能与效率
- 实验显示算法在FFHQ数据集上性能-复杂度权衡更优，量化下仍稳健

## 摘要（原文）

> Message-passing algorithms have been adapted for compressive imaging by incorporating various off-the-shelf image denoisers. However, these denoisers rely largely on generic or hand-crafted priors and often fall short in accurately capturing the complex statistical structure of natural images. As a result, traditional plug-and-play (PnP) methods often lead to suboptimal reconstruction, especially in highly underdetermined regimes. Recently, score-based generative models have emerged as a powerful framework for accurately characterizing sophisticated image distribution. Yet, their direct use for posterior sampling typically incurs prohibitive computational complexity. In this paper, by exploiting the close connection between score-based generative modeling and empirical Bayes denoising, we devise a message-passing framework that integrates a score-based minimum mean-squared error (MMSE) denoiser for compressive image recovery. The resulting algorithm, named score-based turbo message passing (STMP), combines the fast convergence of message passing with the expressive power of score-based generative priors. For practical systems with quantized measurements, we further propose quantized STMP (Q-STMP), which augments STMP with a component-wise MMSE dequantization module. We demonstrate that the asymptotic performance of STMP and Q-STMP can be accurately predicted by a set of state-evolution (SE) equations. Experiments on the FFHQ dataset demonstrate that STMP strikes a significantly better performance-complexity tradeoff compared with competing baselines, and that Q-STMP remains robust even under 1-bit quantization. Remarkably, both STMP and Q-STMP typically converge within 10 iterations.

