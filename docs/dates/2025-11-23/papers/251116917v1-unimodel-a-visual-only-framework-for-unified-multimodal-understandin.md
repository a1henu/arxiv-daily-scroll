---
layout: default
title: UniModel: A Visual-Only Framework for Unified Multimodal Understanding and Generation
---

# UniModel: A Visual-Only Framework for Unified Multimodal Understanding and Generation
**arXiv**：[2511.16917v1](https://arxiv.org/abs/2511.16917) · [PDF](https://arxiv.org/pdf/2511.16917.pdf)  
**作者**：Chi Zhang, Jiepeng Wang, Youming Wang, Yuanzhi Liang, Xiaoyan Yang, Zuoxin Li, Haibin Huang, Xuelong Li  

**一句话要点**：提出UniModel以统一视觉理解与生成，通过像素级扩散框架实现多模态学习。

**关键词**：统一多模态模型, 像素级扩散, 视觉空间映射, 生成与理解, 扩散变换器

## 3 点简述
- 核心问题：多模态学习中模态差异阻碍统一模型开发。
- 方法要点：将文本和图像映射到共享视觉空间，使用像素到像素变换。
- 实验或效果：在文本到图像和图像到文本任务中展示强对齐和可控性。

## 摘要（原文）

> We present UniModel, a unified generative model that jointly supports visual understanding and visual generation within a single pixel-to-pixel diffusion framework. Our goal is to achieve unification along three axes: the model, the tasks, and the representations. At the representation level, we eliminate modality discrepancies by mapping both text and images into a shared visual space: textual prompts are rendered as painted text images on a clean canvas, and all inputs and outputs are treated purely as RGB pixels. This yields a fully vision-native formulation of multimodal learning. At the task level, a broad range of vision-language problems are cast as pixel-to-pixel transformations in this visual space. For understanding tasks, the model takes an RGB image and produces a painted text image that visually encodes the semantic prediction. For generation tasks, painted text images serve as visual conditions that guide realistic and semantically aligned image synthesis. Captioning and text-to-image generation thus become different directions of the same underlying visual translation process. At the model level, we instantiate a single Unified Diffusion Transformer trained with rectified flow in pixel space. A shared backbone jointly learns bidirectional mappings between natural images and painted text images, with lightweight task embeddings to specify the desired direction. Experiments on text-to-image synthesis and image-to-text understanding demonstrate strong cross-modal alignment and emergent controllability such as cycle-consistent image-caption-image loops. Our initial exploration suggests that unifying model, tasks, and representations in a single visual space is a promising paradigm for general-purpose multimodal intelligence.

