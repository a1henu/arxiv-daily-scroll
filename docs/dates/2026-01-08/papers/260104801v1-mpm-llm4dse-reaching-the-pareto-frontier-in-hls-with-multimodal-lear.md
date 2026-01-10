---
layout: default
title: MPM-LLM4DSE: Reaching the Pareto Frontier in HLS with Multimodal Learning and LLM-Driven Exploration
---

# MPM-LLM4DSE: Reaching the Pareto Frontier in HLS with Multimodal Learning and LLM-Driven Exploration
**arXiv**：[2601.04801v1](https://arxiv.org/abs/2601.04801) · [PDF](https://arxiv.org/pdf/2601.04801.pdf)  
**作者**：Lei Xu, Shanshan Wang, Chenglong Xiao  

**一句话要点**：提出MPM-LLM4DSE框架，融合多模态预测与LLM优化以加速HLS设计空间探索。

**关键词**：高层次综合, 设计空间探索, 多模态学习, 大语言模型优化, 提示工程, 性能预测

## 3 点简述
- 核心问题：现有GNN预测方法未能充分捕捉行为描述语义特征，且传统多目标优化算法未显式考虑pragma指令对QoR的影响。
- 方法要点：结合多模态预测模型融合行为描述与流图特征，并采用LLM作为优化器，通过提示工程指导高质量配置生成。
- 实验或效果：多模态预测模型性能超越ProgSG达10.25倍，LLM4DSE在DSE任务中平均性能提升39.90%。

## 摘要（原文）

> High-Level Synthesis (HLS) design space exploration (DSE) seeks Pareto-optimal designs within expansive pragma configuration spaces. To accelerate HLS DSE, graph neural networks (GNNs) are commonly employed as surrogates for HLS tools to predict quality of results (QoR) metrics, while multi-objective optimization algorithms expedite the exploration. However, GNN-based prediction methods may not fully capture the rich semantic features inherent in behavioral descriptions, and conventional multi-objective optimization algorithms often do not explicitly account for the domain-specific knowledge regarding how pragma directives influence QoR. To address these limitations, this paper proposes the MPM-LLM4DSE framework, which incorporates a multimodal prediction model (MPM) that simultaneously fuses features from behavioral descriptions and control and data flow graphs. Furthermore, the framework employs a large language model (LLM) as an optimizer, accompanied by a tailored prompt engineering methodology. This methodology incorporates pragma impact analysis on QoR to guide the LLM in generating high-quality configurations (LLM4DSE). Experimental results demonstrate that our multimodal predictive model significantly outperforms state-of-the-art work ProgSG by up to 10.25$\times$. Furthermore, in DSE tasks, the proposed LLM4DSE achieves an average performance gain of 39.90\% over prior methods, validating the effectiveness of our prompting methodology. Code and models are available at https://github.com/wslcccc/MPM-LLM4DSE.

