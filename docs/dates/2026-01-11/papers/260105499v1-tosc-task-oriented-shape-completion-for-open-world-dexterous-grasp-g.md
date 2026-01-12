---
layout: default
title: TOSC: Task-Oriented Shape Completion for Open-World Dexterous Grasp Generation from Partial Point Clouds
---

# TOSC: Task-Oriented Shape Completion for Open-World Dexterous Grasp Generation from Partial Point Clouds
**arXiv**：[2601.05499v1](https://arxiv.org/abs/2601.05499) · [PDF](https://arxiv.org/pdf/2601.05499.pdf)  
**作者**：Weishang Wu, Yifei Shi, Zhiping Cai  

**一句话要点**：提出任务导向形状补全方法，以解决开放世界灵巧抓取中严重部分观测下的形状补全问题。

**关键词**：任务导向形状补全, 灵巧抓取生成, 部分点云, 开放世界对象, 零样本功能理解, 条件流匹配模型

## 3 点简述
- 核心问题：严重部分观测下，通用形状补全失效，影响任务导向灵巧抓取。
- 方法要点：利用预训练基础模型生成任务导向补全候选，通过3D判别自编码器优化最合理候选。
- 实验或效果：在任务导向灵巧抓取和形状补全上达到SOTA，提升抓取位移和Chamfer距离，并展示良好泛化能力。

## 摘要（原文）

> Task-oriented dexterous grasping remains challenging in robotic manipulations of open-world objects under severe partial observation, where significant missing data invalidates generic shape completion. In this paper, to overcome this limitation, we study Task-Oriented Shape Completion, a new task that focuses on completing the potential contact regions rather than the entire shape. We argue that shape completion for grasping should be explicitly guided by the downstream manipulation task. To achieve this, we first generate multiple task-oriented shape completion candidates by leveraging the zero-shot capabilities of object functional understanding from several pre-trained foundation models. A 3D discriminative autoencoder is then proposed to evaluate the plausibility of each generated candidate and optimize the most plausible one from a global perspective. A conditional flow-matching model named FlowGrasp is developed to generate task-oriented dexterous grasps from the optimized shape. Our method achieves state-of-the-art performance in task-oriented dexterous grasping and task-oriented shape completion, improving the Grasp Displacement and the Chamfer Distance over the state-of-the-art by 16.17\% and 55.26%, respectively. In particular, it shows good capabilities in grasping objects with severe missing data. It also demonstrates good generality in handling open-set categories and tasks.

