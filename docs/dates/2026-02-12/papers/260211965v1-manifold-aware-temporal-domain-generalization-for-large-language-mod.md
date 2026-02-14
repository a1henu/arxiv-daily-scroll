---
layout: default
title: Manifold-Aware Temporal Domain Generalization for Large Language Models
---

# Manifold-Aware Temporal Domain Generalization for Large Language Models
**arXiv**：[2602.11965v1](https://arxiv.org/abs/2602.11965) · [PDF](https://arxiv.org/pdf/2602.11965.pdf)  
**作者**：Yiheng Yao, Zekun Cai, Xinyuan Song, Hiroki Hill Kobayashi, Xuan Song, Ryosuke Shibasaki, Liang Zhao  

**一句话要点**：提出MaT-LoRA以解决大语言模型在时间分布偏移下的高效泛化问题。

**关键词**：时间域泛化, 参数高效微调, 低秩适应, 流形学习, 大语言模型, 时间演化建模

## 3 点简述
- 核心问题：大语言模型面临时间分布偏移，现有方法在全参数空间建模计算不可行。
- 方法要点：基于参数高效微调，将时间结构约束到低维流形，通过结构化时间核心建模演化。
- 实验或效果：在合成和真实数据集上验证了优越的时间泛化性能和实际可扩展性。

## 摘要（原文）

> Temporal distribution shifts are pervasive in real-world deployments of Large Language Models (LLMs), where data evolves continuously over time. While Temporal Domain Generalization (TDG) seeks to model such structured evolution, existing approaches characterize model adaptation in the full parameter space. This formulation becomes computationally infeasible for modern LLMs. This paper introduces a geometric reformulation of TDG under parameter-efficient fine-tuning. We establish that the low-dimensional temporal structure underlying model evolution can be preserved under parameter-efficient reparameterization, enabling temporal modeling without operating in the ambient parameter space. Building on this principle, we propose Manifold-aware Temporal LoRA (MaT-LoRA), which constrains temporal updates to a shared low-dimensional manifold within a low-rank adaptation subspace, and models its evolution through a structured temporal core. This reparameterization dramatically reduces temporal modeling complexity while retaining expressive power. Extensive experiments on synthetic and real-world datasets, including scientific documents, news publishers, and review ratings, demonstrate that MaT-LoRA achieves superior temporal generalization performance with practical scalability for LLMs.

