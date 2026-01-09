---
layout: default
title: MiLDEdit: Reasoning-Based Multi-Layer Design Document Editing
---

# MiLDEdit: Reasoning-Based Multi-Layer Design Document Editing
**arXiv**：[2601.04589v1](https://arxiv.org/abs/2601.04589) · [PDF](https://arxiv.org/pdf/2601.04589.pdf)  
**作者**：Zihao Lin, Wanrong Zhu, Jiuxiang Gu, Jihyung Kil, Christopher Tensmeyer, Lin Zhang, Shilong Liu, Ruiyi Zhang, Lifu Huang, Vlad I. Morariu, Tong Sun  

**一句话要点**：提出MiLDEAgent框架以解决多图层设计文档编辑中的细粒度推理与修改问题

**关键词**：多图层文档编辑, 图层感知推理, 自然语言指令编辑, 设计文档基准, 多模态推理, 图像编辑框架

## 3 点简述
- 核心问题：现有方法忽视多图层设计文档编辑，缺乏图层感知推理能力，导致无法从自然语言指令中识别相关图层并协调修改
- 方法要点：结合RL训练的多模态推理器进行图层级理解与图像编辑器进行针对性修改，构建基于推理的编辑框架
- 实验或效果：在MiLDEBench基准上，MiLDEAgent显著优于开源基线，性能接近闭源模型，成为多图层文档编辑的首个强基线

## 摘要（原文）

> Real-world design documents (e.g., posters) are inherently multi-layered, combining decoration, text, and images. Editing them from natural-language instructions requires fine-grained, layer-aware reasoning to identify relevant layers and coordinate modifications. Prior work largely overlooks multi-layer design document editing, focusing instead on single-layer image editing or multi-layer generation, which assume a flat canvas and lack the reasoning needed to determine what and where to modify. To address this gap, we introduce the Multi-Layer Document Editing Agent (MiLDEAgent), a reasoning-based framework that combines an RL-trained multimodal reasoner for layer-wise understanding with an image editor for targeted modifications. To systematically benchmark this setting, we introduce the MiLDEBench, a human-in-the-loop corpus of over 20K design documents paired with diverse editing instructions. The benchmark is complemented by a task-specific evaluation protocol, MiLDEEval, which spans four dimensions including instruction following, layout consistency, aesthetics, and text rendering. Extensive experiments on 14 open-source and 2 closed-source models reveal that existing approaches fail to generalize: open-source models often cannot complete multi-layer document editing tasks, while closed-source models suffer from format violations. In contrast, MiLDEAgent achieves strong layer-aware reasoning and precise editing, significantly outperforming all open-source baselines and attaining performance comparable to closed-source models, thereby establishing the first strong baseline for multi-layer document editing.

