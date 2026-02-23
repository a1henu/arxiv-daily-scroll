---
layout: default
title: ROCKET: Residual-Oriented Multi-Layer Alignment for Spatially-Aware Vision-Language-Action Models
---

# ROCKET: Residual-Oriented Multi-Layer Alignment for Spatially-Aware Vision-Language-Action Models
**arXiv**：[2602.17951v1](https://arxiv.org/abs/2602.17951) · [PDF](https://arxiv.org/pdf/2602.17951.pdf)  
**作者**：Guoheng Sun, Tingting Du, Kaixi Feng, Chenxiang Luo, Xingguo Ding, Zheyu Shen, Ziyao Wang, Yexiao He, Ang Li  

**一句话要点**：提出ROCKET框架，通过残差导向多层对齐增强VLA模型的3D空间理解能力。

**关键词**：视觉-语言-动作模型, 多层表示对齐, 残差学习, 3D空间理解, 梯度优化, 机器人操作

## 3 点简述
- 现有VLA模型基于2D数据预训练，缺乏3D空间理解，单层对齐方法未能充分利用深度信息。
- ROCKET采用共享投影器进行多层对齐，减少梯度冲突，并通过稀疏激活平衡多损失。
- 实验显示ROCKET在LIBERO等基准上以低计算成本达到高成功率，并适用于多种VLA模型。

## 摘要（原文）

> Vision-Language-Action (VLA) models enable instruction-following robotic manipulation, but they are typically pretrained on 2D data and lack 3D spatial understanding. An effective approach is representation alignment, where a strong vision foundation model is used to guide a 2D VLA model. However, existing methods usually apply supervision at only a single layer, failing to fully exploit the rich information distributed across depth; meanwhile, naïve multi-layer alignment can cause gradient interference. We introduce ROCKET, a residual-oriented multi-layer representation alignment framework that formulates multi-layer alignment as aligning one residual stream to another. Concretely, ROCKET employs a shared projector to align multiple layers of the VLA backbone with multiple layers of a powerful 3D vision foundation model via a layer-invariant mapping, which reduces gradient conflicts. We provide both theoretical justification and empirical analyses showing that a shared projector is sufficient and outperforms prior designs, and further propose a Matryoshka-style sparse activation scheme for the shared projector to balance multiple alignment losses. Our experiments show that, combined with a training-free layer selection strategy, ROCKET requires only about 4% of the compute budget while achieving 98.5% state-of-the-art success rate on LIBERO. We further demonstrate the superior performance of ROCKET across LIBERO-Plus and RoboTwin, as well as multiple VLA models. The code and model weights can be found at https://github.com/CASE-Lab-UMD/ROCKET-VLA.

