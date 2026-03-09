---
layout: default
title: PatchCue: Enhancing Vision-Language Model Reasoning with Patch-Based Visual Cues
---

# PatchCue: Enhancing Vision-Language Model Reasoning with Patch-Based Visual Cues
**arXiv**：[2603.05869v1](https://arxiv.org/abs/2603.05869) · [PDF](https://arxiv.org/pdf/2603.05869.pdf)  
**作者**：Yukun Qi, Pei Fu, Hang Li, Yuhan Liu, Chao Jiang, Bin Qin, Zhenbo Luo, Jian Luan  

**一句话要点**：提出PatchCue以增强视觉语言模型的视觉推理能力，通过基于图像块的视觉提示范式。

**关键词**：视觉语言模型, 视觉推理, 图像块提示, 强化学习, 过程监督, 多模态理解

## 3 点简述
- 现有视觉语言模型推理方法如思维链依赖文本，未充分利用视觉信息，像素级提示需精确定位增加学习复杂度。
- PatchCue将图像分割为块，在块级别表示视觉提示，更符合人类感知习惯，并利用现代视觉语言模型的块标记化输入。
- 采用两阶段训练：监督微调输出块级提示，强化学习使用过程监督奖励引导中间推理步骤，实验表明在多项基准上提升性能。

## 摘要（原文）

> Vision-Language Models (VLMs) have achieved remarkable progress on a wide range of challenging multimodal understanding and reasoning tasks. However, existing reasoning paradigms, such as the classical Chain-of-Thought (CoT), rely solely on textual information and often underutilize important visual cues. While prior work has incorporated pixel-level visual cues, these representations require precise spatial localization, introducing additional learning complexity. To address this, we propose PatchCue, a novel patch-based visual cue paradigm designed to significantly enhance the visual reasoning capabilities of VLMs. By partitioning images into patches and representing cues at the patch level, PatchCue aligns better with human perceptual habits and leverages the patch-tokenized input of modern VLMs. We train VLMs using a two-stage approach: cold-start supervised fine-tuning to output patch-level cues, followed by reinforcement learning with a process-supervised cue reward that guides intermediate visual reasoning steps. Extensive experiments on multiple VLMs and diverse benchmarks, including general visual question answering, complex reasoning, and document understanding, demonstrate that PatchCue consistently improves overall model performance. Our results show that patch-level cues outperform both pixel-level bounding boxes and point-based cues, providing a more effective and cognitively aligned visual reasoning paradigm.

