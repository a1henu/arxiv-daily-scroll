---
layout: default
title: Autonomous Agents and Policy Compliance: A Framework for Reasoning About Penalties
---

# Autonomous Agents and Policy Compliance: A Framework for Reasoning About Penalties
**arXiv**：[2512.03931v1](https://arxiv.org/abs/2512.03931) · [PDF](https://arxiv.org/pdf/2512.03931.pdf)  
**作者**：Vineel Tummala, Daniela Inclezan  

**一句话要点**：提出基于逻辑编程的框架，使自主代理能推理政策违规惩罚并权衡高风险目标。

**关键词**：自主代理, 政策合规, 逻辑编程, 惩罚推理, 答案集编程, 政策建模

## 3 点简述
- 核心问题：现有方法侧重确保政策合规，但忽略为达成高风险目标可能需违规的场景。
- 方法要点：扩展AOPL语言以纳入惩罚，集成ASP进行推理，区分违规计划并优先最小化后果。
- 实验或效果：在多个领域实验显示，框架生成更高质量计划，避免有害行动，有时提升计算效率。

## 摘要（原文）

> This paper presents a logic programming-based framework for policy-aware autonomous agents that can reason about potential penalties for non-compliance and act accordingly. While prior work has primarily focused on ensuring compliance, our approach considers scenarios where deviating from policies may be necessary to achieve high-stakes goals. Additionally, modeling non-compliant behavior can assist policymakers by simulating realistic human decision-making. Our framework extends Gelfond and Lobo's Authorization and Obligation Policy Language (AOPL) to incorporate penalties and integrates Answer Set Programming (ASP) for reasoning. Compared to previous approaches, our method ensures well-formed policies, accounts for policy priorities, and enhances explainability by explicitly identifying rule violations and their consequences. Building on the work of Harders and Inclezan, we introduce penalty-based reasoning to distinguish between non-compliant plans, prioritizing those with minimal repercussions. To support this, we develop an automated translation from the extended AOPL into ASP and refine ASP-based planning algorithms to account for incurred penalties. Experiments in two domains demonstrate that our framework generates higher-quality plans that avoid harmful actions while, in some cases, also improving computational efficiency. These findings underscore its potential for enhancing autonomous decision-making and informing policy refinement. Under consideration in Theory and Practice of Logic Programming (TPLP).

