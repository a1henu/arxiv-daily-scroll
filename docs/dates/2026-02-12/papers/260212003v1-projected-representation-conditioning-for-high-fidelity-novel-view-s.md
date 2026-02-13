---
layout: default
title: Projected Representation Conditioning for High-fidelity Novel View Synthesis
---

# Projected Representation Conditioning for High-fidelity Novel View Synthesis
**arXiv**：[2602.12003v1](https://arxiv.org/abs/2602.12003) · [PDF](https://arxiv.org/pdf/2602.12003.pdf)  
**作者**：Min-Seop Kwak, Minkyung Kwon, Jinhyeok Choi, Jiho Park, Seungryong Kim  

**一句话要点**：提出ReNoV框架，利用外部表示增强扩散模型的新视角合成几何一致性

**关键词**：新视角合成, 扩散模型, 表示投影, 几何一致性, 图像修复

## 3 点简述
- 核心问题：扩散模型在新视角合成中几何一致性不足，影响重建保真度和修复质量
- 方法要点：通过表示投影模块将外部表示注入扩散过程，利用其几何和语义对应特性
- 实验或效果：在标准基准测试中优于先前方法，支持从稀疏、未标定图像集合进行鲁棒合成

## 摘要（原文）

> We propose a novel framework for diffusion-based novel view synthesis in which we leverage external representations as conditions, harnessing their geometric and semantic correspondence properties for enhanced geometric consistency in generated novel viewpoints. First, we provide a detailed analysis exploring the correspondence capabilities emergent in the spatial attention of external visual representations. Building from these insights, we propose a representation-guided novel view synthesis through dedicated representation projection modules that inject external representations into the diffusion process, a methodology named ReNoV, short for representation-guided novel view synthesis. Our experiments show that this design yields marked improvements in both reconstruction fidelity and inpainting quality, outperforming prior diffusion-based novel-view methods on standard benchmarks and enabling robust synthesis from sparse, unposed image collections.

