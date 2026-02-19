---
layout: default
title: Leveraging Large Language Models for Causal Discovery: a Constraint-based, Argumentation-driven Approach
---

# Leveraging Large Language Models for Causal Discovery: a Constraint-based, Argumentation-driven Approach
**arXiv**：[2602.16481v1](https://arxiv.org/abs/2602.16481) · [PDF](https://arxiv.org/pdf/2602.16481.pdf)  
**作者**：Zihao Li, Fabrizio Russo  

**一句话要点**：提出基于大语言模型与因果论证框架的因果发现方法，以整合语义先验与统计证据。

**关键词**：因果发现, 大语言模型, 因果论证框架, 语义先验, 条件独立性, 评估协议

## 3 点简述
- 核心问题：因果发现需结合专家知识与数据，但传统方法依赖完美专家，难以处理语义信息。
- 方法要点：利用大语言模型作为不完美专家，从变量描述中提取语义结构先验，融入因果论证框架进行推理。
- 实验或效果：在标准基准和语义合成图上实现先进性能，并引入评估协议以减少记忆偏差。

## 摘要（原文）

> Causal discovery seeks to uncover causal relations from data, typically represented as causal graphs, and is essential for predicting the effects of interventions. While expert knowledge is required to construct principled causal graphs, many statistical methods have been proposed to leverage observational data with varying formal guarantees. Causal Assumption-based Argumentation (ABA) is a framework that uses symbolic reasoning to ensure correspondence between input constraints and output graphs, while offering a principled way to combine data and expertise. We explore the use of large language models (LLMs) as imperfect experts for Causal ABA, eliciting semantic structural priors from variable names and descriptions and integrating them with conditional-independence evidence. Experiments on standard benchmarks and semantically grounded synthetic graphs demonstrate state-of-the-art performance, and we additionally introduce an evaluation protocol to mitigate memorisation bias when assessing LLMs for causal discovery.

