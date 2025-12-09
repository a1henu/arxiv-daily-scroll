---
layout: default
title: Understanding LLM Agent Behaviours via Game Theory: Strategy Recognition, Biases and Multi-Agent Dynamics
---

# Understanding LLM Agent Behaviours via Game Theory: Strategy Recognition, Biases and Multi-Agent Dynamics
**arXiv**：[2512.07462v1](https://arxiv.org/abs/2512.07462) · [PDF](https://arxiv.org/pdf/2512.07462.pdf)  
**作者**：Trung-Kiet Huynh, Duy-Minh Dao-Sy, Thanh-Bang Cao, Phong-Hao Le, Hong-Dan Nguyen, Phu-Quy Nguyen-Lam, Minh-Luan Nguyen-Vo, Hong-Phat Pham, Phu-Hoa Pham, Thien-Kim Than, Chi-Nguyen Tran, Huy Tran, Gia-Thoai Tran-Le, Alessio Buscemi, Le Hong Trang, The Anh Han  

**一句话要点**：扩展FAIRGAME框架以评估LLM在重复社会困境中的战略行为，揭示合作偏差与语言影响

**关键词**：大型语言模型, 博弈论, 多智能体系统, 社会困境, 行为评估, AI治理

## 3 点简述
- 核心问题：理解LLM作为自主决策者在多智能体系统中的战略意图，对AI安全与协调至关重要
- 方法要点：通过收益缩放囚徒困境和动态收益公共物品游戏，系统评估LLM行为模式
- 实验或效果：发现LLM表现出激励敏感合作、跨语言差异和背叛倾向，行为意图受模型和语言影响

## 摘要（原文）

> As Large Language Models (LLMs) increasingly operate as autonomous decision-makers in interactive and multi-agent systems and human societies, understanding their strategic behaviour has profound implications for safety, coordination, and the design of AI-driven social and economic infrastructures. Assessing such behaviour requires methods that capture not only what LLMs output, but the underlying intentions that guide their decisions. In this work, we extend the FAIRGAME framework to systematically evaluate LLM behaviour in repeated social dilemmas through two complementary advances: a payoff-scaled Prisoners Dilemma isolating sensitivity to incentive magnitude, and an integrated multi-agent Public Goods Game with dynamic payoffs and multi-agent histories. These environments reveal consistent behavioural signatures across models and languages, including incentive-sensitive cooperation, cross-linguistic divergence and end-game alignment toward defection. To interpret these patterns, we train traditional supervised classification models on canonical repeated-game strategies and apply them to FAIRGAME trajectories, showing that LLMs exhibit systematic, model- and language-dependent behavioural intentions, with linguistic framing at times exerting effects as strong as architectural differences. Together, these findings provide a unified methodological foundation for auditing LLMs as strategic agents and reveal systematic cooperation biases with direct implications for AI governance, collective decision-making, and the design of safe multi-agent systems.

