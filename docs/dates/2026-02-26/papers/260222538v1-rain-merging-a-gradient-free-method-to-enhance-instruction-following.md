---
layout: default
title: RAIN-Merging: A Gradient-Free Method to Enhance Instruction Following in Large Reasoning Models with Preserved Thinking Format
---

# RAIN-Merging: A Gradient-Free Method to Enhance Instruction Following in Large Reasoning Models with Preserved Thinking Format
**arXiv**：[2602.22538v1](https://arxiv.org/abs/2602.22538) · [PDF](https://arxiv.org/pdf/2602.22538.pdf)  
**作者**：Zhehao Huang, Yuhang Liu, Baijiong Lin, Yixin Lou, Zhengbao He, Hanling Tian, Tao Li, Xiaolin Huang  

**一句话要点**：提出RAIN-Merging方法，通过梯度自由合并增强大型推理模型的指令遵循能力，同时保持推理格式。

**关键词**：大型推理模型, 指令遵循, 模型合并, 零空间投影, 梯度自由优化

## 3 点简述
- 核心问题：大型推理模型在推理链上表现优异，但常无法忠实遵循输出格式、约束或特定指令。
- 方法要点：利用任务向量分析，通过零空间投影和指令注意力缩放，实现轻量级合并，减少干扰。
- 实验或效果：在四个指令遵循基准和九个推理与通用能力基准上，显著提升指令遵循性，同时维持推理质量。

## 摘要（原文）

> Large reasoning models (LRMs) excel at a long chain of reasoning but often fail to faithfully follow instructions regarding output format, constraints, or specific requirements. We investigate whether this gap can be closed by integrating an instruction-tuned model (ITM) into an LRM. Analyzing their differences in parameter space, namely task vectors, we find that their principal subspaces are nearly orthogonal across key modules, suggesting a lightweight merging with minimal interference. However, we also demonstrate that naive merges are fragile because they overlook the output format mismatch between LRMs (with explicit thinking and response segments) and ITMs (answers-only). We introduce RAIN-Merging (Reasoning-Aware Instruction-attention guided Null-space projection Merging), a gradient-free method that integrates instruction following while preserving thinking format and reasoning performance. First, with a small reasoning calibration set, we project the ITM task vector onto the null space of forward features at thinking special tokens, which preserves the LRM's structured reasoning mechanisms. Second, using a small instruction calibration set, we estimate instruction attention to derive module-specific scaling that amplifies instruction-relevant components and suppresses leakage. Across four instruction-following benchmarks and nine reasoning & general capability benchmarks, RAIN-Merging substantially improves instruction adherence while maintaining reasoning quality. The gains are consistent across model scales and architectures, translating to improved performance in agent settings.

