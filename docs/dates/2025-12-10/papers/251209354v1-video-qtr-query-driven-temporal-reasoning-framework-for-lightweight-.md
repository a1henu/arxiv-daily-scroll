---
layout: default
title: Video-QTR: Query-Driven Temporal Reasoning Framework for Lightweight Video Understanding
---

# Video-QTR: Query-Driven Temporal Reasoning Framework for Lightweight Video Understanding
**arXiv**：[2512.09354v1](https://arxiv.org/abs/2512.09354) · [PDF](https://arxiv.org/pdf/2512.09354.pdf)  
**作者**：Xinkui Zhao, Zuxin Wang, Yifan Zhang, Guanjie Cheng, Yueshen Xu, Shuiguang Deng, Chang Liu, Naibo Wang, Jianwei Yin  

**一句话要点**：提出Video-QTR框架，通过查询驱动的时间推理解决长视频理解的计算效率问题。

**关键词**：长视频理解, 查询驱动推理, 轻量级框架, 时间推理, 计算效率

## 3 点简述
- 核心问题：传统方法在长视频理解中因密集帧编码导致高计算和内存开销，限制实际应用。
- 方法要点：采用查询驱动的时间推理，动态分配感知资源，形成推理与感知的自适应反馈循环。
- 实验或效果：在多个基准测试中达到先进性能，同时减少输入帧消耗高达73%。

## 摘要（原文）

> The rapid development of multimodal large-language models (MLLMs) has significantly expanded the scope of visual language reasoning, enabling unified systems to interpret and describe complex visual content. However, applying these models to long-video understanding remains computationally intensive. Dense frame encoding generates excessive visual tokens, leading to high memory consumption, redundant computation, and limited scalability in real-world applications. This inefficiency highlights a key limitation of the traditional process-then-reason paradigm, which analyzes visual streams exhaustively before semantic reasoning. To address this challenge, we introduce Video-QTR (Query-Driven Temporal Reasoning), a lightweight framework that redefines video comprehension as a query-guided reasoning process. Instead of encoding every frame, Video-QTR dynamically allocates perceptual resources based on the semantic intent of the query, creating an adaptive feedback loop between reasoning and perception. Extensive experiments across five benchmarks: MSVD-QA, Activity Net-QA, Movie Chat, and Video MME demonstrate that Video-QTR achieves state-of-the-art performance while reducing input frame consumption by up to 73%. These results confirm that query-driven temporal reasoning provides an efficient and scalable solution for video understanding.

