---
layout: default
title: ReasonBENCH: Benchmarking the (In)Stability of LLM Reasoning
---

# ReasonBENCH: Benchmarking the (In)Stability of LLM Reasoning
**arXiv**：[2512.07795v1](https://arxiv.org/abs/2512.07795) · [PDF](https://arxiv.org/pdf/2512.07795.pdf)  
**作者**：Nearchos Potamitis, Lars Klein, Akhil Arora  

**一句话要点**：提出ReasonBENCH基准以量化大语言模型推理的不稳定性

**关键词**：大语言模型推理, 基准测试, 不确定性量化, 可复现性评估, 多轮协议, 性能稳定性

## 3 点简述
- 核心问题：当前评估忽视随机解码导致的不稳定性，影响性能可靠性和可复现性
- 方法要点：提供模块化评估库、多轮协议和公开排行榜，标准化推理框架与任务
- 实验或效果：发现多数推理策略不稳定，性能相近方法置信区间差异可达四倍

## 摘要（原文）

> Large language models (LLMs) are increasingly deployed in settings where reasoning, such as multi-step problem solving and chain-of-thought, is essential. Yet, current evaluation practices overwhelmingly report single-run accuracy while ignoring the intrinsic uncertainty that naturally arises from stochastic decoding. This omission creates a blind spot because practitioners cannot reliably assess whether a method's reported performance is stable, reproducible, or cost-consistent. We introduce ReasonBENCH, the first benchmark designed to quantify the underlying instability in LLM reasoning. ReasonBENCH provides (i) a modular evaluation library that standardizes reasoning frameworks, models, and tasks, (ii) a multi-run protocol that reports statistically reliable metrics for both quality and cost, and (iii) a public leaderboard to encourage variance-aware reporting. Across tasks from different domains, we find that the vast majority of reasoning strategies and models exhibit high instability. Notably, even strategies with similar average performance can display confidence intervals up to four times wider, and the top-performing methods often incur higher and less stable costs. Such instability compromises reproducibility across runs and, consequently, the reliability of reported performance. To better understand these dynamics, we further analyze the impact of prompts, model families, and scale on the trade-off between solve rate and stability. Our results highlight reproducibility as a critical dimension for reliable LLM reasoning and provide a foundation for future reasoning methods and uncertainty quantification techniques. ReasonBENCH is publicly available at https://github.com/au-clan/ReasonBench .

