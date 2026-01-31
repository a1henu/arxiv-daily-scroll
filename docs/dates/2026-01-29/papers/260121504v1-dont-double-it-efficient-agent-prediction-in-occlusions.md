---
layout: default
title: Don't double it: Efficient Agent Prediction in Occlusions
---

# Don't double it: Efficient Agent Prediction in Occlusions
**arXiv**：[2601.21504v1](https://arxiv.org/abs/2601.21504) · [PDF](https://arxiv.org/pdf/2601.21504.pdf)  
**作者**：Anna Rothenhäusler, Markus Mazzola, Andreas Look, Raghu Rajan, Joschka Bödecker  

**一句话要点**：提出MatchInformer方法，通过匈牙利匹配和轨迹解耦，提升自动驾驶中遮挡交通代理的预测效率与准确性。

**关键词**：遮挡预测, 匈牙利匹配, 轨迹解耦, 自动驾驶, Transformer架构, MCC评估

## 3 点简述
- 核心问题：遮挡交通代理预测中，现有方法常产生冗余预测，增加计算负担并影响下游规划。
- 方法要点：基于SceneInformer架构，集成匈牙利匹配确保预测与真值一对一对应，并解耦代理朝向与运动以优化轨迹预测。
- 实验或效果：在Waymo Open Motion Dataset上验证，改进遮挡区域推理，提升轨迹预测准确性，使用MCC评估处理类别不平衡。

## 摘要（原文）

> Occluded traffic agents pose a significant challenge for autonomous vehicles, as hidden pedestrians or vehicles can appear unexpectedly, yet this problem remains understudied. Existing learning-based methods, while capable of inferring the presence of hidden agents, often produce redundant occupancy predictions where a single agent is identified multiple times. This issue complicates downstream planning and increases computational load. To address this, we introduce MatchInformer, a novel transformer-based approach that builds on the state-of-the-art SceneInformer architecture. Our method improves upon prior work by integrating Hungarian Matching, a state-of-the-art object matching algorithm from object detection, into the training process to enforce a one-to-one correspondence between predictions and ground truth, thereby reducing redundancy. We further refine trajectory forecasts by decoupling an agent's heading from its motion, a strategy that improves the accuracy and interpretability of predicted paths. To better handle class imbalances, we propose using the Matthews Correlation Coefficient (MCC) to evaluate occupancy predictions. By considering all entries in the confusion matrix, MCC provides a robust measure even in sparse or imbalanced scenarios. Experiments on the Waymo Open Motion Dataset demonstrate that our approach improves reasoning about occluded regions and produces more accurate trajectory forecasts than prior methods.

