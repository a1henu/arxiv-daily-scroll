---
layout: default
title: Topology-Guaranteed Image Segmentation: Enforcing Connectivity, Genus, and Width Constraints
---

# Topology-Guaranteed Image Segmentation: Enforcing Connectivity, Genus, and Width Constraints
**arXiv**：[2601.11409v1](https://arxiv.org/abs/2601.11409) · [PDF](https://arxiv.org/pdf/2601.11409.pdf)  
**作者**：Wenxiao Li, Xue-Cheng Tai, Jun Liu  

**一句话要点**：提出整合宽度信息的拓扑框架，以增强图像分割中的连通性和亏格保持能力。

**关键词**：图像分割, 拓扑约束, 持续同调, 变分模型, 宽度属性, 神经网络

## 3 点简述
- 现有拓扑方法缺乏宽度信息，限制分割结构如厚度和长度的准确捕捉。
- 结合持续同调和PDE平滑，修改上水平集极值，使拓扑结构自然包含宽度属性。
- 通过变分约束和神经网络，实验验证方法能有效保持拓扑不变性和宽度特征。

## 摘要（原文）

> Existing research highlights the crucial role of topological priors in image segmentation, particularly in preserving essential structures such as connectivity and genus. Accurately capturing these topological features often requires incorporating width-related information, including the thickness and length inherent to the image structures. However, traditional mathematical definitions of topological structures lack this dimensional width information, limiting methods like persistent homology from fully addressing practical segmentation needs. To overcome this limitation, we propose a novel mathematical framework that explicitly integrates width information into the characterization of topological structures. This method leverages persistent homology, complemented by smoothing concepts from partial differential equations (PDEs), to modify local extrema of upper-level sets. This approach enables the resulting topological structures to inherently capture width properties. We incorporate this enhanced topological description into variational image segmentation models. Using some proper loss functions, we are also able to design neural networks that can segment images with the required topological and width properties. Through variational constraints on the relevant topological energies, our approach successfully preserves essential topological invariants such as connectivity and genus counts, simultaneously ensuring that segmented structures retain critical width attributes, including line thickness and length. Numerical experiments demonstrate the effectiveness of our method, showcasing its capability to maintain topological fidelity while explicitly embedding width characteristics into segmented image structures.

