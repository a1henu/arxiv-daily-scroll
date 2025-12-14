---
layout: default
title: Empowering Dynamic Urban Navigation with Stereo and Mid-Level Vision
---

# Empowering Dynamic Urban Navigation with Stereo and Mid-Level Vision
**arXiv**：[2512.10956v1](https://arxiv.org/abs/2512.10956) · [PDF](https://arxiv.org/pdf/2512.10956.pdf)  
**作者**：Wentao Zhou, Xuweiyi Chen, Vignesh Rajagopal, Jeffrey Chen, Rohan Chandra, Zezhou Cheng  

**一句话要点**：提出StereoWalker，结合立体视觉与中层视觉模块以提升动态城市导航性能

**关键词**：立体视觉导航, 中层视觉模块, 动态场景理解, 深度估计, 像素跟踪, 机器人导航基础模型

## 3 点简述
- 问题：现有导航基础模型依赖单目视觉，忽略中层视觉先验，在动态场景中效率低下且受深度尺度模糊限制
- 方法：引入立体输入解决深度模糊，并集成深度估计和密集像素跟踪等中层视觉模块以增强几何与动态理解
- 效果：仅需1.5%训练数据即可达到先进水平，全数据下超越现有方法，立体视觉优于单目输入

## 摘要（原文）

> The success of foundation models in language and vision motivated research in fully end-to-end robot navigation foundation models (NFMs). NFMs directly map monocular visual input to control actions and ignore mid-level vision modules (tracking, depth estimation, etc) entirely. While the assumption that vision capabilities will emerge implicitly is compelling, it requires large amounts of pixel-to-action supervision that are difficult to obtain. The challenge is especially pronounced in dynamic and unstructured settings, where robust navigation requires precise geometric and dynamic understanding, while the depth-scale ambiguity in monocular views further limits accurate spatial reasoning. In this paper, we show that relying on monocular vision and ignoring mid-level vision priors is inefficient.
>   We present StereoWalker, which augments NFMs with stereo inputs and explicit mid-level vision such as depth estimation and dense pixel tracking. Our intuition is straightforward: stereo inputs resolve the depth-scale ambiguity, and modern mid-level vision models provide reliable geometric and motion structure in dynamic scenes. We also curate a large stereo navigation dataset with automatic action annotation from Internet stereo videos to support training of StereoWalker and to facilitate future research. Through our experiments, we find that mid-level vision enables StereoWalker to achieve a comparable performance as the state-of-the-art using only 1.5% of the training data, and surpasses the state-of-the-art using the full data. We also observe that stereo vision yields higher navigation performance than monocular input.

