---
layout: default
title: Quantum Diffusion Models: Score Reversal Is Not Free in Gaussian Dynamics
---

# Quantum Diffusion Models: Score Reversal Is Not Free in Gaussian Dynamics
**arXiv**：[2603.06488v1](https://arxiv.org/abs/2603.06488) · [PDF](https://arxiv.org/pdf/2603.06488.pdf)  
**作者**：Ammar Fayad  

**一句话要点**：揭示量子扩散模型中高斯动力学下分数反转的完全正性约束与修复代价

**关键词**：量子扩散模型, 高斯动力学, 完全正性, 分数反转, Wigner函数, 信息衰减

## 3 点简述
- 研究量子扩散模型中高斯马尔可夫动力学的分数反转问题，关注完全正性耦合
- 发现固定扩散Wigner分数反向漂移在特定条件下违反完全正性，需额外扩散修复
- 推导修复代价的下界，涉及几何常数与最坏情况信息衰减

## 摘要（原文）

> Diffusion-based generative modeling suggests reversing a noising semigroup by adding a score drift. For continuous-variable Gaussian Markov dynamics, complete positivity couples drift and diffusion at the generator level. For a quantum-limited attenuator with thermal parameter $ν$ and squeezing $r$, the fixed-diffusion Wigner-score (Bayes) reverse drift violates CP iff $\cosh(2r)>ν$. Any Gaussian CP repair must inject extra diffusion, implying $-2\ln F\ge c_{\text{geom}}(ν_{\min})I_{\mathrm{dec}}^{\mathrm{wc}}$.

