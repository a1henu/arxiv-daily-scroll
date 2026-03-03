---
layout: default
title: MixerCSeg: An Efficient Mixer Architecture for Crack Segmentation via Decoupled Mamba Attention
---

# MixerCSeg: An Efficient Mixer Architecture for Crack Segmentation via Decoupled Mamba Attention
**arXiv**：[2603.01361v1](https://arxiv.org/abs/2603.01361) · [PDF](https://arxiv.org/pdf/2603.01361.pdf)  
**作者**：Zilong Zhao, Zhengming Ding, Pei Niu, Wenhao Sun, Feng Guo  

**一句话要点**：提出MixerCSeg混合架构，通过解耦Mamba注意力高效解决裂缝分割中复杂模式建模问题。

**关键词**：裂缝分割, 混合架构, Mamba注意力, 边缘增强, 高效模型, 像素级分割

## 3 点简述
- 核心问题：现有CNN、Transformer和Mamba模型在裂缝分割中仅捕获部分空间或结构信息，导致复杂裂缝模式建模存在明显差距。
- 方法要点：设计TransMixer核心模块，结合CNN局部纹理、Transformer全局依赖和Mamba序列上下文路径，并引入DEGConv和SRF模块增强结构保真度。
- 实验或效果：在多个基准测试中实现最先进性能，仅需2.05 GFLOPs和2.54 M参数，展示高效性和强表示能力。

## 摘要（原文）

> Feature encoders play a key role in pixel-level crack segmentation by shaping the representation of fine textures and thin structures. Existing CNN-, Transformer-, and Mamba-based models each capture only part of the required spatial or structural information, leaving clear gaps in modeling complex crack patterns. To address this, we present MixerCSeg, a mixer architecture designed like a coordinated team of specialists, where CNN-like pathways focus on local textures, Transformer-style paths capture global dependencies, and Mamba-inspired flows model sequential context within a single encoder. At the core of MixerCSeg is the TransMixer, which explores Mamba's latent attention behavior while establishing dedicated pathways that naturally express both locality and global awareness. To further enhance structural fidelity, we introduce a spatial block processing strategy and a Direction-guided Edge Gated Convolution (DEGConv) that strengthens edge sensitivity under irregular crack geometries with minimal computational overhead. A Spatial Refinement Multi-Level Fusion (SRF) module is then employed to refine multi-scale details without increasing complexity. Extensive experiments on multiple crack segmentation benchmarks show that MixerCSeg achieves state-of-the-art performance with only 2.05 GFLOPs and 2.54 M parameters, demonstrating both efficiency and strong representational capability. The code is available at https://github.com/spiderforest/MixerCSeg.

