---
layout: default
title: Bounded State in an Infinite Horizon: Proactive Hierarchical Memory for Ad-Hoc Recall over Streaming Dialogues
---

# Bounded State in an Infinite Horizon: Proactive Hierarchical Memory for Ad-Hoc Recall over Streaming Dialogues
**arXiv**：[2603.04885v1](https://arxiv.org/abs/2603.04885) · [PDF](https://arxiv.org/pdf/2603.04885.pdf)  
**作者**：Bingbing Wang, Jing Li, Ruifeng Xu  

**一句话要点**：提出ProStream框架以解决无限流对话中的有界状态记忆与即时召回问题

**关键词**：流式对话, 记忆机制, 即时召回, 分层蒸馏, 自适应优化, 基准评估

## 3 点简述
- 核心问题：现有记忆机制在无限流对话中无法支持即时召回，面临保真度与效率的权衡
- 方法要点：采用主动分层记忆框架，通过多粒度蒸馏和自适应时空优化实现有界知识状态
- 实验或效果：在STEM-Bench基准上，ProStream在准确性和效率上均优于基线方法

## 摘要（原文）

> Real-world dialogue usually unfolds as an infinite stream. It thus requires bounded-state memory mechanisms to operate within an infinite horizon. However, existing read-then-think memory is fundamentally misaligned with this setting, as it cannot support ad-hoc memory recall while streams unfold. To explore this challenge, we introduce \textbf{STEM-Bench}, the first benchmark for \textbf{ST}reaming \textbf{E}valuation of \textbf{M}emory. It comprises over 14K QA pairs in dialogue streams that assess perception fidelity, temporal reasoning, and global awareness under infinite-horizon constraints. The preliminary analysis on STEM-Bench indicates a critical \textit{fidelity-efficiency dilemma}: retrieval-based methods use fragment context, while full-context models incur unbounded latency. To resolve this, we propose \textbf{ProStream}, a proactive hierarchical memory framework for streaming dialogues. It enables ad-hoc memory recall on demand by reasoning over continuous streams with multi-granular distillation. Moreover, it employs Adaptive Spatiotemporal Optimization to dynamically optimize retention based on expected utility. It enables a bounded knowledge state for lower inference latency without sacrificing reasoning fidelity. Experiments show that ProStream outperforms baselines in both accuracy and efficiency.

