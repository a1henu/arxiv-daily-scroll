---
layout: default
title: AV-Unified: A Unified Framework for Audio-visual Scene Understanding
---

# AV-Unified: A Unified Framework for Audio-visual Scene Understanding
**arXiv**：[2603.06530v1](https://arxiv.org/abs/2603.06530) · [PDF](https://arxiv.org/pdf/2603.06530.pdf)  
**作者**：Guangyao Li, Xin Wang, Wenwu Zhu  

**一句话要点**：提出AV-Unified统一框架，以联合学习多种音频-视觉场景理解任务

**关键词**：音频-视觉场景理解, 统一框架, 多任务学习, 时空感知, 跨模态关联, 任务提示

## 3 点简述
- 当前音频-视觉任务如事件定位和分割多独立研究，难以全面理解复杂场景和探索任务间关系
- AV-Unified通过离散化输入输出为共享表示，并设计多尺度时空感知网络来捕捉音频-视觉关联
- 在多个基准数据集上验证了框架在时空任务中的有效性

## 摘要（原文）

> When humans perceive the world, they naturally integrate multiple audio-visual tasks within dynamic, real-world scenes. However, current works such as event localization, parsing, segmentation and question answering are mostly explored individually, making it challenging to comprehensively understand complex audio-visual scenes and explore inter-task relationships. Hence, we propose \textbf{AV-Unified}, a unified framework that enables joint learning across a wide range of audio-visual scene understanding tasks. AV-Unified standardizes the diverse input-output formats of each task and incorporates a multi-scale spatiotemporal perception network to effectively capture audio-visual associations. Specifically, we unify the inputs and outputs of all supported tasks by converting them into sequences of discrete tokens, establishing a shared representation that allows a single architecture to be trained jointly across heterogeneous varied datasets. Considering the varying temporal granularity of audio-visual events, a multi-scale temporal perception module is designed to capture key cues. Meanwhile, to overcome the lack of auditory supervision in the visual domain, we design a cross-modal guidance-based spatial perception module that models spatial audio-visual associations. Furthermore, task-specific text prompts are employed to enhance the model's adaptability and task-awareness. Extensive experiments on benchmark datasets (e.g., AVE, LLP, MUSIC-AVQA, VGG-SS and AVS) demonstrate the effectiveness of AV-Unified across temporal, spatial, and spatiotemporal tasks.

