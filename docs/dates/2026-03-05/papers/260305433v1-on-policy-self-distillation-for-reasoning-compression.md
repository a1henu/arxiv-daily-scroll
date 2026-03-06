---
layout: default
title: On-Policy Self-Distillation for Reasoning Compression
---

# On-Policy Self-Distillation for Reasoning Compression
**arXiv**：[2603.05433v1](https://arxiv.org/abs/2603.05433) · [PDF](https://arxiv.org/pdf/2603.05433.pdf)  
**作者**：Hejian Sang, Yuanda Xu, Zhengze Zhou, Ran He, Zhipeng Wang, Jiachen Sun  

**一句话要点**：提出在线策略自蒸馏方法以压缩推理模型输出，提升效率与准确性

**关键词**：推理压缩, 自蒸馏, 在线策略学习, 反向KL散度, 模型效率

## 3 点简述
- 核心问题：推理模型输出包含冗余和有害噪声，影响效率与准确性。
- 方法要点：通过“简洁”指令引导模型生成教师logits，在自身输出上最小化反向KL散度进行自蒸馏。
- 实验效果：在MATH-500和AIME 2024上实现显著token压缩和准确性提升。

## 摘要（原文）

> Reasoning models think out loud, but much of what they say is noise. We introduce OPSDC (On-Policy Self-Distillation for Reasoning Compression), a method that teaches models to reason more concisely by
>   distilling their own concise behavior back into themselves. The entire approach reduces to one idea: condition the same model on a "be concise" instruction to obtain teacher logits, and minimize per-token
>   reverse KL on the student's own rollouts. No ground-truth answers, no token budgets, no difficulty estimators. Just self-distillation. Yet this simplicity belies surprising sophistication: OPSDC automatically
>   compresses easy problems aggressively while preserving the deliberation needed for hard ones. On Qwen3-8B and Qwen3-14B, we achieve 57-59% token reduction on MATH-500 while improving accuracy by 9-16 points
>   absolute. On AIME 2024, the 14B model gains 10 points with 41% compression. The secret? Much of what reasoning models produce is not just redundant-it is actively harmful, compounding errors with every
>   unnecessary token.

