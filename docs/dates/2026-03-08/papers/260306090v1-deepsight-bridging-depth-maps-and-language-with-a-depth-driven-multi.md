---
layout: default
title: DeepSight: Bridging Depth Maps and Language with a Depth-Driven Multimodal Model
---

# DeepSight: Bridging Depth Maps and Language with a Depth-Driven Multimodal Model
**arXiv**：[2603.06090v1](https://arxiv.org/abs/2603.06090) · [PDF](https://arxiv.org/pdf/2603.06090.pdf)  
**作者**：Hao Yang, Hongbo Zhang, Yanyan Zhao, Bing Qin  

**一句话要点**：提出DeepSight深度多模态大语言模型，以增强三维场景理解，解决现有模型深度信息解释不足的问题。

**关键词**：深度多模态大语言模型, 三维场景理解, 深度图像-文本对, 深度指令数据集, ViT编码器改进, 深度问答基准

## 3 点简述
- 核心问题：现有多模态大语言模型在视觉数据中深度信息解释上表现不佳，影响三维场景理解。
- 方法要点：构建深度图像-文本对数据集和深度指令数据集，改进CLIP的ViT编码器以更有效捕捉深度连续变化。
- 实验或效果：基于深度图像数据集开发问答基准，实验显示DeepSight显著提升深度感知和下游任务性能。

## 摘要（原文）

> Multimodal large language models (MLLMs) have achieved impressive performance across various tasks such as image captioning and visual question answer(VQA); however, they often struggle to accurately interpret depth information inherent in visual data. In this work, we introduce DeepSight, the first dedicated depth MLLM designed to enhance three-dimensional scene understanding. Unlike conventional methods that align RGB image encodings with text, our approach takes advantage of the unique characteristics of depth images: single-channel grayscale images where the pixel values directly reflect depth cues to improve spatial reasoning. To address challenges associated with limited depth data and the inadequacy of simple channel replication, we construct a novel depth image-text pair dataset and a depth instruction dataset. Depth maps are generated from visual images using the GLPN model, and GPT-4 is employed to curate corresponding depth instructions, an approach validated by LLaVA. Additionally, we modify the ViT encoder in CLIP to incorporate local object information, thereby capturing the subtle continuous variations of depth more effectively. To evaluate the performance of our model, we develop a comprehensive depth question answer benchmark based on existing depth image datasets, which rigorously assesses understanding in typical depth map scenarios. Experimental results demonstrate that DeepSight significantly enhances depth perception and downstream task performance, marking a substantial step forward in multimodal three-dimensional understanding.

