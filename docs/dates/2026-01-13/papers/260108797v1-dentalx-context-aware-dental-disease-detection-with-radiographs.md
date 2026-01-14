---
layout: default
title: DentalX: Context-Aware Dental Disease Detection with Radiographs
---

# DentalX: Context-Aware Dental Disease Detection with Radiographs
**arXiv**：[2601.08797v1](https://arxiv.org/abs/2601.08797) · [PDF](https://arxiv.org/pdf/2601.08797.pdf)  
**作者**：Zhi Qin Tan, Xiatian Zhu, Owen Addison, Yunpeng Li  

**一句话要点**：提出DentalX，利用口腔结构信息增强X光片中的牙科疾病检测，以解决视觉模糊问题。

**关键词**：牙科疾病检测, X光片分析, 上下文感知, 语义分割, 结构信息整合

## 3 点简述
- 核心问题：牙科X光片疾病检测因视觉证据细微而困难，现有方法基于自然图像检测模型效果不佳。
- 方法要点：引入结构上下文提取模块，通过牙科解剖语义分割辅助任务，整合结构信息到疾病检测中。
- 实验或效果：在专用基准测试中，DentalX显著优于先前方法，两个任务相互受益于模型优化。

## 摘要（原文）

> Diagnosing dental diseases from radiographs is time-consuming and challenging due to the subtle nature of diagnostic evidence. Existing methods, which rely on object detection models designed for natural images with more distinct target patterns, struggle to detect dental diseases that present with far less visual support. To address this challenge, we propose {\bf DentalX}, a novel context-aware dental disease detection approach that leverages oral structure information to mitigate the visual ambiguity inherent in radiographs. Specifically, we introduce a structural context extraction module that learns an auxiliary task: semantic segmentation of dental anatomy. The module extracts meaningful structural context and integrates it into the primary disease detection task to enhance the detection of subtle dental diseases. Extensive experiments on a dedicated benchmark demonstrate that DentalX significantly outperforms prior methods in both tasks. This mutual benefit arises naturally during model optimization, as the correlation between the two tasks is effectively captured. Our code is available at https://github.com/zhiqin1998/DentYOLOX.

