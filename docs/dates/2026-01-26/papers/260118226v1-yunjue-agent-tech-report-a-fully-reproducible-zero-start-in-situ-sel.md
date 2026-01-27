---
layout: default
title: Yunjue Agent Tech Report: A Fully Reproducible, Zero-Start In-Situ Self-Evolving Agent System for Open-Ended Tasks
---

# Yunjue Agent Tech Report: A Fully Reproducible, Zero-Start In-Situ Self-Evolving Agent System for Open-Ended Tasks
**arXiv**：[2601.18226v1](https://arxiv.org/abs/2601.18226) · [PDF](https://arxiv.org/pdf/2601.18226.pdf)  
**作者**：Haotian Li, Shijun Yang, Weizhen Qi, Silei Zhao, Rui Hua, Mingzhu Song, Xiaojian Yang, Chao Peng  

**一句话要点**：提出原位自进化范式，通过工具进化解决开放任务中能力边界僵化问题

**关键词**：智能体系统, 原位自进化, 工具进化, 开放任务, 零启动学习, 进化收敛度量

## 3 点简述
- 核心问题：传统智能体在开放环境中因任务分布漂移和外部监督稀缺而能力受限
- 方法要点：基于原位自进化，利用任务交互反馈迭代合成、优化和重用工具以扩展能力
- 实验或效果：在零启动设置下，五个基准测试中表现优于基线，并展示知识可迁移性

## 摘要（原文）

> Conventional agent systems often struggle in open-ended environments where task distributions continuously drift and external supervision is scarce. Their reliance on static toolsets or offline training lags behind these dynamics, leaving the system's capability boundaries rigid and unknown. To address this, we propose the In-Situ Self-Evolving paradigm. This approach treats sequential task interactions as a continuous stream of experience, enabling the system to distill short-term execution feedback into long-term, reusable capabilities without access to ground-truth labels. Within this framework, we identify tool evolution as the critical pathway for capability expansion, which provides verifiable, binary feedback signals. Within this framework, we develop Yunjue Agent, a system that iteratively synthesizes, optimizes, and reuses tools to navigate emerging challenges. To optimize evolutionary efficiency, we further introduce a Parallel Batch Evolution strategy. Empirical evaluations across five diverse benchmarks under a zero-start setting demonstrate significant performance gains over proprietary baselines. Additionally, complementary warm-start evaluations confirm that the accumulated general knowledge can be seamlessly transferred to novel domains. Finally, we propose a novel metric to monitor evolution convergence, serving as a function analogous to training loss in conventional optimization. We open-source our codebase, system traces, and evolved tools to facilitate future research in resilient, self-evolving intelligence.

