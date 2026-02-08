---
layout: default
title: Context Forcing: Consistent Autoregressive Video Generation with Long Context
---

# Context Forcing: Consistent Autoregressive Video Generation with Long Context
**arXiv**：[2602.06028v1](https://arxiv.org/abs/2602.06028) · [PDF](https://arxiv.org/pdf/2602.06028.pdf)  
**作者**：Shuo Chen, Cong Wei, Sun Sun, Ping Nie, Kai Zhou, Ge Zhang, Ming-Hsuan Yang, Wenhu Chen  

**一句话要点**：提出Context Forcing框架，通过长上下文教师模型解决长视频生成中的学生-教师不匹配问题。

**关键词**：长视频生成, 自回归模型, 上下文管理, 蒸馏训练, 时间一致性

## 3 点简述
- 核心问题：现有流式调优方法中，短上下文教师无法指导长上下文学生，导致全局时间依赖缺失。
- 方法要点：引入长上下文教师和Slow-Fast Memory架构，消除监督不匹配，降低计算成本。
- 实验或效果：实现超过20秒的有效上下文长度，在长视频评估指标上超越现有方法。

## 摘要（原文）

> Recent approaches to real-time long video generation typically employ streaming tuning strategies, attempting to train a long-context student using a short-context (memoryless) teacher. In these frameworks, the student performs long rollouts but receives supervision from a teacher limited to short 5-second windows. This structural discrepancy creates a critical \textbf{student-teacher mismatch}: the teacher's inability to access long-term history prevents it from guiding the student on global temporal dependencies, effectively capping the student's context length. To resolve this, we propose \textbf{Context Forcing}, a novel framework that trains a long-context student via a long-context teacher. By ensuring the teacher is aware of the full generation history, we eliminate the supervision mismatch, enabling the robust training of models capable of long-term consistency. To make this computationally feasible for extreme durations (e.g., 2 minutes), we introduce a context management system that transforms the linearly growing context into a \textbf{Slow-Fast Memory} architecture, significantly reducing visual redundancy. Extensive results demonstrate that our method enables effective context lengths exceeding 20 seconds -- 2 to 10 times longer than state-of-the-art methods like LongLive and Infinite-RoPE. By leveraging this extended context, Context Forcing preserves superior consistency across long durations, surpassing state-of-the-art baselines on various long video evaluation metrics.

