---
layout: default
title: SFCo-Nav: Efficient Zero-Shot Visual Language Navigation via Collaboration of Slow LLM and Fast Attributed Graph Alignment
---

# SFCo-Nav: Efficient Zero-Shot Visual Language Navigation via Collaboration of Slow LLM and Fast Attributed Graph Alignment
**arXiv**：[2603.01477v1](https://arxiv.org/abs/2603.01477) · [PDF](https://arxiv.org/pdf/2603.01477.pdf)  
**作者**：Chaoran Xiong, Litao Wei, Xinhao Hu, Kehui Ma, Ziyi Xia, Zixin Jiang, Zhen Sun, Ling Pei  

**一句话要点**：提出SFCo-Nav框架，通过慢快认知协作实现高效零样本视觉语言导航

**关键词**：视觉语言导航, 零样本学习, 慢快协作, 图对齐, 异步触发, 机器人导航

## 3 点简述
- 现有零样本视觉语言导航方法依赖每步VLM-LLM推理，导致高延迟和计算成本
- SFCo-Nav整合慢LLM规划器、快反应导航器和异步桥接模块，仅在必要时触发慢LLM
- 在R2R和REVERIE基准上，成功率达先进水平，轨迹令牌消耗减半，速度提升超3.5倍

## 摘要（原文）

> Recent advances in large vision-language models (VLMs) and large language models (LLMs) have enabled zero-shot approaches to visual language navigation (VLN), where an agent follows natural language instructions using only ego perception and reasoning. However, existing zero-shot methods typically construct a naive observation graph and perform per-step VLM-LLM inference on it, resulting in high latency and computation costs that limit real-time deployment. To address this, we present SFCo-Nav, an efficient zero-shot VLN framework inspired by the principle of slow-fast cognitive collaboration. SFCo-Nav integrates three key modules: 1) a slow LLM-based planner that produces a strategic chain of subgoals, each linked to an imagined object graph; 2) a fast reactive navigator for real-time object graph construction and subgoal execution; and 3) a lightweight asynchronous slow-fast bridge aligns advanced structured, attributed imagined and perceived graphs to estimate navigation confidence, triggering the slow LLM planner only when necessary. To the best of our knowledge, SFCo-Nav is the first slow-fast collaboration zero-shot VLN system supporting asynchronous LLM triggering according to the internal confidence. Evaluated on the public R2R and REVERIE benchmarks, SFCo-Nav matches or exceeds prior state-of-the-art zero-shot VLN success rates while cutting total token consumption per trajectory by over 50% and running more than 3.5 times faster. Finally, we demonstrate SFCo-Nav on a legged robot in a hotel suite, showcasing its efficiency and practicality in indoor environments.

