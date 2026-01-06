---
layout: default
title: Seeing the Unseen: Zooming in the Dark with Event Cameras
---

# Seeing the Unseen: Zooming in the Dark with Event Cameras
**arXiv**：[2601.02206v1](https://arxiv.org/abs/2601.02206) · [PDF](https://arxiv.org/pdf/2601.02206.pdf)  
**作者**：Dachun Kai, Zeyu Xiao, Huyue Zhu, Jiaxiao Wang, Yueyi Zhang, Xiaoyan Sun  

**一句话要点**：提出RetinexEVSR框架，利用事件相机和Retinex先验解决低光视频超分辨率问题。

**关键词**：低光视频超分辨率, 事件相机, Retinex模型, 跨模态融合, 双向融合策略

## 3 点简述
- 核心问题：低光低分辨率视频恢复细节困难，现有方法因对比度低和高频信息不足而受限。
- 方法要点：引入双向跨模态融合策略，结合事件信号和RGB帧，通过光照引导和事件引导模块增强细节。
- 实验或效果：在三个数据集上达到最先进性能，SDSD基准上提升2.95 dB并减少65%运行时间。

## 摘要（原文）

> This paper addresses low-light video super-resolution (LVSR), aiming to restore high-resolution videos from low-light, low-resolution (LR) inputs. Existing LVSR methods often struggle to recover fine details due to limited contrast and insufficient high-frequency information. To overcome these challenges, we present RetinexEVSR, the first event-driven LVSR framework that leverages high-contrast event signals and Retinex-inspired priors to enhance video quality under low-light scenarios. Unlike previous approaches that directly fuse degraded signals, RetinexEVSR introduces a novel bidirectional cross-modal fusion strategy to extract and integrate meaningful cues from noisy event data and degraded RGB frames. Specifically, an illumination-guided event enhancement module is designed to progressively refine event features using illumination maps derived from the Retinex model, thereby suppressing low-light artifacts while preserving high-contrast details. Furthermore, we propose an event-guided reflectance enhancement module that utilizes the enhanced event features to dynamically recover reflectance details via a multi-scale fusion mechanism. Experimental results show that our RetinexEVSR achieves state-of-the-art performance on three datasets. Notably, on the SDSD benchmark, our method can get up to 2.95 dB gain while reducing runtime by 65% compared to prior event-based methods. Code: https://github.com/DachunKai/RetinexEVSR.

