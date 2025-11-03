---
layout: default
title: Generating Accurate and Detailed Captions for High-Resolution Images
---

# Generating Accurate and Detailed Captions for High-Resolution Images
**arXiv**：[2510.27164v1](https://arxiv.org/abs/2510.27164) · [PDF](https://arxiv.org/pdf/2510.27164.pdf)  
**作者**：Hankyeol Lee, Gawon Seo, Kyounggyu Lee, Dogun Kim, Kyungwoo Song, Jiyoung Jung  

**一句话要点**：提出多阶段管道以增强高分辨率图像的准确详细描述

**关键词**：高分辨率图像描述, 视觉语言模型, 对象检测, 幻觉减少, 多模态集成

## 3 点简述
- 核心问题：视觉语言模型在低分辨率预训练下，对高分辨率图像生成描述时丢失细节和对象。
- 方法要点：集成视觉语言模型、大语言模型和对象检测，通过对象识别与验证丰富描述。
- 实验或效果：在定制数据集上评估，显示描述更详细可靠，并有效减少幻觉。

## 摘要（原文）

> Vision-language models (VLMs) often struggle to generate accurate and
> detailed captions for high-resolution images since they are typically
> pre-trained on low-resolution inputs (e.g., 224x224 or 336x336 pixels).
> Downscaling high-resolution images to these dimensions may result in the loss
> of visual details and the omission of important objects. To address this
> limitation, we propose a novel pipeline that integrates vision-language models,
> large language models (LLMs), and object detection systems to enhance caption
> quality. Our proposed pipeline refines captions through a novel, multi-stage
> process. Given a high-resolution image, an initial caption is first generated
> using a VLM, and key objects in the image are then identified by an LLM. The
> LLM predicts additional objects likely to co-occur with the identified key
> objects, and these predictions are verified by object detection systems. Newly
> detected objects not mentioned in the initial caption undergo focused,
> region-specific captioning to ensure they are incorporated. This process
> enriches caption detail while reducing hallucinations by removing references to
> undetected objects. We evaluate the enhanced captions using pairwise comparison
> and quantitative scoring from large multimodal models, along with a benchmark
> for hallucination detection. Experiments on a curated dataset of
> high-resolution images demonstrate that our pipeline produces more detailed and
> reliable image captions while effectively minimizing hallucinations.

