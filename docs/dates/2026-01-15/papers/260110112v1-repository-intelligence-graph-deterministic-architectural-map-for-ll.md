---
layout: default
title: Repository Intelligence Graph: Deterministic Architectural Map for LLM Code Assistants
---

# Repository Intelligence Graph: Deterministic Architectural Map for LLM Code Assistants
**arXiv**：[2601.10112v1](https://arxiv.org/abs/2601.10112) · [PDF](https://arxiv.org/pdf/2601.10112.pdf)  
**作者**：Tsvi Cherny-Shahar, Amiram Yehudai  

**一句话要点**：提出Repository Intelligence Graph以解决多语言项目中LLM代码助手构建和测试结构恢复难题

**关键词**：代码仓库智能图, 构建系统分析, 多语言项目, LLM代码助手, 确定性提取器, 测试结构恢复

## 3 点简述
- 核心问题：多语言项目中，跨语言依赖和异构构建系统导致代码助手难以准确恢复构建和测试结构。
- 方法要点：引入RIG作为确定性架构图，通过SPADE提取器从构建和测试工件生成LLM友好的JSON视图。
- 实验或效果：在八个仓库中，RIG将平均准确率提升12.2%，完成时间减少53.9%，多语言仓库效果更显著。

## 摘要（原文）

> Repository aware coding agents often struggle to recover build and test structure, especially in multilingual projects where cross language dependencies are encoded across heterogeneous build systems and tooling. We introduce the Repository Intelligence Graph (RIG), a deterministic, evidence backed architectural map that represents buildable components, aggregators, runners, tests, external packages, and package managers, connected by explicit dependency and coverage edges that trace back to concrete build and test definitions. We also present SPADE, a deterministic extractor that constructs RIG from build and test artifacts (currently with an automatic CMake plugin based on the CMake File API and CTest metadata), and exposes RIG as an LLM friendly JSON view that agents can treat as the authoritative description of repository structure.
>   We evaluate three commercial agents (Claude Code, Cursor, Codex) on eight repositories spanning low to high build oriented complexity, including the real world MetaFFI project. Each agent answers thirty structured questions per repository with and without RIG in context, and we measure accuracy, wall clock completion time, and efficiency (seconds per correct answer). Across repositories and agents, providing RIG improves mean accuracy by 12.2\% and reduces completion time by 53.9\%, yielding a mean 57.8\% reduction in seconds per correct answer. Gains are larger in multilingual repositories, which improve by 17.7\% in accuracy and 69.5\% in efficiency on average, compared to 6.6\% and 46.1\% in single language repositories. Qualitative analysis suggests that RIG shifts failures from structural misunderstandings toward reasoning mistakes over a correct structure, while rare regressions highlight that graph based reasoning quality remains a key factor.

