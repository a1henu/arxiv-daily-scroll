---
layout: default
title: TextResNet: Decoupling and Routing Optimization Signals in Compound AI Systems via Deep Residual Tuning
---

# TextResNet: Decoupling and Routing Optimization Signals in Compound AI Systems via Deep Residual Tuning
**arXiv**：[2602.08306v1](https://arxiv.org/abs/2602.08306) · [PDF](https://arxiv.org/pdf/2602.08306.pdf)  
**作者**：Suizhi Huang, Mei Li, Han Yu, Xiaoxiao Li  

**一句话要点**：提出TextResNet框架以解决复合AI系统中深度链路的语义纠缠问题

**关键词**：复合AI系统, 文本梯度优化, 语义解耦, 深度残差调优, 因果路由

## 3 点简述
- 核心问题：文本梯度优化器在深度链路中因语义纠缠导致归因模糊，性能受限
- 方法要点：通过前向加性语义增量、后向语义梯度分解、因果路由和密度感知调度实现信号解耦与优化
- 实验或效果：相比TextGrad，TextResNet在复合AI系统中性能更优且稳定性显著提升

## 摘要（原文）

> Textual Gradient-style optimizers (TextGrad) enable gradient-like feedback propagation through compound AI systems. However, they do not work well for deep chains. The root cause of this limitation stems from the Semantic Entanglement problem in these extended workflows. In standard textual backpropagation, feedback signals mix local critiques with upstream contexts, leading to Attribution Ambiguity. To address this challenge, we propose TextResNet, a framework that reformulates the optimization process to achieve precise signal routing via four key innovations. Firstly, in the forward pass, it enforces Additive Semantic Deltas to preserve an Identity Highway for gradient flow. Secondly, in the backward pass, it introduces Semantic Gradient Decomposition via a Semantic Projector to disentangle feedback into causally independent subspaces. Thirdly, it implements Causal Routing, which routes projected signals to their specific components. Finally, it performs Density-Aware Optimization Scheduling to leverage the disentangled signals to dynamically allocate resources to key system bottlenecks. Our results show that TextResNet not only achieves superior performance compared to TextGrad, but also exhibits remarkable stability for agentic tasks in compound AI systems where baselines collapse. Code is available at https://github.com/JeanDiable/TextResNet.

