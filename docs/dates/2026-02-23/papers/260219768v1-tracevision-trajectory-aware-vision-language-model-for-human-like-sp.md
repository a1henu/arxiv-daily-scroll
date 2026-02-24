---
layout: default
title: TraceVision: Trajectory-Aware Vision-Language Model for Human-Like Spatial Understanding
---

# TraceVision: Trajectory-Aware Vision-Language Model for Human-Like Spatial Understanding
**arXiv**：[2602.19768v1](https://arxiv.org/abs/2602.19768) · [PDF](https://arxiv.org/pdf/2602.19768.pdf)  
**作者**：Fan Yang, Shurong Zheng, Hongyin Zhao, Yufei Zhan, Xin Li, Yousong Zhu, Chaoyang Zhao Ming Tang, Jinqiao Wang  

**一句话要点**：提出TraceVision轨迹感知视觉语言模型，以解决现有模型在模拟人类视觉注意轨迹和区域关联解释方面的不足。

**关键词**：轨迹感知视觉语言模型, 视觉注意轨迹, 区域关联解释, 轨迹引导分割, 视频场景理解, 三阶段训练

## 3 点简述
- 核心问题：现有大型视觉语言模型侧重于全局图像理解，难以模拟人类视觉注意轨迹和解释描述与特定区域的关联。
- 方法要点：设计轨迹感知视觉感知模块，通过几何简化提取语义关键点，并采用三阶段训练管道引导描述生成和区域定位。
- 实验或效果：在轨迹引导描述、文本引导轨迹预测、理解和分割等任务上实现最先进性能，支持跨帧跟踪和时间注意分析。

## 摘要（原文）

> Recent Large Vision-Language Models (LVLMs) demonstrate remarkable capabilities in image understanding and natural language generation. However, current approaches focus predominantly on global image understanding, struggling to simulate human visual attention trajectories and explain associations between descriptions and specific regions. We propose TraceVision, a unified vision-language model integrating trajectory-aware spatial understanding in an end-to-end framework. TraceVision employs a Trajectory-aware Visual Perception (TVP) module for bidirectional fusion of visual features and trajectory information. We design geometric simplification to extract semantic keypoints from raw trajectories and propose a three-stage training pipeline where trajectories guide description generation and region localization. We extend TraceVision to trajectory-guided segmentation and video scene understanding, enabling cross-frame tracking and temporal attention analysis. We construct the Reasoning-based Interactive Localized Narratives (RILN) dataset to enhance logical reasoning and interpretability. Extensive experiments on trajectory-guided captioning, text-guided trajectory prediction, understanding, and segmentation demonstrate that TraceVision achieves state-of-the-art performance, establishing a foundation for intuitive spatial interaction and interpretable visual understanding.

