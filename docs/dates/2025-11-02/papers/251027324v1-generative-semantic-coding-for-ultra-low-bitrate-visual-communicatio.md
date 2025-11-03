---
layout: default
title: Generative Semantic Coding for Ultra-Low Bitrate Visual Communication and Analysis
---

# Generative Semantic Coding for Ultra-Low Bitrate Visual Communication and Analysis
**arXiv**：[2510.27324v1](https://arxiv.org/abs/2510.27324) · [PDF](https://arxiv.org/pdf/2510.27324.pdf)  
**作者**：Weiming Chen, Yijia Wang, Zhihan Zhu, Zhihai He  

**一句话要点**：提出生成语义编码方法，用于超低码率视觉通信与分析

**关键词**：超低码率视觉通信, 生成语义编码, 修正流模型, 视觉场景重建, 远程视觉分析

## 3 点简述
- 核心问题：超低码率下如何准确重建视觉场景，不牺牲分析精度
- 方法要点：结合文本描述与编码潜变量，引导修正流模型精确生成
- 实验效果：相同质量下，比现有方法显著降低带宽需求

## 摘要（原文）

> We consider the problem of ultra-low bit rate visual communication for remote
> vision analysis, human interactions and control in challenging scenarios with
> very low communication bandwidth, such as deep space exploration, battlefield
> intelligence, and robot navigation in complex environments. In this paper, we
> ask the following important question: can we accurately reconstruct the visual
> scene using only a very small portion of the bit rate in existing coding
> methods while not sacrificing the accuracy of vision analysis and performance
> of human interactions? Existing text-to-image generation models offer a new
> approach for ultra-low bitrate image description. However, they can only
> achieve a semantic-level approximation of the visual scene, which is far
> insufficient for the purpose of visual communication and remote vision analysis
> and human interactions. To address this important issue, we propose to
> seamlessly integrate image generation with deep image compression, using joint
> text and coding latent to guide the rectified flow models for precise
> generation of the visual scene. The semantic text description and coding latent
> are both encoded and transmitted to the decoder at a very small bit rate.
> Experimental results demonstrate that our method can achieve the same image
> reconstruction quality and vision analysis accuracy as existing methods while
> using much less bandwidth. The code will be released upon paper acceptance.

