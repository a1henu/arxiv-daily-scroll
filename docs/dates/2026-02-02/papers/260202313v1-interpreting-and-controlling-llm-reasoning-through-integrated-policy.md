---
layout: default
title: Interpreting and Controlling LLM Reasoning through Integrated Policy Gradient
---

# Interpreting and Controlling LLM Reasoning through Integrated Policy Gradient
**arXiv**：[2602.02313v1](https://arxiv.org/abs/2602.02313) · [PDF](https://arxiv.org/pdf/2602.02313.pdf)  
**作者**：Changming Li, Kaixing Zhang, Haoyun Xu, Yingdong Shi, Zheng Zhang, Kaitao Song, Kan Ren  

**一句话要点**：提出集成策略梯度以定位和调控大语言模型推理机制

**关键词**：大语言模型, 推理机制, 策略梯度, 模型可解释性, 行为调控

## 3 点简述
- 问题：现有方法难以精确定位复杂推理机制或捕捉内部到输出的序列影响
- 方法：基于结果导向和序列影响感知，通过反向传播复合结果信号来归因推理行为
- 效果：实证评估显示更精确的定位，并能可靠调控多种推理模型的推理能力

## 摘要（原文）

> Large language models (LLMs) demonstrate strong reasoning abilities in solving complex real-world problems. Yet, the internal mechanisms driving these complex reasoning behaviors remain opaque. Existing interpretability approaches targeting reasoning either identify components (e.g., neurons) correlated with special textual patterns, or rely on human-annotated contrastive pairs to derive control vectors. Consequently, current methods struggle to precisely localize complex reasoning mechanisms or capture sequential influence from model internal workings to the reasoning outputs. In this paper, built on outcome-oriented and sequential-influence-aware principles, we focus on identifying components that have sequential contribution to reasoning behavior where outcomes are cumulated by long-range effects. We propose Integrated Policy Gradient (IPG), a novel framework that attributes reasoning behaviors to model's inner components by propagating compound outcome-based signals such as post reasoning accuracy backward through model inference trajectories. Empirical evaluations demonstrate that our approach achieves more precise localization and enables reliable modulation of reasoning behaviors (e.g., reasoning capability, reasoning strength) across diverse reasoning models.

