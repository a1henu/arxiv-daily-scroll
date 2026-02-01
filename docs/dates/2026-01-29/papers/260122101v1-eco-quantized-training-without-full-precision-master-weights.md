---
layout: default
title: ECO: Quantized Training without Full-Precision Master Weights
---

# ECO: Quantized Training without Full-Precision Master Weights
**arXiv**：[2601.22101v1](https://arxiv.org/abs/2601.22101) · [PDF](https://arxiv.org/pdf/2601.22101.pdf)  
**作者**：Mahdi Nikdan, Amir Zandieh, Dan Alistarh, Vahab Mirrokni  

**一句话要点**：提出ECO优化器以消除大语言模型量化训练中的主权重内存开销

**关键词**：量化训练, 误差补偿优化器, 大语言模型, 稀疏专家混合模型, 内存效率, FP8量化

## 3 点简述
- 量化训练依赖高精度主权重缓冲，导致内存开销大，尤其在稀疏专家混合模型中
- ECO通过直接更新量化参数并注入量化误差到动量中，形成无额外内存的误差反馈循环
- 实验表明ECO在多种模型和精度下匹配基线准确性，显著改善内存与验证损失帕累托前沿

## 摘要（原文）

> Quantization has significantly improved the compute and memory efficiency of Large Language Model (LLM) training. However, existing approaches still rely on accumulating their updates in high-precision: concretely, gradient updates must be applied to a high-precision weight buffer, known as $\textit{master weights}$. This buffer introduces substantial memory overhead, particularly for Sparse Mixture of Experts (SMoE) models, where model parameters and optimizer states dominate memory usage. To address this, we introduce the Error-Compensating Optimizer (ECO), which eliminates master weights by applying updates directly to quantized parameters. ECO quantizes weights after each step and carefully injects the resulting quantization error into the optimizer momentum, forming an error-feedback loop with no additional memory. We prove that, under standard assumptions and a decaying learning rate, ECO converges to a constant-radius neighborhood of the optimum, while naive master-weight removal can incur an error that is inversely proportional to the learning rate. We show empirical results for pretraining small Transformers (30-800M), a Gemma-3 1B model, and a 2.1B parameter Sparse MoE model with FP8 quantization, and fine-tuning DeepSeek-MoE-16B in INT4 precision. Throughout, ECO matches baselines with master weights up to near-lossless accuracy, significantly shifting the static memory vs validation loss Pareto frontier.

