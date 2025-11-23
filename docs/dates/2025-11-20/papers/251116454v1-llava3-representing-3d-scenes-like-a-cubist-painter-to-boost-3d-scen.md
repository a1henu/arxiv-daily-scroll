---
layout: default
title: LLaVA$^3$: Representing 3D Scenes like a Cubist Painter to Boost 3D Scene Understanding of VLMs
---

# LLaVA$^3$: Representing 3D Scenes like a Cubist Painter to Boost 3D Scene Understanding of VLMs
**arXiv**：[2511.16454v1](https://arxiv.org/abs/2511.16454) · [PDF](https://arxiv.org/pdf/2511.16454.pdf)  
**作者**：Doriand Petit, Steve Bourgeois, Vincent Gay-Bellile, Florian Chabot, Loïc Barthe  

**一句话要点**：提出LLaVA³方法，通过多视角2D图像提升VLM的3D场景理解能力

**关键词**：3D场景理解, 视觉语言模型, 多视角图像, 立体主义表示, 3D视觉问答

## 3 点简述
- 核心问题：3D场景理解因训练数据稀缺而受限，而2D数据丰富。
- 方法要点：受立体主义启发，用多视角图像构建全向视觉表示描述3D场景。
- 实验或效果：在3D VQA和语言接地任务中优于现有2D方法。

## 摘要（原文）

> Developing a multi-modal language model capable of understanding 3D scenes remains challenging due to the limited availability of 3D training data, in contrast to the abundance of 2D datasets used for vision-language models (VLM). As an alternative, we introduce LLaVA$^3$ (pronounced LLaVA-Cube), a novel method that improves the 3D scene understanding capabilities of VLM using only multi-view 2D images and without any fine-tuning. Inspired by Cubist painters, who represented multiple viewpoints of a 3D object within a single picture, we propose to describe the 3D scene for the VLM through omnidirectional visual representations of each object. These representations are derived from an intermediate multi-view 3D reconstruction of the scene. Extensive experiments on 3D VQA and 3D language grounding show that our approach outperforms previous 2D-based VLM solutions.

