---
layout: default
title: Fine-Grained Model Merging via Modular Expert Recombination
---

# Fine-Grained Model Merging via Modular Expert Recombination
**arXiv**：[2602.06552v1](https://arxiv.org/abs/2602.06552) · [PDF](https://arxiv.org/pdf/2602.06552.pdf)  
**作者**：Haiyun Qiu, Xingyu Wu, Liang Feng, Kay Chen Tan  

**一句话要点**：提出MERGE方法，通过模块化专家重组实现细粒度模型合并，以解决实例特定模型不可重用和组件合并敏感性差异问题。

**关键词**：模型合并, 模块化专家, 细粒度合并, 双目标优化, 路由网络, 存储效率

## 3 点简述
- 核心问题：现有实例特定模型合并方法缺乏可重用性，且忽略同源组件（如注意力层）的合并敏感性和多样性。
- 方法要点：MERGE将组件级合并建模为双目标优化问题，平衡跨任务性能和存储效率，并构建可重用模块专家库，通过轻量路由网络动态重组模块。
- 实验或效果：在多种模型规模、任务类型和微调策略下，MERGE持续优于基线方法，并有效泛化。

## 摘要（原文）

> Model merging constructs versatile models by integrating task-specific models without requiring labeled data or expensive joint retraining. Although recent methods improve adaptability to heterogeneous tasks by generating customized merged models for each instance, they face two critical limitations. First, the instance-specific merged models lack reusability, restricting the exploitation of high-quality merging configurations and efficient batch inference. Second, these methods treat each task-specific model as a monolithic whole, overlooking the diverse mergeability of homologous components such as attention and multilayer perceptron layers, and the differing merging sensitivities across components. To address these limitations, we propose MERGE (\underline{M}odular \underline{E}xpert \underline{R}ecombination for fine-\underline{G}rained m\underline{E}rging), a method that enables component-wise model merging and input-aware, on-demand module recombination at inference. MERGE formulates component-wise merging as a bi-objective optimization problem that balances cross-task performance and storage efficiency, and develops a surrogate-assisted evolutionary algorithm to efficiently identify Pareto-optimal merging configurations. These high-quality configurations underpin a reusable modular expert library, from which a lightweight routing network dynamically activates and recombines modular experts to assemble input-specific models and enable efficient inference under storage constraints. Extensive experiments across various model scales, task types, and fine-tuning strategies demonstrate that MERGE consistently outperforms strong baselines and generalizes effectively.

