---
layout: default
title: ProGS: Towards Progressive Coding for 3D Gaussian Splatting
---

# ProGS: Towards Progressive Coding for 3D Gaussian Splatting
**arXiv**：[2603.09703v1](https://arxiv.org/abs/2603.09703) · [PDF](https://arxiv.org/pdf/2603.09703.pdf)  
**作者**：Zhiye Tang, Lingzhuo Liu, Shengjie Jiao, Qiudan Zhang, Junhui Hou, You Yang, Xu Wang  

**一句话要点**：提出ProGS渐进编码方法，以解决3D高斯泼溅数据在流媒体应用中的压缩与传输问题。

**关键词**：3D高斯泼溅, 渐进编码, 八叉树压缩, 流媒体传输, 视觉保真度

## 3 点简述
- 核心问题：现有3D高斯泼溅压缩方法不支持渐进编码，难以适应流媒体带宽变化。
- 方法要点：基于八叉树结构组织数据，引入互信息增强机制减少冗余，实现高效渐进编码。
- 实验或效果：相比原始格式，存储减少45倍，视觉性能提升超10%，支持实时应用。

## 摘要（原文）

> With the emergence of 3D Gaussian Splatting (3DGS), numerous pioneering efforts have been made to address the effective compression issue of massive 3DGS data. 3DGS offers an efficient and scalable representation of 3D scenes by utilizing learnable 3D Gaussians, but the large size of the generated data has posed significant challenges for storage and transmission. Existing methods, however, have been limited by their inability to support progressive coding, a crucial feature in streaming applications with varying bandwidth. To tackle this limitation, this paper introduce a novel approach that organizes 3DGS data into an octree structure, enabling efficient progressive coding. The proposed ProGS is a streaming-friendly codec that facilitates progressive coding for 3D Gaussian splatting, and significantly improves both compression efficiency and visual fidelity. The proposed method incorporates mutual information enhancement mechanisms to mitigate structural redundancy, leveraging the relevance between nodes in the octree hierarchy. By adapting the octree structure and dynamically adjusting the anchor nodes, ProGS ensures scalable data compression without compromising the rendering quality. ProGS achieves a remarkable 45X reduction in file storage compared to the original 3DGS format, while simultaneously improving visual performance by over 10%. This demonstrates that ProGS can provide a robust solution for real-time applications with varying network conditions.

