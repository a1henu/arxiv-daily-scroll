---
layout: default
title: Reward-Guided Discrete Diffusion via Clean-Sample Markov Chain for Molecule and Biological Sequence Design
---

# Reward-Guided Discrete Diffusion via Clean-Sample Markov Chain for Molecule and Biological Sequence Design
**arXiv**：[2602.09424v1](https://arxiv.org/abs/2602.09424) · [PDF](https://arxiv.org/pdf/2602.09424.pdf)  
**作者**：Prin Phunyaphibarn, Minhyuk Sung  

**一句话要点**：提出Clean-Sample Markov Chain采样器，通过清洁样本马尔可夫链实现分子和生物序列设计的奖励引导离散扩散。

**关键词**：离散扩散模型, 奖励引导采样, 分子设计, 生物序列生成, 马尔可夫链蒙特卡洛, 清洁样本采样

## 3 点简述
- 核心问题：现有离散扩散模型依赖中间奖励进行引导，但科学领域奖励函数非平滑导致中间奖励噪声大，性能受限。
- 方法要点：基于Metropolis-Hastings算法构建清洁样本马尔可夫链，其平稳分布为目标分布，通过顺序应用前向和后向扩散过程设计提案分布，实现无需中间奖励的局部搜索。
- 实验或效果：在分子和生物序列生成任务中，使用多种奖励函数验证，CSMC方法一致优于依赖中间奖励的先前方法。

## 摘要（原文）

> Discrete diffusion models have recently emerged as a powerful class of generative models for chemistry and biology data. In these fields, the goal is to generate various samples with high rewards (e.g., drug-likeness in molecules), making reward-based guidance crucial. Most existing methods are based on guiding the diffusion model using intermediate rewards but tend to underperform since intermediate rewards are noisy due to the non-smooth nature of reward functions used in scientific domains. To address this, we propose Clean-Sample Markov Chain (CSMC) Sampler, a method that performs effective test-time reward-guided sampling for discrete diffusion models, enabling local search without relying on intermediate rewards. CSMC constructs a Markov chain of clean samples using the Metropolis-Hastings algorithm such that its stationary distribution is the target distribution. We design a proposal distribution by sequentially applying the forward and backward diffusion processes, making the acceptance probability tractable. Experiments on molecule and biological sequence generation with various reward functions demonstrate that our method consistently outperforms prior approaches that rely on intermediate rewards.

