---
layout: default
title: A saccade-inspired approach to image classification using visiontransformer attention maps
---

# A saccade-inspired approach to image classification using visiontransformer attention maps
**arXiv**：[2603.09613v1](https://arxiv.org/abs/2603.09613) · [PDF](https://arxiv.org/pdf/2603.09613.pdf)  
**作者**：Matthis Dallain, Laurent Rodriguez, Laurent Udo Perrinet, Benoît Miramond  

**一句话要点**：提出基于DINO注意力图的眼跳启发方法，用于高效图像分类

**关键词**：视觉Transformer, 注意力机制, 眼跳模拟, 图像分类, 生物启发视觉, 高效处理

## 3 点简述
- 核心问题：传统AI系统全图处理效率低，人类视觉通过选择性注意实现高效感知
- 方法要点：利用DINO生成类人眼注视的注意力图，模拟眼跳聚焦关键区域进行信息处理
- 实验或效果：在ImageNet分类任务中，选择性处理保持大部分性能，有时优于全图处理

## 摘要（原文）

> Human vision achieves remarkable perceptual performance while operating under strict metabolic constraints. A key ingredient is the selective attention mechanism, driven by rapid saccadic eye movements that constantly reposition the high-resolution fovea onto task-relevant locations, unlike conventional AI systems that process entire images with equal emphasis. Our work aims to draw inspiration from the human visual system to create smarter, more efficient image processing models. Using DINO, a self-supervised Vision Transformer that produces attention maps strikingly similar to human gaze patterns, we explore a saccade inspired method to focus the processing of information on key regions in visual space. To do so, we use the ImageNet dataset in a standard classification task and measure how each successive saccade affects the model's class scores. This selective-processing strategy preserves most of the full-image classification performance and can even outperform it in certain cases. By benchmarking against established saliency models built for human gaze prediction, we demonstrate that DINO provides superior fixation guidance for selecting informative regions. These findings highlight Vision Transformer attention as a promising basis for biologically inspired active vision and open new directions for efficient, neuromorphic visual processing.

