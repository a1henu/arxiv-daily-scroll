---
layout: default
title: Diffusion Reconstruction-based Data Likelihood Estimation for Core-Set Selection
---

# Diffusion Reconstruction-based Data Likelihood Estimation for Core-Set Selection
**arXiv**：[2511.19274v1](https://arxiv.org/abs/2511.19274) · [PDF](https://arxiv.org/pdf/2511.19274.pdf)  
**作者**：Mingyang Chen, Jiawei Du, Bo Huang, Yi Wang, Xiaobo Zhang, Wei Wang  

**一句话要点**：提出基于扩散重建的数据似然估计方法以优化核心集选择

**关键词**：核心集选择, 扩散模型, 数据似然估计, 重建偏差, 信息理论优化

## 3 点简述
- 现有核心集选择方法依赖启发式评分，缺乏数据似然显式建模
- 利用扩散模型通过部分反向去噪重建偏差估计数据似然
- 在ImageNet上实验，仅用50%数据接近全数据训练效果

## 摘要（原文）

> Existing core-set selection methods predominantly rely on heuristic scoring signals such as training dynamics or model uncertainty, lacking explicit modeling of data likelihood. This omission may hinder the constructed subset from capturing subtle yet critical distributional structures that underpin effective model training. In this work, we propose a novel, theoretically grounded approach that leverages diffusion models to estimate data likelihood via reconstruction deviation induced by partial reverse denoising. Specifically, we establish a formal connection between reconstruction error and data likelihood, grounded in the Evidence Lower Bound (ELBO) of Markovian diffusion processes, thereby enabling a principled, distribution-aware scoring criterion for data selection. Complementarily, we introduce an efficient information-theoretic method to identify the optimal reconstruction timestep, ensuring that the deviation provides a reliable signal indicative of underlying data likelihood. Extensive experiments on ImageNet demonstrate that reconstruction deviation offers an effective scoring criterion, consistently outperforming existing baselines across selection ratios, and closely matching full-data training using only 50% of the data. Further analysis shows that the likelihood-informed nature of our score reveals informative insights in data selection, shedding light on the interplay between data distributional characteristics and model learning preferences.

