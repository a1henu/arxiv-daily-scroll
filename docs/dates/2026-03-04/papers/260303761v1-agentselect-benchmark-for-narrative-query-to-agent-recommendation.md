---
layout: default
title: AgentSelect: Benchmark for Narrative Query-to-Agent Recommendation
---

# AgentSelect: Benchmark for Narrative Query-to-Agent Recommendation
**arXiv**：[2603.03761v1](https://arxiv.org/abs/2603.03761) · [PDF](https://arxiv.org/pdf/2603.03761.pdf)  
**作者**：Yunxiao Shi, Wujiang Xu, Tingwei Chen, Haoning Shang, Ling Yang, Yunfeng Wan, Zhuo Cao, Xing Zi, Dimitris N. Metaxas, Min Xu  

**一句话要点**：提出AgentSelect基准，通过叙事查询到智能体推荐解决智能体配置选择问题。

**关键词**：智能体推荐, 基准构建, 能力配置, 查询条件监督, 数据统一, 迁移学习

## 3 点简述
- 核心问题：现有基准评估孤立组件，缺乏查询条件监督以推荐端到端智能体配置。
- 方法要点：将智能体选择重构为基于能力配置的叙事查询到智能体推荐，统一异构评估数据。
- 实验或效果：分析显示从密集头部重用到长尾监督的转变，模型在AgentSelect上训练可迁移到未见市场。

## 摘要（原文）

> LLM agents are rapidly becoming the practical interface for task automation, yet the ecosystem lacks a principled way to choose among an exploding space of deployable configurations. Existing LLM leaderboards and tool/agent benchmarks evaluate components in isolation and remain fragmented across tasks, metrics, and candidate pools, leaving a critical research gap: there is little query-conditioned supervision for learning to recommend end-to-end agent configurations that couple a backbone model with a toolkit. We address this gap with AgentSelect, a benchmark that reframes agent selection as narrative query-to-agent recommendation over capability profiles and systematically converts heterogeneous evaluation artifacts into unified, positive-only interaction data. AgentSelectcomprises 111,179 queries, 107,721 deployable agents, and 251,103 interaction records aggregated from 40+ sources, spanning LLM-only, toolkit-only, and compositional agents. Our analyses reveal a regime shift from dense head reuse to long-tail, near one-off supervision, where popularity-based CF/GNN methods become fragile and content-aware capability matching is essential. We further show that Part~III synthesized compositional interactions are learnable, induce capability-sensitive behavior under controlled counterfactual edits, and improve coverage over realistic compositions; models trained on AgentSelect also transfer to a public agent marketplace (MuleRun), yielding consistent gains on an unseen catalog. Overall, AgentSelect provides the first unified data and evaluation infrastructure for agent recommendation, which establishes a reproducible foundation to study and accelerate the emerging agent ecosystem.

