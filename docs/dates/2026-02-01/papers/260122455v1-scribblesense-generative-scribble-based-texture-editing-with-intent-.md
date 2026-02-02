---
layout: default
title: ScribbleSense: Generative Scribble-Based Texture Editing with Intent Prediction
---

# ScribbleSense: Generative Scribble-Based Texture Editing with Intent Prediction
**arXiv**：[2601.22455v1](https://arxiv.org/abs/2601.22455) · [PDF](https://arxiv.org/pdf/2601.22455.pdf)  
**作者**：Yudi Zhang, Yeming Geng, Lei Zhang  

**一句话要点**：提出ScribbleSense方法，结合多模态大语言模型和图像生成模型，解决基于涂鸦的3D纹理编辑中意图模糊和语义定位不清的问题。

**关键词**：3D纹理编辑, 涂鸦交互, 多模态大语言模型, 意图预测, 图像生成, 语义定位

## 3 点简述
- 核心问题：现有涂鸦交互方法因涂鸦指令抽象，导致编辑意图模糊和目标语义位置不明确。
- 方法要点：利用多模态大语言模型预测涂鸦编辑意图，并通过全局生成图像提取局部纹理细节以锚定语义。
- 实验或效果：实验表明该方法有效利用多模态大语言模型优势，在涂鸦纹理编辑中实现先进的交互性能。

## 摘要（原文）

> Interactive 3D model texture editing presents enhanced opportunities for creating 3D assets, with freehand drawing style offering the most intuitive experience. However, existing methods primarily support sketch-based interactions for outlining, while the utilization of coarse-grained scribble-based interaction remains limited. Furthermore, current methodologies often encounter challenges due to the abstract nature of scribble instructions, which can result in ambiguous editing intentions and unclear target semantic locations. To address these issues, we propose ScribbleSense, an editing method that combines multimodal large language models (MLLMs) and image generation models to effectively resolve these challenges. We leverage the visual capabilities of MLLMs to predict the editing intent behind the scribbles. Once the semantic intent of the scribble is discerned, we employ globally generated images to extract local texture details, thereby anchoring local semantics and alleviating ambiguities concerning the target semantic locations. Experimental results indicate that our method effectively leverages the strengths of MLLMs, achieving state-of-the-art interactive editing performance for scribble-based texture editing.

