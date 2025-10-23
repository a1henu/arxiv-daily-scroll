---
layout: default
title: Using Temperature Sampling to Effectively Train Robot Learning Policies on Imbalanced Datasets
---

# Using Temperature Sampling to Effectively Train Robot Learning Policies on Imbalanced Datasets
**arXiv**：[2510.19373v1](https://arxiv.org/abs/2510.19373) · [PDF](https://arxiv.org/pdf/2510.19373.pdf)  
**作者**：Basavasagar Patil, Sydney Belt, Jayjun Lee, Nima Fazeli, Bernadette Bucher  

**一句话要点**：提出温度采样方法以解决机器人学习策略在数据集不平衡时的泛化问题

**关键词**：机器人学习, 数据集不平衡, 采样策略, 策略训练, 泛化提升

## 3 点简述
- 机器人数据集因任务相似导致动作序列不平衡，影响模型训练
- 采用简单采样策略，易于集成代码库，提升泛化能力
- 实验显示在低资源任务中性能显著提升，高资源任务无退化

## 摘要（原文）

> Increasingly large datasets of robot actions and sensory observations are
> being collected to train ever-larger neural networks. These datasets are
> collected based on tasks and while these tasks may be distinct in their
> descriptions, many involve very similar physical action sequences (e.g., 'pick
> up an apple' versus 'pick up an orange'). As a result, many datasets of robotic
> tasks are substantially imbalanced in terms of the physical robotic actions
> they represent. In this work, we propose a simple sampling strategy for policy
> training that mitigates this imbalance. Our method requires only a few lines of
> code to integrate into existing codebases and improves generalization. We
> evaluate our method in both pre-training small models and fine-tuning large
> foundational models. Our results show substantial improvements on low-resource
> tasks compared to prior state-of-the-art methods, without degrading performance
> on high-resource tasks. This enables more effective use of model capacity for
> multi-task policies. We also further validate our approach in a real-world
> setup on a Franka Panda robot arm across a diverse set of tasks.

