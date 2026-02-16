---
layout: default
title: SPRig: Self-Supervised Pose-Invariant Rigging from Mesh Sequences
---

# SPRig: Self-Supervised Pose-Invariant Rigging from Mesh Sequences
**arXiv**：[2602.12740v1](https://arxiv.org/abs/2602.12740) · [PDF](https://arxiv.org/pdf/2602.12740.pdf)  
**作者**：Ruipeng Wang, Langkun Zhong, Miaowei Wang  

**一句话要点**：提出SPRig框架，通过跨帧一致性损失学习姿态不变的绑定，解决序列数据中缺乏标准姿态的绑定问题。

**关键词**：姿态不变绑定, 自监督学习, 网格序列, 跨帧一致性, 时间稳定性

## 3 点简述
- 核心问题：现有绑定方法依赖标准姿态，在序列数据中导致姿态依赖和拓扑不一致。
- 方法要点：基于现有模型，引入跨帧一致性损失进行微调，实现姿态不变的绑定学习。
- 实验或效果：验证显示方法在时间稳定性上达到SOTA，减少基线方法的伪影，代码将公开。

## 摘要（原文）

> State-of-the-art rigging methods assume a canonical rest pose--an assumption that fails for sequential data (e.g., animal motion capture or AIGC/video-derived mesh sequences) that lack the T-pose. Applied frame-by-frame, these methods are not pose-invariant and produce topological inconsistencies across frames. Thus We propose SPRig, a general fine-tuning framework that enforces cross-frame consistency losses to learn pose-invariant rigs on top of existing models. We validate our approach on rigging using a new permutation-invariant stability protocol. Experiments demonstrate SOTA temporal stability: our method produces coherent rigs from challenging sequences and dramatically reduces the artifacts that plague baseline methods. The code will be released publicly upon acceptance.

