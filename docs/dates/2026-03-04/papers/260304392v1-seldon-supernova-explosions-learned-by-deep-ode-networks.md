---
layout: default
title: SELDON: Supernova Explosions Learned by Deep ODE Networks
---

# SELDON: Supernova Explosions Learned by Deep ODE Networks
**arXiv**：[2603.04392v1](https://arxiv.org/abs/2603.04392) · [PDF](https://arxiv.org/pdf/2603.04392.pdf)  
**作者**：Jiezhong Wu, Jack O'Brien, Jennifer Li, M. S. Krafczyk, Ved G. Shah, Amanda R. Wasserman, Daniel W. Apley, Gautham Narayan, Noelle I. Samia  

**一句话要点**：提出SELDON以解决稀疏不规则天体光变曲线连续时间预测问题

**关键词**：连续时间预测, 变分自编码器, 神经ODE, 稀疏时间序列, 天体光变曲线, 可解释建模

## 3 点简述
- 核心问题：传统物理推断方法无法处理未来天文观测中大量稀疏、非平稳、异方差的光变曲线数据。
- 方法要点：结合掩码GRU-ODE编码器、神经ODE传播器和可解释高斯基解码器，实现连续时间建模。
- 实验或效果：模型能快速推断物理参数，支持天体光谱后续观测的优先级排序，适用于多领域稀疏时间序列。

## 摘要（原文）

> The discovery rate of optical transients will explode to 10 million public alerts per night once the Vera C. Rubin Observatory's Legacy Survey of Space and Time comes online, overwhelming the traditional physics-based inference pipelines. A continuous-time forecasting AI model is of interest because it can deliver millisecond-scale inference for thousands of objects per day, whereas legacy MCMC codes need hours per object. In this paper, we propose SELDON, a new continuous-time variational autoencoder for panels of sparse and irregularly time-sampled (gappy) astrophysical light curves that are nonstationary, heteroscedastic, and inherently dependent. SELDON combines a masked GRU-ODE encoder with a latent neural ODE propagator and an interpretable Gaussian-basis decoder. The encoder learns to summarize panels of imbalanced and correlated data even when only a handful of points are observed. The neural ODE then integrates this hidden state forward in continuous time, extrapolating to future unseen epochs. This extrapolated time series is further encoded by deep sets to a latent distribution that is decoded to a weighted sum of Gaussian basis functions, the parameters of which are physically meaningful. Such parameters (e.g., rise time, decay rate, peak flux) directly drive downstream prioritization of spectroscopic follow-up for astrophysical surveys. Beyond astronomy, the architecture of SELDON offers a generic recipe for interpretable and continuous-time sequence modeling in any time domain where data are multivariate, sparse, heteroscedastic, and irregularly spaced.

