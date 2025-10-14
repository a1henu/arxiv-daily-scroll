---
layout: default
title: DTEA: Dynamic Topology Weaving and Instability-Driven Entropic Attenuation for Medical Image Segmentation
---

# DTEA: Dynamic Topology Weaving and Instability-Driven Entropic Attenuation for Medical Image Segmentation
**arXiv**：[2510.11259v1](https://arxiv.org/abs/2510.11259) · [PDF](https://arxiv.org/pdf/2510.11259.pdf)  
**作者**：Weixuan Li, Quanjun Li, Guang Yu, Song Yang, Zimeng Li, Chi-Man Pun, Yupeng Liu, Xuhang Chen  

**一句话要点**：提出DTEA模型以解决医学图像分割中结构表示不足和上下文建模弱的问题

**关键词**：医学图像分割, 动态拓扑编织, 熵扰动门控, 语义拓扑重构, 超图建模, 空间注意力

## 3 点简述
- 核心问题：现有方法在复杂临床场景中泛化能力差，结构表示和上下文建模不足
- 方法要点：引入STR模块构建动态超图建模解剖依赖，EPG模块过滤高熵通道增强空间注意力
- 实验或效果：在三个基准数据集上验证，实现更高分割精度和更好泛化性能

## 摘要（原文）

> In medical image segmentation, skip connections are used to merge global
> context and reduce the semantic gap between encoder and decoder. Current
> methods often struggle with limited structural representation and insufficient
> contextual modeling, affecting generalization in complex clinical scenarios. We
> propose the DTEA model, featuring a new skip connection framework with the
> Semantic Topology Reconfiguration (STR) and Entropic Perturbation Gating (EPG)
> modules. STR reorganizes multi-scale semantic features into a dynamic
> hypergraph to better model cross-resolution anatomical dependencies, enhancing
> structural and semantic representation. EPG assesses channel stability after
> perturbation and filters high-entropy channels to emphasize clinically
> important regions and improve spatial attention. Extensive experiments on three
> benchmark datasets show our framework achieves superior segmentation accuracy
> and better generalization across various clinical settings. The code is
> available at
> \href{https://github.com/LWX-Research/DTEA}{https://github.com/LWX-Research/DTEA}.

