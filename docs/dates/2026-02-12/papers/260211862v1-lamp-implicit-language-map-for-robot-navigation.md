---
layout: default
title: LAMP: Implicit Language Map for Robot Navigation
---

# LAMP: Implicit Language Map for Robot Navigation
**arXiv**：[2602.11862v1](https://arxiv.org/abs/2602.11862) · [PDF](https://arxiv.org/pdf/2602.11862.pdf)  
**作者**：Sibaek Lee, Hyeonwoo Yu, Giseop Kim, Sunwook Choi  

**一句话要点**：提出LAMP框架，通过隐式语言场解决机器人零样本导航中的内存与细粒度规划问题。

**关键词**：机器人导航, 隐式表示, 语言驱动规划, 零样本学习, 梯度优化, 贝叶斯框架

## 3 点简述
- 现有方法因显式存储语言向量导致内存需求大、分辨率有限，难以扩展到大环境。
- LAMP采用隐式神经场编码语言特征，结合稀疏图实现粗到细路径规划，并通过梯度优化提升目标区域精度。
- 实验在仿真和真实多楼层环境中验证了LAMP在内存效率和目标到达准确性上的优势。

## 摘要（原文）

> Recent advances in vision-language models have made zero-shot navigation feasible, enabling robots to follow natural language instructions without requiring labeling. However, existing methods that explicitly store language vectors in grid or node-based maps struggle to scale to large environments due to excessive memory requirements and limited resolution for fine-grained planning. We introduce LAMP (Language Map), a novel neural language field-based navigation framework that learns a continuous, language-driven map and directly leverages it for fine-grained path generation. Unlike prior approaches, our method encodes language features as an implicit neural field rather than storing them explicitly at every location. By combining this implicit representation with a sparse graph, LAMP supports efficient coarse path planning and then performs gradient-based optimization in the learned field to refine poses near the goal. This coarse-to-fine pipeline, language-driven, gradient-guided optimization is the first application of an implicit language map for precise path generation. This refinement is particularly effective at selecting goal regions not directly observed by leveraging semantic similarities in the learned feature space. To further enhance robustness, we adopt a Bayesian framework that models embedding uncertainty via the von Mises-Fisher distribution, thereby improving generalization to unobserved regions. To scale to large environments, LAMP employs a graph sampling strategy that prioritizes spatial coverage and embedding confidence, retaining only the most informative nodes and substantially reducing computational overhead. Our experimental results, both in NVIDIA Isaac Sim and on a real multi-floor building, demonstrate that LAMP outperforms existing explicit methods in both memory efficiency and fine-grained goal-reaching accuracy.

