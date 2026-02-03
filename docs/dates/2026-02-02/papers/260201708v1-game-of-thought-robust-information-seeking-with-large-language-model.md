---
layout: default
title: Game of Thought: Robust Information Seeking with Large Language Models Using Game Theory
---

# Game of Thought: Robust Information Seeking with Large Language Models Using Game Theory
**arXiv**：[2602.01708v1](https://arxiv.org/abs/2602.01708) · [PDF](https://arxiv.org/pdf/2602.01708.pdf)  
**作者**：Langyuan Cui, Chun Kai Ling, Hwee Tou Ng  

**一句话要点**：提出Game of Thought框架，应用博弈论近似纳什均衡策略以提升LLMs在信息缺失场景下的最坏情况性能。

**关键词**：大语言模型, 信息寻求, 博弈论, 纳什均衡, 战略语言搜索, 最坏情况性能

## 3 点简述
- 核心问题：LLMs在信息缺失任务中，现有方法简化假设导致最坏情况性能下降，影响高风险应用。
- 方法要点：基于二十问游戏，形式化战略语言搜索问题为双人零和扩展形式博弈，应用博弈论技术近似纳什均衡策略。
- 实验或效果：实证表明，相比直接提示和启发式搜索方法，该框架在所有测试设置中一致提升最坏情况性能。

## 摘要（原文）

> Large Language Models (LLMs) are increasingly deployed in real-world scenarios where they may lack sufficient information to complete a given task. In such settings, the ability to actively seek out missing information becomes a critical capability. Existing approaches to enhancing this ability often rely on simplifying assumptions that degrade \textit{worst-case} performance. This is an issue with serious implications in high-stakes applications. In this work, we use the game of Twenty Questions to evaluate the information-seeking ability of LLMs. We introduce and formalize its adversarial counterpart, the Strategic Language Search (SLS) problem along with its variants as a two-player zero-sum extensive form game. We propose Game of Thought (GoT), a framework that applies game-theoretic techniques to approximate a Nash equilibrium (NE) strategy for the restricted variant of the game. Empirical results demonstrate that our approach consistently improves worst-case performance compared to (1) direct prompting-based methods and (2) heuristic-guided search methods across all tested settings.

