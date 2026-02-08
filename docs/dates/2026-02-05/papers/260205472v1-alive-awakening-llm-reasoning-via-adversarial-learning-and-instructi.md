---
layout: default
title: ALIVE: Awakening LLM Reasoning via Adversarial Learning and Instructive Verbal Evaluation
---

# ALIVE: Awakening LLM Reasoning via Adversarial Learning and Instructive Verbal Evaluation
**arXiv**：[2602.05472v1](https://arxiv.org/abs/2602.05472) · [PDF](https://arxiv.org/pdf/2602.05472.pdf)  
**作者**：Yiwen Duan, Jing Ye, Xinpei Zhao  

**一句话要点**：提出ALIVE框架，通过对抗学习和指导性语言评估解决大语言模型推理中的奖励瓶颈问题。

**关键词**：大语言模型推理, 对抗学习, 指导性语言评估, 奖励瓶颈, 认知协同, 无监督对齐

## 3 点简述
- 核心问题：传统强化学习依赖标量奖励，成本高、跨域脆弱且忽视解决方案逻辑，阻碍模型推理能力发展。
- 方法要点：基于认知协同原则，统一问题提出、解决和评判于单一策略模型，结合对抗学习和指导性语言反馈，使模型从原始语料内化评估标准。
- 实验或效果：在数学推理、代码生成和逻辑推理基准测试中，ALIVE缓解奖励信号限制，提升准确性、跨域泛化能力和自校正率。

## 摘要（原文）

> The quest for expert-level reasoning in Large Language Models (LLMs) has been hampered by a persistent \textit{reward bottleneck}: traditional reinforcement learning (RL) relies on scalar rewards that are \textbf{costly} to scale, \textbf{brittle} across domains, and \textbf{blind} to the underlying logic of a solution. This reliance on external, impoverished signals prevents models from developing a deep, self-contained understanding of reasoning principles. We introduce \textbf{ALIVE} (\emph{Adversarial Learning with Instructive Verbal Evaluation}), a hands-free alignment framework that moves beyond scalar reward optimization toward intrinsic reasoning acquisition. Grounded in the principle of \emph{Cognitive Synergy}, ALIVE unifies problem posing, solving, and judging within a single policy model to internalize the logic of correctness. By coupling adversarial learning with instructive verbal feedback, ALIVE enables models to internalize evaluative criteria directly from raw corpora, effectively transforming external critiques into an endogenous reasoning faculty. Empirical evaluations across mathematical reasoning, code generation, and general logical inference benchmarks demonstrate that ALIVE consistently mitigates reward signal limitations. With identical data and compute, it achieves accuracy gains, markedly improved cross-domain generalization, and higher self-correction rates. These results indicate that the reasoning trinity fosters a self-sustaining trajectory of capability growth, positioning ALIVE as a scalable foundation for general-purpose reasoning alignment without human-in-the-loop supervision.

