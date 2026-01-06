---
layout: default
title: Robust Egocentric Visual Attention Prediction Through Language-guided Scene Context-aware Learning
---

# Robust Egocentric Visual Attention Prediction Through Language-guided Scene Context-aware Learning
**arXiv**：[2601.01818v1](https://arxiv.org/abs/2601.01818) · [PDF](https://arxiv.org/pdf/2601.01818.pdf)  
**作者**：Sungjune Park, Hongda Mao, Qingshuang Chen, Yong Man Ro, Yelin Kim  

**一句话要点**：提出语言引导的场景上下文感知学习框架，以增强动态第一人称视频中的视觉注意力预测鲁棒性。

**关键词**：第一人称视觉注意力预测, 语言引导学习, 场景上下文感知, 动态视频分析, 鲁棒性增强

## 3 点简述
- 核心问题：动态第一人称视频场景复杂且模糊，导致视觉注意力预测困难。
- 方法要点：设计基于语言场景描述的上下文感知器，生成视频表示，并通过聚焦目标区域和抑制无关区域的目标进行训练。
- 实验或效果：在Ego4D和AEA数据集上实现最先进性能，提升跨多样动态场景的鲁棒性。

## 摘要（原文）

> As the demand for analyzing egocentric videos grows, egocentric visual attention prediction, anticipating where a camera wearer will attend, has garnered increasing attention. However, it remains challenging due to the inherent complexity and ambiguity of dynamic egocentric scenes. Motivated by evidence that scene contextual information plays a crucial role in modulating human attention, in this paper, we present a language-guided scene context-aware learning framework for robust egocentric visual attention prediction. We first design a context perceiver which is guided to summarize the egocentric video based on a language-based scene description, generating context-aware video representations. We then introduce two training objectives that: 1) encourage the framework to focus on the target point-of-interest regions and 2) suppress distractions from irrelevant regions which are less likely to attract first-person attention. Extensive experiments on Ego4D and Aria Everyday Activities (AEA) datasets demonstrate the effectiveness of our approach, achieving state-of-the-art performance and enhanced robustness across diverse, dynamic egocentric scenarios.

