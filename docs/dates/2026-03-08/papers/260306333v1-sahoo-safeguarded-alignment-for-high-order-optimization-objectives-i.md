---
layout: default
title: SAHOO: Safeguarded Alignment for High-Order Optimization Objectives in Recursive Self-Improvement
---

# SAHOO: Safeguarded Alignment for High-Order Optimization Objectives in Recursive Self-Improvement
**arXiv**：[2603.06333v1](https://arxiv.org/abs/2603.06333) · [PDF](https://arxiv.org/pdf/2603.06333.pdf)  
**作者**：Subramanyam Sahoo, Aman Chadha, Vinija Jain, Divya Chaudhary  

**一句话要点**：提出SAHOO框架以解决递归自改进中的对齐漂移问题，通过三重保障实现可测量控制。

**关键词**：递归自改进, 对齐漂移, 目标漂移指数, 约束保持, 回归风险量化, 代码生成

## 3 点简述
- 核心问题：递归自改进中迭代自我修改可能导致对齐漂移，需监控和约束风险。
- 方法要点：引入目标漂移指数、约束保持检查和回归风险量化三重保障机制。
- 实验或效果：在189个任务中提升代码生成18.3%、数学推理16.8%，并保持低违规率。

## 摘要（原文）

> Recursive self-improvement is moving from theory to practice: modern systems can critique, revise, and evaluate their own outputs, yet iterative self-modification risks subtle alignment drift. We introduce SAHOO, a practical framework to monitor and control drift through three safeguards: (i) the Goal Drift Index (GDI), a learned multi-signal detector combining semantic, lexical, structural, and distributional measures; (ii) constraint preservation checks that enforce safety-critical invariants such as syntactic correctness and non-hallucination; and (iii) regression-risk quantification to flag improvement cycles that undo prior gains. Across 189 tasks in code generation, mathematical reasoning, and truthfulness, SAHOO produces substantial quality gains, including 18.3 percent improvement in code tasks and 16.8 percent in reasoning, while preserving constraints in two domains and maintaining low violations in truthfulness. Thresholds are calibrated on a small validation set of 18 tasks across three cycles. We further map the capability-alignment frontier, showing efficient early improvement cycles but rising alignment costs later and exposing domain-specific tensions such as fluency versus factuality. SAHOO therefore makes alignment preservation during recursive self-improvement measurable, deployable, and systematically validated at scale.

