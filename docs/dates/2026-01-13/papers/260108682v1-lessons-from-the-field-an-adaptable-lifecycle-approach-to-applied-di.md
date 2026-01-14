---
layout: default
title: Lessons from the Field: An Adaptable Lifecycle Approach to Applied Dialogue Summarization
---

# Lessons from the Field: An Adaptable Lifecycle Approach to Applied Dialogue Summarization
**arXiv**：[2601.08682v1](https://arxiv.org/abs/2601.08682) · [PDF](https://arxiv.org/pdf/2601.08682.pdf)  
**作者**：Kushal Chawla, Chenyang Zhu, Pengshan Cai, Sangwoo Cho, Scott Novotney, Ayushman Singh, Jonah Lewis, Keasha Safewright, Alfy Samuel, Erin Babinsky, Shi-Xiong Zhang, Sambit Sahu  

**一句话要点**：提出可适应生命周期方法以解决工业中多轮对话摘要的复杂需求演化问题

**关键词**：多轮对话摘要, 代理架构, 生命周期方法, 工业应用, 需求演化, 供应商锁定

## 3 点简述
- 核心问题：工业多轮对话摘要需满足动态、多面需求，但现有研究依赖静态数据集，难以适应实际场景变化
- 方法要点：基于代理架构分解任务，实现组件优化，并分享评估、数据瓶颈和供应商锁定等实践洞察
- 实验或效果：未知，但提供行业案例研究，指导构建可靠、可适应摘要系统

## 摘要（原文）

> Summarization of multi-party dialogues is a critical capability in industry, enhancing knowledge transfer and operational effectiveness across many domains. However, automatically generating high-quality summaries is challenging, as the ideal summary must satisfy a set of complex, multi-faceted requirements. While summarization has received immense attention in research, prior work has primarily utilized static datasets and benchmarks, a condition rare in practical scenarios where requirements inevitably evolve. In this work, we present an industry case study on developing an agentic system to summarize multi-party interactions. We share practical insights spanning the full development lifecycle to guide practitioners in building reliable, adaptable summarization systems, as well as to inform future research, covering: 1) robust methods for evaluation despite evolving requirements and task subjectivity, 2) component-wise optimization enabled by the task decomposition inherent in an agentic architecture, 3) the impact of upstream data bottlenecks, and 4) the realities of vendor lock-in due to the poor transferability of LLM prompts.

