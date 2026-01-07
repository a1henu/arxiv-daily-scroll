---
layout: default
title: On the Intrinsic Limits of Transformer Image Embeddings in Non-Solvable Spatial Reasoning
---

# On the Intrinsic Limits of Transformer Image Embeddings in Non-Solvable Spatial Reasoning
**arXiv**：[2601.03048v1](https://arxiv.org/abs/2601.03048) · [PDF](https://arxiv.org/pdf/2601.03048.pdf)  
**作者**：Siyi Lyu, Quan Liu, Feng Yan  

**一句话要点**：提出Transformer图像嵌入在非可解空间推理中的内在复杂性边界，基于群同态与电路复杂度理论。

**关键词**：空间推理, Vision Transformers, 群同态, 电路复杂度, 非可解群, 潜在空间探测

## 3 点简述
- 核心问题：Vision Transformers在空间推理任务（如心理旋转）中系统性失败，归因于架构内在电路复杂性而非数据规模。
- 方法要点：形式化空间理解为学习群同态，证明非可解群（如SO(3)）的嵌入计算下界为NC^1-完全，而恒定深度ViTs限于TC^0。
- 实验或效果：通过潜在空间探测验证复杂性差距，显示ViT表示在非可解任务中随组合深度增加发生结构崩溃。

## 摘要（原文）

> Vision Transformers (ViTs) excel in semantic recognition but exhibit systematic failures in spatial reasoning tasks such as mental rotation. While often attributed to data scale, we propose that this limitation arises from the intrinsic circuit complexity of the architecture. We formalize spatial understanding as learning a Group Homomorphism: mapping image sequences to a latent space that preserves the algebraic structure of the underlying transformation group. We demonstrate that for non-solvable groups (e.g., the 3D rotation group $\mathrm{SO}(3)$), maintaining such a structure-preserving embedding is computationally lower-bounded by the Word Problem, which is $\mathsf{NC^1}$-complete. In contrast, we prove that constant-depth ViTs with polynomial precision are strictly bounded by $\mathsf{TC^0}$. Under the conjecture $\mathsf{TC^0} \subsetneq \mathsf{NC^1}$, we establish a complexity boundary: constant-depth ViTs fundamentally lack the logical depth to efficiently capture non-solvable spatial structures. We validate this complexity gap via latent-space probing, demonstrating that ViT representations suffer a structural collapse on non-solvable tasks as compositional depth increases.

