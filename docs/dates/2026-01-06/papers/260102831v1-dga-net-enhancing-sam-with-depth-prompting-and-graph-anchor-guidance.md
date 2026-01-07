---
layout: default
title: DGA-Net: Enhancing SAM with Depth Prompting and Graph-Anchor Guidance for Camouflaged Object Detection
---

# DGA-Net: Enhancing SAM with Depth Prompting and Graph-Anchor Guidance for Camouflaged Object Detection
**arXiv**：[2601.02831v1](https://arxiv.org/abs/2601.02831) · [PDF](https://arxiv.org/pdf/2601.02831.pdf)  
**作者**：Yuetong Li, Qing Zhang, Yilin Zhao, Gongyang Li, Zeming Liu  

**一句话要点**：提出DGA-Net，通过深度提示和图锚引导增强SAM，用于伪装目标检测。

**关键词**：伪装目标检测, 深度提示, 图锚引导, 跨模态增强, Segment Anything Model

## 3 点简述
- 核心问题：现有方法依赖稀疏提示，难以充分利用深度信息进行伪装目标检测。
- 方法要点：引入深度提示范式，结合跨模态图增强模块和锚引导细化模块，提升分割精度。
- 实验或效果：定量和定性实验表明，DGA-Net优于当前最先进的伪装目标检测方法。

## 摘要（原文）

> To fully exploit depth cues in Camouflaged Object Detection (COD), we present DGA-Net, a specialized framework that adapts the Segment Anything Model (SAM) via a novel ``depth prompting" paradigm. Distinguished from existing approaches that primarily rely on sparse prompts (e.g., points or boxes), our method introduces a holistic mechanism for constructing and propagating dense depth prompts. Specifically, we propose a Cross-modal Graph Enhancement (CGE) module that synthesizes RGB semantics and depth geometric within a heterogeneous graph to form a unified guidance signal. Furthermore, we design an Anchor-Guided Refinement (AGR) module. To counteract the inherent information decay in feature hierarchies, AGR forges a global anchor and establishes direct non-local pathways to broadcast this guidance from deep to shallow layers, ensuring precise and consistent segmentation. Quantitative and qualitative experimental results demonstrate that our proposed DGA-Net outperforms the state-of-the-art COD methods.

