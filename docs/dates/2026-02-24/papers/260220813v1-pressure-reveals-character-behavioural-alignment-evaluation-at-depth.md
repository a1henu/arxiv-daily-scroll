---
layout: default
title: Pressure Reveals Character: Behavioural Alignment Evaluation at Depth
---

# Pressure Reveals Character: Behavioural Alignment Evaluation at Depth
**arXiv**：[2602.20813v1](https://arxiv.org/abs/2602.20813) · [PDF](https://arxiv.org/pdf/2602.20813.pdf)  
**作者**：Nora Petrova, John Burden  

**一句话要点**：提出基于压力场景的行为对齐基准，以评估语言模型在现实压力下的表现。

**关键词**：语言模型对齐, 行为评估基准, 多轮场景测试, 压力测试, 对齐一致性

## 3 点简述
- 核心问题：现有对齐评估缺乏现实多轮场景，导致模型行为与声称不符。
- 方法要点：构建904个多轮场景，涵盖六个类别，模拟冲突指令和工具访问。
- 实验或效果：评估24个前沿模型，发现对齐表现呈现统一结构，多数模型存在一致弱点。

## 摘要（原文）

> Evaluating alignment in language models requires testing how they behave under realistic pressure, not just what they claim they would do. While alignment failures increasingly cause real-world harm, comprehensive evaluation frameworks with realistic multi-turn scenarios remain lacking. We introduce an alignment benchmark spanning 904 scenarios across six categories -- Honesty, Safety, Non-Manipulation, Robustness, Corrigibility, and Scheming -- validated as realistic by human raters. Our scenarios place models under conflicting instructions, simulated tool access, and multi-turn escalation to reveal behavioural tendencies that single-turn evaluations miss. Evaluating 24 frontier models using LLM judges validated against human annotations, we find that even top-performing models exhibit gaps in specific categories, while the majority of models show consistent weaknesses across the board. Factor analysis reveals that alignment behaves as a unified construct (analogous to the g-factor in cognitive research) with models scoring high on one category tending to score high on others. We publicly release the benchmark and an interactive leaderboard to support ongoing evaluation, with plans to expand scenarios in areas where we observe persistent weaknesses and to add new models as they are released.

