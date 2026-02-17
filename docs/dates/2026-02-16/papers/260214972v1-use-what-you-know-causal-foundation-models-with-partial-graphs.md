---
layout: default
title: Use What You Know: Causal Foundation Models with Partial Graphs
---

# Use What You Know: Causal Foundation Models with Partial Graphs
**arXiv**：[2602.14972v1](https://arxiv.org/abs/2602.14972) · [PDF](https://arxiv.org/pdf/2602.14972.pdf)  
**作者**：Arik Reuter, Anish Dhir, Cristiana Diaconu, Jake Robertson, Ole Ossen, Frank Hutter, Adrian Weller, Mark van der Wilk, Bernhard Schölkopf  

**一句话要点**：提出基于因果信息条件化的因果基础模型，以利用领域知识提升预测性能。

**关键词**：因果基础模型, 因果图条件化, 注意力机制, 领域知识融合, 因果推断

## 3 点简述
- 核心问题：现有因果基础模型无法融入领域知识，导致预测次优。
- 方法要点：通过注意力机制注入可学习偏置，条件化于因果图或祖先信息。
- 实验或效果：条件化模型匹配专用模型性能，有效利用部分因果信息。

## 摘要（原文）

> Estimating causal quantities traditionally relies on bespoke estimators tailored to specific assumptions. Recently proposed Causal Foundation Models (CFMs) promise a more unified approach by amortising causal discovery and inference in a single step. However, in their current state, they do not allow for the incorporation of any domain knowledge, which can lead to suboptimal predictions. We bridge this gap by introducing methods to condition CFMs on causal information, such as the causal graph or more readily available ancestral information. When access to complete causal graph information is too strict a requirement, our approach also effectively leverages partial causal information. We systematically evaluate conditioning strategies and find that injecting learnable biases into the attention mechanism is the most effective method to utilise full and partial causal information. Our experiments show that this conditioning allows a general-purpose CFM to match the performance of specialised models trained on specific causal structures. Overall, our approach addresses a central hurdle on the path towards all-in-one causal foundation models: the capability to answer causal queries in a data-driven manner while effectively leveraging any amount of domain expertise.

