---
layout: default
title: Stratified Hazard Sampling: Minimal-Variance Event Scheduling for CTMC/DTMC Discrete Diffusion and Flow Models
---

# Stratified Hazard Sampling: Minimal-Variance Event Scheduling for CTMC/DTMC Discrete Diffusion and Flow Models
**arXiv**：[2601.02799v1](https://arxiv.org/abs/2601.02799) · [PDF](https://arxiv.org/pdf/2601.02799.pdf)  
**作者**：Seunghwan Jang, SooJean Han  

**一句话要点**：提出分层风险采样以最小化CTMC/DTMC离散扩散模型推理中的编辑方差

**关键词**：离散扩散模型, 推理采样, 方差最小化, 分层采样, 累积风险, 非自回归生成

## 3 点简述
- 核心问题：独立伯努利采样导致编辑次数和时机方差大，引发欠编辑或过编辑
- 方法要点：通过分层累积风险安排事件，保持期望编辑数并最小化方差
- 实验或效果：实现最小可能方差，保留多模态性，支持词汇约束变体

## 摘要（原文）

> CTMC/DTMC-based discrete generative models, including uniform-noise discrete diffusion (e.g., D3PM/CTDD) and discrete flow matching, enable non-autoregressive sequence generation by repeatedly replacing tokens through a time-inhomogeneous Markov process. Inference is typically implemented with step-based simulation: each token decides to jump via independent Bernoulli (or categorical) draws at every discretization step. Under uniform-noise initialization, where self-correction requires multiple edits per position, these independent decisions induce substantial variance in both the number and timing of edits, leading to characteristic failure modes such as under-editing (residual noise) or over-editing (cascading unnecessary substitutions), decreasing reproducibility.
>   We propose Stratified Hazard Sampling (SHS), a drop-in and hyperparameter-free inference principle for any sampler that admits a stay-vs.-replace decomposition. SHS models per-token edits as events driven by cumulative hazard (CTMC) or cumulative jump mass (DTMC) and places events by stratifying this cumulative quantity: with a single random phase per position, a token jumps whenever its accumulated hazard crosses unit-spaced thresholds. This preserves the expected number of jumps while achieving the minimum possible variance among unbiased integer estimators (bounded by 1/4), without altering per-jump destination sampling and thus retaining multimodality. We also introduce a phase-allocation variant for blacklist-style lexical constraints that prioritizes early edits at high-risk positions to mitigate late-masking artifacts.

