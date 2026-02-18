---
layout: default
title: ExpertWeaver: Unlocking the Inherent MoE in Dense LLMs with GLU Activation Patterns
---

# ExpertWeaver: Unlocking the Inherent MoE in Dense LLMs with GLU Activation Patterns
**arXiv**：[2602.15521v1](https://arxiv.org/abs/2602.15521) · [PDF](https://arxiv.org/pdf/2602.15521.pdf)  
**作者**：Ziyu Zhao, Tong Zhu, Zhi Zhang, Tiantian Fan, Jinluan Yang, Kun Kuang, Zhongyu Wei, Fei Wu, Yu Cheng  

**一句话要点**：提出ExpertWeaver框架，利用GLU激活模式解锁稠密LLM中的固有MoE结构

**关键词**：稠密转MoE, GLU激活模式, 专家构建, 训练免费框架, 动态结构剪枝, 降循环初始化

## 3 点简述
- 核心问题：现有稠密转MoE方法破坏模型内在激活模式，导致专家构建不优
- 方法要点：基于GLU激活模式划分神经元，构建共享专家和路由专家，无需训练
- 实验或效果：在动态结构剪枝和降循环初始化中显著优于现有方法

## 摘要（原文）

> Mixture-of-Experts (MoE) effectively scales model capacity while preserving computational efficiency through sparse expert activation. However, training high-quality MoEs from scratch is prohibitively expensive. A promising alternative is to convert pretrained dense models into sparse MoEs. Existing dense-to-MoE methods fall into two categories: \textbf{dynamic structural pruning} that converts dense models into MoE architectures with moderate sparsity to balance performance and inference efficiency, and \textbf{downcycling} approaches that use pretrained dense models to initialize highly sparse MoE architectures. However, existing methods break the intrinsic activation patterns within dense models, leading to suboptimal expert construction. In this work, we argue that the Gated Linear Unit (GLU) mechanism provides a natural blueprint for dense-to-MoE conversion. We show that the fine-grained neural-wise activation patterns of GLU reveal a coarse-grained structure, uncovering an inherent MoE architecture composed of consistently activated universal neurons and dynamically activated specialized neurons. Leveraging this discovery, we introduce ExpertWeaver, a training-free framework that partitions neurons according to their activation patterns and constructs shared experts and specialized routed experts with layer-adaptive configurations. Our experiments demonstrate that ExpertWeaver significantly outperforms existing methods, both as a training-free dynamic structural pruning technique and as a downcycling strategy for superior MoE initialization.

