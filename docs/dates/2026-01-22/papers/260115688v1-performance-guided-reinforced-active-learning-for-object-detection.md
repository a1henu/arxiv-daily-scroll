---
layout: default
title: Performance-guided Reinforced Active Learning for Object Detection
---

# Performance-guided Reinforced Active Learning for Object Detection
**arXiv**：[2601.15688v1](https://arxiv.org/abs/2601.15688) · [PDF](https://arxiv.org/pdf/2601.15688.pdf)  
**作者**：Zhixuan Liang, Xingyu Zeng, Rui Zhao, Ping Luo  

**一句话要点**：提出MGRAL方法，通过强化学习优化目标检测中的主动学习样本选择，以mAP提升为奖励。

**关键词**：主动学习, 目标检测, 强化学习, mAP优化, 批量选择, 性能引导

## 3 点简述
- 核心问题：现有主动学习方法评估数据信息性时未直接关联下游任务性能如mAP。
- 方法要点：利用期望模型输出变化作为信息性，采用基于策略梯度的强化学习代理进行批量样本选择。
- 实验或效果：在PASCAL VOC和COCO基准上验证，MGRAL在主动学习曲线中表现最佳，并提供了可视化支持。

## 摘要（原文）

> Active learning (AL) strategies aim to train high-performance models with minimal labeling efforts, only selecting the most informative instances for annotation. Current approaches to evaluating data informativeness predominantly focus on the data's distribution or intrinsic information content and do not directly correlate with downstream task performance, such as mean average precision (mAP) in object detection. Thus, we propose Performance-guided (i.e. mAP-guided) Reinforced Active Learning for Object Detection (MGRAL), a novel approach that leverages the concept of expected model output changes as informativeness. To address the combinatorial explosion challenge of batch sample selection and the non-differentiable correlation between model performance and selected batches, MGRAL skillfully employs a reinforcement learning-based sampling agent that optimizes selection using policy gradient with mAP improvement as reward. Moreover, to reduce the computational overhead of mAP estimation with unlabeled samples, MGRAL utilizes an unsupervised way with fast look-up tables, ensuring feasible deployment. We evaluate MGRAL's active learning performance on detection tasks over PASCAL VOC and COCO benchmarks. Our approach demonstrates the highest AL curve with convincing visualizations, establishing a new paradigm in reinforcement learning-driven active object detection.

