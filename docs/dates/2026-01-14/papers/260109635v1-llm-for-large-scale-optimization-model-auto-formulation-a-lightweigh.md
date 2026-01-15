---
layout: default
title: LLM for Large-Scale Optimization Model Auto-Formulation: A Lightweight Few-Shot Learning Approach
---

# LLM for Large-Scale Optimization Model Auto-Formulation: A Lightweight Few-Shot Learning Approach
**arXiv**：[2601.09635v1](https://arxiv.org/abs/2601.09635) · [PDF](https://arxiv.org/pdf/2601.09635.pdf)  
**作者**：Kuo Liang, Yuhang Lu, Jianming Mao, Shuyi Sun, Chunwei Yang, Congcong Zeng, Xiao Jin, Hanzhang Qin, Ruihao Zhu, Chung-Piaw Teo  

**一句话要点**：提出LEAN-LLM-OPT框架，通过轻量级少样本学习实现大规模优化模型自动构建

**关键词**：大规模优化, 自动建模, 少样本学习, LLM代理, 工作流构建, 基准测试

## 3 点简述
- 核心问题：大规模优化模型构建耗时费力，需自动化解决方案。
- 方法要点：基于LLM代理团队动态构建工作流，分解任务并利用工具处理数据。
- 实验或效果：在基准测试和新加坡航空案例中表现优异，达到领先水平。

## 摘要（原文）

> Large-scale optimization is a key backbone of modern business decision-making. However, building these models is often labor-intensive and time-consuming. We address this by proposing LEAN-LLM-OPT, a LightwEight AgeNtic workflow construction framework for LLM-assisted large-scale OPTimization auto-formulation. LEAN-LLM-OPT takes as input a problem description together with associated datasets and orchestrates a team of LLM agents to produce an optimization formulation. Specifically, upon receiving a query, two upstream LLM agents dynamically construct a workflow that specifies, step-by-step, how optimization models for similar problems can be formulated. A downstream LLM agent then follows this workflow to generate the final output. Leveraging LLMs' text-processing capabilities and common modeling practices, the workflow decomposes the modeling task into a sequence of structured sub-tasks and offloads mechanical data-handling operations to auxiliary tools. This design alleviates the downstream agent's burden related to planning and data handling, allowing it to focus on the most challenging components that cannot be readily standardized. Extensive simulations show that LEAN-LLM-OPT, instantiated with GPT-4.1 and the open source gpt-oss-20B, achieves strong performance on large-scale optimization modeling tasks and is competitive with state-of-the-art approaches. In addition, in a Singapore Airlines choice-based revenue management use case, LEAN-LLM-OPT demonstrates practical value by achieving leading performance across a range of scenarios. Along the way, we introduce Large-Scale-OR and Air-NRM, the first comprehensive benchmarks for large-scale optimization auto-formulation. The code and data of this work is available at https://github.com/CoraLiang01/lean-llm-opt.

