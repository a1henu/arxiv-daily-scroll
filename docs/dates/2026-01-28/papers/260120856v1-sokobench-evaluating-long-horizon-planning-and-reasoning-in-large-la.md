---
layout: default
title: SokoBench: Evaluating Long-Horizon Planning and Reasoning in Large Language Models
---

# SokoBench: Evaluating Long-Horizon Planning and Reasoning in Large Language Models
**arXiv**：[2601.20856v1](https://arxiv.org/abs/2601.20856) · [PDF](https://arxiv.org/pdf/2601.20856.pdf)  
**作者**：Sebastiano Monti, Carlo Nicolini, Gianni Pellegrini, Jacopo Staiano, Bruno Lepri  

**一句话要点**：提出SokoBench基准以评估大语言模型的长时程规划能力

**关键词**：长时程规划, 大语言模型评估, Sokoban基准, 推理能力, PDDL工具

## 3 点简述
- 核心问题：大语言模型在长时程规划和推理方面的能力尚未被充分研究。
- 方法要点：基于Sokoban谜题设计新基准，简化以隔离长时程规划与状态持久性。
- 实验或效果：发现规划性能在超过25步时显著下降，PDDL工具带来有限改进。

## 摘要（原文）

> Although the capabilities of large language models have been increasingly tested on complex reasoning tasks, their long-horizon planning abilities have not yet been extensively investigated. In this work, we provide a systematic assessment of the planning and long-horizon reasoning capabilities of state-of-the-art Large Reasoning Models (LRMs). We propose a novel benchmark based on Sokoban puzzles, intentionally simplified to isolate long-horizon planning from state persistence. Our findings reveal a consistent degradation in planning performance when more than 25 moves are required to reach the solution, suggesting a fundamental constraint on forward planning capacity. We show that equipping LRMs with Planning Domain Definition Language (PDDL) parsing, validation, and solving tools allows for modest improvements, suggesting inherent architectural limitations which might not be overcome by test-time scaling approaches alone.

