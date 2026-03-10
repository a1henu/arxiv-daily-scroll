---
layout: default
title: Foley-Flow: Coordinated Video-to-Audio Generation with Masked Audio-Visual Alignment and Dynamic Conditional Flows
---

# Foley-Flow: Coordinated Video-to-Audio Generation with Masked Audio-Visual Alignment and Dynamic Conditional Flows
**arXiv**：[2603.08126v1](https://arxiv.org/abs/2603.08126) · [PDF](https://arxiv.org/pdf/2603.08126.pdf)  
**作者**：Shentong Mo, Yibing Song  

**一句话要点**：提出FoleyFlow以解决视频到音频生成中的语义与节奏对齐问题

**关键词**：视频到音频生成, 音频-视觉对齐, 掩码建模, 动态条件流, 节奏同步, 语义一致性

## 3 点简述
- 核心问题：现有方法在视频到音频生成中难以实现语义和节奏的严格对齐
- 方法要点：通过掩码建模训练对齐单模态编码器，并利用动态条件流进行音频生成
- 实验或效果：在标准基准测试中性能超越现有方法，生成音频在语义和节奏上更协调

## 摘要（原文）

> Coordinated audio generation based on video inputs typically requires a strict audio-visual (AV) alignment, where both semantics and rhythmics of the generated audio segments shall correspond to those in the video frames. Previous studies leverage a two-stage design where the AV encoders are firstly aligned via contrastive learning, then the encoded video representations guide the audio generation process. We observe that both contrastive learning and global video guidance are effective in aligning overall AV semantics while limiting temporally rhythmic synchronization. In this work, we propose FoleyFlow to first align unimodal AV encoders via masked modeling training, where the masked audio segments are recovered under the guidance of the corresponding video segments. After training, the AV encoders which are separately pretrained using only unimodal data are aligned with semantic and rhythmic consistency. Then, we develop a dynamic conditional flow for the final audio generation. Built upon the efficient velocity flow generation framework, our dynamic conditional flow utilizes temporally varying video features as the dynamic condition to guide corresponding audio segment generations. To this end, we extract coherent semantic and rhythmic representations during masked AV alignment, and use this representation of video segments to guide audio generation temporally. Our audio results are evaluated on the standard benchmarks and largely surpass existing results under several metrics. The superior performance indicates that FoleyFlow is effective in generating coordinated audios that are both semantically and rhythmically coherent to various video sequences.

