---
layout: default
title: Improving Zero-shot ADL Recognition with Large Language Models through Event-based Context and Confidence
---

# Improving Zero-shot ADL Recognition with Large Language Models through Event-based Context and Confidence
**arXiv**：[2601.08241v1](https://arxiv.org/abs/2601.08241) · [PDF](https://arxiv.org/pdf/2601.08241.pdf)  
**作者**：Michele Fiori, Gabriele Civitarese, Marco Colussi, Claudio Bettini  

**一句话要点**：提出基于事件分割和置信度估计的方法，以改进零样本ADL识别在智能家居中的应用。

**关键词**：零样本学习, 大型语言模型, 活动识别, 智能家居, 事件分割, 置信度估计

## 3 点简述
- 核心问题：现有零样本方法依赖时间分割，与LLM上下文推理能力不匹配，且缺乏置信度估计。
- 方法要点：采用事件分割替代时间分割，并引入新方法估计预测置信度。
- 实验或效果：事件分割在复杂数据集上优于时间分割方法，并超越监督方法，置信度有效区分预测正误。

## 摘要（原文）

> Unobtrusive sensor-based recognition of Activities of Daily Living (ADLs) in smart homes by processing data collected from IoT sensing devices supports applications such as healthcare, safety, and energy management. Recent zero-shot methods based on Large Language Models (LLMs) have the advantage of removing the reliance on labeled ADL sensor data. However, existing approaches rely on time-based segmentation, which is poorly aligned with the contextual reasoning capabilities of LLMs. Moreover, existing approaches lack methods for estimating prediction confidence. This paper proposes to improve zero-shot ADL recognition with event-based segmentation and a novel method for estimating prediction confidence. Our experimental evaluation shows that event-based segmentation consistently outperforms time-based LLM approaches on complex, realistic datasets and surpasses supervised data-driven methods, even with relatively small LLMs (e.g., Gemma 3 27B). The proposed confidence measure effectively distinguishes correct from incorrect predictions.

