---
layout: default
title: LiveCultureBench: a Multi-Agent, Multi-Cultural Benchmark for Large Language Models in Dynamic Social Simulations
---

# LiveCultureBench: a Multi-Agent, Multi-Cultural Benchmark for Large Language Models in Dynamic Social Simulations
**arXiv**：[2603.01952v1](https://arxiv.org/abs/2603.01952) · [PDF](https://arxiv.org/pdf/2603.01952.pdf)  
**作者**：Viet-Thanh Pham, Lizhen Qu, Thuy-Trang Vu, Gholamreza Haffari, Dinh Phung  

**一句话要点**：提出LiveCultureBench多文化动态基准，评估大语言模型在模拟社会中的任务完成与文化规范遵循。

**关键词**：多文化基准, 社会模拟, LLM代理评估, 规范遵循, 任务完成, 评估可靠性

## 3 点简述
- 核心问题：现有评估侧重任务成功，忽略文化适宜性与评估可靠性。
- 方法要点：构建多文化模拟城镇，嵌入LLM代理，结合任务与规范评估。
- 实验或效果：研究跨文化鲁棒性、任务-规范权衡及LLM作为评估者的可靠性。

## 摘要（原文）

> Large language models (LLMs) are increasingly deployed as autonomous agents, yet evaluations focus primarily on task success rather than cultural appropriateness or evaluator reliability. We introduce LiveCultureBench, a multi-cultural, dynamic benchmark that embeds LLMs as agents in a simulated town and evaluates them on both task completion and adherence to socio-cultural norms. The simulation models a small city as a location graph with synthetic residents having diverse demographic and cultural profiles. Each episode assigns one resident a daily goal while others provide social context. An LLM-based verifier generates structured judgments on norm violations and task progress, which we aggregate into metrics capturing task-norm trade-offs and verifier uncertainty. Using LiveCultureBench across models and cultural profiles, we study (i) cross-cultural robustness of LLM agents, (ii) how they balance effectiveness against norm sensitivity, and (iii) when LLM-as-a-judge evaluation is reliable for automated benchmarking versus when human oversight is needed.

