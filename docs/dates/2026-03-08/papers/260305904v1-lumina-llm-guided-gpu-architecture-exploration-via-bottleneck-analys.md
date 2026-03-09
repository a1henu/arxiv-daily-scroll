---
layout: default
title: LUMINA: LLM-Guided GPU Architecture Exploration via Bottleneck Analysis
---

# LUMINA: LLM-Guided GPU Architecture Exploration via Bottleneck Analysis
**arXiv**：[2603.05904v1](https://arxiv.org/abs/2603.05904) · [PDF](https://arxiv.org/pdf/2603.05904.pdf)  
**作者**：Tao Zhang, Rui Ma, Shuotao Xu, Peng Cheng, Yongqiang Xiong  

**一句话要点**：提出LUMINA框架，利用LLM引导瓶颈分析以高效探索GPU架构设计空间

**关键词**：GPU架构探索, LLM引导优化, 瓶颈分析, 设计空间探索, AI辅助设计

## 3 点简述
- 核心问题：GPU设计空间探索面临样本量大、模拟成本高和优化目标复杂的挑战
- 方法要点：通过LLM从模拟器代码提取知识并自动生成与校正设计规则
- 实验或效果：在470万样本空间中，仅用20步找到优于A100的设计，效率提升17.5倍

## 摘要（原文）

> GPU design space exploration (DSE) for modern AI workloads, such as Large-Language Model (LLM) inference, is challenging because of GPUs' vast, multi-modal design spaces, high simulation costs, and complex design optimization objectives (e.g. performance, power and area trade-offs). Existing automated DSE methods are often prohibitively expensive, either requiring an excessive number of exploration samples or depending on intricate, manually crafted analyses of interdependent critical paths guided by human heuristics.
>   We present LUMINA, an LLM-driven GPU architecture exploration framework that leverage AI to enhance the DSE efficiency and efficacy for GPUs. LUMINA extracts architectural knowledge from simulator code and performs sensitivity studies to automatically compose DSE rules,which are auto-corrected during exploration. A core component of LUMINA is a DSE Benchmark that comprehensively evaluates and enhances LLMs' capabilities across three fundamental skills required for architecture optimization, which provides a principled and reproducible basis for model selection and ensuring consistent architectural reasoning.
>   In the design space with 4.7 million possible samples, LUMINA identifies 6 designs of better performance and area than an A100 GPU efficiently, using only 20 steps via LLM-assisted bottleneck analysis. In comparison, LUMINA achieves 17.5x higher than design space exploration efficiency, and 32.9% better designs (i.e. Pareto Hypervolume) than Machine-Learning baselines, showcasing its ability to deliver high-quality design guidance with minimal search cost.

