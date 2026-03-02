---
layout: default
title: PseudoAct: Leveraging Pseudocode Synthesis for Flexible Planning and Action Control in Large Language Model Agents
---

# PseudoAct: Leveraging Pseudocode Synthesis for Flexible Planning and Action Control in Large Language Model Agents
**arXiv**：[2602.23668v1](https://arxiv.org/abs/2602.23668) · [PDF](https://arxiv.org/pdf/2602.23668.pdf)  
**作者**：Yihan, Wen, Xin Chen  

**一句话要点**：提出PseudoAct框架，通过伪代码合成解决大语言模型代理在复杂长程任务中的冗余与不稳定问题。

**关键词**：大语言模型代理, 伪代码合成, 长程任务规划, 控制流编码, 工具协调, 决策效率

## 3 点简述
- 核心问题：现有大语言模型代理在复杂长程任务中常出现冗余工具使用、推理不稳定和高令牌消耗。
- 方法要点：利用大语言模型合成结构化伪代码计划，明确编码控制流如序列、条件、循环和并行组合。
- 实验或效果：在基准数据集上显著优于现有反应式代理方法，在FEVER上成功率提升20.93%，HotpotQA上达到新SOTA。

## 摘要（原文）

> Large language model (LLM) agents typically rely on reactive decision-making paradigms such as ReAct, selecting actions conditioned on growing execution histories. While effective for short tasks, these approaches often lead to redundant tool usage, unstable reasoning, and high token consumption in complex long-horizon tasks involving branching, iteration, or multi-tool coordination. To address these limitations, this paper introduces PseudoAct, a novel framework for flexible planning and action control in LLM agents through pseudocode synthesis. Leveraging the ability of LLMs to express task-solving strategies as code, PseudoAct synthesizes a structured pseudocode plan that decomposes a task into subtasks and explicitly encodes control flow, including sequencing, conditionals, loops, parallel composition, and combinations of these logic primitives. Actions are then executed by following this global plan, making the decision logic explicit and temporally coherent. This design reduces redundant actions, prevents infinite loops, and avoids uninformative alternative exploration, enabling consistent and efficient long-horizon decision-making. Experiments on benchmark datasets show that our method significantly outperforms existing reactive agent approaches, achieving a 20.93% absolute gain in success rate on FEVER and setting a new state-of-the-art on HotpotQA.

