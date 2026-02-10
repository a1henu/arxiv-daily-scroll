---
layout: default
title: Towards Efficient Large Language Reasoning Models via Extreme-Ratio Chain-of-Thought Compression
---

# Towards Efficient Large Language Reasoning Models via Extreme-Ratio Chain-of-Thought Compression
**arXiv**：[2602.08324v1](https://arxiv.org/abs/2602.08324) · [PDF](https://arxiv.org/pdf/2602.08324.pdf)  
**作者**：Yuntian Tang, Bohan Jia, Wenxuan Huang, Lianyue Zhang, Jiao Xie, Wenxi Li, Wei Li, Jie Hu, Xinghao Chen, Rongrong Ji, Shaohui Lin  

**一句话要点**：提出Extra-CoT框架以解决高压缩比下思维链推理的保真度与效率问题

**关键词**：思维链压缩, 大语言模型推理, 强化学习优化, 数学推理, 令牌效率

## 3 点简述
- 核心问题：现有思维链压缩方法在高压缩比时逻辑保真度损失大，导致性能下降
- 方法要点：通过语义保留压缩器生成高保真监督数据，结合混合比例微调和分层奖励强化学习优化
- 实验或效果：在数学推理基准上实现超73%令牌减少且准确率提升0.6%，优于现有方法

## 摘要（原文）

> Chain-of-Thought (CoT) reasoning successfully enhances the reasoning capabilities of Large Language Models (LLMs), yet it incurs substantial computational overhead for inference. Existing CoT compression methods often suffer from a critical loss of logical fidelity at high compression ratios, resulting in significant performance degradation. To achieve high-fidelity, fast reasoning, we propose a novel EXTreme-RAtio Chain-of-Thought Compression framework, termed Extra-CoT, which aggressively reduces the token budget while preserving answer accuracy. To generate reliable, high-fidelity supervision, we first train a dedicated semantically-preserved compressor on mathematical CoT data with fine-grained annotations. An LLM is then fine-tuned on these compressed pairs via a mixed-ratio supervised fine-tuning (SFT), teaching it to follow a spectrum of compression budgets and providing a stable initialization for reinforcement learning (RL). We further propose Constrained and Hierarchical Ratio Policy Optimization (CHRPO) to explicitly incentivize question-solving ability under lower budgets by a hierarchical reward. Experiments on three mathematical reasoning benchmarks show the superiority of Extra-CoT. For example, on MATH-500 using Qwen3-1.7B, Extra-CoT achieves over 73\% token reduction with an accuracy improvement of 0.6\%, significantly outperforming state-of-the-art (SOTA) methods.

