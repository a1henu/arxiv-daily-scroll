---
layout: default
title: WS-IMUBench: Can Weakly Supervised Methods from Audio, Image, and Video Be Adapted for IMU-based Temporal Action Localization?
---

# WS-IMUBench: Can Weakly Supervised Methods from Audio, Image, and Video Be Adapted for IMU-based Temporal Action Localization?
**arXiv**：[2602.01850v1](https://arxiv.org/abs/2602.01850) · [PDF](https://arxiv.org/pdf/2602.01850.pdf)  
**作者**：Pei Li, Jiaxi Yin, Lei Ouyang, Shihan Pan, Ge Wang, Han Ding, Fei Wang  

**一句话要点**：提出WS-IMUBench基准，评估弱监督方法从音频、图像和视频迁移到IMU时序动作定位的效果。

**关键词**：弱监督学习, 时序动作定位, 惯性测量单元, 基准评估, 迁移学习, 序列标注

## 3 点简述
- 核心问题：IMU时序动作定位依赖密集帧级标注，成本高且难以扩展。
- 方法要点：系统评估七种弱监督方法在七个IMU数据集上的迁移性能，仅使用序列级标签。
- 实验或效果：发现迁移效果依赖模态，弱监督在有利数据集上可竞争，失败模式源于短动作和时序模糊。

## 摘要（原文）

> IMU-based Human Activity Recognition (HAR) has enabled a wide range of ubiquitous computing applications, yet its dominant clip classification paradigm cannot capture the rich temporal structure of real-world behaviors. This motivates a shift toward IMU Temporal Action Localization (IMU-TAL), which predicts both action categories and their start/end times in continuous streams. However, current progress is strongly bottlenecked by the need for dense, frame-level boundary annotations, which are costly and difficult to scale. To address this bottleneck, we introduce WS-IMUBench, a systematic benchmark study of weakly supervised IMU-TAL (WS-IMU-TAL) under only sequence-level labels. Rather than proposing a new localization algorithm, we evaluate how well established weakly supervised localization paradigms from audio, image, and video transfer to IMU-TAL under only sequence-level labels. We benchmark seven representative weakly supervised methods on seven public IMU datasets, resulting in over 3,540 model training runs and 7,080 inference evaluations. Guided by three research questions on transferability, effectiveness, and insights, our findings show that (i) transfer is modality-dependent, with temporal-domain methods generally more stable than image-derived proposal-based approaches; (ii) weak supervision can be competitive on favorable datasets (e.g., with longer actions and higher-dimensional sensing); and (iii) dominant failure modes arise from short actions, temporal ambiguity, and proposal quality. Finally, we outline concrete directions for advancing WS-IMU-TAL (e.g., IMU-specific proposal generation, boundary-aware objectives, and stronger temporal reasoning). Beyond individual results, WS-IMUBench establishes a reproducible benchmarking template, datasets, protocols, and analyses, to accelerate community-wide progress toward scalable WS-IMU-TAL.

