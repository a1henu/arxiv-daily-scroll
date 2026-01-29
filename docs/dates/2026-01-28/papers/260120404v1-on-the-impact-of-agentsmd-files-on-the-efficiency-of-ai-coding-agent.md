---
layout: default
title: On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents
---

# On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents
**arXiv**：[2601.20404v1](https://arxiv.org/abs/2601.20404) · [PDF](https://arxiv.org/pdf/2601.20404.pdf)  
**作者**：Jai Lal Lulla, Seyedmoein Mohsenimofidi, Matthias Galster, Jie M. Zhang, Sebastian Baltes, Christoph Treude  

**一句话要点**：研究AGENTS.md文件对AI编码代理在GitHub拉取请求中运行效率的影响

**关键词**：AI编码代理, 仓库配置, 运行效率, 令牌消耗, GitHub拉取请求

## 3 点简述
- 核心问题：未知AI编码代理在软件仓库中的配置工件如何影响其操作效率。
- 方法要点：分析10个仓库和124个拉取请求，比较有无AGENTS.md文件时的运行时间和令牌消耗。
- 实验或效果：AGENTS.md文件关联更低的中位运行时间和输出令牌消耗，任务完成行为相似。

## 摘要（原文）

> AI coding agents such as Codex and Claude Code are increasingly used to autonomously contribute to software repositories. However, little is known about how repository-level configuration artifacts affect operational efficiency of the agents. In this paper, we study the impact of AGENTS.md files on the runtime and token consumption of AI coding agents operating on GitHub pull requests. We analyze 10 repositories and 124 pull requests, executing agents under two conditions: with and without an AGENTS.md file. We measure wall-clock execution time and token usage during agent execution. Our results show that the presence of AGENTS.md is associated with a lower median runtime ($Δ28.64$%) and reduced output token consumption ($Δ16.58$%), while maintaining a comparable task completion behavior. Based on these results, we discuss immediate implications for the configuration and deployment of AI coding agents in practice, and outline a broader research agenda on the role of repository-level instructions in shaping the behavior, efficiency, and integration of AI coding agents in software development workflows.

