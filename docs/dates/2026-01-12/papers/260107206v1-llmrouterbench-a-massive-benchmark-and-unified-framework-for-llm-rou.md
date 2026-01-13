---
layout: default
title: LLMRouterBench: A Massive Benchmark and Unified Framework for LLM Routing
---

# LLMRouterBench: A Massive Benchmark and Unified Framework for LLM Routing
**arXiv**：[2601.07206v1](https://arxiv.org/abs/2601.07206) · [PDF](https://arxiv.org/pdf/2601.07206.pdf)  
**作者**：Hao Li, Yiqun Zhang, Zhaoyan Guo, Chenxu Wang, Shengji Tang, Qiaosheng Zhang, Yang Chen, Biqing Qi, Peng Ye, Lei Bai, Zhen Wang, Shuyue Hu  

**一句话要点**：提出LLMRouterBench大规模基准与统一框架，用于评估大语言模型路由性能与成本权衡。

**关键词**：大语言模型路由, 基准测试, 模型集成, 性能成本权衡, 统一评估框架

## 3 点简述
- 核心问题：大语言模型路由中，现有方法性能相似且与Oracle差距大，主要由模型召回失败导致。
- 方法要点：构建包含400K实例、21数据集和33模型的大规模基准，集成10种代表性路由基线。
- 实验或效果：确认模型互补性，发现骨干嵌入模型影响有限，大集成收益递减，支持延迟感知分析。

## 摘要（原文）

> Large language model (LLM) routing assigns each query to the most suitable model from an ensemble. We introduce LLMRouterBench, a large-scale benchmark and unified framework for LLM routing. It comprises over 400K instances from 21 datasets and 33 models. Moreover, it provides comprehensive metrics for both performance-oriented routing and performance-cost trade-off routing, and integrates 10 representative routing baselines. Using LLMRouterBench, we systematically re-evaluate the field. While confirming strong model complementarity-the central premise of LLM routing-we find that many routing methods exhibit similar performance under unified evaluation, and several recent approaches, including commercial routers, fail to reliably outperform a simple baseline. Meanwhile, a substantial gap remains to the Oracle, driven primarily by persistent model-recall failures. We further show that backbone embedding models have limited impact, that larger ensembles exhibit diminishing returns compared to careful model curation, and that the benchmark also enables latency-aware analysis. All code and data are available at https://github.com/ynulihao/LLMRouterBench.

