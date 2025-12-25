---
layout: default
title: Transductive Visual Programming: Evolving Tool Libraries from Experience for Spatial Reasoning
---

# Transductive Visual Programming: Evolving Tool Libraries from Experience for Spatial Reasoning
**arXiv**：[2512.20934v1](https://arxiv.org/abs/2512.20934) · [PDF](https://arxiv.org/pdf/2512.20934.pdf)  
**作者**：Shengguang Wu, Xiaohan Wang, Yuhui Zhang, Hao Zhu, Serena Yeung-Levy  

**一句话要点**：提出Transductive Visual Programming，通过经验演化工具库以解决3D空间推理问题

**关键词**：视觉编程, 空间推理, 工具演化, 经验学习, 3D场景理解, 自进化代理

## 3 点简述
- 核心问题：现有视觉编程方法依赖固定工具集或先验工具归纳，导致程序次优和工具利用率低
- 方法要点：TVP从经验中积累解决方案并抽象为可重用工具，实现工具库的自我演化
- 实验或效果：在Omni3D-Bench上超越GPT-4o 22%，工具使用频率比归纳方法高5倍，泛化能力强

## 摘要（原文）

> Spatial reasoning in 3D scenes requires precise geometric calculations that challenge vision-language models. Visual programming addresses this by decomposing problems into steps calling specialized tools, yet existing methods rely on either fixed toolsets or speculative tool induction before solving problems, resulting in suboptimal programs and poor utilization of induced tools. We present Transductive Visual Programming (TVP), a novel framework that builds new tools from its own experience rather than speculation. TVP first solves problems using basic tools while accumulating experiential solutions into an Example Library, then abstracts recurring patterns from these programs into reusable higher-level tools for an evolving Tool Library. This allows TVP to tackle new problems with increasingly powerful tools learned from experience. On Omni3D-Bench, TVP achieves state-of-the-art performance, outperforming GPT-4o by 22% and the previous best visual programming system by 11%. Our transductively learned tools are used 5x more frequently as core program dependency than inductively created ones, demonstrating more effective tool discovery and reuse. The evolved tools also show strong generalization to unseen spatial tasks, achieving superior performance on benchmarks from SpatialScore-Hard collection without any testset-specific modification. Our work establishes experience-driven transductive tool creation as a powerful paradigm for building self-evolving visual programming agents that effectively tackle challenging spatial reasoning tasks. We release our code at https://transductive-visualprogram.github.io/.

