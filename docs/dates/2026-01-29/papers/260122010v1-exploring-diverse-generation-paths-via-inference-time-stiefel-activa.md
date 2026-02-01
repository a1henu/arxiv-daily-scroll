---
layout: default
title: Exploring Diverse Generation Paths via Inference-time Stiefel Activation Steering
---

# Exploring Diverse Generation Paths via Inference-time Stiefel Activation Steering
**arXiv**：[2601.22010v1](https://arxiv.org/abs/2601.22010) · [PDF](https://arxiv.org/pdf/2601.22010.pdf)  
**作者**：Dongxuan Zhu, Ly Tran Ho Khanh, Andy Yat-Ming Cheung, Man-Chung Yue, Viet Anh Nguyen  

**一句话要点**：提出STARS方法，通过推理时Stiefel激活引导解决语言模型生成路径同质化问题。

**关键词**：推理时干预, 激活引导, Stiefel流形优化, 生成多样性, 语言模型

## 3 点简述
- 语言模型生成路径同质化，易陷入模式崩溃，采样方法难以保证多轮生成的多样性。
- STARS在推理时收集隐藏激活，在Stiefel流形上联合优化正交引导方向，最大化激活几何体积。
- 在测试用例生成和科学发现基准上，STARS优于标准采样方法，提升多样性且不牺牲质量。

## 摘要（原文）

> Language models often default to a narrow set of high-probability outputs, leaving their generation paths homogeneous and prone to mode collapse. Sampling-based strategies inject randomness but still struggle to guarantee diversity across multiple concurrent generation runs. We address this limitation by introducing STARS ($\textbf{St}$iefel-based $\textbf{A}$ctivation Steering for Diverse $\textbf{R}$ea$\textbf{S}$oning), a training-free, inference-time intervention method that transforms activation steering into an exploration engine. At each token, STARS collects the hidden activations of concurrent generation runs and optimizes multiple additive steering directions jointly on the Stiefel manifold. STARS maximizes the geometric volume of the steered activations, while the Stiefel manifold induces orthogonality of the steering interventions. This formulation explicitly promotes divergent activation vectors of concurrent generation runs, and implicitly promotes divergent generation trajectories. This manifold optimization formulation can be solved using a Riemannian gradient descent algorithm with convergence guarantees, but this algorithm is too time-consuming for real-time inference. To guarantee low latency, we further design a lightweight one-step update with an aggressive, closed-form stepsize. For test case generation and scientific discovery benchmarks, STARS consistently outperforms standard sampling methods, achieving greater diversity without sacrificing qualitative performance.

