---
layout: default
title: $\text{H}^2$em: Learning Hierarchical Hyperbolic Embeddings for Compositional Zero-Shot Learning
---

# $\text{H}^2$em: Learning Hierarchical Hyperbolic Embeddings for Compositional Zero-Shot Learning
**arXiv**：[2512.20029v1](https://arxiv.org/abs/2512.20029) · [PDF](https://arxiv.org/pdf/2512.20029.pdf)  
**作者**：Lin Li, Jiahui Li, Jiaming Lei, Jun Xiao, Feifei Shao, Long Chen  

**一句话要点**：提出H2em框架，利用双曲几何学习层次嵌入以解决组合零样本学习中的层次结构建模问题。

**关键词**：组合零样本学习, 双曲几何嵌入, 层次结构建模, 双层次蕴含损失, 判别对齐损失, 跨模态注意力

## 3 点简述
- 核心问题：现有方法在欧氏空间中难以建模大规模层次结构，影响组合零样本学习的泛化能力。
- 方法要点：设计双曲几何嵌入框架，结合双层次蕴含损失和判别对齐损失，增强层次保持和细粒度区分。
- 实验或效果：在三个基准测试中实现最先进性能，适用于封闭和开放世界场景。

## 摘要（原文）

> Compositional zero-shot learning (CZSL) aims to recognize unseen state-object compositions by generalizing from a training set of their primitives (state and object). Current methods often overlook the rich hierarchical structures, such as the semantic hierarchy of primitives (e.g., apple fruit) and the conceptual hierarchy between primitives and compositions (e.g, sliced apple apple). A few recent efforts have shown effectiveness in modeling these hierarchies through loss regularization within Euclidean space. In this paper, we argue that they fail to scale to the large-scale taxonomies required for real-world CZSL: the space's polynomial volume growth in flat geometry cannot match the exponential structure, impairing generalization capacity. To this end, we propose H2em, a new framework that learns Hierarchical Hyperbolic EMbeddings for CZSL. H2em leverages the unique properties of hyperbolic geometry, a space naturally suited for embedding tree-like structures with low distortion. However, a naive hyperbolic mapping may suffer from hierarchical collapse and poor fine-grained discrimination. We further design two learning objectives to structure this space: a Dual-Hierarchical Entailment Loss that uses hyperbolic entailment cones to enforce the predefined hierarchies, and a Discriminative Alignment Loss with hard negative mining to establish a large geodesic distance between semantically similar compositions. Furthermore, we devise Hyperbolic Cross-Modal Attention to realize instance-aware cross-modal infusion within hyperbolic geometry. Extensive ablations on three benchmarks demonstrate that H2em establishes a new state-of-the-art in both closed-world and open-world scenarios. Our codes will be released.

