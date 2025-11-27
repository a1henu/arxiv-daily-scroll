---
layout: default
title: Learning When to Stop: Adaptive Latent Reasoning via Reinforcement Learning
---

# Learning When to Stop: Adaptive Latent Reasoning via Reinforcement Learning
**arXiv**：[2511.21581v1](https://arxiv.org/abs/2511.21581) · [PDF](https://arxiv.org/pdf/2511.21581.pdf)  
**作者**：Alex Ning, Yen-Ling Kuo, Gabe Gomes  

**一句话要点**：提出自适应潜在推理方法以减少推理长度并保持准确性

**关键词**：潜在推理, 强化学习, 推理长度优化, Transformer模型, 知识蒸馏

## 3 点简述
- 核心问题：潜在推理模型需优化推理长度以降低计算成本
- 方法要点：结合强化学习自适应调整推理长度，最小化长度并维持精度
- 实验效果：在GSM8K-Aug数据集上推理长度减少52%，准确性无损失

## 摘要（原文）

> Latent reasoning represents a new development in Transformer language models that has shown potential in compressing reasoning lengths compared to chain-of-thought reasoning. By directly passing the information-rich previous final latent state into the next sequence, latent reasoning removes the restriction to human language tokens as the medium for reasoning. We develop adaptive-length latent reasoning models and introduce a post-SFT reinforcement-learning methodology to optimize latent reasoning length by minimizing reasoning length while maintaining accuracy. This, in turn, further reduces compute usage and raises the bar on the compressive capabilities of latent reasoning models. Experiments on the Llama 3.2 1B model and the GSM8K-Aug dataset show a $52\%$ drop in total reasoning length with no penalty to accuracy. In future work, we plan to extend to additional models and datasets, analyze relationships between training coefficients, experiment with architecture variations, and continue our knowledge distillation for latent reasoning SFT efforts. We make our code and pretrained weights available at https://github.com/apning/adaptive-latent-reasoning.

