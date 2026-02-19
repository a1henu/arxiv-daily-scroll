---
layout: default
title: SPARC: Scenario Planning and Reasoning for Automated C Unit Test Generation
---

# SPARC: Scenario Planning and Reasoning for Automated C Unit Test Generation
**arXiv**：[2602.16671v1](https://arxiv.org/abs/2602.16671) · [PDF](https://arxiv.org/pdf/2602.16671.pdf)  
**作者**：Jaid Monwar Chowdhury, Chi-An Fu, Reyhaneh Jabbarvand  

**一句话要点**：提出SPARC框架，通过场景规划与推理解决C语言单元测试生成的语义鸿沟问题。

**关键词**：C语言单元测试生成, 神经符号框架, 场景规划, LLM推理对齐, 控制流图分析, 迭代自校正

## 3 点简述
- 核心问题：C语言单元测试生成存在高意图与低语法约束的语义鸿沟，导致LLM直接生成代码时出现跳码失败。
- 方法要点：采用神经符号框架，结合控制流图分析、操作映射、路径目标合成和迭代自校正验证四阶段。
- 实验或效果：在59个真实和算法主题上，SPARC在行覆盖、分支覆盖和突变得分上显著优于基线，测试保留率达94.3%。

## 摘要（原文）

> Automated unit test generation for C remains a formidable challenge due to the semantic gap between high-level program intent and the rigid syntactic constraints of pointer arithmetic and manual memory management. While Large Language Models (LLMs) exhibit strong generative capabilities, direct intent-to-code synthesis frequently suffers from the leap-to-code failure mode, where models prematurely emit code without grounding in program structure, constraints, and semantics. This will result in non-compilable tests, hallucinated function signatures, low branch coverage, and semantically irrelevant assertions that cannot properly capture bugs. We introduce SPARC, a neuro-symbolic, scenario-based framework that bridges this gap through four stages: (1) Control Flow Graph (CFG) analysis, (2) an Operation Map that grounds LLM reasoning in validated utility helpers, (3) Path-targeted test synthesis, and (4) an iterative, self-correction validation loop using compiler and runtime feedback. We evaluate SPARC on 59 real-world and algorithmic subjects, where it outperforms the vanilla prompt generation baseline by 31.36% in line coverage, 26.01% in branch coverage, and 20.78% in mutation score, matching or exceeding the symbolic execution tool KLEE on complex subjects. SPARC retains 94.3% of tests through iterative repair and produces code with significantly higher developer-rated readability and maintainability. By aligning LLM reasoning with program structure, SPARC provides a scalable path for industrial-grade testing of legacy C codebases.

