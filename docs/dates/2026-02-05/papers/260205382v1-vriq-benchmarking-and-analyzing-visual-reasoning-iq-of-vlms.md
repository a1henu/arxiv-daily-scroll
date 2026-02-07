---
layout: default
title: VRIQ: Benchmarking and Analyzing Visual-Reasoning IQ of VLMs
---

# VRIQ: Benchmarking and Analyzing Visual-Reasoning IQ of VLMs
**arXiv**：[2602.05382v1](https://arxiv.org/abs/2602.05382) · [PDF](https://arxiv.org/pdf/2602.05382.pdf)  
**作者**：Tina Khezresmaeilzadeh, Jike Zhong, Konstantinos Psounis  

**一句话要点**：提出VRIQ基准以评估和分析视觉语言模型的视觉推理能力

**关键词**：视觉推理基准, 多模态系统, 感知诊断, 抽象推理, 视觉语言模型

## 3 点简述
- 核心问题：评估VLMs在非语言视觉推理任务中的可靠性
- 方法要点：设计抽象谜题和自然图像推理任务，并引入诊断探针分析感知与推理失败原因
- 实验或效果：发现VLMs在抽象任务上表现接近随机，感知限制是主要失败来源

## 摘要（原文）

> Recent progress in Vision Language Models (VLMs) has raised the question of whether they can reliably perform nonverbal reasoning. To this end, we introduce VRIQ (Visual Reasoning IQ), a novel benchmark designed to assess and analyze the visual reasoning ability of VLMs. We evaluate models on two sets of tasks: abstract puzzle-style and natural-image reasoning tasks. We find that on abstract puzzles, performance remains near random with an average accuracy of around 28%, while natural tasks yield better but still weak results with 45% accuracy. We also find that tool-augmented reasoning demonstrates only modest improvements. To uncover the source of this weakness, we introduce diagnostic probes targeting perception and reasoning. Our analysis demonstrates that around 56% of failures arise from perception alone, 43% from both perception and reasoning, and only a mere 1% from reasoning alone. This motivates us to design fine-grained diagnostic probe questions targeting specific perception categories (e.g., shape, count, position, 3D/depth), revealing that certain categories cause more failures than others. Our benchmark and analysis establish that current VLMs, even with visual reasoning tools, remain unreliable abstract reasoners, mostly due to perception limitations, and offer a principled basis for improving visual reasoning in multimodal systems.

