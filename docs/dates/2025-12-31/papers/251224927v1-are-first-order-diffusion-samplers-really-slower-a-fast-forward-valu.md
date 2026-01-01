---
layout: default
title: Are First-Order Diffusion Samplers Really Slower? A Fast Forward-Value Approach
---

# Are First-Order Diffusion Samplers Really Slower? A Fast Forward-Value Approach
**arXiv**：[2512.24927v1](https://arxiv.org/abs/2512.24927) · [PDF](https://arxiv.org/pdf/2512.24927.pdf)  
**作者**：Yuchen Jiao, Na Li, Changxiao Cai, Gen Li  

**一句话要点**：提出基于前向值评估的一阶扩散采样器，在低NFE下提升采样效率与质量。

**关键词**：扩散概率模型, 采样加速, 一阶方法, 前向值评估, ODE求解器, 图像生成

## 3 点简述
- 挑战高阶ODE求解器加速扩散采样的主流观点，强调评估点布局对低NFE精度的影响。
- 设计无需训练的一阶采样器，通过一步前瞻预测器近似前向值评估，理论保证收敛性。
- 在CIFAR-10等基准测试中，相同NFE下采样质量优于或媲美高阶方法，验证评估布局的独立加速潜力。

## 摘要（原文）

> Higher-order ODE solvers have become a standard tool for accelerating diffusion probabilistic model (DPM) sampling, motivating the widespread view that first-order methods are inherently slower and that increasing discretization order is the primary path to faster generation. This paper challenges this belief and revisits acceleration from a complementary angle: beyond solver order, the placement of DPM evaluations along the reverse-time dynamics can substantially affect sampling accuracy in the low-neural function evaluation (NFE) regime.
>   We propose a novel training-free, first-order sampler whose leading discretization error has the opposite sign to that of DDIM. Algorithmically, the method approximates the forward-value evaluation via a cheap one-step lookahead predictor. We provide theoretical guarantees showing that the resulting sampler provably approximates the ideal forward-value trajectory while retaining first-order convergence. Empirically, across standard image generation benchmarks (CIFAR-10, ImageNet, FFHQ, and LSUN), the proposed sampler consistently improves sample quality under the same NFE budget and can be competitive with, and sometimes outperform, state-of-the-art higher-order samplers. Overall, the results suggest that the placement of DPM evaluations provides an additional and largely independent design angle for accelerating diffusion sampling.

