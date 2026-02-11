---
layout: default
title: VersaViT: Enhancing MLLM Vision Backbones via Task-Guided Optimization
---

# VersaViT: Enhancing MLLM Vision Backbones via Task-Guided Optimization
**arXiv**：[2602.09934v1](https://arxiv.org/abs/2602.09934) · [PDF](https://arxiv.org/pdf/2602.09934.pdf)  
**作者**：Yikun Liu, Yuan Liu, Shangzhe Di, Haicheng Wang, Zhongyin Zhao, Le Tian, Xiao Zhou, Jie Zhou, Jiangchao Yao, Yanfeng Wang, Weidi Xie  

**一句话要点**：提出VersaViT，通过任务引导优化增强MLLM视觉骨干，实现语言推理与像素级理解的双重能力。

**关键词**：多模态大语言模型, 视觉骨干优化, 密集预测任务, 多任务学习, 后训练框架

## 3 点简述
- 核心问题：MLLM视觉编码器在密集预测任务中表现不佳，特征表示存在缺陷。
- 方法要点：设计多任务框架，通过轻量级任务头和多粒度监督进行协作后训练。
- 实验或效果：在多种下游任务中验证有效性，获得适用于语言和像素级任务的通用视觉骨干。

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) have recently achieved remarkable success in visual-language understanding, demonstrating superior high-level semantic alignment within their vision encoders. An important question thus arises: Can these encoders serve as versatile vision backbones, capable of reliably performing classic vision-centric tasks as well? To address the question, we make the following contributions: (i) we identify that the vision encoders within MLLMs exhibit deficiencies in their dense feature representations, as evidenced by their suboptimal performance on dense prediction tasks (e.g., semantic segmentation, depth estimation); (ii) we propose VersaViT, a well-rounded vision transformer that instantiates a novel multi-task framework for collaborative post-training. This framework facilitates the optimization of the vision backbone via lightweight task heads with multi-granularity supervision; (iii) extensive experiments across various downstream tasks demonstrate the effectiveness of our method, yielding a versatile vision backbone suited for both language-mediated reasoning and pixel-level understanding.

