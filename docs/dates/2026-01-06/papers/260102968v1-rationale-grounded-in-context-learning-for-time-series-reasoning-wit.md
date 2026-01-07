---
layout: default
title: Rationale-Grounded In-Context Learning for Time Series Reasoning with Multimodal Large Language Models
---

# Rationale-Grounded In-Context Learning for Time Series Reasoning with Multimodal Large Language Models
**arXiv**：[2601.02968v1](https://arxiv.org/abs/2601.02968) · [PDF](https://arxiv.org/pdf/2601.02968.pdf)  
**作者**：Qingxiang Liu, Zhiqing Cui, Xiaoliang Luo, Yuqian Wu, Zhuoyang Jiang, Huaiyu Wan, Sheng Sun, Lvchun Wang, Wei Yu, Yuxuan Liang  

**一句话要点**：提出RationaleTS方法，通过基于原理的上下文学习解决多模态大语言模型在时间序列推理中的性能不足问题。

**关键词**：时间序列推理, 多模态大语言模型, 上下文学习, 原理先验, 混合检索

## 3 点简述
- 核心问题：现有模型因缺乏连接时间观测与下游结果的原理先验，导致依赖表面模式匹配而非原则性推理。
- 方法要点：引入标签条件化原理作为指导推理单元，设计混合检索平衡时间模式和语义上下文以检索相关先验。
- 实验或效果：在三个领域的时间序列推理任务上验证了RationaleTS的有效性和效率，代码将开源。

## 摘要（原文）

> The underperformance of existing multimodal large language models for time series reasoning lies in the absence of rationale priors that connect temporal observations to their downstream outcomes, which leads models to rely on superficial pattern matching rather than principled reasoning. We therefore propose the rationale-grounded in-context learning for time series reasoning, where rationales work as guiding reasoning units rather than post-hoc explanations, and develop the RationaleTS method. Specifically, we firstly induce label-conditioned rationales, composed of reasoning paths from observable evidence to the potential outcomes. Then, we design the hybrid retrieval by balancing temporal patterns and semantic contexts to retrieve correlated rationale priors for the final in-context inference on new samples. We conduct extensive experiments to demonstrate the effectiveness and efficiency of our proposed RationaleTS on three-domain time series reasoning tasks. We will release our code for reproduction.

