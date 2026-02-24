---
layout: default
title: TAPE: Tool-Guided Adaptive Planning and Constrained Execution in Language Model Agents
---

# TAPE: Tool-Guided Adaptive Planning and Constrained Execution in Language Model Agents
**arXiv**：[2602.19633v1](https://arxiv.org/abs/2602.19633) · [PDF](https://arxiv.org/pdf/2602.19633.pdf)  
**作者**：Jongwon Jeong, Jungtaek Kim, Kangwook Lee  

**一句话要点**：提出TAPE框架以解决语言模型代理在严格约束环境中的规划与执行问题

**关键词**：语言模型代理, 自适应规划, 约束执行, 工具引导, 图规划, 环境反馈

## 3 点简述
- 核心问题：语言模型代理在单错误导致不可恢复失败的环境中表现脆弱，源于规划不完善和执行随机性
- 方法要点：通过图聚合多计划并使用外部求解器优化规划，执行时采用约束解码和自适应重规划
- 实验或效果：在多个基准测试中显著提升成功率，硬设置平均提高21.0个百分点

## 摘要（原文）

> Language Model (LM) agents have demonstrated remarkable capabilities in solving tasks that require multiple interactions with the environment. However, they remain vulnerable in environments where a single error often leads to irrecoverable failure, particularly under strict feasibility constraints. We systematically analyze existing agent frameworks, identifying imperfect planning and stochastic execution as the primary causes. To address these challenges, we propose Tool-guided Adaptive Planning with constrained Execution (TAPE). TAPE enhances planning capability by aggregating multiple plans into a graph and employing an external solver to identify a feasible path. During execution, TAPE employs constrained decoding to reduce sampling noise, while adaptively re-planning whenever environmental feedback deviates from the intended state. Experiments across Sokoban, ALFWorld, MuSiQue, and GSM8K-Hard demonstrate that TAPE consistently outperforms existing frameworks, with particularly large gains on hard settings, improving success rates by 21.0 percentage points on hard settings on average, and by 20.0 percentage points for weaker base models on average. Code and data available at here.

