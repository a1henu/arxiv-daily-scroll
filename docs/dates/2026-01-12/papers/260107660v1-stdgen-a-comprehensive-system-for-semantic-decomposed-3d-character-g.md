---
layout: default
title: StdGEN++: A Comprehensive System for Semantic-Decomposed 3D Character Generation
---

# StdGEN++: A Comprehensive System for Semantic-Decomposed 3D Character Generation
**arXiv**：[2601.07660v1](https://arxiv.org/abs/2601.07660) · [PDF](https://arxiv.org/pdf/2601.07660.pdf)  
**作者**：Yuze He, Yanning Zhou, Wang Zhao, Jingwen Ye, Zhongkai Wu, Ran Yi, Yong-Jin Liu  

**一句话要点**：提出StdGEN++系统以解决游戏动画中3D角色生成缺乏语义分解和结构灵活性的问题

**关键词**：3D角色生成, 语义分解, 双分支重建模型, 隐式场提取, 纹理分解, 非破坏性编辑

## 3 点简述
- 现有3D生成方法常产生整体网格，缺乏工业流程所需的结构灵活性
- 基于双分支语义感知大重建模型，联合重建几何、颜色和组件语义
- 实验显示在几何精度和语义解缠方面优于现有方法，支持下游编辑和动画

## 摘要（原文）

> We present StdGEN++, a novel and comprehensive system for generating high-fidelity, semantically decomposed 3D characters from diverse inputs. Existing 3D generative methods often produce monolithic meshes that lack the structural flexibility required by industrial pipelines in gaming and animation. Addressing this gap, StdGEN++ is built upon a Dual-branch Semantic-aware Large Reconstruction Model (Dual-Branch S-LRM), which jointly reconstructs geometry, color, and per-component semantics in a feed-forward manner. To achieve production-level fidelity, we introduce a novel semantic surface extraction formalism compatible with hybrid implicit fields. This mechanism is accelerated by a coarse-to-fine proposal scheme, which significantly reduces memory footprint and enables high-resolution mesh generation. Furthermore, we propose a video-diffusion-based texture decomposition module that disentangles appearance into editable layers (e.g., separated iris and skin), resolving semantic confusion in facial regions. Experiments demonstrate that StdGEN++ achieves state-of-the-art performance, significantly outperforming existing methods in geometric accuracy and semantic disentanglement. Crucially, the resulting structural independence unlocks advanced downstream capabilities, including non-destructive editing, physics-compliant animation, and gaze tracking, making it a robust solution for automated character asset production.

