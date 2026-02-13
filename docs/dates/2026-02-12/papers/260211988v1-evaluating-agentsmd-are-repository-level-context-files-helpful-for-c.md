---
layout: default
title: Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?
---

# Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?
**arXiv**：[2602.11988v1](https://arxiv.org/abs/2602.11988) · [PDF](https://arxiv.org/pdf/2602.11988.pdf)  
**作者**：Thibaud Gloaguen, Niels Mündler, Mark Müller, Veselin Raychev, Martin Vechev  

**一句话要点**：评估AGENTS.md：仓库级上下文文件对编码代理任务完成率有负面影响

**关键词**：编码代理, 上下文文件, 任务评估, 软件工程基准, LLM生成, 仓库级优化

## 3 点简述
- 核心问题：研究仓库级上下文文件（如AGENTS.md）是否提升编码代理在真实任务中的性能
- 方法要点：在SWE-bench任务和含开发者提交上下文文件的新问题集上评估编码代理
- 实验或效果：上下文文件降低任务成功率，增加推理成本，建议仅描述最小需求

## 摘要（原文）

> A widespread practice in software development is to tailor coding agents to repositories using context files, such as AGENTS.md, by either manually or automatically generating them. Although this practice is strongly encouraged by agent developers, there is currently no rigorous investigation into whether such context files are actually effective for real-world tasks. In this work, we study this question and evaluate coding agents' task completion performance in two complementary settings: established SWE-bench tasks from popular repositories, with LLM-generated context files following agent-developer recommendations, and a novel collection of issues from repositories containing developer-committed context files.
>   Across multiple coding agents and LLMs, we find that context files tend to reduce task success rates compared to providing no repository context, while also increasing inference cost by over 20%. Behaviorally, both LLM-generated and developer-provided context files encourage broader exploration (e.g., more thorough testing and file traversal), and coding agents tend to respect their instructions. Ultimately, we conclude that unnecessary requirements from context files make tasks harder, and human-written context files should describe only minimal requirements.

