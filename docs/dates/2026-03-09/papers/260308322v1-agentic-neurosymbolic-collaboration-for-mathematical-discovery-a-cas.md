---
layout: default
title: Agentic Neurosymbolic Collaboration for Mathematical Discovery: A Case Study in Combinatorial Design
---

# Agentic Neurosymbolic Collaboration for Mathematical Discovery: A Case Study in Combinatorial Design
**arXiv**：[2603.08322v1](https://arxiv.org/abs/2603.08322) · [PDF](https://arxiv.org/pdf/2603.08322.pdf)  
**作者**：Hai Xia, Carla P. Gomes, Bart Selman, Stefan Szeider  

**一句话要点**：提出神经符号协作方法，在组合设计理论中实现数学发现，获得拉丁方不平衡的紧下界。

**关键词**：神经符号推理, 组合设计理论, 数学发现, 人机协作, 大型语言模型, 符号计算

## 3 点简述
- 核心问题：研究组合设计理论中拉丁方不平衡的紧下界，特别是n≡1(mod3)的困难情况。
- 方法要点：结合大型语言模型、符号计算工具和人类战略指导，通过神经符号协作进行假设生成和验证。
- 实验或效果：获得紧下界4n(n-1)/9，通过Lean 4正式验证，展示系统在纯数学中的发现能力。

## 摘要（原文）

> We study mathematical discovery through the lens of neurosymbolic reasoning, where an AI agent powered by a large language model (LLM), coupled with symbolic computation tools, and human strategic direction, jointly produced a new result in combinatorial design theory. The main result of this human-AI collaboration is a tight lower bound on the imbalance of Latin squares for the notoriously difficult case $n \equiv 1 \pmod{3}$.
>   We reconstruct the discovery process from detailed interaction logs spanning multiple sessions over several days and identify the distinct cognitive contributions of each component. The AI agent proved effective at uncovering hidden structure and generating hypotheses. The symbolic component consists of computer algebra, constraint solvers, and simulated annealing, which provides rigorous verification and exhaustive enumeration. Human steering supplied the critical research pivot that transformed a dead end into a productive inquiry. Our analysis reveals that multi-model deliberation among frontier LLMs proved reliable for criticism and error detection but unreliable for constructive claims.
>   The resulting human-AI mathematical contribution, a tight lower bound of $4n(n{-}1)/9$, is achieved via a novel class of near-perfect permutations. The bound was formally verified in Lean 4. Our experiments show that neurosymbolic systems can indeed produce genuine discoveries in pure mathematics.

