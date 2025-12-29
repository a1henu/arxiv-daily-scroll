---
layout: default
title: Unifying Learning Dynamics and Generalization in Transformers Scaling Law
---

# Unifying Learning Dynamics and Generalization in Transformers Scaling Law
**arXiv**：[2512.22088v1](https://arxiv.org/abs/2512.22088) · [PDF](https://arxiv.org/pdf/2512.22088.pdf)  
**作者**：Chiwun Yang  

**一句话要点**：提出统一学习动态与泛化的Transformer缩放定律理论框架

**关键词**：缩放定律, Transformer, 学习动态, 泛化误差, SGD训练, 理论分析

## 3 点简述
- 核心问题：缩放定律的理论基础不明确，缺乏对学习动态和泛化误差的严格分析
- 方法要点：将Transformer学习动态建模为ODE系统，近似为核行为，分析SGD训练
- 实验或效果：理论推导出泛化误差上界，揭示指数衰减和幂律衰减的相变

## 摘要（原文）

> The scaling law, a cornerstone of Large Language Model (LLM) development, predicts improvements in model performance with increasing computational resources. Yet, while empirically validated, its theoretical underpinnings remain poorly understood. This work formalizes the learning dynamics of transformer-based language models as an ordinary differential equation (ODE) system, then approximates this process to kernel behaviors. Departing from prior toy-model analyses, we rigorously analyze stochastic gradient descent (SGD) training for multi-layer transformers on sequence-to-sequence data with arbitrary data distribution, closely mirroring real-world conditions. Our analysis characterizes the convergence of generalization error to the irreducible risk as computational resources scale with data, especially during the optimization process.
>   We establish a theoretical upper bound on excess risk characterized by a distinct phase transition. In the initial optimization phase, the excess risk decays exponentially relative to the computational cost ${\sf C}$. However, once a specific resource allocation threshold is crossed, the system enters a statistical phase, where the generalization error follows a power-law decay of $Θ(\mathsf{C}^{-1/6})$. Beyond this unified framework, our theory derives isolated scaling laws for model size, training time, and dataset size, elucidating how each variable independently governs the upper bounds of generalization.

