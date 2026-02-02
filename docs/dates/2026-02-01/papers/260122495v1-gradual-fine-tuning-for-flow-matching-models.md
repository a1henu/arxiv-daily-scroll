---
layout: default
title: Gradual Fine-Tuning for Flow Matching Models
---

# Gradual Fine-Tuning for Flow Matching Models
**arXiv**：[2601.22495v1](https://arxiv.org/abs/2601.22495) · [PDF](https://arxiv.org/pdf/2601.22495.pdf)  
**作者**：Gudrun Thorkelsdottir, Arindam Banerjee  

**一句话要点**：提出渐进微调框架以解决流匹配模型在分布偏移下的微调挑战

**关键词**：流匹配模型, 渐进微调, 分布偏移, 生成模型, 温度控制, 最优传输

## 3 点简述
- 核心问题：流匹配模型在数据有限或分布变化时，标准微调可能损害预训练性能
- 方法要点：通过温度控制序列平滑插值预训练与目标漂移，确保理论收敛
- 实验或效果：提升收敛稳定性、缩短概率路径，保持生成质量并加速推理

## 摘要（原文）

> Fine-tuning flow matching models is a central challenge in settings with limited data, evolving distributions, or strict efficiency demands, where unconstrained fine-tuning can erode the accuracy and efficiency gains learned during pretraining. Prior work has produced theoretical guarantees and empirical advances for reward-based fine-tuning formulations, but these methods often impose restrictions on permissible drift structure or training techniques. In this work, we propose Gradual Fine-Tuning (GFT), a principled framework for fine-tuning flow-based generative models when samples from the target distribution are available. For stochastic flows, GFT defines a temperature-controlled sequence of intermediate objectives that smoothly interpolate between the pretrained and target drifts, approaching the true target as the temperature approaches zero. We prove convergence results for both marginal and conditional GFT objectives, enabling the use of suitable (e.g., optimal transport) couplings during GFT while preserving correctness. Empirically, GFT improves convergence stability and shortens probability paths, resulting in faster inference, while maintaining generation quality comparable to standard fine-tuning. Our results position GFT as a theoretically grounded and practically effective alternative for scalable adaptation of flow matching models under distribution shift.

