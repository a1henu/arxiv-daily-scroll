---
layout: default
title: ContextBench: A Benchmark for Context Retrieval in Coding Agents
---

# ContextBench: A Benchmark for Context Retrieval in Coding Agents
**arXiv**：[2602.05892v1](https://arxiv.org/abs/2602.05892) · [PDF](https://arxiv.org/pdf/2602.05892.pdf)  
**作者**：Han Li, Letian Zhu, Bohan Zhang, Rili Feng, Jiaming Wang, Yue Pan, Earl T. Barr, Sarro Federica, Zhaoyang Chu, He Ye  

**一句话要点**：提出ContextBench基准以评估编码代理在问题解决中的上下文检索过程

**关键词**：编码代理评估, 上下文检索基准, 过程导向分析, LLM推理, 软件任务, 自动化评估

## 3 点简述
- 现有评估聚焦任务成功，缺乏对编码代理上下文检索过程的洞察
- ContextBench包含多语言任务和人工标注的黄金上下文，支持自动化评估框架
- 实验显示代理架构对检索提升有限，LLM偏好召回率，存在探索与利用差距

## 摘要（原文）

> LLM-based coding agents have shown strong performance on automated issue resolution benchmarks, yet existing evaluations largely focus on final task success, providing limited insight into how agents retrieve and use code context during problem solving. We introduce ContextBench, a process-oriented evaluation of context retrieval in coding agents. ContextBench consists of 1,136 issue-resolution tasks from 66 repositories across eight programming languages, each augmented with human-annotated gold contexts. We further implement an automated evaluation framework that tracks agent trajectories and measures context recall, precision, and efficiency throughout issue resolution. Using ContextBench, we evaluate four frontier LLMs and five coding agents. Our results show that sophisticated agent scaffolding yields only marginal gains in context retrieval ("The Bitter Lesson" of coding agents), LLMs consistently favor recall over precision, and substantial gaps exist between explored and utilized context. ContextBench augments existing end-to-end benchmarks with intermediate gold-context metrics that unbox the issue-resolution process. These contexts offer valuable intermediate signals for guiding LLM reasoning in software tasks. Data and code are available at: https://cioutn.github.io/context-bench/.

