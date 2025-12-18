---
layout: default
title: A Decision-Theoretic Approach for Managing Misalignment
---

# A Decision-Theoretic Approach for Managing Misalignment
**arXiv**：[2512.15584v1](https://arxiv.org/abs/2512.15584) · [PDF](https://arxiv.org/pdf/2512.15584.pdf)  
**作者**：Daniel A. Herrmann, Abinav Chari, Isabelle Qian, Sree Sharvesh, B. A. Levinstein  

**一句话要点**：提出决策理论框架以管理AI委托中的价值错位风险

**关键词**：价值对齐, 决策理论, AI委托, 不确定性管理, 风险权衡

## 3 点简述
- 核心问题：在不确定性下，何时委托决策给价值错位的AI系统是合理的
- 方法要点：基于价值错位、认知准确性和行动范围权衡，量化委托决策
- 实验或效果：区分通用与上下文特定委托，后者可在显著错位下最优

## 摘要（原文）

> When should we delegate decisions to AI systems? While the value alignment literature has developed techniques for shaping AI values, less attention has been paid to how to determine, under uncertainty, when imperfect alignment is good enough to justify delegation. We argue that rational delegation requires balancing an agent's value (mis)alignment with its epistemic accuracy and its reach (the acts it has available). This paper introduces a formal, decision-theoretic framework to analyze this tradeoff precisely accounting for a principal's uncertainty about these factors. Our analysis reveals a sharp distinction between two delegation scenarios. First, universal delegation (trusting an agent with any problem) demands near-perfect value alignment and total epistemic trust, conditions rarely met in practice. Second, we show that context-specific delegation can be optimal even with significant misalignment. An agent's superior accuracy or expanded reach may grant access to better overall decision problems, making delegation rational in expectation. We develop a novel scoring framework to quantify this ex ante decision. Ultimately, our work provides a principled method for determining when an AI is aligned enough for a given context, shifting the focus from achieving perfect alignment to managing the risks and rewards of delegation under uncertainty.

