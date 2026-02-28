---
layout: default
title: RAIN-Merging: A Gradient-Free Method to Enhance Instruction Following in Large Reasoning Models with Preserved Thinking Format
---

# RAIN-Merging: A Gradient-Free Method to Enhance Instruction Following in Large Reasoning Models with Preserved Thinking Format
**arXiv**：[2602.22538v1](https://arxiv.org/abs/2602.22538) · [PDF](https://arxiv.org/pdf/2602.22538.pdf)  
**作者**：Zhehao Huang, Yuhang Liu, Baijiong Lin, Yixin Lou, Zhengbao He, Hanling Tian, Tao Li, Xiaolin Huang  

**一句话要点**：提出RAIN-Merging以增强大型推理模型的指令遵循能力，同时保持推理格式与性能。

**关键词**：大型推理模型, 指令遵循, 模型合并, 零梯度方法, 任务向量, 推理性能

## 3 点简述
- 核心问题：大型推理模型在指令遵循上存在不足，如输出格式不匹配。
- 方法要点：通过零梯度方法，在空空间投影任务向量并缩放指令相关组件。
- 实验或效果：在多个基准测试中显著提升指令遵循，同时维持推理质量。

## 摘要（原文）

> Large reasoning models (LRMs) excel at a long chain of reasoning but often fail to faithfully follow instructions regarding output format, constraints, or specific requirements. We investigate whether this gap can be closed by integrating an instruction-tuned model (ITM) into an LRM. Analyzing their differences in parameter space, namely task vectors, we find that their principal subspaces are nearly orthogonal across key modules, suggesting a lightweight merging with minimal interference. However, we also demonstrate that naive merges are fragile because they overlook the output format mismatch between LRMs (with explicit thinking and response segments) and ITMs (answers-only). We introduce RAIN-Merging (Reasoning-Aware Instruction-attention guided Null-space projection Merging), a gradient-free method that integrates instruction following while preserving thinking format and reasoning performance. First, with a small reasoning calibration set, we project the ITM task vector onto the null space of forward features at thinking special tokens, which preserves the LRM's structured reasoning mechanisms. Second, using a small instruction calibration set, we estimate instruction attention to derive module-specific scaling that amplifies instruction-relevant components and suppresses leakage. Across four instruction-following benchmarks and nine reasoning & general capability benchmarks, RAIN-Merging substantially improves instruction adherence while maintaining reasoning quality. The gains are consistent across model scales and architectures, translating to improved performance in agent settings.

