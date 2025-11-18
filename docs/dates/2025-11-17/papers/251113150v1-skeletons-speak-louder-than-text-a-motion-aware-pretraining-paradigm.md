---
layout: default
title: Skeletons Speak Louder than Text: A Motion-Aware Pretraining Paradigm for Video-Based Person Re-Identification
---

# Skeletons Speak Louder than Text: A Motion-Aware Pretraining Paradigm for Video-Based Person Re-Identification
**arXiv**：[2511.13150v1](https://arxiv.org/abs/2511.13150) · [PDF](https://arxiv.org/pdf/2511.13150.pdf)  
**作者**：Rifen Lin, Alex Jinpeng Wang, Jiawei Mo, Min Li  

**一句话要点**：提出骨架驱动的预训练框架CSIP-ReID，以解决视频行人重识别中文本模态无法捕捉细粒度运动的问题。

**关键词**：视频行人重识别, 骨架序列, 对比学习, 多模态预训练, 时序建模, 泛化能力

## 3 点简述
- 核心问题：文本模态在视频行人重识别中难以捕捉细粒度时间运动，导致现有方法缺乏真正多模态预训练。
- 方法要点：采用对比学习对齐骨架与视觉特征，并引入原型融合更新器和骨架引导时序建模模块。
- 实验或效果：在标准视频ReID基准上达到新SOTA，并在骨架ReID任务中表现出强泛化能力。

## 摘要（原文）

> Multimodal pretraining has revolutionized visual understanding, but its impact on video-based person re-identification (ReID) remains underexplored. Existing approaches often rely on video-text pairs, yet suffer from two fundamental limitations: (1) lack of genuine multimodal pretraining, and (2) text poorly captures fine-grained temporal motion-an essential cue for distinguishing identities in video. In this work, we take a bold departure from text-based paradigms by introducing the first skeleton-driven pretraining framework for ReID. To achieve this, we propose Contrastive Skeleton-Image Pretraining for ReID (CSIP-ReID), a novel two-stage method that leverages skeleton sequences as a spatiotemporally informative modality aligned with video frames. In the first stage, we employ contrastive learning to align skeleton and visual features at sequence level. In the second stage, we introduce a dynamic Prototype Fusion Updater (PFU) to refine multimodal identity prototypes, fusing motion and appearance cues. Moreover, we propose a Skeleton Guided Temporal Modeling (SGTM) module that distills temporal cues from skeleton data and integrates them into visual features. Extensive experiments demonstrate that CSIP-ReID achieves new state-of-the-art results on standard video ReID benchmarks (MARS, LS-VID, iLIDS-VID). Moreover, it exhibits strong generalization to skeleton-only ReID tasks (BIWI, IAS), significantly outperforming previous methods. CSIP-ReID pioneers an annotation-free and motion-aware pretraining paradigm for ReID, opening a new frontier in multimodal representation learning.

