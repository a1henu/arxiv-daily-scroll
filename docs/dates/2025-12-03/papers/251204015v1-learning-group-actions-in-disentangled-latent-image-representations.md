---
layout: default
title: Learning Group Actions In Disentangled Latent Image Representations
---

# Learning Group Actions In Disentangled Latent Image Representations
**arXiv**：[2512.04015v1](https://arxiv.org/abs/2512.04015) · [PDF](https://arxiv.org/pdf/2512.04015.pdf)  
**作者**：Farhana Hossain Swarnali, Miaomiao Zhang, Tonmoy Hossain  

**一句话要点**：提出端到端框架以自动学习潜在图像表示中的群作用，实现可控变换。

**关键词**：群作用学习, 潜在表示解耦, 端到端框架, 图像变换控制, 自动结构发现

## 3 点简述
- 核心问题：现有方法需手动划分潜在变量，难以自动学习群作用在表示空间中的变换相关结构。
- 方法要点：使用可学习二元掩码与直通估计，动态划分潜在表示，联合优化解耦与群变换映射。
- 实验或效果：在五个2D/3D图像数据集上验证，自动学习解耦潜在因子，下游分类任务确认表示有效性。

## 摘要（原文）

> Modeling group actions on latent representations enables controllable transformations of high-dimensional image data. Prior works applying group-theoretic priors or modeling transformations typically operate in the high-dimensional data space, where group actions apply uniformly across the entire input, making it difficult to disentangle the subspace that varies under transformations. While latent-space methods offer greater flexibility, they still require manual partitioning of latent variables into equivariant and invariant subspaces, limiting the ability to robustly learn and operate group actions within the representation space. To address this, we introduce a novel end-to-end framework that for the first time learns group actions on latent image manifolds, automatically discovering transformation-relevant structures without manual intervention. Our method uses learnable binary masks with straight-through estimation to dynamically partition latent representations into transformation-sensitive and invariant components. We formulate this within a unified optimization framework that jointly learns latent disentanglement and group transformation mappings. The framework can be seamlessly integrated with any standard encoder-decoder architecture. We validate our approach on five 2D/3D image datasets, demonstrating its ability to automatically learn disentangled latent factors for group actions in diverse data, while downstream classification tasks confirm the effectiveness of the learned representations. Our code is publicly available at https://github.com/farhanaswarnali/Learning-Group-Actions-In-Disentangled-Latent-Image-Representations .

