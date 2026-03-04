---
layout: default
title: SaFeR-ToolKit: Structured Reasoning via Virtual Tool Calling for Multimodal Safety
---

# SaFeR-ToolKit: Structured Reasoning via Virtual Tool Calling for Multimodal Safety
**arXiv**：[2603.02635v1](https://arxiv.org/abs/2603.02635) · [PDF](https://arxiv.org/pdf/2603.02635.pdf)  
**作者**：Zixuan Xu, Tiancheng He, Huahui Yi, Kun Wang, Xi Chen, Gongli Xi, Qiankun Li, Kang Li, Yang Liu, Zhigang Zeng  

**一句话要点**：提出SaFeR-ToolKit，通过虚拟工具调用结构化推理以提升多模态安全性

**关键词**：多模态安全, 结构化推理, 虚拟工具调用, 课程学习, 视觉语言模型, 对齐训练

## 3 点简述
- 核心问题：视觉语言模型易受多模态越狱和过度拒绝影响，因安全依赖视觉证据和用户意图，而现有对齐方法仅监督最终响应。
- 方法要点：将安全决策形式化为可检查协议，包括规划器定义角色、工具集和约束图，响应器在最终答案前输出类型化键值工具轨迹，并通过三阶段课程训练单策略确保协议遵循。
- 实验效果：在Qwen2.5-VL模型上显著提升安全、帮助性和推理严谨性分数，同时保持通用能力，代码已开源。

## 摘要（原文）

> Vision-language models remain susceptible to multimodal jailbreaks and over-refusal because safety hinges on both visual evidence and user intent, while many alignment pipelines supervise only the final response. To address this, we present SaFeR-ToolKit, which formalizes safety decision-making as a checkable protocol. Concretely, a planner specifies a persona, a Perception $\to$ Reasoning $\to$ Decision tool set, and a constrained transition graph, while a responder outputs a typed key-value tool trace before the final answer. To make the protocol reliably followed in practice, we train a single policy with a three-stage curriculum (SFT $\to$ DPO $\to$ GRPO), where GRPO directly supervises tool usage beyond answer-level feedback. Our contributions are two-fold: I. Dataset. The first tool-based safety reasoning dataset, comprising 31,654 examples (SFT 6k, DPO 18.6k, GRPO 6k) plus 1k held-out evaluation. II. Experiments. On Qwen2.5-VL, SaFeR-ToolKit significantly improves Safety/Helpfulness/Reasoning Rigor on 3B (29.39/45.04/4.98 $\to$ 84.40/71.13/78.87) and 7B (53.21/52.92/19.26 $\to$ 86.34/80.79/85.34), while preserving general capabilities (3B: 58.67 $\to$ 59.21; 7B: 66.39 $\to$ 66.81). Codes are available at https://github.com/Duebassx/SaFeR_ToolKit.

