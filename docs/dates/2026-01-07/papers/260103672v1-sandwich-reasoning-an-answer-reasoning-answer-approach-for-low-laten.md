---
layout: default
title: Sandwich Reasoning: An Answer-Reasoning-Answer Approach for Low-Latency Query Correction
---

# Sandwich Reasoning: An Answer-Reasoning-Answer Approach for Low-Latency Query Correction
**arXiv**：[2601.03672v1](https://arxiv.org/abs/2601.03672) · [PDF](https://arxiv.org/pdf/2601.03672.pdf)  
**作者**：Chen Zhang, Kepu Zhang, Jiatong Zhang, Xiao Zhang, Jun Xu  

**一句话要点**：提出Sandwich Reasoning方法以解决查询纠正中延迟与准确性的权衡问题

**关键词**：查询纠正, 推理对齐, 强化学习, 低延迟优化, 在线搜索

## 3 点简述
- 核心问题：链式思维推理提升准确性但延迟过高，影响实时查询纠正。
- 方法要点：采用答案-推理-答案范式，结合一致性强化学习对齐初始与最终答案。
- 实验或效果：在保持SOTA准确性的同时，延迟降低40-70%，解决在线搜索的权衡。

## 摘要（原文）

> Query correction is a critical entry point in modern search pipelines, demanding high accuracy strictly within real-time latency constraints. Chain-of-Thought (CoT) reasoning improves accuracy but incurs prohibitive latency for real-time query correction. A potential solution is to output an answer before reasoning to reduce latency; however, under autoregressive decoding, the early answer is independent of subsequent reasoning, preventing the model from leveraging its reasoning capability to improve accuracy. To address this issue, we propose Sandwich Reasoning (SandwichR), a novel approach that explicitly aligns a fast initial answer with post-hoc reasoning, enabling low-latency query correction without sacrificing reasoning-aware accuracy. SandwichR follows an Answer-Reasoning-Answer paradigm, producing an initial correction, an explicit reasoning process, and a final refined correction. To align the initial answer with post-reasoning insights, we design a consistency-aware reinforcement learning (RL) strategy: a dedicated consistency reward enforces alignment between the initial and final corrections, while margin-based rejection sampling prioritizes borderline samples where reasoning drives the most impactful corrective gains. Additionally, we construct a high-quality query correction dataset, addressing the lack of specialized benchmarks for complex query correction. Experimental results demonstrate that SandwichR achieves SOTA accuracy comparable to standard CoT while delivering a 40-70% latency reduction, resolving the latency-accuracy trade-off in online search.

