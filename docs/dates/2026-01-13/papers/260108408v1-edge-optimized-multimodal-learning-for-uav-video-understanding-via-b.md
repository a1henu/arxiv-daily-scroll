---
layout: default
title: Edge-Optimized Multimodal Learning for UAV Video Understanding via BLIP-2
---

# Edge-Optimized Multimodal Learning for UAV Video Understanding via BLIP-2
**arXiv**：[2601.08408v1](https://arxiv.org/abs/2601.08408) · [PDF](https://arxiv.org/pdf/2601.08408.pdf)  
**作者**：Yizhan Feng, Hichem Snoussi, Jing Teng, Jian Liu, Yuyang Wang, Abel Cherouat, Tian Wang  

**一句话要点**：提出基于BLIP-2的轻量级多模态任务平台，以解决无人机边缘设备计算资源有限与视觉语言模型高计算成本之间的矛盾。

**关键词**：无人机视频理解, 边缘计算优化, 多模态学习, 轻量级模型, 关键帧采样, 提示优化

## 3 点简述
- 核心问题：无人机边缘设备计算资源有限，难以部署大型视觉语言模型进行实时视觉理解。
- 方法要点：集成BLIP-2与YOLO模型，设计内容感知关键帧采样和统一提示优化方案，扩展多任务能力。
- 实验或效果：未知，但方法旨在无需无人机数据特定微调下，提升视频级交互任务的准确性和上下文相关性。

## 摘要（原文）

> The demand for real-time visual understanding and interaction in complex scenarios is increasingly critical for unmanned aerial vehicles. However, a significant challenge arises from the contradiction between the high computational cost of large Vision language models and the limited computing resources available on UAV edge devices. To address this challenge, this paper proposes a lightweight multimodal task platform based on BLIP-2, integrated with YOLO-World and YOLOv8-Seg models. This integration extends the multi-task capabilities of BLIP-2 for UAV applications with minimal adaptation and without requiring task-specific fine-tuning on drone data. Firstly, the deep integration of BLIP-2 with YOLO models enables it to leverage the precise perceptual results of YOLO for fundamental tasks like object detection and instance segmentation, thereby facilitating deeper visual-attention understanding and reasoning. Secondly, a content-aware key frame sampling mechanism based on K-Means clustering is designed, which incorporates intelligent frame selection and temporal feature concatenation. This equips the lightweight BLIP-2 architecture with the capability to handle video-level interactive tasks effectively. Thirdly, a unified prompt optimization scheme for multi-task adaptation is implemented. This scheme strategically injects structured event logs from the YOLO models as contextual information into BLIP-2's input. Combined with output constraints designed to filter out technical details, this approach effectively guides the model to generate accurate and contextually relevant outputs for various tasks.

