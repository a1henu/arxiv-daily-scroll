---
layout: default
title: Sound Source Localization for Spatial Mapping of Surgical Actions in Dynamic Scenes
---

# Sound Source Localization for Spatial Mapping of Surgical Actions in Dynamic Scenes
**arXiv**：[2510.24332v1](https://arxiv.org/abs/2510.24332) · [PDF](https://arxiv.org/pdf/2510.24332.pdf)  
**作者**：Jonas Hein, Lazaros Vlachopoulos, Maurits Geert Laurent Olthof, Bastian Sigrist, Philipp Fürnstahl, Matthias Seibold  

**一句话要点**：提出基于声源定位的4D音频-视觉框架，以增强动态手术场景的多模态理解。

**关键词**：声源定位, 手术场景理解, 多模态融合, 4D音频-视觉表示, 变换器检测

## 3 点简述
- 核心问题：当前手术场景理解依赖视觉或端到端学习，缺乏细粒度上下文建模。
- 方法要点：使用相控麦克风阵列和RGB-D相机，通过变换器检测声学事件并投影到动态点云。
- 实验或效果：在模拟手术中验证，实现准确3D声源定位和稳健多模态数据融合。

## 摘要（原文）

> Purpose: Surgical scene understanding is key to advancing computer-aided and
> intelligent surgical systems. Current approaches predominantly rely on visual
> data or end-to-end learning, which limits fine-grained contextual modeling.
> This work aims to enhance surgical scene representations by integrating 3D
> acoustic information, enabling temporally and spatially aware multimodal
> understanding of surgical environments.
>   Methods: We propose a novel framework for generating 4D audio-visual
> representations of surgical scenes by projecting acoustic localization
> information from a phased microphone array onto dynamic point clouds from an
> RGB-D camera. A transformer-based acoustic event detection module identifies
> relevant temporal segments containing tool-tissue interactions which are
> spatially localized in the audio-visual scene representation. The system was
> experimentally evaluated in a realistic operating room setup during simulated
> surgical procedures performed by experts.
>   Results: The proposed method successfully localizes surgical acoustic events
> in 3D space and associates them with visual scene elements. Experimental
> evaluation demonstrates accurate spatial sound localization and robust fusion
> of multimodal data, providing a comprehensive, dynamic representation of
> surgical activity.
>   Conclusion: This work introduces the first approach for spatial sound
> localization in dynamic surgical scenes, marking a significant advancement
> toward multimodal surgical scene representations. By integrating acoustic and
> visual data, the proposed framework enables richer contextual understanding and
> provides a foundation for future intelligent and autonomous surgical systems.

