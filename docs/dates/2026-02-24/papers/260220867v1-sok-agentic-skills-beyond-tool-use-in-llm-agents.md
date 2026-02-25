---
layout: default
title: SoK: Agentic Skills -- Beyond Tool Use in LLM Agents
---

# SoK: Agentic Skills -- Beyond Tool Use in LLM Agents
**arXiv**：[2602.20867v1](https://arxiv.org/abs/2602.20867) · [PDF](https://arxiv.org/pdf/2602.20867.pdf)  
**作者**：Yanna Jiang, Delong Li, Haiyu Deng, Baihe Ma, Xu Wang, Qin Wang, Guangsheng Yu  

**一句话要点**：提出智能体技能生命周期框架与分类法，以提升长流程任务执行可靠性

**关键词**：智能体技能, 生命周期管理, 设计模式, 安全风险, 技能评估, 长流程任务

## 3 点简述
- 核心问题：智能体系统依赖可重用程序能力（技能）执行长流程任务，但缺乏系统化生命周期管理。
- 方法要点：建立技能全生命周期（发现、实践、蒸馏等）映射，引入设计模式和表示×范围分类法。
- 实验或效果：分析安全风险（如恶意技能案例），调查评估方法，显示精选技能可提高成功率。

## 摘要（原文）

> Agentic systems increasingly rely on reusable procedural capabilities, \textit{a.k.a., agentic skills}, to execute long-horizon workflows reliably. These capabilities are callable modules that package procedural knowledge with explicit applicability conditions, execution policies, termination criteria, and reusable interfaces. Unlike one-off plans or atomic tool calls, skills operate (and often do well) across tasks.
>   This paper maps the skill layer across the full lifecycle (discovery, practice, distillation, storage, composition, evaluation, and update) and introduces two complementary taxonomies. The first is a system-level set of \textbf{seven design patterns} capturing how skills are packaged and executed in practice, from metadata-driven progressive disclosure and executable code skills to self-evolving libraries and marketplace distribution. The second is an orthogonal \textbf{representation $\times$ scope} taxonomy describing what skills \emph{are} (natural language, code, policy, hybrid) and what environments they operate over (web, OS, software engineering, robotics).
>   We analyze the security and governance implications of skill-based agents, covering supply-chain risks, prompt injection via skill payloads, and trust-tiered execution, grounded by a case study of the ClawHavoc campaign in which nearly 1{,}200 malicious skills infiltrated a major agent marketplace, exfiltrating API keys, cryptocurrency wallets, and browser credentials at scale. We further survey deterministic evaluation approaches, anchored by recent benchmark evidence that curated skills can substantially improve agent success rates while self-generated skills may degrade them. We conclude with open challenges toward robust, verifiable, and certifiable skills for real-world autonomous agents.

