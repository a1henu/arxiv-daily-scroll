---
layout: default
title: ViSS-R1: Self-Supervised Reinforcement Video Reasoning
---

# ViSS-R1: Self-Supervised Reinforcement Video Reasoning
**arXiv**：[2511.13054v1](https://arxiv.org/abs/2511.13054) · [PDF](https://arxiv.org/pdf/2511.13054.pdf)  
**作者**：Bo Fang, Yuxin Song, Qiangqiang Wu, Haoyuan Sun, Wenhao Wu, Antoni B. Chan  

**一句话要点**：提出ViSS-R1框架，通过自监督强化学习提升多模态大语言模型的复杂视频推理能力

**关键词**：自监督学习, 强化学习, 视频推理, 多模态大语言模型, R1后训练, 视觉变换

## 3 点简述
- 核心问题：当前R1方法在视频推理中过度依赖文本，忽视视觉信息，易导致捷径学习和幻觉
- 方法要点：引入Pretext-GRPO算法，通过自监督任务奖励模型处理变换后的视觉输入
- 实验或效果：在六个视频推理基准上验证了ViSS-R1的有效性和优越性

## 摘要（原文）

> Complex video reasoning remains a significant challenge for Multimodal Large Language Models (MLLMs), as current R1-based methodologies often prioritize text-centric reasoning derived from text-based and image-based developments. In video tasks, such strategies frequently underutilize rich visual information, leading to potential shortcut learning and increased susceptibility to hallucination. To foster a more robust, visual-centric video understanding, we start by introducing a novel self-supervised reinforcement learning GRPO algorithm (Pretext-GRPO) within the standard R1 pipeline, in which positive rewards are assigned for correctly solving pretext tasks on transformed visual inputs, which makes the model to non-trivially process the visual information. Building on the effectiveness of Pretext-GRPO, we further propose the ViSS-R1 framework, which streamlines and integrates pretext-task-based self-supervised learning directly into the MLLM's R1 post-training paradigm. Instead of relying solely on sparse visual cues, our framework compels models to reason about transformed visual input by simultaneously processing both pretext questions (concerning transformations) and true user queries. This necessitates identifying the applied transformation and reconstructing the original video to formulate accurate final answers. Comprehensive evaluations on six widely-used video reasoning and understanding benchmarks demonstrate the effectiveness and superiority of our Pretext-GRPO and ViSS-R1 for complex video reasoning. Our codes and models will be publicly available.

