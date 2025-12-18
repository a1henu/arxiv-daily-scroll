---
layout: default
title: FADTI: Fourier and Attention Driven Diffusion for Multivariate Time Series Imputation
---

# FADTI: Fourier and Attention Driven Diffusion for Multivariate Time Series Imputation
**arXiv**：[2512.15116v1](https://arxiv.org/abs/2512.15116) · [PDF](https://arxiv.org/pdf/2512.15116.pdf)  
**作者**：Runze Li, Hanchen Wang, Wenjie Zhang, Binghao Li, Yu Zhang, Xuemin Lin, Ying Zhang  

**一句话要点**：提出FADTI框架，通过傅里叶偏置投影和注意力机制解决多元时间序列插补问题。

**关键词**：多元时间序列插补, 扩散模型, 傅里叶变换, 注意力机制, 频域归纳偏置, 高缺失率处理

## 3 点简述
- 核心问题：现有Transformer和扩散模型缺乏显式归纳偏置和频率感知，限制在结构化缺失和分布偏移下的泛化能力。
- 方法要点：引入可学习傅里叶偏置投影模块，结合自注意力和门控卷积，注入频域归纳偏置以自适应编码平稳与非平稳模式。
- 实验或效果：在多个基准测试中，包括新生物时间序列数据集，FADTI优于现有方法，尤其在高缺失率下表现突出。

## 摘要（原文）

> Multivariate time series imputation is fundamental in applications such as healthcare, traffic forecasting, and biological modeling, where sensor failures and irregular sampling lead to pervasive missing values. However, existing Transformer- and diffusion-based models lack explicit inductive biases and frequency awareness, limiting their generalization under structured missing patterns and distribution shifts. We propose FADTI, a diffusion-based framework that injects frequency-informed feature modulation via a learnable Fourier Bias Projection (FBP) module and combines it with temporal modeling through self-attention and gated convolution. FBP supports multiple spectral bases, enabling adaptive encoding of both stationary and non-stationary patterns. This design injects frequency-domain inductive bias into the generative imputation process. Experiments on multiple benchmarks, including a newly introduced biological time series dataset, show that FADTI consistently outperforms state-of-the-art methods, particularly under high missing rates. Code is available at https://anonymous.4open.science/r/TimeSeriesImputation-52BF

