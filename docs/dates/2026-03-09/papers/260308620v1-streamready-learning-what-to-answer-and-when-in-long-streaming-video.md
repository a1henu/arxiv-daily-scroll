---
layout: default
title: StreamReady: Learning What to Answer and When in Long Streaming Videos
---

# StreamReady: Learning What to Answer and When in Long Streaming Videos
**arXiv**：[2603.08620v1](https://arxiv.org/abs/2603.08620) · [PDF](https://arxiv.org/pdf/2603.08620.pdf)  
**作者**：Shehreen Azad, Vibhav Vineet, Yogesh Singh Rawat  

**一句话要点**：提出StreamReady框架，通过答案准备度评分解决流式视频中何时回答的问题。

**关键词**：流式视频理解, 时序推理, 答案准备度评分, 长视频基准, 实时问答

## 3 点简述
- 核心问题：流式视频理解需在证据出现时及时回答，过早或过晚均影响实用性。
- 方法要点：引入答案准备度评分，结合非对称惩罚，通过轻量机制决定回答时机。
- 实验或效果：在ProReady-QA基准上表现优异，并在多个长视频基准上超越先前方法。

## 摘要（原文）

> Streaming video understanding often involves time-sensitive scenarios where models need to answer exactly when the supporting visual evidence appears: answering before the evidence reflects speculation, answering after it has passed reduces real-time utility. To capture this behavior, we introduce a readiness-aware formulation of streaming video understanding with the Answer Readiness Score (ARS), a timing-aware objective with asymmetric early and late penalties. When combined with correctness, ARS defines an effective accuracy that measures not just whether a model is right, but whether it answers at the appropriate moment. Building on this formulation, we introduce StreamReady, a framework to unify temporal reasoning with on-time answering through a lightweight readiness mechanism that decides if sufficient evidence has been observed before responding. To evaluate this capability, we further introduce ProReady-QA, a benchmark with annotated answer evidence windows and proactive multi-turn questions across local and global contexts. StreamReady achieves superior performance on ProReady-QA, and consistently outperforms prior methods across eight additional streaming and offline long-video benchmarks, demonstrating robust and broadly generalizable video understanding capability.

