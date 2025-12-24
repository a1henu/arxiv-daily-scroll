---
layout: default
title: MAPI-GNN: Multi-Activation Plane Interaction Graph Neural Network for Multimodal Medical Diagnosis
---

# MAPI-GNN: Multi-Activation Plane Interaction Graph Neural Network for Multimodal Medical Diagnosis
**arXiv**：[2512.20026v1](https://arxiv.org/abs/2512.20026) · [PDF](https://arxiv.org/pdf/2512.20026.pdf)  
**作者**：Ziwei Qin, Xuhui Song, Deqing Huang, Na Qin, Jun Li  

**一句话要点**：提出MAPI-GNN以解决多模态医疗诊断中单图建模患者特异性病理关系不足的问题。

**关键词**：图神经网络, 多模态医疗诊断, 动态图构建, 语义解耦, 患者特异性建模

## 3 点简述
- 核心问题：现有图神经网络依赖单一静态图，难以建模患者特异性病理关系。
- 方法要点：通过语义解耦特征子空间学习多面图配置，动态构建激活图堆栈。
- 实验或效果：在超过1300个样本的两个任务中，显著优于现有方法。

## 摘要（原文）

> Graph neural networks are increasingly applied to multimodal medical diagnosis for their inherent relational modeling capabilities. However, their efficacy is often compromised by the prevailing reliance on a single, static graph built from indiscriminate features, hindering the ability to model patient-specific pathological relationships. To this end, the proposed Multi-Activation Plane Interaction Graph Neural Network (MAPI-GNN) reconstructs this single-graph paradigm by learning a multifaceted graph profile from semantically disentangled feature subspaces. The framework first uncovers latent graph-aware patterns via a multi-dimensional discriminator; these patterns then guide the dynamic construction of a stack of activation graphs; and this multifaceted profile is finally aggregated and contextualized by a relational fusion engine for a robust diagnosis. Extensive experiments on two diverse tasks, comprising over 1300 patient samples, demonstrate that MAPI-GNN significantly outperforms state-of-the-art methods.

