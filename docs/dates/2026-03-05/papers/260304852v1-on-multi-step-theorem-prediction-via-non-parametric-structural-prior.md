---
layout: default
title: On Multi-Step Theorem Prediction via Non-Parametric Structural Priors
---

# On Multi-Step Theorem Prediction via Non-Parametric Structural Priors
**arXiv**：[2603.04852v1](https://arxiv.org/abs/2603.04852) · [PDF](https://arxiv.org/pdf/2603.04852.pdf)  
**作者**：Junbo Zhao, Ting Zhang, Can Li, Wei He, Jingdong Wang, Hua Huang  

**一句话要点**：提出定理优先图以解决多步定理预测中的结构漂移问题

**关键词**：多步定理预测, 上下文学习, 定理优先图, 结构漂移, 符号推理, 检索增强

## 3 点简述
- 核心问题：多步定理预测中，现有方法泛化性差，且上下文学习存在结构漂移导致性能下降
- 方法要点：利用历史解迹构建定理优先图，施加拓扑约束以结构化搜索，无需梯度优化
- 实验或效果：在FormalGeo7k基准上达到89.29%准确率，超越上下文学习基线并匹配监督模型

## 摘要（原文）

> Multi-step theorem prediction is a central challenge in automated reasoning. Existing neural-symbolic approaches rely heavily on supervised parametric models, which exhibit limited generalization to evolving theorem libraries. In this work, we explore training-free theorem prediction through the lens of in-context learning (ICL). We identify a critical scalability bottleneck, termed Structural Drift: as reasoning depth increases, the performance of vanilla ICL degrades sharply, often collapsing to near zero. We attribute this failure to the LLM's inability to recover latent topological dependencies, leading to unstructured exploration. To address this issue, we propose Theorem Precedence Graphs, which encode temporal dependencies from historical solution traces as directed graphs, and impose explicit topological constraints that effectively prune the search space during inference. Coupled with retrieval-augmented graph construction and a stepwise symbolic executor, our approach enables LLMs to act as structured planners without any gradient-based optimization. Experiments on the FormalGeo7k benchmark show that our method achieves 89.29% accuracy, substantially outperforming ICL baselines and matching state-of-the-art supervised models. These results indicate that explicit structural priors offer a promising direction for scaling LLM-based symbolic reasoning.

