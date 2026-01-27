---
layout: default
title: MultiVis-Agent: A Multi-Agent Framework with Logic Rules for Reliable and Comprehensive Cross-Modal Data Visualization
---

# MultiVis-Agent: A Multi-Agent Framework with Logic Rules for Reliable and Comprehensive Cross-Modal Data Visualization
**arXiv**：[2601.18320v1](https://arxiv.org/abs/2601.18320) · [PDF](https://arxiv.org/pdf/2601.18320.pdf)  
**作者**：Jinwei Lu, Yuanfeng Song, Chen Zhang, Raymond Chi-Wing Wong  

**一句话要点**：提出MultiVis-Agent多智能体框架，结合逻辑规则解决跨模态可视化生成中的复杂性与可靠性问题。

**关键词**：多智能体框架, 逻辑规则增强, 跨模态可视化, 可靠性保证, 多场景生成, LLM推理指导

## 3 点简述
- 核心问题：现有系统存在单模态输入、一次性生成和僵化流程等局限，LLM方法易导致灾难性失败和无限循环。
- 方法要点：设计四层逻辑规则框架，提供数学可靠性保证，指导LLM推理而非替代，支持多模态多场景可视化任务。
- 实验或效果：在MultiVis-Bench基准上，可视化得分达75.63%，任务完成率99.58%，代码执行成功率94.56%，显著优于基线。

## 摘要（原文）

> Real-world visualization tasks involve complex, multi-modal requirements that extend beyond simple text-to-chart generation, requiring reference images, code examples, and iterative refinement. Current systems exhibit fundamental limitations: single-modality input, one-shot generation, and rigid workflows. While LLM-based approaches show potential for these complex requirements, they introduce reliability challenges including catastrophic failures and infinite loop susceptibility. To address this gap, we propose MultiVis-Agent, a logic rule-enhanced multi-agent framework for reliable multi-modal and multi-scenario visualization generation. Our approach introduces a four-layer logic rule framework that provides mathematical guarantees for system reliability while maintaining flexibility. Unlike traditional rule-based systems, our logic rules are mathematical constraints that guide LLM reasoning rather than replacing it. We formalize the MultiVis task spanning four scenarios from basic generation to iterative refinement, and develop MultiVis-Bench, a benchmark with over 1,000 cases for multi-modal visualization evaluation. Extensive experiments demonstrate that our approach achieves 75.63% visualization score on challenging tasks, significantly outperforming baselines (57.54-62.79%), with task completion rates of 99.58% and code execution success rates of 94.56% (vs. 74.48% and 65.10% without logic rules), successfully addressing both complexity and reliability challenges in automated visualization generation.

