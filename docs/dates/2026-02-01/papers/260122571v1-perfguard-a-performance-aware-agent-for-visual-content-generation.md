---
layout: default
title: PerfGuard: A Performance-Aware Agent for Visual Content Generation
---

# PerfGuard: A Performance-Aware Agent for Visual Content Generation
**arXiv**：[2601.22571v1](https://arxiv.org/abs/2601.22571) · [PDF](https://arxiv.org/pdf/2601.22571.pdf)  
**作者**：Zhipeng Chen, Zhongrui Zhang, Chao Zhang, Yifan Xu, Lan Yang, Jun Liu, Ke Li, Yi-Zhe Song  

**一句话要点**：提出PerfGuard性能感知代理框架以解决视觉内容生成中工具性能不确定性导致的规划与执行问题

**关键词**：视觉内容生成, 性能感知代理, 工具选择优化, 任务规划, AIGC框架, 自适应更新

## 3 点简述
- 现有LLM代理框架依赖文本描述，忽略工具性能边界，导致规划不确定性
- PerfGuard引入性能感知选择建模、自适应偏好更新和能力对齐规划优化机制
- 实验显示在工具选择准确性、执行可靠性和用户意图对齐方面优于现有方法

## 摘要（原文）

> The advancement of Large Language Model (LLM)-powered agents has enabled automated task processing through reasoning and tool invocation capabilities. However, existing frameworks often operate under the idealized assumption that tool executions are invariably successful, relying solely on textual descriptions that fail to distinguish precise performance boundaries and cannot adapt to iterative tool updates. This gap introduces uncertainty in planning and execution, particularly in domains like visual content generation (AIGC), where nuanced tool performance significantly impacts outcomes. To address this, we propose PerfGuard, a performance-aware agent framework for visual content generation that systematically models tool performance boundaries and integrates them into task planning and scheduling. Our framework introduces three core mechanisms: (1) Performance-Aware Selection Modeling (PASM), which replaces generic tool descriptions with a multi-dimensional scoring system based on fine-grained performance evaluations; (2) Adaptive Preference Update (APU), which dynamically optimizes tool selection by comparing theoretical rankings with actual execution rankings; and (3) Capability-Aligned Planning Optimization (CAPO), which guides the planner to generate subtasks aligned with performance-aware strategies. Experimental comparisons against state-of-the-art methods demonstrate PerfGuard's advantages in tool selection accuracy, execution reliability, and alignment with user intent, validating its robustness and practical utility for complex AIGC tasks. The project code is available at https://github.com/FelixChan9527/PerfGuard.

