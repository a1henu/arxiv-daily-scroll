---
layout: default
title: Affective Flow Language Model for Emotional Support Conversation
---

# Affective Flow Language Model for Emotional Support Conversation
**arXiv**：[2602.08826v1](https://arxiv.org/abs/2602.08826) · [PDF](https://arxiv.org/pdf/2602.08826.pdf)  
**作者**：Chenghui Zou, Ning Wang, Tiesunlong Shen, Luwei Xiao, Chuan Ma, Xiangpeng Li, Rui Mao, Erik Cambria  

**一句话要点**：提出情感流语言模型以解决情感支持对话中多轮策略监督不足的问题。

**关键词**：情感支持对话, 语言模型对齐, 情感流建模, 策略学习, 多轮对话

## 3 点简述
- 现有方法依赖稀疏结果级信号，对中间策略决策监督有限。
- 通过建模连续情感流，引入细粒度监督以估计中间效用和学习策略过渡。
- 实验显示在多种情感场景下显著优于基线，包括超越GPT-4o和Claude-3.5。

## 摘要（原文）

> Large language models (LLMs) have been widely applied to emotional support conversation (ESC). However, complex multi-turn support remains challenging.This is because existing alignment schemes rely on sparse outcome-level signals, thus offering limited supervision for intermediate strategy decisions. To fill this gap, this paper proposes affective flow language model for emotional support conversation (AFlow), a framework that introduces fine-grained supervision on dialogue prefixes by modeling a continuous affective flow along multi-turn trajectories. AFlow can estimate intermediate utility over searched trajectories and learn preference-consistent strategy transitions. To improve strategy coherence and empathetic response quality, a subpath-level flow-balance objective is presented to propagate preference signals to intermediate states. Experiment results show consistent and significant improvements over competitive baselines in diverse emotional contexts. Remarkably, AFlow with a compact open-source backbone outperforms proprietary LMMs such as GPT-4o and Claude-3.5 on major ESC metrics. Our code is available at https://github.com/chzou25-lgtm/AffectiveFlow.

