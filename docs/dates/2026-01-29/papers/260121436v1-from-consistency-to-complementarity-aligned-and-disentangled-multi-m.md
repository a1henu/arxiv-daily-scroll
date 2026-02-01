---
layout: default
title: From Consistency to Complementarity: Aligned and Disentangled Multi-modal Learning for Time Series Understanding and Reasoning
---

# From Consistency to Complementarity: Aligned and Disentangled Multi-modal Learning for Time Series Understanding and Reasoning
**arXiv**：[2601.21436v1](https://arxiv.org/abs/2601.21436) · [PDF](https://arxiv.org/pdf/2601.21436.pdf)  
**作者**：Hang Ni, Weijia Zhang, Fei Wang, Zezhi Shao, Hao Liu  

**一句话要点**：提出MADI模型，通过细粒度对齐和解耦交互解决时间序列多模态理解中的对齐和语义纠缠问题。

**关键词**：时间序列理解, 多模态学习, 细粒度对齐, 语义解耦, 大语言模型, 互补推理

## 3 点简述
- 核心问题：时间序列多模态学习存在细粒度时间错位和共享与模态特定语义的严重纠缠，阻碍局部解释和互补推理。
- 方法要点：采用补丁级对齐、离散解耦交互和关键令牌高亮，实现跨模态精细对应和语义分离。
- 实验或效果：在合成和真实基准测试中，MADI持续优于通用LLM和专门时间序列MLLM，提升推理性能。

## 摘要（原文）

> Advances in multi-modal large language models (MLLMs) have inspired time series understanding and reasoning tasks, that enable natural language querying over time series, producing textual analyses of complex temporal dynamics. Recent attempts hybridize numerical time series with their visualized plots, facilitating precise value reasoning and visual structure comprehension for comprehensive time series understanding of MLLMs. However, effective cross-modal integration remains challenging due to fine-grained temporal misalignment across modalities and severe entanglement between shared and modality-specific semantics, which hinder localized interpretation and complementary reasoning. To address these issues, we propose MADI, a multi-modal LLM enhanced with fine-grained alignment and disentangled interaction, featuring (1) Patch-level Alignment, which enforces physically grounded fine-grained correspondence across heterogeneous modalities, (2) Discrete Disentangled Interaction, which separates modality-common semantics into compact discrete latents and adaptively synergizes the purified modality-unique information, and (3) Critical-token Highlighting, which emphasizes informative, query-relevant signals for robust reasoning. Experiments on synthetic and real-world benchmarks show that MADI consistently outperforms general-purpose LLMs and time-series-specialized MLLMs.

