---
layout: default
title: Towards Source-Aware Object Swapping with Initial Noise Perturbation
---

# Towards Source-Aware Object Swapping with Initial Noise Perturbation
**arXiv**：[2602.23697v1](https://arxiv.org/abs/2602.23697) · [PDF](https://arxiv.org/pdf/2602.23697.pdf)  
**作者**：Jiahui Zhan, Xianbing Sun, Xiangnan Zhu, Yikun Ji, Ruitong Liu, Liqing Zhang, Jianfu Zhang  

**一句话要点**：提出SourceSwap框架，通过初始噪声扰动实现源感知物体交换，无需额外数据或微调。

**关键词**：物体交换, 自监督学习, 初始噪声扰动, 跨物体对齐, 零样本推理, 伪配对合成

## 3 点简述
- 现有物体交换方法依赖微调或配对数据，难以学习跨物体对齐。
- SourceSwap利用频率分离扰动合成伪配对，训练双U-Net实现直接跨物体对齐。
- 实验显示SourceSwap在保真度、场景保留和和谐度上表现优越，支持零样本推理。

## 摘要（原文）

> Object swapping aims to replace a source object in a scene with a reference object while preserving object fidelity, scene fidelity, and object-scene harmony. Existing methods either require per-object finetuning and slow inference or rely on extra paired data that mostly depict the same object across contexts, forcing models to rely on background cues rather than learning cross-object alignment. We propose SourceSwap, a self-supervised and source-aware framework that learns cross-object alignment. Our key insight is to synthesize high-quality pseudo pairs from any image via a frequency-separated perturbation in the initial-noise space, which alters appearance while preserving pose, coarse shape, and scene layout, requiring no videos, multi-view data, or additional images. We then train a dual U-Net with full-source conditioning and a noise-free reference encoder, enabling direct inter-object alignment, zero-shot inference without per-object finetuning, and lightweight iterative refinement. We further introduce SourceBench, a high-quality benchmark with higher resolution, more categories, and richer interactions. Experiments demonstrate that SourceSwap achieves superior fidelity, stronger scene preservation, and more natural harmony, and it transfers well to edits such as subject-driven refinement and face swapping.

