---
layout: default
title: From Entropy to Epiplexity: Rethinking Information for Computationally Bounded Intelligence
---

# From Entropy to Epiplexity: Rethinking Information for Computationally Bounded Intelligence
**arXiv**：[2601.03220v1](https://arxiv.org/abs/2601.03220) · [PDF](https://arxiv.org/pdf/2601.03220.pdf)  
**作者**：Marc Finzi, Shikai Qiu, Yiding Jiang, Pavel Izmailov, J. Zico Kolter, Andrew Gordon Wilson  

**一句话要点**：提出epiplexity以量化计算受限智能体从数据中学习的有用信息

**关键词**：信息论, 计算复杂度, 数据选择, epiplexity, 结构内容, 时间受限熵

## 3 点简述
- 核心问题：传统信息论假设无限计算能力，无法评估数据对计算受限智能体的有用信息
- 方法要点：引入epiplexity，区分数据中的结构内容与时间受限熵，捕捉计算可学习信息
- 实验或效果：提出epiplexity估计方法，验证其能区分数据源、跟踪下游性能并指导数据选择

## 摘要（原文）

> Can we learn more from data than existed in the generating process itself? Can new and useful information be constructed from merely applying deterministic transformations to existing data? Can the learnable content in data be evaluated without considering a downstream task? On these questions, Shannon information and Kolmogorov complexity come up nearly empty-handed, in part because they assume observers with unlimited computational capacity and fail to target the useful information content. In this work, we identify and exemplify three seeming paradoxes in information theory: (1) information cannot be increased by deterministic transformations; (2) information is independent of the order of data; (3) likelihood modeling is merely distribution matching. To shed light on the tension between these results and modern practice, and to quantify the value of data, we introduce epiplexity, a formalization of information capturing what computationally bounded observers can learn from data. Epiplexity captures the structural content in data while excluding time-bounded entropy, the random unpredictable content exemplified by pseudorandom number generators and chaotic dynamical systems. With these concepts, we demonstrate how information can be created with computation, how it depends on the ordering of the data, and how likelihood modeling can produce more complex programs than present in the data generating process itself. We also present practical procedures to estimate epiplexity which we show capture differences across data sources, track with downstream performance, and highlight dataset interventions that improve out-of-distribution generalization. In contrast to principles of model selection, epiplexity provides a theoretical foundation for data selection, guiding how to select, generate, or transform data for learning systems.

