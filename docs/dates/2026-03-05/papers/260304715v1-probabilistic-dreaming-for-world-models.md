---
layout: default
title: Probabilistic Dreaming for World Models
---

# Probabilistic Dreaming for World Models
**arXiv**：[2603.04715v1](https://arxiv.org/abs/2603.04715) · [PDF](https://arxiv.org/pdf/2603.04715.pdf)  
**作者**：Gavin Wong  

**一句话要点**：提出概率性做梦方法以增强世界模型在并行探索和假设保持中的性能

**关键词**：世界模型, 概率性做梦, 并行探索, 潜在状态, 样本效率, MPE SimpleTag

## 3 点简述
- 核心问题：传统做梦方法在并行探索和互斥未来假设保持上存在局限，影响世界模型的鲁棒性和样本效率。
- 方法要点：引入概率方法，支持并行探索多个潜在状态，并保持互斥未来的不同假设，同时保留连续潜在变量的梯度特性。
- 实验或效果：在MPE SimpleTag领域评估，相比标准Dreamer模型，得分提升4.5%，回合回报方差降低28%。

## 摘要（原文）

> "Dreaming" enables agents to learn from imagined experiences, enabling more robust and sample-efficient learning of world models. In this work, we consider innovations to the state-of-the-art Dreamer model using probabilistic methods that enable: (1) the parallel exploration of many latent states; and (2) maintaining distinct hypotheses for mutually exclusive futures while retaining the desirable gradient properties of continuous latents. Evaluating on the MPE SimpleTag domain, our method outperforms standard Dreamer with a 4.5% score improvement and 28% lower variance in episode returns. We also discuss limitations and directions for future work, including how optimal hyperparameters (e.g. particle count K) scale with environmental complexity, and methods to capture epistemic uncertainty in world models.

