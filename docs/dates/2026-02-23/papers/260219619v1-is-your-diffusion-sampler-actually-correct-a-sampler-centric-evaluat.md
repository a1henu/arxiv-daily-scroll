---
layout: default
title: Is Your Diffusion Sampler Actually Correct? A Sampler-Centric Evaluation of Discrete Diffusion Language Models
---

# Is Your Diffusion Sampler Actually Correct? A Sampler-Centric Evaluation of Discrete Diffusion Language Models
**arXiv**：[2602.19619v1](https://arxiv.org/abs/2602.19619) · [PDF](https://arxiv.org/pdf/2602.19619.pdf)  
**作者**：Luhan Tang, Longxuan Yu, Shaorong Zhang, Greg Ver Steeg  

**一句话要点**：提出采样器中心化评估框架，揭示离散扩散语言模型采样器分布错误问题

**关键词**：离散扩散语言模型, 采样器评估, 隐马尔可夫模型, 分布正确性, 去噪误差隔离

## 3 点简述
- 核心问题：现有评估指标混淆去噪器近似误差与采样器诱导误差，难以准确评估离散扩散模型
- 方法要点：引入基于隐马尔可夫模型后验的采样器中心化框架，隔离采样器误差在受控环境中
- 实验或效果：显示少步离散扩散采样器分布不正确，改进负对数似然等指标不保证正确采样

## 摘要（原文）

> Discrete diffusion language models (dLLMs) provide a fast and flexible alternative to autoregressive models (ARMs) via iterative denoising with parallel updates. However, their evaluation is challenging: existing metrics conflate denoiser approximation error with sampler-induced error from the sampling dynamics, a problem that does not arise for ARMs whose autoregressive sampling exactly reflects the learned probability model. We introduce a sampler-centric oracle framework that replaces learned denoisers with an exact Hidden Markov Model posterior derived from a ground-truth Markov chain, isolating sampler-induced error in a controlled setting. We show that few-step discrete diffusion samplers are not distributionally correct even under an oracle denoiser, with transition-level mismatch that vanishes only as the number of steps approaches the sequence length. Moreover, improvements in negative log-likelihood, generative perplexity, or MAUVE do not imply correct sampling. Code is available at https://luhantang.github.io/dllm_sampler

