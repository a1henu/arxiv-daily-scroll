---
layout: default
title: Axe: A Simple Unified Layout Abstraction for Machine Learning Compilers
---

# Axe: A Simple Unified Layout Abstraction for Machine Learning Compilers
**arXiv**：[2601.19092v1](https://arxiv.org/abs/2601.19092) · [PDF](https://arxiv.org/pdf/2601.19092.pdf)  
**作者**：Bohan Hou, Hongyi Jin, Guanjie Wang, Jinqi Chen, Yaxing Cai, Lijie Yang, Zihao Ye, Yaoyao Ding, Ruihang Lai, Tianqi Chen  

**一句话要点**：提出Axe布局抽象以统一机器学习编译中的跨设备和设备内布局映射

**关键词**：机器学习编译, 布局抽象, 张量映射, 异构加速, 性能优化, 统一布局

## 3 点简述
- 核心问题：现代深度学习工作负载需协调数据和计算在设备网格、内存层次和异构加速器上的放置
- 方法要点：Axe布局通过命名轴将逻辑张量坐标映射到多轴物理空间，统一分块、分片、复制和偏移
- 实验或效果：实验显示统一方法在最新GPU、多设备环境和加速器后端上接近手动调优内核性能

## 摘要（原文）

> Scaling modern deep learning workloads demands coordinated placement of data and compute across device meshes, memory hierarchies, and heterogeneous accelerators. We present Axe Layout, a hardware-aware abstraction that maps logical tensor coordinates to a multi-axis physical space via named axes. Axe unifies tiling, sharding, replication, and offsets across inter-device distribution and on-device layouts, enabling collective primitives to be expressed consistently from device meshes to threads. Building on Axe, we design a multi-granularity, distribution-aware DSL and compiler that composes thread-local control with collective operators in a single kernel. Experiments show that our unified approach can bring performance close to hand-tuned kernels on across latest GPU devices and multi-device environments and accelerator backends.

