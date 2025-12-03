---
layout: default
title: Adapting Tensor Kernel Machines to Enable Efficient Transfer Learning for Seizure Detection
---

# Adapting Tensor Kernel Machines to Enable Efficient Transfer Learning for Seizure Detection
**arXiv**：[2512.02626v1](https://arxiv.org/abs/2512.02626) · [PDF](https://arxiv.org/pdf/2512.02626.pdf)  
**作者**：Seline J. S. de Rooij, Borbála Hunyadi  

**一句话要点**：提出自适应张量核机以在资源受限设备上实现高效癫痫检测迁移学习

**关键词**：迁移学习, 张量核机, 癫痫检测, 自适应模型, 低秩张量网络, 资源受限设备

## 3 点简述
- 核心问题：迁移学习在癫痫检测中需高效适应患者数据，但传统方法参数多、计算慢。
- 方法要点：基于自适应SVM，利用张量核机通过正则化迁移知识，在原始域学习紧凑非线性模型。
- 实验或效果：在耳后EEG数据上，患者适应模型性能优于独立和全特定模型，参数减少约100倍，推理更快。

## 摘要（原文）

> Transfer learning aims to optimize performance in a target task by learning from a related source problem. In this work, we propose an efficient transfer learning method using a tensor kernel machine. Our method takes inspiration from the adaptive SVM and hence transfers 'knowledge' from the source to the 'adapted' model via regularization. The main advantage of using tensor kernel machines is that they leverage low-rank tensor networks to learn a compact non-linear model in the primal domain. This allows for a more efficient adaptation without adding more parameters to the model. To demonstrate the effectiveness of our approach, we apply the adaptive tensor kernel machine (Adapt-TKM) to seizure detection on behind-the-ear EEG. By personalizing patient-independent models with a small amount of patient-specific data, the patient-adapted model (which utilizes the Adapt-TKM), achieves better performance compared to the patient-independent and fully patient-specific models. Notably, it is able to do so while requiring around 100 times fewer parameters than the adaptive SVM model, leading to a correspondingly faster inference speed. This makes the Adapt-TKM especially useful for resource-constrained wearable devices.

