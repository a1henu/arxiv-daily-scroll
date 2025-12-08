---
layout: default
title: Active Video Perception: Iterative Evidence Seeking for Agentic Long Video Understanding
---

# Active Video Perception: Iterative Evidence Seeking for Agentic Long Video Understanding
**arXiv**：[2512.05774v1](https://arxiv.org/abs/2512.05774) · [PDF](https://arxiv.org/pdf/2512.05774.pdf)  
**作者**：Ziyang Wang, Honglu Zhou, Shijie Wang, Junnan Li, Caiming Xiong, Silvio Savarese, Mohit Bansal, Michael S. Ryoo, Juan Carlos Niebles  

**一句话要点**：提出主动视频感知框架以解决长视频理解中查询相关证据稀疏与计算浪费问题

**关键词**：长视频理解, 主动感知, 多模态大语言模型, 迭代推理, 查询相关证据提取, 计算效率优化

## 3 点简述
- 核心问题：长视频理解依赖稀疏、分散的线索，现有方法因查询无关感知而浪费计算并模糊细节
- 方法要点：基于主动感知理论，设计迭代计划-观察-反思流程，由MLLM代理主动决策视频交互以提取查询相关证据
- 实验或效果：在五个长视频理解基准上实现最高性能，平均准确率提升5.7%，推理时间仅需18.4%，输入令牌减少至12.4%

## 摘要（原文）

> Long video understanding (LVU) is challenging because answering real-world queries often depends on sparse, temporally dispersed cues buried in hours of mostly redundant and irrelevant content. While agentic pipelines improve video reasoning capabilities, prevailing frameworks rely on a query-agnostic captioner to perceive video information, which wastes computation on irrelevant content and blurs fine-grained temporal and spatial information. Motivated by active perception theory, we argue that LVU agents should actively decide what, when, and where to observe, and continuously assess whether the current observation is sufficient to answer the query. We present Active Video Perception (AVP), an evidence-seeking framework that treats the video as an interactive environment and acquires compact, queryrelevant evidence directly from pixels. Concretely, AVP runs an iterative plan-observe-reflect process with MLLM agents. In each round, a planner proposes targeted video interactions, an observer executes them to extract time-stamped evidence, and a reflector evaluates the sufficiency of the evidence for the query, either halting with an answer or triggering further observation. Across five LVU benchmarks, AVP achieves highest performance with significant improvements. Notably, AVP outperforms the best agentic method by 5.7% in average accuracy while only requires 18.4% inference time and 12.4% input tokens.

