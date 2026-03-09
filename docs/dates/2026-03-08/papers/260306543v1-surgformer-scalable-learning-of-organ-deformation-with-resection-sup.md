---
layout: default
title: SurgFormer: Scalable Learning of Organ Deformation with Resection Support and Real-Time Inference
---

# SurgFormer: Scalable Learning of Organ Deformation with Resection Support and Real-Time Inference
**arXiv**：[2603.06543v1](https://arxiv.org/abs/2603.06543) · [PDF](https://arxiv.org/pdf/2603.06543.pdf)  
**作者**：Ashkan Shahbazi, Elaheh Akbari, Kyvia Pereira, Jon S. Heiselman, Annie C. Benson, Garrison L. H. Johnston, Jie Ying Wu, Nabil Simaan, Michael I. Miga, Soheil Kolouri  

**一句话要点**：提出SurgFormer以解决软组织变形模拟中高保真求解器计算成本高的问题，支持实时推理与切除条件模拟。

**关键词**：软组织变形模拟, 多分辨率Transformer, 切除条件模拟, 实时推理, 体积网格, XFEM监督

## 3 点简述
- 核心问题：高保真生物力学求解器计算成本高，难以用于交互式软组织变形模拟。
- 方法要点：基于多分辨率门控Transformer，通过局部消息传递、全局自注意力和前馈更新，自适应整合信息，并引入切除嵌入处理拓扑变化。
- 实验或效果：在统一协议生成的胆囊切除术和阑尾切除术数据集上，SurgFormer实现高精度与高效率，优于多种基线方法。

## 摘要（原文）

> We introduce SurgFormer, a multiresolution gated transformer for data driven soft tissue simulation on volumetric meshes. High fidelity biomechanical solvers are often too costly for interactive use, so we train SurgFormer on solver generated data to predict nodewise displacement fields at near real time rates. SurgFormer builds a fixed mesh hierarchy and applies repeated multibranch blocks that combine local message passing, coarse global self attention, and pointwise feedforward updates, fused by learned per node, per channel gates to adaptively integrate local and long range information while remaining scalable on large meshes. For cut conditioned simulation, resection information is encoded as a learned cut embedding and provided as an additional input, enabling a unified model for both standard deformation prediction and topology altering cases. We also introduce two surgical simulation datasets generated under a unified protocol with XFEM based supervision: a cholecystectomy resection dataset and an appendectomy manipulation and resection dataset with cut and uncut cases. To our knowledge, this is the first learned volumetric surrogate setting to study XFEM supervised cut conditioned deformation within the same volumetric pipeline as standard deformation prediction. Across diverse baselines, SurgFormer achieves strong accuracy with favorable efficiency, making it a practical backbone for both tasks. {Code, data, and project page: \href{https://mint-vu.github.io/SurgFormer/}{available here}}

