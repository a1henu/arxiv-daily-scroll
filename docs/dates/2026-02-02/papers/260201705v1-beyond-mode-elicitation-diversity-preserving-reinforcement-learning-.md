---
layout: default
title: Beyond Mode Elicitation: Diversity-Preserving Reinforcement Learning via Latent Diffusion Reasoner
---

# Beyond Mode Elicitation: Diversity-Preserving Reinforcement Learning via Latent Diffusion Reasoner
**arXiv**：[2602.01705v1](https://arxiv.org/abs/2602.01705) · [PDF](https://arxiv.org/pdf/2602.01705.pdf)  
**作者**：Haoqiang Kang, Yizhe Zhang, Nikki Lijing Kuang, Yi-An Ma, Lianhui Qin  

**一句话要点**：提出LaDi-RL框架，通过潜在扩散推理解决强化学习中多样性崩溃问题，提升LLM推理能力。

**关键词**：强化学习, 潜在扩散模型, 推理优化, 多样性保持, 代码生成, 数学推理

## 3 点简述
- 核心问题：离散强化学习在优化CoT生成时，因模式引发行为导致多样性崩溃，限制探索效率。
- 方法要点：在连续潜在空间进行探索，利用引导扩散建模，解耦潜在探索与文本生成，保留多解模式。
- 实验或效果：在代码生成和数学推理基准上，pass@1和pass@k均优于离散RL基线，绝对增益显著。

## 摘要（原文）

> Recent reinforcement learning (RL) methods improve LLM reasoning by optimizing discrete Chain-of-Thought (CoT) generation; however, exploration in token space often suffers from diversity collapse as policy entropy decreases due to mode elicitation behavior in discrete RL. To mitigate this issue, we propose Latent Diffusion Reasoning with Reinforcement Learning (LaDi-RL), a framework that conducts exploration directly in a continuous latent space, where latent variables encode semantic-level reasoning trajectories. By modeling exploration via guided diffusion, multi-step denoising distributes stochasticity and preserves multiple coexisting solution modes without mutual suppression. Furthermore, by decoupling latent-space exploration from text-space generation, we show that latent diffusion-based optimization is more effective than text-space policy optimization alone, while a complementary text policy provides additional gains when combined with latent exploration. Experiments on code generation and mathematical reasoning benchmarks demonstrate consistent improvements in both pass@1 and pass@k over discrete RL baselines, with absolute pass@1 gains of +9.4% on code generation and +5.7% on mathematical reasoning, highlighting diffusion-based latent RL as a principled alternative to discrete token-level RL for reasoning.

