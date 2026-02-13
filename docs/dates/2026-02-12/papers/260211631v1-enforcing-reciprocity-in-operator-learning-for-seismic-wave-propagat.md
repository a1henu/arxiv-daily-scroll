---
layout: default
title: Enforcing Reciprocity in Operator Learning for Seismic Wave Propagation
---

# Enforcing Reciprocity in Operator Learning for Seismic Wave Propagation
**arXiv**：[2602.11631v1](https://arxiv.org/abs/2602.11631) · [PDF](https://arxiv.org/pdf/2602.11631.pdf)  
**作者**：Caifeng Zou, Yaozhong Shi, Zachary E. Ross, Robert W. Clayton, Kamyar Azizzadenesheli  

**一句话要点**：提出RENO架构以在算子学习中强制互易性，用于地震波传播建模

**关键词**：算子学习, 地震波传播, 互易性, Transformer, 物理一致性, 推理加速

## 3 点简述
- 传统方法计算成本高，数据驱动方法缺乏物理一致性，互易性是波传播的基本物理定律
- RENO基于Transformer，通过交叉注意力和交换操作硬编码互易性，保证源和接收器位置交换下的不变性
- 在真实配置中，相比未强制互易性的神经算子，推理速度提升一个数量级，内存占用相似，支持多源无串扰

## 摘要（原文）

> Accurate and efficient wavefield modeling underpins seismic structure and source studies. Traditional methods comply with physical laws but are computationally intensive. Data-driven methods, while opening new avenues for advancement, have yet to incorporate strict physical consistency. The principle of reciprocity is one of the most fundamental physical laws in wave propagation. We introduce the Reciprocity-Enforced Neural Operator (RENO), a transformer-based architecture for modeling seismic wave propagation that hard-codes the reciprocity principle. The model leverages the cross-attention mechanism and commutative operations to guarantee invariance under swapping source and receiver positions. Beyond improved physical consistency, the proposed architecture supports simultaneous realizations for multiple sources without crosstalk issues. This yields an order-of-magnitude inference speedup at a similar memory footprint over an reciprocity-unenforced neural operator on a realistic configuration. We demonstrate the functionality using the reciprocity relation for particle velocity fields under single forces. This architecture is also applicable to pressure fields under dilatational sources and travel-time fields governed by the eikonal equation, paving the way for encoding more complex reciprocity relations.

