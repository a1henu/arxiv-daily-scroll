---
layout: default
title: Efficient, Property-Aligned Fan-Out Retrieval via RL-Compiled Diffusion
---

# Efficient, Property-Aligned Fan-Out Retrieval via RL-Compiled Diffusion
**arXiv**：[2603.06397v1](https://arxiv.org/abs/2603.06397) · [PDF](https://arxiv.org/pdf/2603.06397.pdf)  
**作者**：Pengcheng Jiang, Judith Yue Li, Moonkyung Ryu, R. Lily Hu, Kun Su, Zhong Yi Wan, Liam Hebert, Hao Peng, Jiawei Han, Dima Kuzmin, Craig Boutilier  

**一句话要点**：提出R4T方法，通过RL编译扩散模型实现高效、属性对齐的扇出检索

**关键词**：集合值检索, 扇出检索, 强化学习, 扩散模型, 检索效率

## 3 点简述
- 核心问题：集合值检索需优化高阶属性，但现有方法效率低或训练目标不匹配
- 方法要点：使用RL训练扇出LLM，合成目标一致训练对，训练轻量扩散检索器
- 实验或效果：在时尚和音乐基准上提升检索质量，查询延迟降低一个数量级

## 摘要（原文）

> Many modern retrieval problems are set-valued: given a broad intent, the system must return a collection of results that optimizes higher-order properties
>   (e.g., diversity, coverage, complementarity, coherence) while remaining grounded with respect to a fixed database. Set-valued objectives are typically
>   non-decomposable and are not captured by existing supervised (query, content) datasets which only prioritize top-1 retrieval. Consequently, fan-out
>   retrieval is often employed to generate diverse subqueries to retrieve item sets. While reinforcement learning (RL) can optimize set-level objectives via
>   interaction, deploying an RL-tuned LLM for fan-out retrieval is prohibitively expensive at inference time. Conversely, diffusion-based generative
>   retrieval enables efficient single-pass fan-out in embedding space, but requires objective-aligned training targets. To address these issues, we propose
>   R4T (Retrieve-for-Train), which uses RL once as an objective transducer in a three-step process: (i) train a fan-out LLM with composite set-level rewards,
>   (ii) synthesize objective-consistent training pairs, and (iii) train a lightweight diffusion retriever to model the conditional distribution of set-valued
>   outputs. Across large-scale fashion and music benchmarks consisting of curated item sets, we show that R4T improves retrieval quality relative to strong
>   baselines while reducing query-time fan-out latency by an order of magnitude.

