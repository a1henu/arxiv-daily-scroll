---
layout: default
title: MoGen: A Unified Collaborative Framework for Controllable Multi-Object Image Generation
---

# MoGen: A Unified Collaborative Framework for Controllable Multi-Object Image Generation
**arXiv**：[2601.05546v1](https://arxiv.org/abs/2601.05546) · [PDF](https://arxiv.org/pdf/2601.05546.pdf)  
**作者**：Yanfeng Li, Yue Sun, Keren Fu, Sio-Kei Im, Xiaoming Liu, Guangtao Zhai, Xiaohong Liu, Tao Tan  

**一句话要点**：提出MoGen框架以解决多对象图像生成中语义对齐与灵活控制问题

**关键词**：多对象图像生成, 语义对齐, 自适应控制, 区域语义锚定, 多模态引导

## 3 点简述
- 现有方法依赖外部控制信号，导致输入格式僵化且兼容性差
- 设计区域语义锚定模块，实现语言描述与图像区域的精确对齐
- 引入自适应多模态引导模块，支持动态细粒度控制并提升生成质量

## 摘要（原文）

> Existing multi-object image generation methods face difficulties in achieving precise alignment between localized image generation regions and their corresponding semantics based on language descriptions, frequently resulting in inconsistent object quantities and attribute aliasing. To mitigate this limitation, mainstream approaches typically rely on external control signals to explicitly constrain the spatial layout, local semantic and visual attributes of images. However, this strong dependency makes the input format rigid, rendering it incompatible with the heterogeneous resource conditions of users and diverse constraint requirements. To address these challenges, we propose MoGen, a user-friendly multi-object image generation method. First, we design a Regional Semantic Anchor (RSA) module that precisely anchors phrase units in language descriptions to their corresponding image regions during the generation process, enabling text-to-image generation that follows quantity specifications for multiple objects. Building upon this foundation, we further introduce an Adaptive Multi-modal Guidance (AMG) module, which adaptively parses and integrates various combinations of multi-source control signals to formulate corresponding structured intent. This intent subsequently guides selective constraints on scene layouts and object attributes, achieving dynamic fine-grained control. Experimental results demonstrate that MoGen significantly outperforms existing methods in generation quality, quantity consistency, and fine-grained control, while exhibiting superior accessibility and control flexibility. Code is available at: https://github.com/Tear-kitty/MoGen/tree/master.

