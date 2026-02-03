---
layout: default
title: Optimizing Tensor Train Decomposition in DNNs for RISC-V Architectures Using Design Space Exploration and Compiler Optimizations
---

# Optimizing Tensor Train Decomposition in DNNs for RISC-V Architectures Using Design Space Exploration and Compiler Optimizations
**arXiv**：[2602.01996v1](https://arxiv.org/abs/2602.01996) · [PDF](https://arxiv.org/pdf/2602.01996.pdf)  
**作者**：Theologos Anthimopoulos, Milad Kokhazadeh, Vasilios Kelefouras, Benjamin Himpel, Georgios Keramidas  

**一句话要点**：提出基于设计空间探索和编译器优化的张量列车分解方法，以优化RISC-V架构上DNN全连接层部署。

**关键词**：张量列车分解, 设计空间探索, 编译器优化, RISC-V架构, 全连接层压缩, 边缘计算

## 3 点简述
- 核心问题：DNN全连接层在RISC-V等资源受限设备上部署时面临高计算和内存需求挑战。
- 方法要点：通过张量列车分解压缩全连接层，结合设计空间剪枝和编译器优化提升性能。
- 实验或效果：在相同压缩模型上，优化后层比IREE快3倍，比Pluto快8倍。

## 摘要（原文）

> Deep neural networks (DNNs) have become indispensable in many real-life applications like natural language processing, and autonomous systems. However, deploying DNNs on resource-constrained devices, e.g., in RISC-V platforms, remains challenging due to the high computational and memory demands of fully connected (FC) layers, which dominate resource consumption. Low-rank factorization (LRF) offers an effective approach to compressing FC layers, but the vast design space of LRF solutions involves complex trade-offs among FLOPs, memory size, inference time, and accuracy, making the LRF process complex and time-consuming. This paper introduces an end-to-end LRF design space exploration methodology and a specialized design tool for optimizing FC layers on RISC-V processors. Using Tensor Train Decomposition (TTD) offered by TensorFlow T3F library, the proposed work prunes the LRF design space by excluding first, inefficient decomposition shapes and second, solutions with poor inference performance on RISC-V architectures. Compiler optimizations are then applied to enhance custom T3F layer performance, minimizing inference time and boosting computational efficiency. On average, our TT-decomposed layers run 3x faster than IREE and 8x faster than Pluto on the same compressed model. This work provides an efficient solution for deploying DNNs on edge and embedded devices powered by RISC-V architectures.

