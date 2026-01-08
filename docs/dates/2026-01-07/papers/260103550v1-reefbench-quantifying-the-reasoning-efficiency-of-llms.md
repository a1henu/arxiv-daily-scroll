---
layout: default
title: ReEfBench: Quantifying the Reasoning Efficiency of LLMs
---

# ReEfBench: Quantifying the Reasoning Efficiency of LLMs
**arXiv**：[2601.03550v1](https://arxiv.org/abs/2601.03550) · [PDF](https://arxiv.org/pdf/2601.03550.pdf)  
**作者**：Zhizhang Fu, Yuancheng Gu, Chenkai Hu, Hanmeng Liu, Yue Zhang  

**一句话要点**：提出ReEfBench框架以量化大语言模型的推理效率，解决现有评估方法混淆性能来源的问题。

**关键词**：推理效率评估, 神经符号框架, 思维链分析, 训练策略影响, 模型规模效应, 蒸馏限制

## 3 点简述
- 核心问题：现有思维链评估方法难以区分性能提升源于真实推理还是冗长生成。
- 方法要点：设计神经符号框架，非侵入式地评估推理过程，识别行为原型和失败模式。
- 实验或效果：分析推理模式、训练策略和模型规模的影响，揭示扩展生成非深度推理必需，并指出训练和蒸馏的约束。

## 摘要（原文）

> Test-time scaling has enabled Large Language Models (LLMs) to tackle complex reasoning, yet the limitations of current Chain-of-Thought (CoT) evaluation obscures whether performance gains stem from genuine reasoning or mere verbosity. To address this, (1) we propose a novel neuro-symbolic framework for the non-intrusive, comprehensive process-centric evaluation of reasoning. (2) Through this lens, we identify four distinct behavioral prototypes and diagnose the failure modes. (3) We examine the impact of inference mode, training strategy, and model scale. Our analysis reveals that extended token generation is not a prerequisite for deep reasoning. Furthermore, we reveal critical constraints: mixing long and short CoT data in training risks in premature saturation and collapse, while distillation into smaller models captures behavioral length but fails to replicate logical efficacy due to intrinsic capacity limits.

