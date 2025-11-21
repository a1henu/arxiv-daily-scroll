---
layout: default
title: SwiTrack: Tri-State Switch for Cross-Modal Object Tracking
---

# SwiTrack: Tri-State Switch for Cross-Modal Object Tracking
**arXiv**：[2511.16227v1](https://arxiv.org/abs/2511.16227) · [PDF](https://arxiv.org/pdf/2511.16227.pdf)  
**作者**：Boyue Xu, Ruichao Hou, Tongwei Ren, Dongming Zhou, Gangshan Wu, Jinde Cao  

**一句话要点**：提出SwiTrack三态切换框架以解决跨模态目标跟踪中的特征提取与漂移问题

**关键词**：跨模态目标跟踪, RGB-NIR跟踪, 三态切换框架, 特征校准, 目标漂移缓解, 实时跟踪

## 3 点简述
- 核心问题：现有方法在RGB-NIR跨模态跟踪中难以提取模态特有特征并易发生目标漂移
- 方法要点：采用三流架构，包括视觉编码器、NIR门控适配器和一致性轨迹预测模块
- 实验或效果：在基准测试中精度和成功率分别提升7.2%和4.3%，实时跟踪达65帧/秒

## 摘要（原文）

> Cross-modal object tracking (CMOT) is an emerging task that maintains target consistency while the video stream switches between different modalities, with only one modality available in each frame, mostly focusing on RGB-Near Infrared (RGB-NIR) tracking. Existing methods typically connect parallel RGB and NIR branches to a shared backbone, which limits the comprehensive extraction of distinctive modality-specific features and fails to address the issue of object drift, especially in the presence of unreliable inputs. In this paper, we propose SwiTrack, a novel state-switching framework that redefines CMOT through the deployment of three specialized streams. Specifically, RGB frames are processed by the visual encoder, while NIR frames undergo refinement via a NIR gated adapter coupled with the visual encoder to progressively calibrate shared latent space features, thereby yielding more robust cross-modal representations. For invalid modalities, a consistency trajectory prediction module leverages spatio-temporal cues to estimate target movement, ensuring robust tracking and mitigating drift. Additionally, we incorporate dynamic template reconstruction to iteratively update template features and employ a similarity alignment loss to reinforce feature consistency. Experimental results on the latest benchmarks demonstrate that our tracker achieves state-of-the-art performance, boosting precision rate and success rate gains by 7.2\% and 4.3\%, respectively, while maintaining real-time tracking at 65 frames per second. Code and models are available at https://github.com/xuboyue1999/SwiTrack.git.

