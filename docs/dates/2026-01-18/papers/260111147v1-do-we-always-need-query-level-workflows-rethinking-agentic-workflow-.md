---
layout: default
title: Do We Always Need Query-Level Workflows? Rethinking Agentic Workflow Generation for Multi-Agent Systems
---

# Do We Always Need Query-Level Workflows? Rethinking Agentic Workflow Generation for Multi-Agent Systems
**arXiv**：[2601.11147v1](https://arxiv.org/abs/2601.11147) · [PDF](https://arxiv.org/pdf/2601.11147.pdf)  
**作者**：Zixu Wang, Bingbing Xu, Yige Yuan, Huawei Shen, Xueqi Cheng  

**一句话要点**：提出SCALE框架以低成本生成任务级工作流，减少多智能体系统开销

**关键词**：多智能体系统, 工作流生成, 任务级评估, 自预测优化, 令牌效率, 生成式奖励建模

## 3 点简述
- 核心问题：现有方法在任务级或查询级生成工作流，但成本效益不明确
- 方法要点：通过自预测优化器和少量校准评估，避免全验证执行
- 实验或效果：在多个数据集上性能仅平均下降0.61%，令牌使用减少高达83%

## 摘要（原文）

> Multi-Agent Systems (MAS) built on large language models typically solve complex tasks by coordinating multiple agents through workflows. Existing approaches generates workflows either at task level or query level, but their relative costs and benefits remain unclear. After rethinking and empirical analyses, we show that query-level workflow generation is not always necessary, since a small set of top-K best task-level workflows together already covers equivalent or even more queries. We further find that exhaustive execution-based task-level evaluation is both extremely token-costly and frequently unreliable. Inspired by the idea of self-evolution and generative reward modeling, we propose a low-cost task-level generation framework \textbf{SCALE}, which means \underline{\textbf{S}}elf prediction of the optimizer with few shot \underline{\textbf{CAL}}ibration for \underline{\textbf{E}}valuation instead of full validation execution. Extensive experiments demonstrate that \textbf{SCALE} maintains competitive performance, with an average degradation of just 0.61\% compared to existing approach across multiple datasets, while cutting overall token usage by up to 83\%.

