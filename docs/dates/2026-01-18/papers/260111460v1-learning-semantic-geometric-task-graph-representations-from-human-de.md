---
layout: default
title: Learning Semantic-Geometric Task Graph-Representations from Human Demonstrations
---

# Learning Semantic-Geometric Task Graph-Representations from Human Demonstrations
**arXiv**：[2601.11460v1](https://arxiv.org/abs/2601.11460) · [PDF](https://arxiv.org/pdf/2601.11460.pdf)  
**作者**：Franziska Herbert, Vignesh Prasad, Han Liu, Dorothea Koert, Georgia Chalvatzaki  

**一句话要点**：提出语义几何任务图表示，从人类演示中学习结构化任务表示以支持长时程操作推理。

**关键词**：任务图表示, 语义几何学习, 人类演示, 双臂操作, 长时程推理, Transformer解码器

## 3 点简述
- 核心问题：如何从人类演示中联合捕获任务的离散语义结构和对象几何关系的时序演化，以支持长时程操作任务的理解。
- 方法要点：结合MPNN编码器和Transformer解码器，学习语义几何任务图表示，分离场景表示学习和动作条件推理。
- 实验或效果：在人类演示数据集上验证表示有效性，并成功迁移到物理双臂机器人进行在线动作选择。

## 摘要（原文）

> Learning structured task representations from human demonstrations is essential for understanding long-horizon manipulation behaviors, particularly in bimanual settings where action ordering, object involvement, and interaction geometry can vary significantly. A key challenge lies in jointly capturing the discrete semantic structure of tasks and the temporal evolution of object-centric geometric relations in a form that supports reasoning over task progression. In this work, we introduce a semantic-geometric task graph-representation that encodes object identities, inter-object relations, and their temporal geometric evolution from human demonstrations. Building on this formulation, we propose a learning framework that combines a Message Passing Neural Network (MPNN) encoder with a Transformer-based decoder, decoupling scene representation learning from action-conditioned reasoning about task progression. The encoder operates solely on temporal scene graphs to learn structured representations, while the decoder conditions on action-context to predict future action sequences, associated objects, and object motions over extended time horizons. Through extensive evaluation on human demonstration datasets, we show that semantic-geometric task graph-representations are particularly beneficial for tasks with high action and object variability, where simpler sequence-based models struggle to capture task progression. Finally, we demonstrate that task graph representations can be transferred to a physical bimanual robot and used for online action selection, highlighting their potential as reusable task abstractions for downstream decision-making in manipulation systems.

