---
layout: default
title: Borrowing from anything: A generalizable framework for reference-guided instance editing
---

# Borrowing from anything: A generalizable framework for reference-guided instance editing
**arXiv**：[2512.15138v1](https://arxiv.org/abs/2512.15138) · [PDF](https://arxiv.org/pdf/2512.15138.pdf)  
**作者**：Shengxiao Zhou, Chenghua Li, Jianhao Huang, Qinghao Hu, Yifan Zhang  

**一句话要点**：提出GENIE框架以解决参考引导实例编辑中的语义纠缠问题

**关键词**：实例编辑, 语义解缠, 参考引导, 空间对齐, 注意力融合

## 3 点简述
- 核心问题：参考图像的内在外观与外在属性语义纠缠，限制编辑效果
- 方法要点：通过空间对齐、自适应残差缩放和渐进注意力融合实现显式解缠
- 实验或效果：在AnyInsertion数据集上达到最先进的保真度和鲁棒性

## 摘要（原文）

> Reference-guided instance editing is fundamentally limited by semantic entanglement, where a reference's intrinsic appearance is intertwined with its extrinsic attributes. The key challenge lies in disentangling what information should be borrowed from the reference, and determining how to apply it appropriately to the target. To tackle this challenge, we propose GENIE, a Generalizable Instance Editing framework capable of achieving explicit disentanglement. GENIE first corrects spatial misalignments with a Spatial Alignment Module (SAM). Then, an Adaptive Residual Scaling Module (ARSM) learns what to borrow by amplifying salient intrinsic cues while suppressing extrinsic attributes, while a Progressive Attention Fusion (PAF) mechanism learns how to render this appearance onto the target, preserving its structure. Extensive experiments on the challenging AnyInsertion dataset demonstrate that GENIE achieves state-of-the-art fidelity and robustness, setting a new standard for disentanglement-based instance editing.

