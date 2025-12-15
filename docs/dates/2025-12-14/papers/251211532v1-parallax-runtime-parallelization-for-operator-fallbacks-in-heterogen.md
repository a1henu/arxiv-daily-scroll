---
layout: default
title: Parallax: Runtime Parallelization for Operator Fallbacks in Heterogeneous Edge Systems
---

# Parallax: Runtime Parallelization for Operator Fallbacks in Heterogeneous Edge Systems
**arXiv**：[2512.11532v1](https://arxiv.org/abs/2512.11532) · [PDF](https://arxiv.org/pdf/2512.11532.pdf)  
**作者**：Chong Tang, Hao Dai, Jagmohan Chauhan  

**一句话要点**：提出Parallax框架以加速移动设备上动态DNN推理的算子回退问题

**关键词**：移动DNN推理, 算子回退, 并行化框架, 内存管理, 异构边缘系统

## 3 点简述
- 核心问题：移动设备上动态控制流算子回退CPU执行导致高延迟和内存峰值
- 方法要点：通过计算图分区、分支感知内存管理和自适应调度实现并行化
- 实验或效果：在三种移动设备上评估，实现最高46%延迟降低和平均26.5%内存开销

## 摘要（原文）

> The growing demand for real-time DNN applications on edge devices necessitates faster inference of increasingly complex models. Although many devices include specialized accelerators (e.g., mobile GPUs), dynamic control-flow operators and unsupported kernels often fall back to CPU execution. Existing frameworks handle these fallbacks poorly, leaving CPU cores idle and causing high latency and memory spikes. We introduce Parallax, a framework that accelerates mobile DNN inference without model refactoring or custom operator implementations. Parallax first partitions the computation DAG to expose parallelism, then employs branch-aware memory management with dedicated arenas and buffer reuse to reduce runtime footprint. An adaptive scheduler executes branches according to device memory constraints, meanwhile, fine-grained subgraph control enables heterogeneous inference of dynamic models. By evaluating on five representative DNNs across three different mobile devices, Parallax achieves up to 46% latency reduction, maintains controlled memory overhead (26.5% on average), and delivers up to 30% energy savings compared with state-of-the-art frameworks, offering improvements aligned with the responsiveness demands of real-time mobile inference.

