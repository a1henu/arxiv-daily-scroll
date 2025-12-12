---
layout: default
title: Guided Transfer Learning for Discrete Diffusion Models
---

# Guided Transfer Learning for Discrete Diffusion Models
**arXiv**：[2512.10877v1](https://arxiv.org/abs/2512.10877) · [PDF](https://arxiv.org/pdf/2512.10877.pdf)  
**作者**：Julian Kleutgens, Claudio Battiloro, Lingkai Kong, Benjamin Grewe, Francesca Dominici, Mauricio Tec  

**一句话要点**：提出引导式迁移学习以解决离散扩散模型在新领域适应中的计算成本问题

**关键词**：离散扩散模型, 迁移学习, 引导采样, 语言建模, 计算效率

## 3 点简述
- 离散扩散模型依赖大数据集，迁移学习需微调模型，计算成本高
- 基于比率引导，无需修改预训练去噪器，统一处理离散时间和连续时间扩散
- 通过高效采样器聚焦关键位置和候选词，降低大规模语言建模的计算负担

## 摘要（原文）

> Discrete diffusion models achieve strong performance across language and other discrete domains, providing a powerful alternative to autoregressive models. However, their strong performance relies on large training datasets, which are costly or risky to obtain, especially when adapting to new domains. Transfer learning is the natural way to adapt pretrained discrete diffusion models, but current methods require fine-tuning large diffusion models, which is computationally expensive and often impractical. Building on ratio-based transfer learning for continuous diffusion, we provide Guided Transfer Learning for discrete diffusion models (GTL). This enables sampling from a target distribution without modifying the pretrained denoiser. The same guidance formulation applies to both discrete-time diffusion and continuous-time score-based discrete diffusion, yielding a unified treatment. Guided discrete diffusion often requires many forward passes of the guidance network, which becomes impractical for large vocabularies and long sequences. To address this, we further present an efficient guided sampler that concentrates evaluations on planner-selected positions and top candidate tokens, thus lowering sampling time and computation. This makes guided language modeling practical at scale for large vocabularies and long sequences. We evaluate GTL on sequential data, including synthetic Markov chains and language modeling, and provide empirical analyses of its behavior.

