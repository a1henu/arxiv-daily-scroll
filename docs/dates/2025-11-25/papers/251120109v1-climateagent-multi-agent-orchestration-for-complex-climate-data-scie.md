---
layout: default
title: CLIMATEAGENT: Multi-Agent Orchestration for Complex Climate Data Science Workflows
---

# CLIMATEAGENT: Multi-Agent Orchestration for Complex Climate Data Science Workflows
**arXiv**：[2511.20109v1](https://arxiv.org/abs/2511.20109) · [PDF](https://arxiv.org/pdf/2511.20109.pdf)  
**作者**：Hyeonjae Kim, Chenyue Li, Wen Deng, Mengxi Jin, Wen Huang, Mengqian Lu, Binhang Yuan  

**一句话要点**：提出ClimateAgent多智能体框架以解决气候科学工作流自动化问题

**关键词**：多智能体系统, 气候数据科学, 工作流自动化, 动态API集成, 自校正执行, 基准评估

## 3 点简述
- 核心问题：通用LLM智能体和静态脚本在气候数据科学中缺乏上下文和灵活性
- 方法要点：通过多智能体编排分解任务，动态获取数据并生成代码与报告
- 实验或效果：在85个任务基准上实现100%完成率和8.32报告质量分，优于基线

## 摘要（原文）

> Climate science demands automated workflows to transform comprehensive questions into data-driven statements across massive, heterogeneous datasets. However, generic LLM agents and static scripting pipelines lack climate-specific context and flexibility, thus, perform poorly in practice. We present ClimateAgent, an autonomous multi-agent framework that orchestrates end-to-end climate data analytic workflows. ClimateAgent decomposes user questions into executable sub-tasks coordinated by an Orchestrate-Agent and a Plan-Agent; acquires data via specialized Data-Agents that dynamically introspect APIs to synthesize robust download scripts; and completes analysis and reporting with a Coding-Agent that generates Python code, visualizations, and a final report with a built-in self-correction loop. To enable systematic evaluation, we introduce Climate-Agent-Bench-85, a benchmark of 85 real-world tasks spanning atmospheric rivers, drought, extreme precipitation, heat waves, sea surface temperature, and tropical cyclones. On Climate-Agent-Bench-85, ClimateAgent achieves 100% task completion and a report quality score of 8.32, outperforming GitHub-Copilot (6.27) and a GPT-5 baseline (3.26). These results demonstrate that our multi-agent orchestration with dynamic API awareness and self-correcting execution substantially advances reliable, end-to-end automation for climate science analytic tasks.

