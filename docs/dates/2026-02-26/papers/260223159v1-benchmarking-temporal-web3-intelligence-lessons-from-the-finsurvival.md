---
layout: default
title: Benchmarking Temporal Web3 Intelligence: Lessons from the FinSurvival 2025 Challenge
---

# Benchmarking Temporal Web3 Intelligence: Lessons from the FinSurvival 2025 Challenge
**arXiv**：[2602.23159v1](https://arxiv.org/abs/2602.23159) · [PDF](https://arxiv.org/pdf/2602.23159.pdf)  
**作者**：Oshani Seneviratne, Fernando Spadea, Adrien Pavao, Aaron Micah Green, Kristin P. Bennett  

**一句话要点**：提出FinSurvival 2025挑战赛作为基准，以解决Temporal Web3领域缺乏共享、可复现基准的问题。

**关键词**：时间Web3智能, 生存预测, 基准设计, 去中心化平台, 时间动态建模

## 3 点简述
- 核心问题：Temporal Web3领域缺乏捕获真实世界时间动态（如审查和非平稳性）的共享基准，阻碍方法进展。
- 方法要点：基于Aave v3协议的2180万交易记录，设计16个生存预测任务来建模用户行为转换。
- 实验或效果：领域感知的时间特征构建显著优于通用建模方法，为下一代时间基准提供经验教训。

## 摘要（原文）

> Temporal Web analytics increasingly relies on large-scale, longitudinal data to understand how users, content, and systems evolve over time. A rapidly growing frontier is the \emph{Temporal Web3}: decentralized platforms whose behavior is recorded as immutable, time-stamped event streams. Despite the richness of this data, the field lacks shared, reproducible benchmarks that capture real-world temporal dynamics, specifically censoring and non-stationarity, across extended horizons. This absence slows methodological progress and limits the transfer of techniques between Web3 and broader Web domains. In this paper, we present the \textit{FinSurvival Challenge 2025} as a case study in benchmarking \emph{temporal Web3 intelligence}. Using 21.8 million transaction records from the Aave v3 protocol, the challenge operationalized 16 survival prediction tasks to model user behavior transitions.We detail the benchmark design and the winning solutions, highlighting how domain-aware temporal feature construction significantly outperformed generic modeling approaches. Furthermore, we distill lessons for next-generation temporal benchmarks, arguing that Web3 systems provide a high-fidelity sandbox for studying temporal challenges, such as churn, risk, and evolution that are fundamental to the wider Web.

