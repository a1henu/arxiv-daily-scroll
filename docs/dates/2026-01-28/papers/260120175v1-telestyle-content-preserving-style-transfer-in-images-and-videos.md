---
layout: default
title: TeleStyle: Content-Preserving Style Transfer in Images and Videos
---

# TeleStyle: Content-Preserving Style Transfer in Images and Videos
**arXiv**：[2601.20175v1](https://arxiv.org/abs/2601.20175) · [PDF](https://arxiv.org/pdf/2601.20175.pdf)  
**作者**：Shiwen Zhang, Xiaoyan Yang, Bojia Zi, Haibin Huang, Chi Zhang, Xuelong Li  

**一句话要点**：提出TeleStyle以解决扩散变换器中内容与风格特征纠缠问题，实现图像与视频内容保持的风格迁移。

**关键词**：内容保持风格迁移, 扩散变换器, 课程持续学习, 视频风格化, 轻量模型, 美学质量评估

## 3 点简述
- 核心问题：扩散变换器内部表示中内容与风格特征纠缠，导致内容保持风格迁移困难。
- 方法要点：基于Qwen-Image-Edit构建轻量模型，采用课程持续学习框架训练混合数据集，并引入视频模块增强时序一致性。
- 实验或效果：在风格相似性、内容一致性和美学质量三个核心指标上达到最先进性能。

## 摘要（原文）

> Content-preserving style transfer, generating stylized outputs based on content and style references, remains a significant challenge for Diffusion Transformers (DiTs) due to the inherent entanglement of content and style features in their internal representations. In this technical report, we present TeleStyle, a lightweight yet effective model for both image and video stylization. Built upon Qwen-Image-Edit, TeleStyle leverages the base model's robust capabilities in content preservation and style customization. To facilitate effective training, we curated a high-quality dataset of distinct specific styles and further synthesized triplets using thousands of diverse, in-the-wild style categories. We introduce a Curriculum Continual Learning framework to train TeleStyle on this hybrid dataset of clean (curated) and noisy (synthetic) triplets. This approach enables the model to generalize to unseen styles without compromising precise content fidelity. Additionally, we introduce a video-to-video stylization module to enhance temporal consistency and visual quality. TeleStyle achieves state-of-the-art performance across three core evaluation metrics: style similarity, content consistency, and aesthetic quality. Code and pre-trained models are available at https://github.com/Tele-AI/TeleStyle

