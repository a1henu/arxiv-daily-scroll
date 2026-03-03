---
layout: default
title: Mitigating topology biases in Graph Diffusion via Counterfactual Intervention
---

# Mitigating topology biases in Graph Diffusion via Counterfactual Intervention
**arXiv**：[2603.02005v1](https://arxiv.org/abs/2603.02005) · [PDF](https://arxiv.org/pdf/2603.02005.pdf)  
**作者**：Wendi Wang, Jiaxi Yang, Yongkang Du, Lu Lin  

**一句话要点**：提出FairGDiff以缓解图扩散中的拓扑偏见，平衡公平性与实用性

**关键词**：图扩散模型, 拓扑偏见, 反事实干预, 公平图生成, 因果模型

## 3 点简述
- 图扩散模型在生成任务中常放大敏感属性导致的拓扑偏见，现有方法受限
- 基于因果模型和反事实干预，FairGDiff在扩散过程中直接去偏，保持结构完整性
- 在真实数据集上实验显示，FairGDiff在公平性与实用性间取得更优权衡

## 摘要（原文）

> Graph diffusion models have gained significant attention in graph generation tasks, but they often inherit and amplify topology biases from sensitive attributes (e.g. gender, age, region), leading to unfair synthetic graphs. Existing fair graph generation using diffusion models is limited to specific graph-based applications with complete labels or requires simultaneous updates for graph structure and node attributes, making them unsuitable for general usage. To relax these limitations by applying the debiasing method directly on graph topology, we propose Fair Graph Diffusion Model (FairGDiff), a counterfactual-based one-step solution that mitigates topology biases while balancing fairness and utility. In detail, we construct a causal model to capture the relationship between sensitive attributes, biased link formation, and the generated graph structure. By answering the counterfactual question "Would the graph structure change if the sensitive attribute were different?", we estimate an unbiased treatment and incorporate it into the diffusion process. FairGDiff integrates counterfactual learning into both forward diffusion and backward denoising, ensuring that the generated graphs are independent of sensitive attributes while preserving structural integrity. Extensive experiments on real-world datasets demonstrate that FairGDiff achieves a superior trade-off between fairness and utility, outperforming existing fair graph generation methods while maintaining scalability.

