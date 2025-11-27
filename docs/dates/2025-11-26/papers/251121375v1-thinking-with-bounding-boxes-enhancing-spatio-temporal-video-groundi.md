---
layout: default
title: Thinking With Bounding Boxes: Enhancing Spatio-Temporal Video Grounding via Reinforcement Fine-Tuning
---

# Thinking With Bounding Boxes: Enhancing Spatio-Temporal Video Grounding via Reinforcement Fine-Tuning
**arXiv**：[2511.21375v1](https://arxiv.org/abs/2511.21375) · [PDF](https://arxiv.org/pdf/2511.21375.pdf)  
**作者**：Xin Gu, Haoji Zhang, Qihang Fan, Jingxuan Niu, Zhipeng Zhang, Libo Zhang, Guang Chen, Fan Chen, Longyin Wen, Sijie Zhu  

**一句话要点**：提出STVG-o1框架，通过强化微调提升多模态大语言模型在时空视频定位中的性能。

**关键词**：时空视频定位, 多模态大语言模型, 强化学习微调, 边界框思维链, 几何感知奖励

## 3 点简述
- 核心问题：多模态大语言模型在时空视频定位中因训练目标不匹配和细粒度对齐弱而表现不佳。
- 方法要点：引入边界框思维链机制和几何感知的多维强化奖励函数进行微调。
- 实验效果：在HCSTVG数据集上超越最佳任务特定方法，并在多数据集上展示强泛化能力。

## 摘要（原文）

> Spatio-temporal video grounding (STVG) requires localizing a target object in untrimmed videos both temporally and spatially from natural language descriptions. Despite their strong language understanding, multimodal large language models (MLLMs) underperform on STVG due to misaligned training objectives and weak fine-grained region-word alignment in standard visual encoders. To address this, we propose STVG-o1, the first framework that enables off-the-shelf MLLMs to achieve state-of-the-art STVG performance without any architectural modifications. Our method introduces a bounding-box chain-of-thought mechanism that explicitly reasons about spatio-temporal locations in an intermediate step before producing the final prediction. We further design a multi-dimensional reinforcement reward function consisting of format, consistency, temporal, spatial, and think rewards, which provides geometry-aware supervision through reinforcement fine-tuning. Evaluated on HCSTVG-v1/v2 and VidSTG, STVG-o1 sets new state-of-the-art results on HCSTVG, outperforming the best task-specific method by 7.3\% m\_tIoU on HCSTVG-v1, matching specialized models on VidSTG, and surpassing all existing MLLM-based approaches by large margins. It also demonstrates strong open-vocabulary generalization across datasets, establishing MLLMs as viable and powerful backbones for precise spatio-temporal grounding. Our code and models will be released.

