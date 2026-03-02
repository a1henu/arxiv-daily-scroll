---
layout: default
title: Selective Denoising Diffusion Model for Time Series Anomaly Detection
---

# Selective Denoising Diffusion Model for Time Series Anomaly Detection
**arXiv**：[2602.23662v1](https://arxiv.org/abs/2602.23662) · [PDF](https://arxiv.org/pdf/2602.23662.pdf)  
**作者**：Kohei Obata, Zheng Chen, Yasuko Matsubara, Lingwei Zhu, Yasushi Sakurai  

**一句话要点**：提出AnomalyFilter选择性去噪扩散模型以提升时间序列异常检测性能

**关键词**：时间序列异常检测, 扩散模型, 选择性去噪, 重构误差, 生成模型

## 3 点简述
- 现有基于扩散模型的时间序列异常检测方法依赖条件策略，难以准确重构正常部分，导致检测性能不佳。
- AnomalyFilter通过掩码高斯噪声训练和去噪过程，仅处理异常部分，保留正常部分，实现选择性过滤。
- 在五个数据集上的实验表明，该方法显著降低正常部分重构误差，验证了其在异常检测中的有效性。

## 摘要（原文）

> Time series anomaly detection (TSAD) has been an important area of research for decades, with reconstruction-based methods, mostly based on generative models, gaining popularity and demonstrating success. Diffusion models have recently attracted attention due to their advanced generative capabilities. Existing diffusion-based methods for TSAD rely on a conditional strategy, which reconstructs input instances from white noise with the aid of the conditioner. However, this poses challenges in accurately reconstructing the normal parts, resulting in suboptimal detection performance. In response, we propose a novel diffusion-based method, named AnomalyFilter, which acts as a selective filter that only denoises anomaly parts in the instance while retaining normal parts. To build such a filter, we mask Gaussian noise during the training phase and conduct the denoising process without adding noise to the instances. The synergy of the two simple components greatly enhances the performance of naive diffusion models. Extensive experiments on five datasets demonstrate that AnomalyFilter achieves notably low reconstruction error on normal parts, providing empirical support for its effectiveness in anomaly detection. AnomalyFilter represents a pioneering approach that focuses on the noise design of diffusion models specifically tailored for TSAD.

