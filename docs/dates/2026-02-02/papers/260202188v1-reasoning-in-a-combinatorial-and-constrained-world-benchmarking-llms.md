---
layout: default
title: Reasoning in a Combinatorial and Constrained World: Benchmarking LLMs on Natural-Language Combinatorial Optimization
---

# Reasoning in a Combinatorial and Constrained World: Benchmarking LLMs on Natural-Language Combinatorial Optimization
**arXiv**：[2602.02188v1](https://arxiv.org/abs/2602.02188) · [PDF](https://arxiv.org/pdf/2602.02188.pdf)  
**作者**：Xia Jiang, Jing Chen, Cong Zhang, Jie Gao, Chengpeng Hu, Chenhao Zhang, Yaoxin Wu, Yingqian Zhang  

**一句话要点**：提出NLCO基准以评估大语言模型在自然语言组合优化任务中的端到端推理能力

**关键词**：自然语言组合优化, 大语言模型评估, 端到端推理, 约束处理, 解空间搜索, 基准测试

## 3 点简述
- 核心问题：大语言模型在组合优化任务中的能力未充分探索，需评估其在高维解空间搜索和硬约束处理的表现
- 方法要点：构建NLCO基准，涵盖43个组合优化问题，采用四层分类法进行细粒度评估，提供求解器标注的解决方案
- 实验或效果：实验显示高性能模型在小实例上可行性和解质量强，但随实例规模增大而下降，且任务类型对性能有系统性影响

## 摘要（原文）

> While large language models (LLMs) have shown strong performance in math and logic reasoning, their ability to handle combinatorial optimization (CO) -- searching high-dimensional solution spaces under hard constraints -- remains underexplored. To bridge the gap, we introduce NLCO, a \textbf{N}atural \textbf{L}anguage \textbf{C}ombinatorial \textbf{O}ptimization benchmark that evaluates LLMs on end-to-end CO reasoning: given a language-described decision-making scenario, the model must output a discrete solution without writing code or calling external solvers. NLCO covers 43 CO problems and is organized using a four-layer taxonomy of variable types, constraint families, global patterns, and objective classes, enabling fine-grained evaluation. We provide solver-annotated solutions and comprehensively evaluate LLMs by feasibility, solution optimality, and reasoning efficiency. Experiments across a wide range of modern LLMs show that high-performing models achieve strong feasibility and solution quality on small instances, but both degrade as instance size grows, even if more tokens are used for reasoning. We also observe systematic effects across the taxonomy: set-based tasks are relatively easy, whereas graph-structured problems and bottleneck objectives lead to more frequent failures.

