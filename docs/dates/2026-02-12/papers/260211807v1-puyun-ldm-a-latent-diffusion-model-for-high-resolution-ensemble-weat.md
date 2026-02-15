---
layout: default
title: PuYun-LDM: A Latent Diffusion Model for High-Resolution Ensemble Weather Forecasts
---

# PuYun-LDM: A Latent Diffusion Model for High-Resolution Ensemble Weather Forecasts
**arXiv**：[2602.11807v1](https://arxiv.org/abs/2602.11807) · [PDF](https://arxiv.org/pdf/2602.11807.pdf)  
**作者**：Lianjun Wu, Shengchen Zhu, Yuxuan Liu, Liuyu Kai, Xiaoduan Feng, Duomin Wang, Wenshuo Liu, Jingxuan Zhang, Kelvin Li, Bin Wang  

**一句话要点**：提出PuYun-LDM以解决高分辨率集合天气预报中潜在扩散模型扩散能力受限的问题

**关键词**：集合天气预报, 潜在扩散模型, 3D掩码自编码器, 变量感知正则化, 高分辨率气象数据, 谱异质性

## 3 点简述
- 核心问题：高分辨率集合天气预报中，潜在扩散模型扩散能力受限，且气象数据缺乏通用基础模型和语义结构，现有频率方法在变量间谱异质性下正则化不均。
- 方法要点：引入3D掩码自编码器编码天气状态演化特征作为扩散模型条件，并提出变量感知掩码频率建模策略自适应调整正则化阈值。
- 实验或效果：PuYun-LDM在短预报时效优于ENS，长时效与ENS相当，可在单GPU上快速生成15天全球预报。

## 摘要（原文）

> Latent diffusion models (LDMs) suffer from limited diffusability in high-resolution (<=0.25°) ensemble weather forecasting, where diffusability characterizes how easily a latent data distribution can be modeled by a diffusion process. Unlike natural image fields, meteorological fields lack task-agnostic foundation models and explicit semantic structures, making VFM-based regularization inapplicable. Moreover, existing frequency-based approaches impose identical spectral regularization across channels under a homogeneity assumption, which leads to uneven regularization strength under the inter-variable spectral heterogeneity in multivariate meteorological data. To address these challenges, we propose a 3D Masked AutoEncoder (3D-MAE) that encodes weather-state evolution features as an additional conditioning for the diffusion model, together with a Variable-Aware Masked Frequency Modeling (VA-MFM) strategy that adaptively selects thresholds based on the spectral energy distribution of each variable. Together, we propose PuYun-LDM, which enhances latent diffusability and achieves superior performance to ENS at short lead times while remaining comparable to ENS at longer horizons. PuYun-LDM generates a 15-day global forecast with a 6-hour temporal resolution in five minutes on a single NVIDIA H200 GPU, while ensemble forecasts can be efficiently produced in parallel.

