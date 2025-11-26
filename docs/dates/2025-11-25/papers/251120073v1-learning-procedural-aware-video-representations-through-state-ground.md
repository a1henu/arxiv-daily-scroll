---
layout: default
title: Learning Procedural-aware Video Representations through State-Grounded Hierarchy Unfolding
---

# Learning Procedural-aware Video Representations through State-Grounded Hierarchy Unfolding
**arXiv**：[2511.20073v1](https://arxiv.org/abs/2511.20073) · [PDF](https://arxiv.org/pdf/2511.20073.pdf)  
**作者**：Jinghan Zhao, Yifei Huang, Feng Lu  

**一句话要点**：提出任务-步骤-状态框架，通过状态监督提升程序感知视频表示学习

**关键词**：程序感知视频表示, 状态监督, 层次结构展开, 渐进预训练, 任务识别, 步骤预测

## 3 点简述
- 核心问题：现有方法中任务和步骤描述与视觉细节对齐不稳健，影响程序语义注入。
- 方法要点：引入状态作为视觉基础语义层，采用渐进预训练策略展开层次结构。
- 实验或效果：在COIN和CrossTask数据集上，任务识别等下游任务性能优于基线。

## 摘要（原文）

> Learning procedural-aware video representations is a key step towards building agents that can reason about and execute complex tasks. Existing methods typically address this problem by aligning visual content with textual descriptions at the task and step levels to inject procedural semantics into video representations. However, due to their high level of abstraction, 'task' and 'step' descriptions fail to form a robust alignment with the concrete, observable details in visual data. To address this, we introduce 'states', i.e., textual snapshots of object configurations, as a visually-grounded semantic layer that anchors abstract procedures to what a model can actually see. We formalize this insight in a novel Task-Step-State (TSS) framework, where tasks are achieved via steps that drive transitions between observable states. To enforce this structure, we propose a progressive pre-training strategy that unfolds the TSS hierarchy, forcing the model to ground representations in states while associating them with steps and high-level tasks. Extensive experiments on the COIN and CrossTask datasets show that our method outperforms baseline models on multiple downstream tasks, including task recognition, step recognition, and next step prediction. Ablation studies show that introducing state supervision is a key driver of performance gains across all tasks. Additionally, our progressive pretraining strategy proves more effective than standard joint training, as it better enforces the intended hierarchical structure.

