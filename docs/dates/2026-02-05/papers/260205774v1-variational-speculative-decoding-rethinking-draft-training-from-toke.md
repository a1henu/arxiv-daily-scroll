---
layout: default
title: Variational Speculative Decoding: Rethinking Draft Training from Token Likelihood to Sequence Acceptance
---

# Variational Speculative Decoding: Rethinking Draft Training from Token Likelihood to Sequence Acceptance
**arXiv**：[2602.05774v1](https://arxiv.org/abs/2602.05774) · [PDF](https://arxiv.org/pdf/2602.05774.pdf)  
**作者**：Xiandong Zou, Jianshu Li, Jing Huang, Pan Zhou  

**一句话要点**：提出变分推测解码以优化草稿训练，提升大模型推理速度

**关键词**：推测解码, 变分推断, 大语言模型, 推理加速, 草稿训练, 序列接受

## 3 点简述
- 现有推测解码方法训练与解码存在差异，草稿训练仅优化单一路径，而解码需验证多条路径
- VSD将草稿训练建模为变分推断，最大化目标模型接受概率，通过ELBO提升草稿质量并减少分布差异
- 实验显示VSD在LLMs和MLLMs上比EAGLE-3和ViSpec提速最高达9.6%和7.9%，显著提升解码效率

## 摘要（原文）

> Speculative decoding accelerates inference for (M)LLMs, yet a training-decoding discrepancy persists: while existing methods optimize single greedy trajectories, decoding involves verifying and ranking multiple sampled draft paths. We propose Variational Speculative Decoding (VSD), formulating draft training as variational inference over latent proposals (draft paths). VSD maximizes the marginal probability of target-model acceptance, yielding an ELBO that promotes high-quality latent proposals while minimizing divergence from the target distribution. To enhance quality and reduce variance, we incorporate a path-level utility and optimize via an Expectation-Maximization procedure. The E-step draws MCMC samples from an oracle-filtered posterior, while the M-step maximizes weighted likelihood using Adaptive Rejection Weighting (ARW) and Confidence-Aware Regularization (CAR). Theoretical analysis confirms that VSD increases expected acceptance length and speedup. Extensive experiments across LLMs and MLLMs show that VSD achieves up to a 9.6% speedup over EAGLE-3 and 7.9% over ViSpec, significantly improving decoding efficiency.

