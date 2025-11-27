---
layout: default
title: G$^2$VLM: Geometry Grounded Vision Language Model with Unified 3D Reconstruction and Spatial Reasoning
---

# G$^2$VLM: Geometry Grounded Vision Language Model with Unified 3D Reconstruction and Spatial Reasoning
**arXiv**：[2511.21688v1](https://arxiv.org/abs/2511.21688) · [PDF](https://arxiv.org/pdf/2511.21688.pdf)  
**作者**：Wenbo Hu, Jingli Lin, Yilin Long, Yunlong Ran, Lihan Jiang, Yifan Wang, Chenming Zhu, Runsen Xu, Tai Wang, Jiangmiao Pang  

**一句话要点**：提出G²VLM模型，通过统一3D重建与空间推理解决视觉语言模型空间智能不足问题。

**关键词**：几何基础视觉语言模型, 3D重建, 空间推理, 多视图图像训练, 上下文学习, 统一设计

## 3 点简述
- 核心问题：视觉语言模型在空间理解和推理任务中表现不佳，缺乏从2D图像重建3D空间的几何学习过程。
- 方法要点：G²VLM利用学习到的3D视觉几何特征，直接预测3D属性并通过上下文学习和交错推理增强空间推理。
- 实验或效果：在3D重建任务中与先进前馈模型相当，在空间理解与推理任务中表现优于或竞争于现有方法。

## 摘要（原文）

> Vision-Language Models (VLMs) still lack robustness in spatial intelligence, demonstrating poor performance on spatial understanding and reasoning tasks. We attribute this gap to the absence of a visual geometry learning process capable of reconstructing 3D space from 2D images. We present G$^2$VLM, a geometry grounded vision-language model that bridges two fundamental aspects of spatial intelligence: spatial 3D reconstruction and spatial understanding. G$^2$VLM natively leverages learned 3D visual geometry features to directly predict 3D attributes and enhance spatial reasoning tasks via in-context learning and interleaved reasoning. Our unified design is highly scalable for spatial understanding: it trains on abundant multi-view image and video data, while simultaneously leveraging the benefits of 3D visual priors that are typically only derived from hard-to-collect annotations. Experimental results demonstrate G$^2$VLM is proficient in both tasks, achieving comparable results to state-of-the-art feed-forward 3D reconstruction models and achieving better or competitive results across spatial understanding and reasoning tasks. By unifying a semantically strong VLM with low-level 3D vision tasks, we hope G$^2$VLM can serve as a strong baseline for the community and unlock more future applications, such as 3D scene editing.

