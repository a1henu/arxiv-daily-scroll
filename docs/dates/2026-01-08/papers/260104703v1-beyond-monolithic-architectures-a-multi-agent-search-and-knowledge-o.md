---
layout: default
title: Beyond Monolithic Architectures: A Multi-Agent Search and Knowledge Optimization Framework for Agentic Search
---

# Beyond Monolithic Architectures: A Multi-Agent Search and Knowledge Optimization Framework for Agentic Search
**arXiv**：[2601.04703v1](https://arxiv.org/abs/2601.04703) · [PDF](https://arxiv.org/pdf/2601.04703.pdf)  
**作者**：Yiqun Chen, Lingyong Yan, Zixuan Yang, Erhan Zhang, Jiashu Zhao, Shuaiqiang Wang, Dawei Yin, Jiaxin Mao  

**一句话要点**：提出多智能体搜索与知识框架M-ASK，以解决单体智能体在代理搜索中的结构瓶颈问题。

**关键词**：代理搜索, 多智能体框架, 知识管理, 回合级奖励, 多跳问答

## 3 点简述
- 核心问题：单体智能体在代理搜索中存在推理输出无约束、奖励稀疏和搜索噪声等结构瓶颈。
- 方法要点：将搜索解耦为搜索行为智能体和知识管理智能体，采用回合级奖励实现稳定协调。
- 实验或效果：在多跳问答基准上超越基线，实现更高答案准确性和更稳定训练动态。

## 摘要（原文）

> Agentic search has emerged as a promising paradigm for complex information seeking by enabling Large Language Models (LLMs) to interleave reasoning with tool use. However, prevailing systems rely on monolithic agents that suffer from structural bottlenecks, including unconstrained reasoning outputs that inflate trajectories, sparse outcome-level rewards that complicate credit assignment, and stochastic search noise that destabilizes learning. To address these challenges, we propose \textbf{M-ASK} (Multi-Agent Search and Knowledge), a framework that explicitly decouples agentic search into two complementary roles: Search Behavior Agents, which plan and execute search actions, and Knowledge Management Agents, which aggregate, filter, and maintain a compact internal context. This decomposition allows each agent to focus on a well-defined subtask and reduces interference between search and context construction. Furthermore, to enable stable coordination, M-ASK employs turn-level rewards to provide granular supervision for both search decisions and knowledge updates. Experiments on multi-hop QA benchmarks demonstrate that M-ASK outperforms strong baselines, achieving not only superior answer accuracy but also significantly more stable training dynamics.\footnote{The source code for M-ASK is available at https://github.com/chenyiqun/M-ASK.}

