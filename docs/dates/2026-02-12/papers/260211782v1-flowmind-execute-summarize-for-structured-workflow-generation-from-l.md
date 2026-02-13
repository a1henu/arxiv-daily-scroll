---
layout: default
title: FlowMind: Execute-Summarize for Structured Workflow Generation from LLM Reasoning
---

# FlowMind: Execute-Summarize for Structured Workflow Generation from LLM Reasoning
**arXiv**：[2602.11782v1](https://arxiv.org/abs/2602.11782) · [PDF](https://arxiv.org/pdf/2602.11782.pdf)  
**作者**：Yihao Liu, Ziyun Zhang, Zile He, Huaqian Cai  

**一句话要点**：提出Execute-Summarize框架以解决LLM推理到结构化工作流生成的准确性问题

**关键词**：结构化工作流生成, LLM推理, 工具使用, 执行轨迹, 解耦框架, 工作流准确性

## 3 点简述
- 核心问题：LLM推理难以准确转化为结构化工作流，执行与构建过程相互干扰导致不准确
- 方法要点：采用解耦的Execute-Summarize框架，先执行任务再独立从执行轨迹重构工作流
- 实验或效果：在FlowBench上实验显示，该方法优于现有方法，提升工作流准确性和鲁棒性

## 摘要（原文）

> LLMs can solve complex tasks through reasoning and tool use, but accurately translating these solutions into structured workflows remains challenging. We model workflows as sequences of tool use and reformulate the problem as designing a mechanism that can both solve tasks and reliably construct workflows. Prior approaches that build workflows during execution often suffer from inaccuracies due to interference between the two processes. We propose an Execute-Summarize(ES) framework that decouples task execution from workflow construction: the model first completes the task using available tools, then independently reconstructs a structured workflow from execution traces. This separation improves workflow accuracy and robustness. We introduce FlowBench and show through extensive experiments that our approach outperforms existing methods, providing a reliable paradigm for grounding free-form LLM reasoning into structured workflows.

