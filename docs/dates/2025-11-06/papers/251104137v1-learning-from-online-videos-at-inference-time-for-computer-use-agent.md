---
layout: default
title: Learning from Online Videos at Inference Time for Computer-Use Agents
---

# Learning from Online Videos at Inference Time for Computer-Use Agents
**arXiv**：[2511.04137v1](https://arxiv.org/abs/2511.04137) · [PDF](https://arxiv.org/pdf/2511.04137.pdf)  
**作者**：Yujian Liu, Ze Wang, Hao Chen, Ximeng Sun, Xiaodong Yu, Jialian Wu, Jiang Liu, Emad Barsoum, Zicheng Liu, Shiyu Chang  

**一句话要点**：提出从在线视频中动态提取轨迹的框架，以提升计算机使用代理在推理时的性能。

**关键词**：计算机使用代理, 在线视频学习, 轨迹分割, 动态选择机制, 视觉语言模型, 推理时学习

## 3 点简述
- 核心问题：计算机使用代理缺乏特定领域程序知识，难以处理多步骤工作流。
- 方法要点：检索视频、分割为动作子序列，并使用两阶段选择机制动态提供上下文指导。
- 实验效果：在基准测试中优于仅使用文本教程的变体，强调视觉信息的重要性。

## 摘要（原文）

> Computer-use agents can operate computers and automate laborious tasks, but
> despite recent rapid progress, they still lag behind human users, especially
> when tasks require domain-specific procedural knowledge about particular
> applications, platforms, and multi-step workflows. Humans can bridge this gap
> by watching video tutorials: we search, skim, and selectively imitate short
> segments that match our current subgoal. In this paper, we study how to enable
> computer-use agents to learn from online videos at inference time effectively.
> We propose a framework that retrieves and filters tutorial videos, converts
> them into structured demonstration trajectories, and dynamically selects
> trajectories as in-context guidance during execution. Particularly, using a
> VLM, we infer UI actions, segment videos into short subsequences of actions,
> and assign each subsequence a textual objective. At inference time, a two-stage
> selection mechanism dynamically chooses a single trajectory to add in context
> at each step, focusing the agent on the most helpful local guidance for its
> next decision. Experiments on two widely used benchmarks show that our
> framework consistently outperforms strong base agents and variants that use
> only textual tutorials or transcripts. Analyses highlight the importance of
> trajectory segmentation and selection, action filtering, and visual
> information, suggesting that abundant online videos can be systematically
> distilled into actionable guidance that improves computer-use agents at
> inference time. Our code is available at
> https://github.com/UCSB-NLP-Chang/video_demo.

