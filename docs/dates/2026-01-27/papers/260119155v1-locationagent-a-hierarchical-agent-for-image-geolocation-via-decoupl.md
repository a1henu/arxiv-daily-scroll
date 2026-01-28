---
layout: default
title: LocationAgent: A Hierarchical Agent for Image Geolocation via Decoupling Strategy and Evidence from Parametric Knowledge
---

# LocationAgent: A Hierarchical Agent for Image Geolocation via Decoupling Strategy and Evidence from Parametric Knowledge
**arXiv**：[2601.19155v1](https://arxiv.org/abs/2601.19155) · [PDF](https://arxiv.org/pdf/2601.19155.pdf)  
**作者**：Qiujun Li, Zijin Xiao, Xulin Wang, Zhidan Ma, Cheng Yang, Haifeng Li  

**一句话要点**：提出LocationAgent，通过解耦策略和外部工具验证解决图像地理定位中的幻觉和泛化问题。

**关键词**：图像地理定位, 分层推理, 外部工具验证, 零样本学习, 中国城市定位基准

## 3 点简述
- 核心问题：现有方法在开放世界或动态知识场景中易产生事实幻觉和泛化瓶颈。
- 方法要点：设计RER架构实现分层推理，并利用外部工具验证地理证据。
- 实验或效果：在零样本设置下显著优于现有方法至少30%，并引入CCL-Bench基准。

## 摘要（原文）

> Image geolocation aims to infer capture locations based on visual content. Fundamentally, this constitutes a reasoning process composed of \textit{hypothesis-verification cycles}, requiring models to possess both geospatial reasoning capabilities and the ability to verify evidence against geographic facts. Existing methods typically internalize location knowledge and reasoning patterns into static memory via supervised training or trajectory-based reinforcement fine-tuning. Consequently, these methods are prone to factual hallucinations and generalization bottlenecks in open-world settings or scenarios requiring dynamic knowledge. To address these challenges, we propose a Hierarchical Localization Agent, called LocationAgent. Our core philosophy is to retain hierarchical reasoning logic within the model while offloading the verification of geographic evidence to external tools. To implement hierarchical reasoning, we design the RER architecture (Reasoner-Executor-Recorder), which employs role separation and context compression to prevent the drifting problem in multi-step reasoning. For evidence verification, we construct a suite of clue exploration tools that provide diverse evidence to support location reasoning. Furthermore, to address data leakage and the scarcity of Chinese data in existing datasets, we introduce CCL-Bench (China City Location Bench), an image geolocation benchmark encompassing various scene granularities and difficulty levels. Extensive experiments demonstrate that LocationAgent significantly outperforms existing methods by at least 30\% in zero-shot settings.

