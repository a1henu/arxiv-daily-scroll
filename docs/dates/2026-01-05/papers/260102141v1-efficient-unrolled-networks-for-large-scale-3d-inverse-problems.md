---
layout: default
title: Efficient Unrolled Networks for Large-Scale 3D Inverse Problems
---

# Efficient Unrolled Networks for Large-Scale 3D Inverse Problems
**arXiv**：[2601.02141v1](https://arxiv.org/abs/2601.02141) · [PDF](https://arxiv.org/pdf/2601.02141.pdf)  
**作者**：Romain Vo, Julián Tachella  

**一句话要点**：提出域划分策略与正规算子近似，以解决大规模3D逆问题中内存限制问题。

**关键词**：3D逆问题, 深度展开网络, 域划分策略, 正规算子近似, 端到端重建, 单GPU训练

## 3 点简述
- 核心问题：大规模3D成像中，全局前向算子内存需求过高，阻碍网络架构整合。
- 方法要点：采用域划分策略和正规算子近似，实现端到端重建模型训练。
- 实验或效果：在3D X射线锥束断层扫描和3D多线圈加速MRI上达到先进性能，仅需单GPU。

## 摘要（原文）

> Deep learning-based methods have revolutionized the field of imaging inverse problems, yielding state-of-the-art performance across various imaging domains. The best performing networks incorporate the imaging operator within the network architecture, typically in the form of deep unrolling. However, in large-scale problems, such as 3D imaging, most existing methods fail to incorporate the operator in the architecture due to the prohibitive amount of memory required by global forward operators, which hinder typical patching strategies. In this work, we present a domain partitioning strategy and normal operator approximations that enable the training of end-to-end reconstruction models incorporating forward operators of arbitrarily large problems into their architecture. The proposed method achieves state-of-the-art performance on 3D X-ray cone-beam tomography and 3D multi-coil accelerated MRI, while requiring only a single GPU for both training and inference.

