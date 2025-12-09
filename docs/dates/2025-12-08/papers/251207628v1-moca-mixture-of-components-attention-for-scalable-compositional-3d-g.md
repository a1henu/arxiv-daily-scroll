---
layout: default
title: MoCA: Mixture-of-Components Attention for Scalable Compositional 3D Generation
---

# MoCA: Mixture-of-Components Attention for Scalable Compositional 3D Generation
**arXiv**：[2512.07628v1](https://arxiv.org/abs/2512.07628) · [PDF](https://arxiv.org/pdf/2512.07628.pdf)  
**作者**：Zhiqi Li, Wenhuan Li, Tengfei Wang, Zhenwei Wang, Junta Wu, Haoyuan Wang, Yunhan Yang, Zehuan Huang, Yang Li, Peidong Liu, Chunchao Guo  

**一句话要点**：提出MoCA注意力机制以解决组合式3D生成中全局注意力计算成本高的问题

**关键词**：组合式3D生成, 注意力机制, 可扩展性, 稀疏全局注意力, 组件路由, 计算优化

## 3 点简述
- 核心问题：组合式3D生成方法在增加组件数量时，全局注意力计算成本呈二次增长，导致可扩展性差。
- 方法要点：设计重要性组件路由选择top-k相关组件进行稀疏全局注意力，并对未选组件进行压缩以保留上下文先验。
- 实验或效果：在组合式物体和场景生成任务上，MoCA优于基线方法，支持高效、细粒度的3D资产创建。

## 摘要（原文）

> Compositionality is critical for 3D object and scene generation, but existing part-aware 3D generation methods suffer from poor scalability due to quadratic global attention costs when increasing the number of components. In this work, we present MoCA, a compositional 3D generative model with two key designs: (1) importance-based component routing that selects top-k relevant components for sparse global attention, and (2) unimportant components compression that preserve contextual priors of unselected components while reducing computational complexity of global attention. With these designs, MoCA enables efficient, fine-grained compositional 3D asset creation with scalable number of components. Extensive experiments show MoCA outperforms baselines on both compositional object and scene generation tasks. Project page: https://lizhiqi49.github.io/MoCA

