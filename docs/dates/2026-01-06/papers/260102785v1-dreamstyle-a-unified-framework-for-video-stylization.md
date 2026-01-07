---
layout: default
title: DreamStyle: A Unified Framework for Video Stylization
---

# DreamStyle: A Unified Framework for Video Stylization
**arXiv**：[2601.02785v1](https://arxiv.org/abs/2601.02785) · [PDF](https://arxiv.org/pdf/2601.02785.pdf)  
**作者**：Mengtian Li, Jinshu Chen, Songtao Zhao, Wanquan Feng, Pengqi Tu, Qian He  

**一句话要点**：提出DreamStyle统一框架以解决视频风格化中条件单一和数据质量低的问题

**关键词**：视频风格化, 统一框架, LoRA训练, 风格一致性, 高质量数据集, 多条件引导

## 3 点简述
- 核心问题：现有方法局限于单一风格条件，且缺乏高质量数据集导致风格不一致和时间闪烁
- 方法要点：基于I2V模型，使用LoRA和特定令牌上矩阵支持文本、风格图像和首帧引导的视频风格化
- 实验或效果：在三种任务中表现优异，在风格一致性和视频质量上优于竞争对手

## 摘要（原文）

> Video stylization, an important downstream task of video generation models, has not yet been thoroughly explored. Its input style conditions typically include text, style image, and stylized first frame. Each condition has a characteristic advantage: text is more flexible, style image provides a more accurate visual anchor, and stylized first frame makes long-video stylization feasible. However, existing methods are largely confined to a single type of style condition, which limits their scope of application. Additionally, their lack of high-quality datasets leads to style inconsistency and temporal flicker. To address these limitations, we introduce DreamStyle, a unified framework for video stylization, supporting (1) text-guided, (2) style-image-guided, and (3) first-frame-guided video stylization, accompanied by a well-designed data curation pipeline to acquire high-quality paired video data. DreamStyle is built on a vanilla Image-to-Video (I2V) model and trained using a Low-Rank Adaptation (LoRA) with token-specific up matrices that reduces the confusion among different condition tokens. Both qualitative and quantitative evaluations demonstrate that DreamStyle is competent in all three video stylization tasks, and outperforms the competitors in style consistency and video quality.

