---
layout: default
title: RIVER: A Real-Time Interaction Benchmark for Video LLMs
---

# RIVER: A Real-Time Interaction Benchmark for Video LLMs
**arXiv**：[2603.03985v1](https://arxiv.org/abs/2603.03985) · [PDF](https://arxiv.org/pdf/2603.03985.pdf)  
**作者**：Yansong Shi, Qingsong Zhao, Tianxiang Jiang, Xiangyu Zeng, Yi Wang, Limin Wang  

**一句话要点**：提出RIVER Bench基准以评估在线视频理解，解决多模态大模型实时交互不足问题。

**关键词**：实时视频交互, 多模态大语言模型, 在线视频理解, 交互式对话, 基准测试

## 3 点简述
- 核心问题：现有多模态大模型多为离线处理，缺乏实时视频交互能力，阻碍实际应用。
- 方法要点：设计包含回顾记忆、实时感知和前瞻预测任务的框架，模拟交互式对话而非整视频响应。
- 实验或效果：评估显示离线模型在实时处理中表现不佳，提出通用改进方法以增强模型实时交互灵活性。

## 摘要（原文）

> The rapid advancement of multimodal large language models has demonstrated impressive capabilities, yet nearly all operate in an offline paradigm, hindering real-time interactivity. Addressing this gap, we introduce the Real-tIme Video intERaction Bench (RIVER Bench), designed for evaluating online video comprehension. RIVER Bench introduces a novel framework comprising Retrospective Memory, Live-Perception, and Proactive Anticipation tasks, closely mimicking interactive dialogues rather than responding to entire videos at once. We conducted detailed annotations using videos from diverse sources and varying lengths, and precisely defined the real-time interactive format. Evaluations across various model categories reveal that while offline models perform well in single question-answering tasks, they struggle with real-time processing. Addressing the limitations of existing models in online video interaction, especially their deficiencies in long-term memory and future perception, we proposed a general improvement method that enables models to interact with users more flexibly in real time. We believe this work will significantly advance the development of real-time interactive video understanding models and inspire future research in this emerging field. Datasets and code are publicly available at https://github.com/OpenGVLab/RIVER.

