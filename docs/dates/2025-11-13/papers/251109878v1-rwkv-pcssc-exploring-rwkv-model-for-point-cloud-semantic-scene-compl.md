---
layout: default
title: RWKV-PCSSC: Exploring RWKV Model for Point Cloud Semantic Scene Completion
---

# RWKV-PCSSC: Exploring RWKV Model for Point Cloud Semantic Scene Completion
**arXiv**：[2511.09878v1](https://arxiv.org/abs/2511.09878) · [PDF](https://arxiv.org/pdf/2511.09878.pdf)  
**作者**：Wenzhe He, Xiaojun Chen, Wentang Chen, Hongyu Wang, Ying Liu, Ruihui Li  

**一句话要点**：提出RWKV-PCSSC以轻量化点云语义场景补全，减少模型参数与内存需求。

**关键词**：点云语义场景补全, RWKV机制, 轻量化网络, 特征恢复, 内存效率优化

## 3 点简述
- 核心问题：现有语义场景补全方法参数多、复杂度高，导致资源需求大。
- 方法要点：引入RWKV机制模块，从部分点云生成粗点云并逐步恢复特征。
- 实验效果：在多个数据集上实现SOTA，参数减少4.18倍，内存效率提升1.37倍。

## 摘要（原文）

> Semantic Scene Completion (SSC) aims to generate a complete semantic scene from an incomplete input. Existing approaches often employ dense network architectures with a high parameter count, leading to increased model complexity and resource demands. To address these limitations, we propose RWKV-PCSSC, a lightweight point cloud semantic scene completion network inspired by the Receptance Weighted Key Value (RWKV) mechanism. Specifically, we introduce a RWKV Seed Generator (RWKV-SG) module that can aggregate features from a partial point cloud to produce a coarse point cloud with coarse features. Subsequently, the point-wise feature of the point cloud is progressively restored through multiple stages of the RWKV Point Deconvolution (RWKV-PD) modules. By leveraging a compact and efficient design, our method achieves a lightweight model representation. Experimental results demonstrate that RWKV-PCSSC reduces the parameter count by 4.18$\times$ and improves memory efficiency by 1.37$\times$ compared to state-of-the-art methods PointSSC. Furthermore, our network achieves state-of-the-art performance on established indoor (SSC-PC, NYUCAD-PC) and outdoor (PointSSC) scene dataset, as well as on our proposed datasets (NYUCAD-PC-V2, 3D-FRONT-PC).

