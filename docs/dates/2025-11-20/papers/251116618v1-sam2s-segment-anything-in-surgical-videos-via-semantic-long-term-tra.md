---
layout: default
title: SAM2S: Segment Anything in Surgical Videos via Semantic Long-term Tracking
---

# SAM2S: Segment Anything in Surgical Videos via Semantic Long-term Tracking
**arXiv**：[2511.16618v1](https://arxiv.org/abs/2511.16618) · [PDF](https://arxiv.org/pdf/2511.16618.pdf)  
**作者**：Haofeng Liu, Ziyue Wang, Sudhanshu Mishra, Mingqi Gao, Guanyi Qin, Chang Han Low, Alex Y. W. Kong, Yueming Jin  

**一句话要点**：提出SAM2S模型以解决手术视频中长时跟踪与语义分割的挑战

**关键词**：手术视频分割, 长时跟踪, 语义学习, 零样本泛化, 交互式分割, 基准数据集

## 3 点简述
- 核心问题：手术视频分割存在领域差异和长时跟踪不足，影响零样本泛化。
- 方法要点：引入DiveMem机制和语义学习，增强SAM2的长时跟踪与抗歧义能力。
- 实验或效果：在SA-SV基准上，SAM2S达到80.42平均J&F，提升17.10点，支持实时推理。

## 摘要（原文）

> Surgical video segmentation is crucial for computer-assisted surgery, enabling precise localization and tracking of instruments and tissues. Interactive Video Object Segmentation (iVOS) models such as Segment Anything Model 2 (SAM2) provide prompt-based flexibility beyond methods with predefined categories, but face challenges in surgical scenarios due to the domain gap and limited long-term tracking. To address these limitations, we construct SA-SV, the largest surgical iVOS benchmark with instance-level spatio-temporal annotations (masklets) spanning eight procedure types (61k frames, 1.6k masklets), enabling comprehensive development and evaluation for long-term tracking and zero-shot generalization. Building on SA-SV, we propose SAM2S, a foundation model enhancing \textbf{SAM2} for \textbf{S}urgical iVOS through: (1) DiveMem, a trainable diverse memory mechanism for robust long-term tracking; (2) temporal semantic learning for instrument understanding; and (3) ambiguity-resilient learning to mitigate annotation inconsistencies across multi-source datasets. Extensive experiments demonstrate that fine-tuning on SA-SV enables substantial performance gains, with SAM2 improving by 12.99 average $\mathcal{J}$\&$\mathcal{F}$ over vanilla SAM2. SAM2S further advances performance to 80.42 average $\mathcal{J}$\&$\mathcal{F}$, surpassing vanilla and fine-tuned SAM2 by 17.10 and 4.11 points respectively, while maintaining 68 FPS real-time inference and strong zero-shot generalization. Code and dataset will be released at https://jinlab-imvr.github.io/SAM2S.

