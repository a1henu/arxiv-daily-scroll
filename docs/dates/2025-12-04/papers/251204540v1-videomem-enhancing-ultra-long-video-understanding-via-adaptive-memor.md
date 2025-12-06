---
layout: default
title: VideoMem: Enhancing Ultra-Long Video Understanding via Adaptive Memory Management
---

# VideoMem: Enhancing Ultra-Long Video Understanding via Adaptive Memory Management
**arXiv**：[2512.04540v1](https://arxiv.org/abs/2512.04540) · [PDF](https://arxiv.org/pdf/2512.04540.pdf)  
**作者**：Hongbo Jin, Qingyuan Wang, Wenhao Zhang, Yang Liu, Sijie Cheng  

**一句话要点**：提出VideoMem框架，通过自适应内存管理解决超长视频理解任务

**关键词**：超长视频理解, 自适应内存管理, 视觉语言模型, 强化学习优化, 序列生成任务

## 3 点简述
- 核心问题：现有视觉语言模型因上下文长度限制和长期记忆保留不足，难以处理超长视频。
- 方法要点：VideoMem采用自适应全局内存缓冲，动态更新以保留关键信息并丢弃冗余内容，结合PRPO算法优化训练。
- 实验或效果：在多个超长视频理解基准测试中，VideoMem显著优于现有开源模型。

## 摘要（原文）

> Ultra long video understanding remains an open challenge, as existing vision language models (VLMs) falter on such content due to limited context length and inefficient long term memory retention. To address this, recent works have attempted to construct external knowledge bases and corresponding retrieval agumented generation (RAG) systems, yet these incur enormous storage and computational overhead. In this paper, we propose VideoMem, a novel framework that pioneers models long video understanding as a sequential generation task via adaptive memory management. Specifically, VideoMem dynamically updates a global memory buffer, which adaptively retains critical information while discarding redundant content across the video timeline. To efficiently train VLMs for such long-term tasks, VideoMem integrates the Progressive Grouped Relative Policy Optimization (PRPO) algorithm, equipped with two core modules: Progressive State Propagation (PSP) adaptively retains valid current states, propagates them to the next rollout step, and gradually narrows the model exploration space. Temporal Cascading Reward (TCR) further alleviates reward sparsity, improving sample utilization and accelerating convergence. Extensive experiments demonstrate that VideoMem significantly outperforms existing open-source models across diverse benchmarks for ultra-long video understanding tasks.

