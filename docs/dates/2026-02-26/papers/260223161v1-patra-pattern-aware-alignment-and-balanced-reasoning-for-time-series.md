---
layout: default
title: PATRA: Pattern-Aware Alignment and Balanced Reasoning for Time Series Question Answering
---

# PATRA: Pattern-Aware Alignment and Balanced Reasoning for Time Series Question Answering
**arXiv**：[2602.23161v1](https://arxiv.org/abs/2602.23161) · [PDF](https://arxiv.org/pdf/2602.23161.pdf)  
**作者**：Junkai Lu, Peng Chen, Xingjian Wu, Yang Shu, Chenjuan Guo, Christian S. Jensen, Bin Yang  

**一句话要点**：提出PATRA模型，通过模式感知对齐和平衡奖励解决时间序列问答中的模式捕获与深度推理问题。

**关键词**：时间序列问答, 模式感知对齐, 平衡奖励, 跨模态理解, 深度推理

## 3 点简述
- 核心问题：现有LLM方法将时间序列视为文本或图像，忽略趋势和季节性模式，且简单任务主导学习，阻碍深度推理。
- 方法要点：引入模式感知机制提取趋势和季节性模式实现深度对齐，设计任务感知平衡奖励协调不同难度任务学习。
- 实验或效果：在多样化时间序列问答任务上超越强基线，展示卓越的跨模态理解和推理能力。

## 摘要（原文）

> Time series reasoning demands both the perception of complex dynamics and logical depth. However, existing LLM-based approaches exhibit two limitations: they often treat time series merely as text or images, failing to capture the patterns like trends and seasonalities needed to answer specific questions; and when trained on a mix of simple and complex tasks, simpler objectives often dominate the learning process, hindering the development of deep reasoning capabilities. To address these limitations, we propose the Pattern-Aware Alignment and Balanced Reasoning model (PATRA), introducing a pattern-aware mechanism that extracts trend and seasonality patterns from time series to achieve deep alignment. Furthermore, we design a task-aware balanced reward to harmonize learning across tasks of varying difficulty, incentivizing the generation of coherent Chains of Thought. Extensive experiments show that PATRA outperforms strong baselines across diverse Time Series Question Answering (TSQA) tasks, demonstrating superior cross-modal understanding and reasoning capability.

