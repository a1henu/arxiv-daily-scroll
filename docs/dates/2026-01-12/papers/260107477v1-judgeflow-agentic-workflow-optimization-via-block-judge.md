---
layout: default
title: JudgeFlow: Agentic Workflow Optimization via Block Judge
---

# JudgeFlow: Agentic Workflow Optimization via Block Judge
**arXiv**：[2601.07477v1](https://arxiv.org/abs/2601.07477) · [PDF](https://arxiv.org/pdf/2601.07477.pdf)  
**作者**：Zihan Ma, Zhikai Zhao, Chuanbo Hua, Federico Berto, Jinkyoo Park  

**一句话要点**：提出JudgeFlow以优化LLM智能体工作流，通过模块化诊断与优化提升效率

**关键词**：智能体工作流优化, 模块化诊断, 责任评分, LLM优化器, 执行轨迹分析, 代码生成

## 3 点简述
- 核心问题：现有方法依赖粗粒度评估，缺乏细粒度信号指导优化，导致修改低效
- 方法要点：引入可配置逻辑块，设计Judge模块分析执行轨迹并分配责任分数，聚焦优化问题模块
- 实验或效果：在数学推理和代码生成基准测试中，JudgeFlow实现更优性能和样本效率

## 摘要（原文）

> Optimizing LLM-based agentic workflows is challenging for scaling AI capabilities. Current methods rely on coarse, end-to-end evaluation signals and lack fine-grained signals on where to refine, often resulting in inefficient or low-impact modifications. To address these limitations, we propose {\our{}}, an Evaluation-Judge-Optimization-Update pipeline. We incorporate reusable, configurable logic blocks into agentic workflows to capture fundamental forms of logic. On top of this abstraction, we design a dedicated Judge module that inspects execution traces -- particularly failed runs -- and assigns rank-based responsibility scores to problematic blocks. These fine-grained diagnostic signals are then leveraged by an LLM-based optimizer, which focuses modifications on the most problematic block in the workflow. Our approach improves sample efficiency, enhances interpretability through block-level diagnostics, and provides a scalable foundation for automating increasingly complex agentic workflows. We evaluate {\our{}} on mathematical reasoning and code generation benchmarks, where {\our{}} achieves superior performance and efficiency compared to existing methods. The source code is publicly available at https://github.com/ma-zihan/JudgeFlow.

