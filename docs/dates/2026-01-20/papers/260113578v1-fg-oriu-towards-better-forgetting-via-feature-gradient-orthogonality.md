---
layout: default
title: FG-OrIU: Towards Better Forgetting via Feature-Gradient Orthogonality for Incremental Unlearning
---

# FG-OrIU: Towards Better Forgetting via Feature-Gradient Orthogonality for Incremental Unlearning
**arXiv**：[2601.13578v1](https://arxiv.org/abs/2601.13578) · [PDF](https://arxiv.org/pdf/2601.13578.pdf)  
**作者**：Qian Feng, JiaHang Tu, Mintong Kang, Hanbin Zhao, Chao Zhang, Hui Qian  

**一句话要点**：提出FG-OrIU框架，通过特征-梯度正交性解决增量遗忘中的浅层遗忘问题

**关键词**：增量遗忘, 特征正交性, 梯度正交性, 深度遗忘, SVD分解, 动态子空间适应

## 3 点简述
- 核心问题：现有增量遗忘方法导致浅层遗忘，残留信息可恢复，影响安全与保留平衡
- 方法要点：利用SVD分解特征空间，在特征和梯度层面施加正交约束，实现深度不可逆遗忘
- 实验或效果：广泛实验验证了方法的有效性，确保遗忘与保留的稳定平衡

## 摘要（原文）

> Incremental unlearning (IU) is critical for pre-trained models to comply with sequential data deletion requests, yet existing methods primarily suppress parameters or confuse knowledge without explicit constraints on both feature and gradient level, resulting in \textit{superficial forgetting} where residual information remains recoverable. This incomplete forgetting risks security breaches and disrupts retention balance, especially in IU scenarios. We propose FG-OrIU (\textbf{F}eature-\textbf{G}radient \textbf{Or}thogonality for \textbf{I}ncremental \textbf{U}nlearning), the first framework unifying orthogonal constraints on both features and gradients level to achieve deep forgetting, where the forgetting effect is irreversible. FG-OrIU decomposes feature spaces via Singular Value Decomposition (SVD), separating forgetting and remaining class features into distinct subspaces. It then enforces dual constraints: feature orthogonal projection on both forgetting and remaining classes, while gradient orthogonal projection prevents the reintroduction of forgotten knowledge and disruption to remaining classes during updates. Additionally, dynamic subspace adaptation merges newly forgetting subspaces and contracts remaining subspaces, ensuring a stable balance between removal and retention across sequential unlearning tasks. Extensive experiments demonstrate the effectiveness of our method.

