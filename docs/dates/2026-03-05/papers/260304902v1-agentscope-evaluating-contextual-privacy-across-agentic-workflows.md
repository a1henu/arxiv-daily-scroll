---
layout: default
title: AgentSCOPE: Evaluating Contextual Privacy Across Agentic Workflows
---

# AgentSCOPE: Evaluating Contextual Privacy Across Agentic Workflows
**arXiv**：[2603.04902v1](https://arxiv.org/abs/2603.04902) · [PDF](https://arxiv.org/pdf/2603.04902.pdf)  
**作者**：Ivoline C. Ngong, Keerthiram Murugesan, Swanand Kadhe, Justin D. Weisz, Amit Dhurandhar, Karthikeyan Natesan Ramamurthy  

**一句话要点**：提出Privacy Flow Graph框架和AgentSCOPE基准，以评估智能体工作流中的上下文隐私风险。

**关键词**：智能体隐私评估, 上下文完整性, 隐私流图, 多工具场景基准, 中间信息流分析, 隐私违规追踪

## 3 点简述
- 核心问题：智能体系统在任务执行中产生多个中间信息流，现有隐私评估仅关注输入输出边界，忽略潜在隐私泄露点。
- 方法要点：基于Contextual Integrity理论，构建Privacy Flow Graph框架，将智能体执行分解为带参数的信息流序列，追踪隐私违规源头。
- 实验或效果：在AgentSCOPE基准上评估7个先进LLM，发现超80%场景存在隐私违规，多数源于工具响应阶段，输出级评估显著低估风险。

## 摘要（原文）

> Agentic systems are increasingly acting on users' behalf, accessing calendars, email, and personal files to complete everyday tasks. Privacy evaluation for these systems has focused on the input and output boundaries, but each task involves several intermediate information flows, from agent queries to tool responses, that are not currently evaluated. We argue that every boundary in an agentic pipeline is a site of potential privacy violation and must be assessed independently. To support this, we introduce the Privacy Flow Graph, a Contextual Integrity-grounded framework that decomposes agentic execution into a sequence of information flows, each annotated with the five CI parameters, and traces violations to their point of origin. We present AgentSCOPE, a benchmark of 62 multi-tool scenarios across eight regulatory domains with ground truth at every pipeline stage. Our evaluation across seven state-of-the-art LLMs show that privacy violations in the pipeline occur in over 80% of scenarios, even when final outputs appear clean (24%), with most violations arising at the tool-response stage where APIs return sensitive data indiscriminately. These results indicate that output-level evaluation alone substantially underestimates the privacy risk of agentic systems.

