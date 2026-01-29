---
layout: default
title: PathWise: Planning through World Model for Automated Heuristic Design via Self-Evolving LLMs
---

# PathWise: Planning through World Model for Automated Heuristic Design via Self-Evolving LLMs
**arXiv**：[2601.20539v1](https://arxiv.org/abs/2601.20539) · [PDF](https://arxiv.org/pdf/2601.20539.pdf)  
**作者**：Oguzhan Gungordu, Siheng Xiong, Faramarz Fekri  

**一句话要点**：提出PathWise框架，通过世界模型规划解决组合优化问题中自动启发式设计的短视与冗余问题。

**关键词**：自动启发式设计, 组合优化问题, 大型语言模型, 多智能体推理, 世界模型规划, 序列决策过程

## 3 点简述
- 现有LLM自动启发式设计依赖固定规则，导致短视生成和冗余评估。
- PathWise将启发式生成建模为基于蕴含图的序列决策过程，支持状态感知规划。
- 实验表明PathWise收敛更快、启发式更优，且能泛化到不同LLM和更大问题规模。

## 摘要（原文）

> Large Language Models (LLMs) have enabled automated heuristic design (AHD) for combinatorial optimization problems (COPs), but existing frameworks' reliance on fixed evolutionary rules and static prompt templates often leads to myopic heuristic generation, redundant evaluations, and limited reasoning about how new heuristics should be derived. We propose a novel multi-agent reasoning framework, referred to as Planning through World Model for Automated Heuristic Design via Self-Evolving LLMs (PathWise), which formulates heuristic generation as a sequential decision process over an entailment graph serving as a compact, stateful memory of the search trajectory. This approach allows the system to carry forward past decisions and reuse or avoid derivation information across generations. A policy agent plans evolutionary actions, a world model agent generates heuristic rollouts conditioned on those actions, and critic agents provide routed reflections summarizing lessons from prior steps, shifting LLM-based AHD from trial-and-error evolution toward state-aware planning through reasoning. Experiments across diverse COPs show that PathWise converges faster to better heuristics, generalizes across different LLM backbones, and scales to larger problem sizes.

