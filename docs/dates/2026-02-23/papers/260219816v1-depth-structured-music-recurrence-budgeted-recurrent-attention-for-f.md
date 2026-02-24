---
layout: default
title: Depth-Structured Music Recurrence: Budgeted Recurrent Attention for Full-Piece Symbolic Music Modeling
---

# Depth-Structured Music Recurrence: Budgeted Recurrent Attention for Full-Piece Symbolic Music Modeling
**arXiv**：[2602.19816v1](https://arxiv.org/abs/2602.19816) · [PDF](https://arxiv.org/pdf/2602.19816.pdf)  
**作者**：Yungang Yi  

**一句话要点**：提出深度结构化音乐循环以在资源受限设备上实现全曲符号音乐建模

**关键词**：符号音乐建模, 长上下文建模, 循环注意力, 资源受限计算, 深度结构化循环

## 3 点简述
- 核心问题：符号音乐生成需长上下文建模，但资源受限设备难以部署高内存和注意力计算。
- 方法要点：引入DSMR，通过分段循环和深度依赖的KV状态预算，扩展上下文至全曲范围。
- 实验或效果：在MAESTRO数据集上验证，两尺度DSMR在有限计算资源下提供质量-效率平衡。

## 摘要（原文）

> Long-context modeling is essential for symbolic music generation, since motif repetition and developmental variation can span thousands of musical events. However, practical composition and performance workflows frequently rely on resource-limited devices (e.g., electronic instruments and portable computers), making heavy memory and attention computation difficult to deploy. We introduce Depth-Structured Music Recurrence (DSMR), a recurrent long-context Transformer for full-piece symbolic music modeling that extends context beyond fixed-length excerpts via segment-level recurrence with detached cross-segment states, featuring a layer-wise memory-horizon schedule that budgets recurrent KV states across depth. DSMR is trained in a single left-to-right pass over each complete composition, akin to how a musician experiences it from beginning to end, while carrying recurrent cross-segment states forward. Within this recurrent framework, we systematically study how depth-wise horizon allocations affect optimization, best-checkpoint perplexity, and efficiency. By allocating different history-window lengths across layers while keeping the total recurrent-state budget fixed, DSMR creates depth-dependent temporal receptive fields within a recurrent attention stack without reducing compute depth. Our main instantiation is a two-scale DSMR schedule that allocates long history windows to lower layers and a uniform short window to the remaining layers. Experiments on the piano performance dataset MAESTRO demonstrate that two-scale DSMR provides a practical quality--efficiency recipe for full-length long-context symbolic music modeling with recurrent attention under limited computational resources.

