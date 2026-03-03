---
layout: default
title: PhysGraph: Physically-Grounded Graph-Transformer Policies for Bimanual Dexterous Hand-Tool-Object Manipulation
---

# PhysGraph: Physically-Grounded Graph-Transformer Policies for Bimanual Dexterous Hand-Tool-Object Manipulation
**arXiv**：[2603.01436v1](https://arxiv.org/abs/2603.01436) · [PDF](https://arxiv.org/pdf/2603.01436.pdf)  
**作者**：Runfa Blark Li, David Kim, Xinshuang Liu, Keito Suzuki, Dwait Bhatt, Nikola Raicevic, Xin Lin, Ki Myung Brian Lee, Nikolay Atanasov, Truong Nguyen  

**一句话要点**：提出PhysGraph，一种基于物理图变换器的策略，用于解决双手灵巧手-工具-物体操作的高维状态挑战。

**关键词**：双手灵巧操作, 图变换器, 物理偏置, 运动学图, 零样本泛化

## 3 点简述
- 核心问题：双手灵巧操作因高维状态和复杂接触动力学而困难，现有方法忽略结构信息。
- 方法要点：将系统表示为运动学图，引入每链接标记化和物理偏置生成器，以注入结构先验。
- 实验或效果：PhysGraph在精度和成功率上显著优于基线，参数更少，并展示零样本泛化能力。

## 摘要（原文）

> Bimanual dexterous manipulation for tool use remains a formidable challenge in robotics due to the high-dimensional state space and complicated contact dynamics. Existing methods naively represent the entire system state as a single configuration vector, disregarding the rich structural and topological information inherent to articulated hands. We present PhysGraph, a physically-grounded graph transformer policy designed explicitly for challenging bimanual hand-tool-object manipulation. Unlike prior works, we represent the bimanual system as a kinematic graph and introduce per-link tokenization to preserve fine-grained local state information. We propose a physically-grounded bias generator that injects structural priors directly into the attention mechanism, including kinematic spatial distance, dynamic contact states, geometric proximity, and anatomical properties. This allows the policy to explicitly reason about physical interactions rather than learning them implicitly from sparse rewards. Extensive experiments show that PhysGraph significantly outperforms baseline - ManipTrans in manipulation precision and task success rates while using only 51% of the parameters of ManipTrans. Furthermore, the inherent topological flexibility of our architecture shows qualitative zero-shot transfer to unseen tool/object geometries, and is sufficiently general to be trained on three robotic hands (Shadow, Allegro, Inspire).

