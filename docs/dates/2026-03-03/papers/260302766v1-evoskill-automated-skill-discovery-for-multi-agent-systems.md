---
layout: default
title: EvoSkill: Automated Skill Discovery for Multi-Agent Systems
---

# EvoSkill: Automated Skill Discovery for Multi-Agent Systems
**arXiv**：[2603.02766v1](https://arxiv.org/abs/2603.02766) · [PDF](https://arxiv.org/pdf/2603.02766.pdf)  
**作者**：Salaheddin Alzubi, Noah Provenzano, Jaydon Bingham, Weiyuan Chen, Tu Vu  

**一句话要点**：提出EvoSkill框架以自动发现和优化多智能体系统中的可重用技能

**关键词**：多智能体系统, 技能发现, 进化算法, 失败分析, 零样本迁移, 自动化优化

## 3 点简述
- 核心问题：现有智能体技能多为手工制作，且进化方法优化低层组件，缺乏通用性和可转移性。
- 方法要点：通过迭代失败分析自动发现和精炼技能，使用帕累托前沿选择提升验证性能的技能。
- 实验或效果：在OfficeQA和SealQA基准上分别提升准确率7.3%和12.1%，并展示技能的零样本迁移能力。

## 摘要（原文）

> Coding agents are increasingly used as general-purpose problem solvers, but their flexibility does not by itself confer the domain expertise needed for specialized tasks. Recent work addresses this through \textit{agent skills}: reusable workflows, and code, that augment agents with domain-specific capabilities. Most skills today are hand-crafted, and existing evolutionary approaches optimize low-level artifacts (e.g. prompts \& code) that are tightly coupled to specific models and tasks. We introduce \textbf{EvoSkill}, a self-evolving framework that automatically discovers and refines agent skills through iterative failure analysis. EvoSkill analyzes execution failures, proposes new skills or edits to existing ones, and materializes them into structured, reusable skill folders. A Pareto frontier of agent programs governs selection, retaining only skills that improve held-out validation performance while the underlying model remains frozen. We evaluate EvoSkill on two benchmarks: OfficeQA, a grounded reasoning benchmark over U.S.\ Treasury data, where it improves exact-match accuracy by \textbf{7.3\%} (60.6\% $\to$ 67.9\%); and SealQA, a search-augmented QA benchmark with noisy retrieval, where it yields a \textbf{12.1\%} gain (26.6\% $\to$ 38.7\%). We also investigate the zero-shot transfer capabilties of skills evolved on one task to the other; in particular: skills evolved from SealQA transfers zero-shot to BrowseComp, improving accuracy by \textbf{5.3\%} without modification demonstrating that skill-level optimization produces transferable capabilities beyond the training task.

