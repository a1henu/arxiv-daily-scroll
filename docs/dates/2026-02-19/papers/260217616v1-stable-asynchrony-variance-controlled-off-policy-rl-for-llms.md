---
layout: default
title: Stable Asynchrony: Variance-Controlled Off-Policy RL for LLMs
---

# Stable Asynchrony: Variance-Controlled Off-Policy RL for LLMs
**arXiv**：[2602.17616v1](https://arxiv.org/abs/2602.17616) · [PDF](https://arxiv.org/pdf/2602.17616.pdf)  
**作者**：Luke Huang, Zhuoyang Zhang, Qinghao Hu, Shang Yang, Song Han  

**一句话要点**：提出VCPO以稳定异步强化学习中的高方差问题，提升大语言模型训练效率。

**关键词**：异步强化学习, 策略梯度方差控制, 大语言模型训练, 有效样本量, 最小方差基线

## 3 点简述
- 核心问题：异步训练导致策略梯度估计方差增大，引发学习不稳定和崩溃。
- 方法要点：基于有效样本量调整学习率，并应用最小方差基线以控制方差。
- 实验或效果：在数学、推理和工具使用任务中提升鲁棒性，训练时间减少2.5倍。

## 摘要（原文）

> Reinforcement learning (RL) is widely used to improve large language models on reasoning tasks, and asynchronous RL training is attractive because it increases end-to-end throughput. However, for widely adopted critic-free policy-gradient methods such as REINFORCE and GRPO, high asynchrony makes the policy-gradient estimator markedly $\textbf{higher variance}$: training on stale rollouts creates heavy-tailed importance ratios, causing a small fraction of samples to dominate updates. This amplification makes gradients noisy and learning unstable relative to matched on-policy training. Across math and general reasoning benchmarks, we find collapse is reliably predicted by effective sample size (ESS) and unstable gradient norms. Motivated by this diagnosis, we propose $\textbf{V}$ariance $\textbf{C}$ontrolled $\textbf{P}$olicy $\textbf{O}$ptimization ($\textbf{VCPO}$), a general stabilization method for REINFORCE/GRPO-style algorithms that (i) scales learning rate based on effective sample size to dampen unreliable updates, and (ii) applies a closed-form minimum-variance baseline for the off-policy setting, avoiding an auxiliary value model and adding minimal overhead. Empirically, VCPO substantially improves robustness for asynchronous training across math, general reasoning, and tool-use tasks, outperforming a broad suite of baselines spanning masking/clipping stabilizers and algorithmic variants. This reduces long-context, multi-turn training time by 2.5$\times$ while matching synchronous performance, demonstrating that explicit control of policy-gradient variance is key for reliable asynchronous RL at scale.

