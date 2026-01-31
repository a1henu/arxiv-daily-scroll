---
layout: default
title: Generation Enhances Understanding in Unified Multimodal Models via Multi-Representation Generation
---

# Generation Enhances Understanding in Unified Multimodal Models via Multi-Representation Generation
**arXiv**：[2601.21406v1](https://arxiv.org/abs/2601.21406) · [PDF](https://arxiv.org/pdf/2601.21406.pdf)  
**作者**：Zihan Su, Hongyang Wei, Kangrui Cen, Yong Wang, Guanhua Chen, Chun Yuan, Xiangxiang Chu  

**一句话要点**：提出UniMRG方法，通过多表示生成增强统一多模态模型的理解能力

**关键词**：统一多模态模型, 多表示生成, 视觉理解增强, 后训练方法, 辅助生成任务

## 3 点简述
- 核心问题：统一多模态模型中生成任务如何提升理解能力，现有方法未充分探索
- 方法要点：训练模型生成像素、深度和分割等多表示，作为辅助任务增强视觉理解
- 实验或效果：实验显示方法提升细粒度感知、减少幻觉、改善空间理解，并增强生成能力

## 摘要（原文）

> Unified Multimodal Models (UMMs) integrate both visual understanding and generation within a single framework. Their ultimate aspiration is to create a cycle where understanding and generation mutually reinforce each other. While recent post-training methods have successfully leveraged understanding to enhance generation, the reverse direction of utilizing generation to improve understanding remains largely unexplored. In this work, we propose UniMRG (Unified Multi-Representation Generation), a simple yet effective architecture-agnostic post-training method. UniMRG enhances the understanding capabilities of UMMs by incorporating auxiliary generation tasks. Specifically, we train UMMs to generate multiple intrinsic representations of input images, namely pixel (reconstruction), depth (geometry), and segmentation (structure), alongside standard visual understanding objectives. By synthesizing these diverse representations, UMMs capture complementary information regarding appearance, spatial relations, and structural layout. Consequently, UMMs develop a deeper and more comprehensive understanding of visual inputs. Extensive experiments across diverse UMM architectures demonstrate that our method notably enhances fine-grained perception, reduces hallucinations, and improves spatial understanding, while simultaneously boosting generation capabilities.

