---
layout: default
title: Shape vs. Context: Examining Human--AI Gaps in Ambiguous Japanese Character Recognition
---

# Shape vs. Context: Examining Human--AI Gaps in Ambiguous Japanese Character Recognition
**arXiv**：[2602.23746v1](https://arxiv.org/abs/2602.23746) · [PDF](https://arxiv.org/pdf/2602.23746.pdf)  
**作者**：Daichi Haraguchi  

**一句话要点**：通过连续插值字符形状比较人类与视觉语言模型在模糊日语字符识别中的决策差异

**关键词**：视觉语言模型, 字符识别, 决策边界, 人类对齐, β-VAE, 模糊字符

## 3 点简述
- 核心问题：视觉语言模型在模糊字符识别中是否与人类决策模式一致，高识别性能不代表行为对齐
- 方法要点：使用β-VAE生成连续插值的日语字符形状，直接比较人类与模型在形状和上下文任务中的决策边界
- 实验或效果：发现人类与模型决策边界在形状任务中不同，上下文在某些条件下能改善对齐，揭示行为差异

## 摘要（原文）

> High text recognition performance does not guarantee that Vision-Language Models (VLMs) share human-like decision patterns when resolving ambiguity. We investigate this behavioral gap by directly comparing humans and VLMs using continuously interpolated Japanese character shapes generated via a $β$-VAE. We estimate decision boundaries in a single-character recognition (shape-only task) and evaluate whether VLM responses align with human judgments under shape in context (i.e., embedding an ambiguous character near the human decision boundary in word-level context). We find that human and VLM decision boundaries differ in the shape-only task, and that shape in context can improve human alignment in some conditions. These results highlight qualitative behavioral differences, offering foundational insights toward human--VLM alignment benchmarking.

