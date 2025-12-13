---
layout: default
title: Topology-Agnostic Animal Motion Generation from Text Prompt
---

# Topology-Agnostic Animal Motion Generation from Text Prompt
**arXiv**：[2512.10352v1](https://arxiv.org/abs/2512.10352) · [PDF](https://arxiv.org/pdf/2512.10352.pdf)  
**作者**：Keyi Chen, Mingze Sun, Zhenyu Liu, Zhangquan Chen, Ruqi Huang  

**一句话要点**：提出OmniZoo数据集与拓扑无关的动物运动生成框架，以解决固定骨骼模板限制问题

**关键词**：动物运动生成, 拓扑无关建模, 文本驱动动画, 多模态数据集, 骨架嵌入

## 3 点简述
- 核心问题：现有运动生成方法依赖固定骨骼模板，无法泛化到不同或扰动拓扑的骨架
- 方法要点：引入Topology-aware Skeleton Embedding Module，将任意骨架编码到共享令牌空间，结合文本语义生成运动
- 实验或效果：基于OmniZoo数据集（140物种，32,979序列），生成时间连贯、物理合理、语义对齐的运动，支持跨物种风格迁移

## 摘要（原文）

> Motion generation is fundamental to computer animation and widely used across entertainment, robotics, and virtual environments. While recent methods achieve impressive results, most rely on fixed skeletal templates, which prevent them from generalizing to skeletons with different or perturbed topologies. We address the core limitation of current motion generation methods - the combined lack of large-scale heterogeneous animal motion data and unified generative frameworks capable of jointly modeling arbitrary skeletal topologies and textual conditions. To this end, we introduce OmniZoo, a large-scale animal motion dataset spanning 140 species and 32,979 sequences, enriched with multimodal annotations. Building on OmniZoo, we propose a generalized autoregressive motion generation framework capable of producing text-driven motions for arbitrary skeletal topologies. Central to our model is a Topology-aware Skeleton Embedding Module that encodes geometric and structural properties of any skeleton into a shared token space, enabling seamless fusion with textual semantics. Given a text prompt and a target skeleton, our method generates temporally coherent, physically plausible, and semantically aligned motions, and further enables cross-species motion style transfer.

