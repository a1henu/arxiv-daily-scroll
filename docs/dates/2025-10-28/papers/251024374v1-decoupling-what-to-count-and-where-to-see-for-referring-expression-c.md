---
layout: default
title: Decoupling What to Count and Where to See for Referring Expression Counting
---

# Decoupling What to Count and Where to See for Referring Expression Counting
**arXiv**：[2510.24374v1](https://arxiv.org/abs/2510.24374) · [PDF](https://arxiv.org/pdf/2510.24374.pdf)  
**作者**：Yuda Zou, Zijian Zhang, Yongchao Xu  

**一句话要点**：提出W2-Net框架，通过双查询机制解决指代表达计数中的属性忽略问题。

**关键词**：指代表达计数, 双查询机制, 子类可分匹配, 视觉语言理解, 对象定位

## 3 点简述
- 核心问题：指代表达计数中，标注点位于类代表位置，导致模型忽略属性信息。
- 方法要点：引入what-to-count和where-to-see查询，分别定位对象和提取属性特征。
- 实验效果：在REC-8K数据集上，计数误差降低22.5%，定位F1提升7%。

## 摘要（原文）

> Referring Expression Counting (REC) extends class-level object counting to
> the fine-grained subclass-level, aiming to enumerate objects matching a textual
> expression that specifies both the class and distinguishing attribute. A
> fundamental challenge, however, has been overlooked: annotation points are
> typically placed on class-representative locations (e.g., heads), forcing
> models to focus on class-level features while neglecting attribute information
> from other visual regions (e.g., legs for "walking"). To address this, we
> propose W2-Net, a novel framework that explicitly decouples the problem into
> "what to count" and "where to see" via a dual-query mechanism. Specifically,
> alongside the standard what-to-count (w2c) queries that localize the object, we
> introduce dedicated where-to-see (w2s) queries. The w2s queries are guided to
> seek and extract features from attribute-specific visual regions, enabling
> precise subclass discrimination. Furthermore, we introduce Subclass Separable
> Matching (SSM), a novel matching strategy that incorporates a repulsive force
> to enhance inter-subclass separability during label assignment. W2-Net
> significantly outperforms the state-of-the-art on the REC-8K dataset, reducing
> counting error by 22.5% (validation) and 18.0% (test), and improving
> localization F1 by 7% and 8%, respectively. Code will be available.

