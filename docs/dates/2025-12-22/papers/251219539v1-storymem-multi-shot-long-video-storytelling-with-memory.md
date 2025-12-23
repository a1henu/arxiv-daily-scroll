---
layout: default
title: StoryMem: Multi-shot Long Video Storytelling with Memory
---

# StoryMem: Multi-shot Long Video Storytelling with Memory
**arXiv**：[2512.19539v1](https://arxiv.org/abs/2512.19539) · [PDF](https://arxiv.org/pdf/2512.19539.pdf)  
**作者**：Kaiwen Zhang, Liming Jiang, Angtian Wang, Jacob Zhiyuan Fang, Tiancheng Zhi, Qing Yan, Hao Kang, Xin Lu, Xingang Pan  

**一句话要点**：提出StoryMem范式，通过显式视觉记忆实现多镜头长视频故事生成

**关键词**：长视频故事生成, 视觉记忆, 视频扩散模型, 多镜头一致性, LoRA微调

## 3 点简述
- 核心问题：长视频故事生成需保持多镜头间一致性和电影质量
- 方法要点：基于记忆库迭代合成镜头，采用M2V设计和LoRA微调注入记忆
- 实验或效果：在ST-Bench上优于先前方法，提升跨镜头一致性和美学质量

## 摘要（原文）

> Visual storytelling requires generating multi-shot videos with cinematic quality and long-range consistency. Inspired by human memory, we propose StoryMem, a paradigm that reformulates long-form video storytelling as iterative shot synthesis conditioned on explicit visual memory, transforming pre-trained single-shot video diffusion models into multi-shot storytellers. This is achieved by a novel Memory-to-Video (M2V) design, which maintains a compact and dynamically updated memory bank of keyframes from historical generated shots. The stored memory is then injected into single-shot video diffusion models via latent concatenation and negative RoPE shifts with only LoRA fine-tuning. A semantic keyframe selection strategy, together with aesthetic preference filtering, further ensures informative and stable memory throughout generation. Moreover, the proposed framework naturally accommodates smooth shot transitions and customized story generation applications. To facilitate evaluation, we introduce ST-Bench, a diverse benchmark for multi-shot video storytelling. Extensive experiments demonstrate that StoryMem achieves superior cross-shot consistency over previous methods while preserving high aesthetic quality and prompt adherence, marking a significant step toward coherent minute-long video storytelling.

