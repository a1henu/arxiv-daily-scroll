---
layout: default
title: Token Maturation: Autoregressive Language Generation via Continuous Token Dynamics
---

# Token Maturation: Autoregressive Language Generation via Continuous Token Dynamics
**arXiv**：[2601.04854v1](https://arxiv.org/abs/2601.04854) · [PDF](https://arxiv.org/pdf/2601.04854.pdf)  
**作者**：Oshri Naparstek  

**一句话要点**：提出连续令牌成熟方法，通过确定性动态过程实现稳定自回归语言生成，无需令牌级采样。

**关键词**：自回归语言模型, 连续令牌表示, 确定性解码, 令牌成熟, 稳定生成

## 3 点简述
- 核心问题：传统自回归模型早期离散化导致生成不稳定、重复和对解码启发式敏感。
- 方法要点：引入连续自回归公式，令牌表示为连续向量，成熟后离散化，避免令牌级采样。
- 实验或效果：仅成熟过程即可用确定性解码生成连贯多样文本，无需额外稳定机制。

## 摘要（原文）

> Autoregressive language models are conventionally defined over discrete token sequences, committing to a specific token at every generation step. This early discretization forces uncertainty to be resolved through token-level sampling, often leading to instability, repetition, and sensitivity to decoding heuristics.
>   In this work, we introduce a continuous autoregressive formulation of language generation in which tokens are represented as continuous vectors that \emph{mature} over multiple update steps before being discretized. Rather than sampling tokens, the model evolves continuous token representations through a deterministic dynamical process, committing to a discrete token only when the representation has sufficiently converged. Discrete text is recovered via hard decoding, while uncertainty is maintained and resolved in the continuous space.
>   We show that this maturation process alone is sufficient to produce coherent and diverse text using deterministic decoding (argmax), without reliance on token-level sampling, diffusion-style denoising, or auxiliary stabilization mechanisms. Additional perturbations, such as stochastic dynamics or history smoothing, can be incorporated naturally but are not required for the model to function.
>   To our knowledge, this is the first autoregressive language model that generates text by evolving continuous token representations to convergence prior to discretization, enabling stable generation without token-level sampling.

