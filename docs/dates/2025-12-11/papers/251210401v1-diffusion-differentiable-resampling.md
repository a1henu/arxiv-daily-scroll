---
layout: default
title: Diffusion differentiable resampling
---

# Diffusion differentiable resampling
**arXiv**：[2512.10401v1](https://arxiv.org/abs/2512.10401) · [PDF](https://arxiv.org/pdf/2512.10401.pdf)  
**作者**：Jennifer Rosina Andersson, Zheng Zhao  

**一句话要点**：提出基于集成分数扩散模型的路径可微重采样方法，用于序列蒙特卡洛中的可微重采样。

**关键词**：可微重采样, 序列蒙特卡洛, 粒子滤波, 扩散模型, 参数估计, 随机滤波

## 3 点简述
- 核心问题：序列蒙特卡洛（如粒子滤波）中的可微重采样问题，现有方法在可微性和信息保留方面存在局限。
- 方法要点：基于集成分数扩散模型，设计一种信息性重采样方法，实现即时路径可微性，并证明其一致性估计。
- 实验或效果：在随机滤波和参数估计任务中，实验显示该方法优于现有最先进的可微重采样方法。

## 摘要（原文）

> This paper is concerned with differentiable resampling in the context of sequential Monte Carlo (e.g., particle filtering). We propose a new informative resampling method that is instantly pathwise differentiable, based on an ensemble score diffusion model. We prove that our diffusion resampling method provides a consistent estimate to the resampling distribution, and we show by experiments that it outperforms the state-of-the-art differentiable resampling methods when used for stochastic filtering and parameter estimation.

