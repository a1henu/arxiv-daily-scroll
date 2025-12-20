---
layout: default
title: Semi-Supervised Online Learning on the Edge by Transforming Knowledge from Teacher Models
---

# Semi-Supervised Online Learning on the Edge by Transforming Knowledge from Teacher Models
**arXiv**：[2512.16866v1](https://arxiv.org/abs/2512.16866) · [PDF](https://arxiv.org/pdf/2512.16866.pdf)  
**作者**：Jiabin Xue  

**一句话要点**：提出知识转换方法，通过教师模型生成伪标签，解决边缘在线学习中未来数据标注难题。

**关键词**：边缘机器学习, 在线学习, 知识蒸馏, 主动学习, 伪标签生成, 因果推理

## 3 点简述
- 核心问题：边缘在线学习中如何为未来未见数据确定标签，以应对动态环境。
- 方法要点：结合知识蒸馏、主动学习和因果推理，教师模型作为预言机生成伪标签训练学生模型。
- 实验效果：模拟实验显示，稳定教师模型下学生模型可达到预期最大性能，适用于教师任务通用或学生标签获取困难的场景。

## 摘要（原文）

> Edge machine learning (Edge ML) enables training ML models using the vast data distributed across network edges. However, many existing approaches assume static models trained centrally and then deployed, making them ineffective against unseen data. To address this, Online Edge ML allows models to be trained directly on edge devices and updated continuously with new data. This paper explores a key challenge of Online Edge ML: "How to determine labels for truly future, unseen data points". We propose Knowledge Transformation (KT), a hybrid method combining Knowledge Distillation, Active Learning, and causal reasoning. In short, KT acts as the oracle in active learning by transforming knowledge from a teacher model to generate pseudo-labels for training a student model. To verify the validity of the method, we conducted simulation experiments with two setups: (1) using a less stable teacher model and (2) a relatively more stable teacher model. Results indicate that when a stable teacher model is given, the student model can eventually reach its expected maximum performance. KT is potentially beneficial for scenarios that meet the following circumstances: (1) when the teacher's task is generic, which means existing pre-trained models might be adequate for its task, so there will be no need to train the teacher model from scratch; and/or (2) when the label for the student's task is difficult or expensive to acquire.

