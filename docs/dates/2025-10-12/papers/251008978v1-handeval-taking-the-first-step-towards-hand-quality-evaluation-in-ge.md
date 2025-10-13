---
layout: default
title: HandEval: Taking the First Step Towards Hand Quality Evaluation in Generated Images
---

# HandEval: Taking the First Step Towards Hand Quality Evaluation in Generated Images
**arXiv**：[2510.08978v1](https://arxiv.org/abs/2510.08978) · [PDF](https://arxiv.org/pdf/2510.08978.pdf)  
**作者**：Zichuan Wang, Bo Peng, Songlin Yang, Zhenchen Tang, Jing Dong  
**一句话要点**：提出HandEval以评估生成图像中手部质量，提升下游任务性能

**关键词**：手部质量评估, 文本到图像生成, 多模态大语言模型, AIGC检测, 数据集构建

## 3 点简述
- 文本到图像模型在复杂局部区域如手部生成细节不准确，影响整体视觉质量
- 基于HandPair数据集和MLLM，开发HandEval模型，结合手部关键点先验知识
- 实验显示HandEval优于现有方法，在图像生成和AIGC检测中显著提升效果

## 摘要（原文）

> Although recent text-to-image (T2I) models have significantly improved the
> overall visual quality of generated images, they still struggle in the
> generation of accurate details in complex local regions, especially human
> hands. Generated hands often exhibit structural distortions and unrealistic
> textures, which can be very noticeable even when the rest of the body is
> well-generated. However, the quality assessment of hand regions remains largely
> neglected, limiting downstream task performance like human-centric generation
> quality optimization and AIGC detection. To address this, we propose the first
> quality assessment task targeting generated hand regions and showcase its
> abundant downstream applications. We first introduce the HandPair dataset for
> training hand quality assessment models. It consists of 48k images formed by
> high- and low-quality hand pairs, enabling low-cost, efficient supervision
> without manual annotation. Based on it, we develop HandEval, a carefully
> designed hand-specific quality assessment model. It leverages the powerful
> visual understanding capability of Multimodal Large Language Model (MLLM) and
> incorporates prior knowledge of hand keypoints, gaining strong perception of
> hand quality. We further construct a human-annotated test set with hand images
> from various state-of-the-art (SOTA) T2I models to validate its quality
> evaluation capability. Results show that HandEval aligns better with human
> judgments than existing SOTA methods. Furthermore, we integrate HandEval into
> image generation and AIGC detection pipelines, prominently enhancing generated
> hand realism and detection accuracy, respectively, confirming its universal
> effectiveness in downstream applications. Code and dataset will be available.

