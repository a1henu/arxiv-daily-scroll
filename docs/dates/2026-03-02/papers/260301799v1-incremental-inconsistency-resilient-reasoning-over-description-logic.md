---
layout: default
title: Incremental, inconsistency-resilient reasoning over Description Logic Abox streams
---

# Incremental, inconsistency-resilient reasoning over Description Logic Abox streams
**arXiv**：[2603.01799v1](https://arxiv.org/abs/2603.01799) · [PDF](https://arxiv.org/pdf/2603.01799.pdf)  
**作者**：Cas Proost, Pieter Bonte  

**一句话要点**：提出增量推理与不一致修复语义，以处理描述逻辑ABox流中的高速度和噪声挑战。

**关键词**：流推理, 描述逻辑ABox, 增量物化, 不一致修复, 滑动窗口, OWL2 RL

## 3 点简述
- 核心问题：数据流的高速度、实时推理需求及噪声与易变性。
- 方法要点：基于滑动窗口的增量物化计算和偏好修复语义处理不一致。
- 实验或效果：详细了OWL2 RL下的半朴素算法，支持一致和不一致场景。

## 摘要（原文）

> More and more, data is being produced in a streaming fashion. This has led to increased interest into how actionable insights can be extracted in real time from data streams through Stream Reasoning. Reasoning over data streams raises multiple challenges, notably the high velocity of data, the real time requirement of the reasoning, and the noisy and volatile nature of streams. This paper proposes novel semantics for incremental reasoning over streams of Description Logic ABoxes, in order to tackle these challenges. To address the first two challenges, our semantics for reasoning over sliding windows on streams allow for incrementally computing the materialization of the window based on the materialization of the previous window. Furthermore, to deal with the volatile nature of streams, we present novel semantics for inconsistency repair on such windows, based on preferred repair semantics. We then detail our proposed semi-naive algorithms for incremental materialization maintenance in the case of OWL2 RL, both in the presence of inconsistencies and without.

