---
layout: default
title: EventMemAgent: Hierarchical Event-Centric Memory for Online Video Understanding with Adaptive Tool Use
---

# EventMemAgent: Hierarchical Event-Centric Memory for Online Video Understanding with Adaptive Tool Use
**arXiv**：[2602.15329v1](https://arxiv.org/abs/2602.15329) · [PDF](https://arxiv.org/pdf/2602.15329.pdf)  
**作者**：Siwei Wen, Zhangcheng Wang, Xingjian Zhang, Lei Huang, Wenjun Wu  

**一句话要点**：提出EventMemAgent框架，通过分层事件记忆和自适应工具使用解决在线视频理解中的长范围推理问题。

**关键词**：在线视频理解, 分层记忆, 事件检测, 自适应工具使用, Agentic强化学习

## 3 点简述
- 核心问题：在线视频理解中，无限流媒体输入与多模态大语言模型有限上下文窗口的冲突。
- 方法要点：采用分层记忆模块，包括短时记忆检测事件边界和长时记忆结构化归档，结合多粒度感知工具包和Agentic RL。
- 实验或效果：在在线视频基准测试中取得竞争性结果，代码将开源。

## 摘要（原文）

> Online video understanding requires models to perform continuous perception and long-range reasoning within potentially infinite visual streams. Its fundamental challenge lies in the conflict between the unbounded nature of streaming media input and the limited context window of Multimodal Large Language Models (MLLMs). Current methods primarily rely on passive processing, which often face a trade-off between maintaining long-range context and capturing the fine-grained details necessary for complex tasks. To address this, we introduce EventMemAgent, an active online video agent framework based on a hierarchical memory module. Our framework employs a dual-layer strategy for online videos: short-term memory detects event boundaries and utilizes event-granular reservoir sampling to process streaming video frames within a fixed-length buffer dynamically; long-term memory structuredly archives past observations on an event-by-event basis. Furthermore, we integrate a multi-granular perception toolkit for active, iterative evidence capture and employ Agentic Reinforcement Learning (Agentic RL) to end-to-end internalize reasoning and tool-use strategies into the agent's intrinsic capabilities. Experiments show that EventMemAgent achieves competitive results on online video benchmarks. The code will be released here: https://github.com/lingcco/EventMemAgent.

