---
layout: default
title: MeshRipple: Structured Autoregressive Generation of Artist-Meshes
---

# MeshRipple: Structured Autoregressive Generation of Artist-Meshes
**arXiv**：[2512.07514v1](https://arxiv.org/abs/2512.07514) · [PDF](https://arxiv.org/pdf/2512.07514.pdf)  
**作者**：Junkai Lin, Hang Long, Huipeng Guo, Jielei Zhang, JiaYi Yang, Tianle Guo, Yang Yang, Jianwen Li, Wenxiao Zhang, Matthias Nießner, Wei Yang  

**一句话要点**：提出MeshRipple以解决自回归网格生成中长程几何依赖断裂问题

**关键词**：自回归网格生成, 长程几何依赖, 表面拓扑, 稀疏注意力, 网格生成模型

## 3 点简述
- 核心问题：自回归网格生成因序列化与滑动窗口推理导致长程几何依赖断裂，产生空洞和碎片化组件。
- 方法要点：采用前沿感知BFS标记化、扩展预测策略和稀疏注意力全局内存，实现连贯表面增长和长程拓扑依赖解析。
- 实验或效果：MeshRipple在表面保真度和拓扑完整性上优于近期基线，生成高质量网格。

## 摘要（原文）

> Meshes serve as a primary representation for 3D assets. Autoregressive mesh generators serialize faces into sequences and train on truncated segments with sliding-window inference to cope with memory limits. However, this mismatch breaks long-range geometric dependencies, producing holes and fragmented components. To address this critical limitation, we introduce MeshRipple, which expands a mesh outward from an active generation frontier, akin to a ripple on a surface.MeshRipple rests on three key innovations: a frontier-aware BFS tokenization that aligns the generation order with surface topology; an expansive prediction strategy that maintains coherent, connected surface growth; and a sparse-attention global memory that provides an effectively unbounded receptive field to resolve long-range topological dependencies.This integrated design enables MeshRipple to generate meshes with high surface fidelity and topological completeness, outperforming strong recent baselines.

