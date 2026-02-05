---
layout: default
title: ReThinker: Scientific Reasoning by Rethinking with Guided Reflection and Confidence Control
---

# ReThinker: Scientific Reasoning by Rethinking with Guided Reflection and Confidence Control
**arXiv**：[2602.04496v1](https://arxiv.org/abs/2602.04496) · [PDF](https://arxiv.org/pdf/2602.04496.pdf)  
**作者**：Zhentao Tang, Yuqi Cui, Shixiong Kai, Wenqian Zhao, Ke Ye, Xing Li, Anxin Tian, Zehua Pei, Hui-Ling Zhen, Shoubo Hu, Xiaoguang Li, Yunhe Wang, Mingxuan Yuan  

**一句话要点**：提出ReThinker框架以解决大语言模型在科学推理任务中的性能限制

**关键词**：科学推理, 置信度控制, 多智能体框架, 自适应工具调用, 数据合成, 专家级基准

## 3 点简述
- 核心问题：大语言模型在专家级科学推理任务中面临工具管道僵化、多智能体协调脆弱和测试时扩展低效的挑战
- 方法要点：引入基于置信度的Solver-Critic-Selector架构，实现动态计算分配、自适应工具调用和引导式多维反思
- 实验或效果：在HLE、GAIA和XBench基准上超越现有工具增强模型和深度研究系统，达到最先进性能

## 摘要（原文）

> Expert-level scientific reasoning remains challenging for large language models, particularly on benchmarks such as Humanity's Last Exam (HLE), where rigid tool pipelines, brittle multi-agent coordination, and inefficient test-time scaling often limit performance. We introduce ReThinker, a confidence-aware agentic framework that orchestrates retrieval, tool use, and multi-agent reasoning through a stage-wise Solver-Critic-Selector architecture. Rather than following a fixed pipeline, ReThinker dynamically allocates computation based on model confidence, enabling adaptive tool invocation, guided multi-dimensional reflection, and robust confidence-weighted selection. To support scalable training without human annotation, we further propose a reverse data synthesis pipeline and an adaptive trajectory recycling strategy that transform successful reasoning traces into high-quality supervision. Experiments on HLE, GAIA, and XBench demonstrate that ReThinker consistently outperforms state-of-the-art foundation models with tools and existing deep research systems, achieving state-of-the-art results on expert-level reasoning tasks.

