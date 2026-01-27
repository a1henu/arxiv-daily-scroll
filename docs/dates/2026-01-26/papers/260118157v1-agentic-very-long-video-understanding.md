---
layout: default
title: Agentic Very Long Video Understanding
---

# Agentic Very Long Video Understanding
**arXiv**：[2601.18157v1](https://arxiv.org/abs/2601.18157) · [PDF](https://arxiv.org/pdf/2601.18157.pdf)  
**作者**：Aniket Rege, Arka Sadhu, Yuliang Li, Kejie Li, Ramya Korlakai Vinayak, Yuning Chai, Yong Jae Lee, Hyo Jin Kim  

**一句话要点**：提出基于实体场景图的EGAgent框架，以解决全天候可穿戴设备中长时程视频理解问题。

**关键词**：长视频理解, 实体场景图, 代理框架, 跨模态推理, 可穿戴设备

## 3 点简述
- 核心问题：现有方法受限于上下文窗口，难以对长达数天或数周的连续视频进行组合式多跳推理。
- 方法要点：采用实体场景图表示人物、地点、物体及其时序关系，结合规划代理和混合搜索工具实现跨模态推理。
- 实验或效果：在EgoLifeQA和Video-MME（Long）数据集上取得领先或竞争性性能，验证了框架的有效性。

## 摘要（原文）

> The advent of always-on personal AI assistants, enabled by all-day wearable devices such as smart glasses, demands a new level of contextual understanding, one that goes beyond short, isolated events to encompass the continuous, longitudinal stream of egocentric video. Achieving this vision requires advances in long-horizon video understanding, where systems must interpret and recall visual and audio information spanning days or even weeks. Existing methods, including large language models and retrieval-augmented generation, are constrained by limited context windows and lack the ability to perform compositional, multi-hop reasoning over very long video streams. In this work, we address these challenges through EGAgent, an enhanced agentic framework centered on entity scene graphs, which represent people, places, objects, and their relationships over time. Our system equips a planning agent with tools for structured search and reasoning over these graphs, as well as hybrid visual and audio search capabilities, enabling detailed, cross-modal, and temporally coherent reasoning. Experiments on the EgoLifeQA and Video-MME (Long) datasets show that our method achieves state-of-the-art performance on EgoLifeQA (57.5%) and competitive performance on Video-MME (Long) (74.1%) for complex longitudinal video understanding tasks.

