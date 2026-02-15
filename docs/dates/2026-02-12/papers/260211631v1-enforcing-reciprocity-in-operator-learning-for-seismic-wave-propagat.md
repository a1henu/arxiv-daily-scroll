---
layout: default
title: Enforcing Reciprocity in Operator Learning for Seismic Wave Propagation
---

# Enforcing Reciprocity in Operator Learning for Seismic Wave Propagation
**arXiv**：[2602.11631v1](https://arxiv.org/abs/2602.11631) · [PDF](https://arxiv.org/pdf/2602.11631.pdf)  
**作者**：Caifeng Zou, Yaozhong Shi, Zachary E. Ross, Robert W. Clayton, Kamyar Azizzadenesheli  

**一句话要点**：提出RENO架构，通过硬编码互易性原理提升地震波传播建模的物理一致性与效率

**关键词**：地震波传播建模, 互易性原理, 神经算子, Transformer架构, 物理一致性, 高效推理

## 3 点简述
- 传统地震波建模方法计算成本高，数据驱动方法缺乏严格物理一致性，互易性原理未充分融入
- RENO基于Transformer，利用交叉注意力和可交换操作硬编码互易性，保证源-接收器位置交换不变性
- 在真实配置中，相比未强制互易性的神经算子，实现推理速度数量级提升，内存占用相似，支持多源无串扰

## 摘要（原文）

> Accurate and efficient wavefield modeling underpins seismic structure and source studies. Traditional methods comply with physical laws but are computationally intensive. Data-driven methods, while opening new avenues for advancement, have yet to incorporate strict physical consistency. The principle of reciprocity is one of the most fundamental physical laws in wave propagation. We introduce the Reciprocity-Enforced Neural Operator (RENO), a transformer-based architecture for modeling seismic wave propagation that hard-codes the reciprocity principle. The model leverages the cross-attention mechanism and commutative operations to guarantee invariance under swapping source and receiver positions. Beyond improved physical consistency, the proposed architecture supports simultaneous realizations for multiple sources without crosstalk issues. This yields an order-of-magnitude inference speedup at a similar memory footprint over an reciprocity-unenforced neural operator on a realistic configuration. We demonstrate the functionality using the reciprocity relation for particle velocity fields under single forces. This architecture is also applicable to pressure fields under dilatational sources and travel-time fields governed by the eikonal equation, paving the way for encoding more complex reciprocity relations.

