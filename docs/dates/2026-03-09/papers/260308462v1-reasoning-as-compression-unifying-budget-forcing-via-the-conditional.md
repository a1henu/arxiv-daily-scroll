---
layout: default
title: Reasoning as Compression: Unifying Budget Forcing via the Conditional Information Bottleneck
---

# Reasoning as Compression: Unifying Budget Forcing via the Conditional Information Bottleneck
**arXiv**：[2603.08462v1](https://arxiv.org/abs/2603.08462) · [PDF](https://arxiv.org/pdf/2603.08462.pdf)  
**作者**：Fabio Valerio Massoli, Andrey Kuzmin, Arash Behboodi  

**一句话要点**：提出基于条件信息瓶颈的统一预算强制方法，以压缩推理过程并提升大语言模型效率

**关键词**：条件信息瓶颈, 预算强制, 思维链压缩, 强化学习目标, 语义先验, 推理效率

## 3 点简述
- 核心问题：思维链提示提高准确性但增加推理成本，现有预算强制方法可能抑制必要推理
- 方法要点：将高效推理建模为条件信息瓶颈问题，引入语义先验替代基于令牌计数的启发式方法
- 实验或效果：在适度压缩下提高准确性，支持激进压缩时最小化准确性下降，保持流畅性和逻辑性

## 摘要（原文）

> Chain-of-Thought (CoT) prompting improves LLM accuracy on complex tasks but often increases token usage and inference cost. Existing "Budget Forcing" methods reducing cost via fine-tuning with heuristic length penalties, suppress both essential reasoning and redundant filler. We recast efficient reasoning as a lossy compression problem under the Information Bottleneck (IB) principle, and identify a key theoretical gap when applying naive IB to transformers: attention violates the Markov property between prompt, reasoning trace, and response. To resolve this issue, we model CoT generation under the Conditional Information Bottleneck (CIB) principle, where the reasoning trace Z acts as a computational bridge that contains only the information about the response Y that is not directly accessible from the prompt X. This yields a general Reinforcement Learning objective: maximize task reward while compressing completions under a prior over reasoning traces, subsuming common heuristics (e.g., length penalties) as special cases (e.g., uniform priors). In contrast to naive token-counting-based approaches, we introduce a semantic prior that measures token cost by surprisal under a language model prior. Empirically, our CIB objective prunes cognitive bloat while preserving fluency and logic, improving accuracy at moderate compression and enabling aggressive compression with minimal accuracy drop.

