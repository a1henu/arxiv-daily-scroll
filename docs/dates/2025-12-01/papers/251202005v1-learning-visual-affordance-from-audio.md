---
layout: default
title: Learning Visual Affordance from Audio
---

# Learning Visual Affordance from Audio
**arXiv**：[2512.02005v1](https://arxiv.org/abs/2512.02005) · [PDF](https://arxiv.org/pdf/2512.02005.pdf)  
**作者**：Lidong Lu, Guo Chen, Zhu Wei, Yicheng Liu, Tong Lu  

**一句话要点**：提出AVAGFormer模型，通过音频信号分割物体交互区域以解决视觉遮挡或歧义问题。

**关键词**：音频-视觉交互, 物体交互分割, 跨模态融合, 零样本学习, 数据集构建

## 3 点简述
- 核心问题：现有方法依赖文本或视频，易受歧义或遮挡限制，需更直观的交互区域理解。
- 方法要点：构建首个AV-AG数据集，提出AVAGFormer模型，融合音频与视觉信号进行掩码预测。
- 实验或效果：AVAGFormer在AV-AG任务上达到最先进性能，超越相关基线，支持零样本泛化评估。

## 摘要（原文）

> We introduce Audio-Visual Affordance Grounding (AV-AG), a new task that segments object interaction regions from action sounds. Unlike existing approaches that rely on textual instructions or demonstration videos, which often limited by ambiguity or occlusion, audio provides real-time, semantically rich, and visually independent cues for affordance grounding, enabling more intuitive understanding of interaction regions. To support this task, we construct the first AV-AG dataset, comprising a large collection of action sounds, object images, and pixel-level affordance annotations. The dataset also includes an unseen subset to evaluate zero-shot generalization. Furthermore, we propose AVAGFormer, a model equipped with a semantic-conditioned cross-modal mixer and a dual-head decoder that effectively fuses audio and visual signals for mask prediction. Experiments show that AVAGFormer achieves state-of-the-art performance on AV-AG, surpassing baselines from related tasks. Comprehensive analyses highlight the distinctions between AV-AG and AVS, the benefits of end-to-end modeling, and the contribution of each component. Code and dataset have been released on https://jscslld.github.io/AVAGFormer/.

