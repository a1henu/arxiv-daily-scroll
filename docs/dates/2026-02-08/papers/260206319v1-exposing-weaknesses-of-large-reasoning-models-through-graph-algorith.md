---
layout: default
title: Exposing Weaknesses of Large Reasoning Models through Graph Algorithm Problems
---

# Exposing Weaknesses of Large Reasoning Models through Graph Algorithm Problems
**arXiv**：[2602.06319v1](https://arxiv.org/abs/2602.06319) · [PDF](https://arxiv.org/pdf/2602.06319.pdf)  
**作者**：Qifan Zhang, Jianhao Ruan, Aochuan Chen, Kang Zeng, Nuo Chen, Jing Tang, Jia Li  

**一句话要点**：提出GrAlgoBench基准，通过图算法问题评估大型推理模型的弱点

**关键词**：图算法基准, 长上下文推理, 模型评估, 推理弱点, 程序化验证

## 3 点简述
- 现有基准在数学、代码和常识推理中缺乏长上下文评估和挑战性
- GrAlgoBench利用图算法问题，支持长上下文推理、难度控制和程序化评估
- 实验揭示LRMs在长上下文下准确率下降和过度思考现象

## 摘要（原文）

> Large Reasoning Models (LRMs) have advanced rapidly; however, existing benchmarks in mathematics, code, and common-sense reasoning remain limited. They lack long-context evaluation, offer insufficient challenge, and provide answers that are difficult to verify programmatically. We introduce GrAlgoBench, a benchmark designed to evaluate LRMs through graph algorithm problems. Such problems are particularly well suited for probing reasoning abilities: they demand long-context reasoning, allow fine-grained control of difficulty levels, and enable standardized, programmatic evaluation. Across nine tasks, our systematic experiments reveal two major weaknesses of current LRMs. First, accuracy deteriorates sharply as context length increases, falling below 50% once graphs exceed 120 nodes. This degradation is driven by frequent execution errors, weak memory, and redundant reasoning. Second, LRMs suffer from an over-thinking phenomenon, primarily caused by extensive yet largely ineffective self-verification, which inflates reasoning traces without improving correctness. By exposing these limitations, GrAlgoBench establishes graph algorithm problems as a rigorous, multidimensional, and practically relevant testbed for advancing the study of reasoning in LRMs. Code is available at https://github.com/Bklight999/GrAlgoBench.

