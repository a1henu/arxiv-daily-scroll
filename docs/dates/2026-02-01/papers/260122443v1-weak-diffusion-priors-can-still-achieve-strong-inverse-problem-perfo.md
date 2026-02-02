---
layout: default
title: Weak Diffusion Priors Can Still Achieve Strong Inverse-Problem Performance
---

# Weak Diffusion Priors Can Still Achieve Strong Inverse-Problem Performance
**arXiv**：[2601.22443v1](https://arxiv.org/abs/2601.22443) · [PDF](https://arxiv.org/pdf/2601.22443.pdf)  
**作者**：Jing Jia, Wei Yuan, Sifan Liu, Liyue Shen, Guanyang Wang  

**一句话要点**：研究弱扩散先验在逆问题中的鲁棒性，揭示其适用条件与理论依据。

**关键词**：扩散模型, 逆问题求解, 贝叶斯一致性, 先验鲁棒性, 测量信息性

## 3 点简述
- 核心问题：弱或不匹配的扩散先验能否有效用于逆问题求解，如用卧室模型恢复人脸。
- 方法要点：通过贝叶斯一致性理论分析，给出高维测量使后验集中于真实信号的条件。
- 实验或效果：广泛实验表明，弱先验在测量信息丰富时性能接近强先验，并识别失效场景。

## 摘要（原文）

> Can a diffusion model trained on bedrooms recover human faces? Diffusion models are widely used as priors for inverse problems, but standard approaches usually assume a high-fidelity model trained on data that closely match the unknown signal. In practice, one often must use a mismatched or low-fidelity diffusion prior. Surprisingly, these weak priors often perform nearly as well as full-strength, in-domain baselines. We study when and why inverse solvers are robust to weak diffusion priors. Through extensive experiments, we find that weak priors succeed when measurements are highly informative (e.g., many observed pixels), and we identify regimes where they fail. Our theory, based on Bayesian consistency, gives conditions under which high-dimensional measurements make the posterior concentrate near the true signal. These results provide a principled justification on when weak diffusion priors can be used reliably.

