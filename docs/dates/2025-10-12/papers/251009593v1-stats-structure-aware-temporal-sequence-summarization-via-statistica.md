---
layout: default
title: STaTS: Structure-Aware Temporal Sequence Summarization via Statistical Window Merging
---

# STaTS: Structure-Aware Temporal Sequence Summarization via Statistical Window Merging
**arXiv**：[2510.09593v1](https://arxiv.org/abs/2510.09593) · [PDF](https://arxiv.org/pdf/2510.09593.pdf)  
**作者**：Disharee Bhowmick, Ranjith Ramanathan, Sathyanarayanan N. Aakur  
**一句话要点**：提出STaTS框架以高效压缩时间序列并保留结构信息
**关键词**：时间序列压缩, 结构感知建模, 无监督学习, 变点检测, 计算效率优化

## 3 点简述
- 时间序列数据常含潜在结构，但现有方法处理效率低且鲁棒性差
- 使用统计差异检测变点，自适应压缩为紧凑令牌序列
- 实验显示压缩达30倍，保持85-90%性能，提升噪声鲁棒性

## 摘要（原文）

> Time series data often contain latent temporal structure, transitions between
> locally stationary regimes, repeated motifs, and bursts of variability, that
> are rarely leveraged in standard representation learning pipelines. Existing
> models typically operate on raw or fixed-window sequences, treating all time
> steps as equally informative, which leads to inefficiencies, poor robustness,
> and limited scalability in long or noisy sequences. We propose STaTS, a
> lightweight, unsupervised framework for Structure-Aware Temporal Summarization
> that adaptively compresses both univariate and multivariate time series into
> compact, information-preserving token sequences. STaTS detects change points
> across multiple temporal resolutions using a BIC-based statistical divergence
> criterion, then summarizes each segment using simple functions like the mean or
> generative models such as GMMs. This process achieves up to 30x sequence
> compression while retaining core temporal dynamics. STaTS operates as a
> model-agnostic preprocessor and can be integrated with existing unsupervised
> time series encoders without retraining. Extensive experiments on 150+
> datasets, including classification tasks on the UCR-85, UCR-128, and UEA-30
> archives, and forecasting on ETTh1 and ETTh2, ETTm1, and Electricity,
> demonstrate that STaTS enables 85-90\% of the full-model performance while
> offering dramatic reductions in computational cost. Moreover, STaTS improves
> robustness under noise and preserves discriminative structure, outperforming
> uniform and clustering-based compression baselines. These results position
> STaTS as a principled, general-purpose solution for efficient, structure-aware
> time series modeling.

