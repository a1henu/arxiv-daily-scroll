---
layout: default
title: Text-Pass Filter: An Efficient Scene Text Detector
---

# Text-Pass Filter: An Efficient Scene Text Detector
**arXiv**：[2601.18098v1](https://arxiv.org/abs/2601.18098) · [PDF](https://arxiv.org/pdf/2601.18098.pdf)  
**作者**：Chuang Yang, Haozhao Ma, Xu Han, Yuan Yuan, Qi Wang  

**一句话要点**：提出Text-Pass Filter以高效检测任意形状文本，避免传统收缩-扩展策略的固有局限。

**关键词**：任意形状文本检测, 带通滤波器模拟, 特征-滤波器对, 实时文本检测, 前景背景区分

## 3 点简述
- 核心问题：传统收缩-扩展策略丢失文本边缘特征，混淆前景背景差异，限制文本识别。
- 方法要点：模拟带通滤波器，为每个文本构建特征-滤波器对，直接分割整体文本，无需复杂解码或后处理。
- 实验或效果：引入REU增强特征一致性，FPU提升前景背景区分，实验显示TPF在效率和准确性上优于现有方法。

## 摘要（原文）

> To pursue an efficient text assembling process, existing methods detect texts via the shrink-mask expansion strategy. However, the shrinking operation loses the visual features of text margins and confuses the foreground and background difference, which brings intrinsic limitations to recognize text features. We follow this issue and design Text-Pass Filter (TPF) for arbitrary-shaped text detection. It segments the whole text directly, which avoids the intrinsic limitations. It is noteworthy that different from previous whole text region-based methods, TPF can separate adhesive texts naturally without complex decoding or post-processing processes, which makes it possible for real-time text detection. Concretely, we find that the band-pass filter allows through components in a specified band of frequencies, called its passband but blocks components with frequencies above or below this band. It provides a natural idea for extracting whole texts separately. By simulating the band-pass filter, TPF constructs a unique feature-filter pair for each text. In the inference stage, every filter extracts the corresponding matched text by passing its pass-feature and blocking other features. Meanwhile, considering the large aspect ratio problem of ribbon-like texts makes it hard to recognize texts wholly, a Reinforcement Ensemble Unit (REU) is designed to enhance the feature consistency of the same text and to enlarge the filter's recognition field to help recognize whole texts. Furthermore, a Foreground Prior Unit (FPU) is introduced to encourage TPF to discriminate the difference between the foreground and background, which improves the feature-filter pair quality. Experiments demonstrate the effectiveness of REU and FPU while showing the TPF's superiority.

