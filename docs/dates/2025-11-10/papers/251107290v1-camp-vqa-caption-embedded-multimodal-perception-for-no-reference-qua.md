---
layout: default
title: CAMP-VQA: Caption-Embedded Multimodal Perception for No-Reference Quality Assessment of Compressed Video
---

# CAMP-VQA: Caption-Embedded Multimodal Perception for No-Reference Quality Assessment of Compressed Video
**arXiv**：[2511.07290v1](https://arxiv.org/abs/2511.07290) · [PDF](https://arxiv.org/pdf/2511.07290.pdf)  
**作者**：Xinyi Wang, Angeliki Katsenou, Junxiao Shen, David Bull  

**一句话要点**：提出CAMP-VQA框架，利用多模态感知评估压缩视频质量，优化用户生成内容交付。

**关键词**：无参考视频质量评估, 多模态感知, 用户生成内容, 压缩视频, 质量感知提示, BLIP-2模型

## 3 点简述
- 核心问题：用户生成视频的非专业采集与转码导致无参考质量评估困难，缺乏细粒度伪影标注。
- 方法要点：结合视频元数据和帧间变化，通过质量感知提示生成细粒度质量描述，融合多模态特征回归质量分数。
- 实验或效果：在多个数据集上优于现有方法，SRCC达0.928，无需昂贵人工标注。

## 摘要（原文）

> The prevalence of user-generated content (UGC) on platforms such as YouTube
> and TikTok has rendered no-reference (NR) perceptual video quality assessment
> (VQA) vital for optimizing video delivery. Nonetheless, the characteristics of
> non-professional acquisition and the subsequent transcoding of UGC video on
> sharing platforms present significant challenges for NR-VQA. Although NR-VQA
> models attempt to infer mean opinion scores (MOS), their modeling of subjective
> scores for compressed content remains limited due to the absence of
> fine-grained perceptual annotations of artifact types. To address these
> challenges, we propose CAMP-VQA, a novel NR-VQA framework that exploits the
> semantic understanding capabilities of large vision-language models. Our
> approach introduces a quality-aware prompting mechanism that integrates video
> metadata (e.g., resolution, frame rate, bitrate) with key fragments extracted
> from inter-frame variations to guide the BLIP-2 pretraining approach in
> generating fine-grained quality captions. A unified architecture has been
> designed to model perceptual quality across three dimensions: semantic
> alignment, temporal characteristics, and spatial characteristics. These
> multimodal features are extracted and fused, then regressed to video quality
> scores. Extensive experiments on a wide variety of UGC datasets demonstrate
> that our model consistently outperforms existing NR-VQA methods, achieving
> improved accuracy without the need for costly manual fine-grained annotations.
> Our method achieves the best performance in terms of average rank and linear
> correlation (SRCC: 0.928, PLCC: 0.938) compared to state-of-the-art methods.
> The source code and trained models, along with a user-friendly demo, are
> available at: https://github.com/xinyiW915/CAMP-VQA.

