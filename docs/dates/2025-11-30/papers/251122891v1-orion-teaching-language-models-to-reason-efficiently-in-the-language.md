---
layout: default
title: ORION: Teaching Language Models to Reason Efficiently in the Language of Thought
---

# ORION: Teaching Language Models to Reason Efficiently in the Language of Thought
**arXiv**：[2511.22891v1](https://arxiv.org/abs/2511.22891) · [PDF](https://arxiv.org/pdf/2511.22891.pdf)  
**作者**：Kumar Tanmay, Kriti Aggarwal, Paul Pu Liang, Subhabrata Mukherjee  

**一句话要点**：提出ORION框架，通过Mentalese压缩推理解决大型推理模型延迟高、冗余多的问题。

**关键词**：压缩推理, 语言思维假说, 强化学习优化, 数学推理, 推理效率, 令牌压缩

## 3 点简述
- 大型推理模型依赖冗长推理链导致高延迟和冗余，影响效率。
- 引入Mentalese语言训练模型进行紧凑符号推理，结合SLPO优化方法奖励简洁正确解。
- 在多个数学基准测试中实现4-16倍令牌压缩、5倍延迟降低和90-98%准确率保持。

## 摘要（原文）

> Large Reasoning Models (LRMs) achieve strong performance in mathematics, code generation, and task planning, but their reliance on long chains of verbose "thinking" tokens leads to high latency, redundancy, and incoherent reasoning paths. Inspired by the Language of Thought Hypothesis, which posits that human reasoning operates over a symbolic, compositional mental language called Mentalese, we introduce a framework that trains models to reason in a similarly compact style. Mentalese encodes abstract reasoning as ultra-compressed, structured tokens, enabling models to solve complex problems with far fewer steps. To improve both efficiency and accuracy, we propose SHORTER LENGTH PREFERENCE OPTIMIZATION (SLPO), a reinforcement learning method that rewards concise solutions that stay correct, while still allowing longer reasoning when needed. Applied to Mentalese-aligned models, SLPO yields significantly higher compression rates by enabling concise reasoning that preserves the benefits of detailed thinking without the computational overhead. Across benchmarks including AIME 2024 and 2025, MinervaMath, OlympiadBench, Math500, and AMC, our ORION models produce reasoning traces with 4-16x fewer tokens, achieve up to 5x lower inference latency, and reduce training costs by 7-9x relative to the DeepSeek R1 Distilled model, while maintaining 90-98% of its accuracy. ORION also surpasses Claude and ChatGPT-4o by up to 5% in accuracy while maintaining 2x compression. These results show that Mentalese-style compressed reasoning offers a step toward human-like cognitive efficiency, enabling real-time, cost-effective reasoning without sacrificing accuracy.

