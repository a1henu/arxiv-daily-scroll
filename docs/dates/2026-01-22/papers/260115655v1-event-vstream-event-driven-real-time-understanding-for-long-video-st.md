---
layout: default
title: Event-VStream: Event-Driven Real-Time Understanding for Long Video Streams
---

# Event-VStream: Event-Driven Real-Time Understanding for Long Video Streams
**arXiv**：[2601.15655v1](https://arxiv.org/abs/2601.15655) · [PDF](https://arxiv.org/pdf/2601.15655.pdf)  
**作者**：Zhenghui Guo, Yuanbin Man, Junyuan Sheng, Bowen Lin, Ahmed Ahmed, Bo Jiang, Boyuan Zhang, Miao Yin, Sian Jin, Omprakash Gnawal, Chengming Zhang  

**一句话要点**：提出Event-VStream框架，通过事件驱动实现长视频流的实时理解

**关键词**：事件驱动视频理解, 长视频流处理, 实时多模态模型, 语义事件检测, 持久记忆库

## 3 点简述
- 核心问题：多模态大语言模型处理长视频流时存在冗余帧处理和上下文遗忘问题
- 方法要点：将连续视频表示为离散语义事件序列，基于运动、语义和预测线索触发语言生成
- 实验或效果：在OVOBench-Realtime上提升10.4分，在Ego4D上保持约70% GPT-5胜率

## 摘要（原文）

> Real-time understanding of long video streams remains challenging for multimodal large language models (VLMs) due to redundant frame processing and rapid forgetting of past context. Existing streaming systems rely on fixed-interval decoding or cache pruning, which either produce repetitive outputs or discard crucial temporal information. We introduce Event-VStream, an event-aware framework that represents continuous video as a sequence of discrete, semantically coherent events. Our system detects meaningful state transitions by integrating motion, semantic, and predictive cues, and triggers language generation only at those boundaries. Each event embedding is consolidated into a persistent memory bank, enabling long-horizon reasoning while maintaining low latency. Across OVOBench-Realtime, and long-form Ego4D evaluations, Event-VStream achieves competitive performance. It improves over a VideoLLM-Online-8B baseline by +10.4 points on OVOBench-Realtime, achieves performance close to Flash-VStream-7B despite using only a general-purpose LLaMA-3-8B text backbone, and maintains around 70% GPT-5 win rate on 2-hour Ego4D streams.

