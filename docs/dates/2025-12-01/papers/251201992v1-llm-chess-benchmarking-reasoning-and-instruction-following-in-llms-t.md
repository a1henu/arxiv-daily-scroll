---
layout: default
title: LLM CHESS: Benchmarking Reasoning and Instruction-Following in LLMs through Chess
---

# LLM CHESS: Benchmarking Reasoning and Instruction-Following in LLMs through Chess
**arXiv**：[2512.01992v1](https://arxiv.org/abs/2512.01992) · [PDF](https://arxiv.org/pdf/2512.01992.pdf)  
**作者**：Sai Kolasani, Maxim Saplin, Nicholas Crispino, Kyle Montgomery, Jared Quincy Davis, Matei Zaharia, Chi Wang, Chenguang Wang  

**一句话要点**：提出LLM CHESS评估框架，通过国际象棋中的扩展代理交互来测试大语言模型的推理和指令遵循能力。

**关键词**：大语言模型评估, 推理能力测试, 指令遵循基准, 国际象棋交互, 动态基准设计

## 3 点简述
- 核心问题：评估大语言模型在复杂动态任务中的推理和指令遵循泛化能力。
- 方法要点：设计基于国际象棋的交互式基准，使用行为指标和Elo评分进行模型排名。
- 实验或效果：揭示推理与非推理模型间的差距，减少过拟合和记忆化，支持未来研究。

## 摘要（原文）

> We introduce LLM CHESS, an evaluation framework designed to probe the generalization of reasoning and instruction-following abilities in large language models (LLMs) through extended agentic interaction in the domain of chess. We rank over 50 open and closed source models by playing against a random opponent using a range of behavioral metrics, including win and loss rates, move quality, move legality, hallucinated actions, and game duration. For a subset of top reasoning models, we derive an Elo estimate by playing against a chess engine with variably configured skill, which allows for comparisons between models in an easily understandable way. Despite the simplicity of the instruction-following task and the weakness of the opponent, many state-of-the-art models struggle to complete games or achieve consistent wins. Similar to other benchmarks on complex reasoning tasks, our experiments reveal a clear separation between reasoning and non-reasoning models. However, unlike existing static benchmarks, the stochastic and dynamic nature of LLM CHESS uniquely reduces overfitting and memorization while preventing benchmark saturation, proving difficult even for top reasoning models. To support future work on evaluating reasoning and instruction-following in LLMs, we release our experimental framework, a public leaderboard, and a dataset of associated games.

