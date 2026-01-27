---
layout: default
title: Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models
---

# Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models
**arXiv**：[2601.18734v1](https://arxiv.org/abs/2601.18734) · [PDF](https://arxiv.org/pdf/2601.18734.pdf)  
**作者**：Siyan Zhao, Zhihui Xie, Mengchen Liu, Jing Huang, Guan Pang, Feiyu Chen, Aditya Grover  

**一句话要点**：提出基于策略的自蒸馏框架，通过单模型扮演师生角色提升大语言模型推理能力。

**关键词**：大语言模型, 知识蒸馏, 推理能力, 自蒸馏, 令牌效率, 数学推理

## 3 点简述
- 核心问题：传统蒸馏方法需独立教师模型且未充分利用数据集中的真实推理轨迹。
- 方法要点：单模型基于不同上下文（如特权信息）同时作为教师和学生，在自身采样轨迹上进行令牌级监督。
- 实验或效果：在数学推理基准上实现4-8倍令牌效率优于强化学习方法，性能超越离策略蒸馏。

## 摘要（原文）

> Knowledge distillation improves large language model (LLM) reasoning by compressing the knowledge of a teacher LLM to train smaller LLMs. On-policy distillation advances this approach by having the student sample its own trajectories while a teacher LLM provides dense token-level supervision, addressing the distribution mismatch between training and inference in off-policy distillation methods. However, on-policy distillation typically requires a separate, often larger, teacher LLM and does not explicitly leverage ground-truth solutions available in reasoning datasets. Inspired by the intuition that a sufficiently capable LLM can rationalize external privileged reasoning traces and teach its weaker self (i.e., the version without access to privileged information), we introduce On-Policy Self-Distillation (OPSD), a framework where a single model acts as both teacher and student by conditioning on different contexts. The teacher policy conditions on privileged information (e.g., verified reasoning traces) while the student policy sees only the question; training minimizes the per-token divergence between these distributions over the student's own rollouts. We demonstrate the efficacy of our method on multiple mathematical reasoning benchmarks, achieving 4-8x token efficiency compared to reinforcement learning methods such as GRPO and superior performance over off-policy distillation methods.

