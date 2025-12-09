---
layout: default
title: DART: Leveraging Multi-Agent Disagreement for Tool Recruitment in Multimodal Reasoning
---

# DART: Leveraging Multi-Agent Disagreement for Tool Recruitment in Multimodal Reasoning
**arXiv**：[2512.07132v1](https://arxiv.org/abs/2512.07132) · [PDF](https://arxiv.org/pdf/2512.07132.pdf)  
**作者**：Nithin Sivakumaran, Justin Chih-Yao Chen, David Wan, Yue Zhang, Jaehong Yoon, Elias Stengel-Eskin, Mohit Bansal  

**一句话要点**：提出DART多智能体框架，利用视觉智能体间的分歧来招募工具以增强多模态推理

**关键词**：多智能体辩论, 视觉工具调用, 多模态推理, 分歧解决, 专家知识增强

## 3 点简述
- 核心问题：多模态推理中，如何有效选择和调用视觉工具以解决智能体间的分歧
- 方法要点：通过多智能体辩论识别分歧，引入工具提供新信息和一致性评分，聚合器选择最佳答案
- 实验或效果：在四个基准测试中优于基线，如A-OKVQA和MMMU分别提升3.4%和2.4%，并适应新工具

## 摘要（原文）

> Specialized visual tools can augment large language models or vision language models with expert knowledge (e.g., grounding, spatial reasoning, medical knowledge, etc.), but knowing which tools to call (and when to call them) can be challenging. We introduce DART, a multi-agent framework that uses disagreements between multiple debating visual agents to identify useful visual tools (e.g., object detection, OCR, spatial reasoning, etc.) that can resolve inter-agent disagreement. These tools allow for fruitful multi-agent discussion by introducing new information, and by providing tool-aligned agreement scores that highlight agents in agreement with expert tools, thereby facilitating discussion. We utilize an aggregator agent to select the best answer by providing the agent outputs and tool information. We test DART on four diverse benchmarks and show that our approach improves over multi-agent debate as well as over single agent tool-calling frameworks, beating the next-strongest baseline (multi-agent debate with a judge model) by 3.4% and 2.4% on A-OKVQA and MMMU respectively. We also find that DART adapts well to new tools in applied domains, with a 1.3% improvement on the M3D medical dataset over other strong tool-calling, single agent, and multi-agent baselines. Additionally, we measure text overlap across rounds to highlight the rich discussion in DART compared to existing multi-agent methods. Finally, we study the tool call distribution, finding that diverse tools are reliably used to help resolve disagreement.

