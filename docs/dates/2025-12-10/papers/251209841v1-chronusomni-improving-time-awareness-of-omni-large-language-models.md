---
layout: default
title: ChronusOmni: Improving Time Awareness of Omni Large Language Models
---

# ChronusOmni: Improving Time Awareness of Omni Large Language Models
**arXiv**：[2512.09841v1](https://arxiv.org/abs/2512.09841) · [PDF](https://arxiv.org/pdf/2512.09841.pdf)  
**作者**：Yijing Chen, Yihan Wu, Kaisi Guan, Yuchen Ren, Yuyue Wang, Ruihua Song, Liyun Ru  

**一句话要点**：提出ChronusOmni以增强全模态大语言模型在视听时序理解中的显式和隐式时序感知能力

**关键词**：全模态大语言模型, 视听时序理解, 跨模态隐式时序, 强化学习, 时序建模, 长视频分析

## 3 点简述
- 核心问题：现有方法在视听时序理解中音频模态利用不足，且忽视跨模态隐式时序关系，如视觉与音频的交叉关联。
- 方法要点：通过文本时间戳令牌与视听表示交错，实现统一时序建模；结合强化学习奖励函数强化时序排序和细粒度推理。
- 实验或效果：在自建数据集ChronusAV上性能提升超30%，并在其他时序基准测试中取得领先，同时保持通用视听理解能力。

## 摘要（原文）

> Time awareness is a fundamental ability of omni large language models, especially for understanding long videos and answering complex questions. Previous approaches mainly target vision-language scenarios and focus on the explicit temporal grounding questions, such as identifying when a visual event occurs or determining what event happens at aspecific time. However, they often make insufficient use of the audio modality, and overlook implicit temporal grounding across modalities--for example, identifying what is visually present when a character speaks, or determining what is said when a visual event occurs--despite such cross-modal temporal relations being prevalent in real-world scenarios. In this paper, we propose ChronusOmni, an omni large language model designed to enhance temporal awareness for both explicit and implicit audiovisual temporal grounding. First, we interleave text-based timestamp tokens with visual and audio representations at each time unit, enabling unified temporal modeling across modalities. Second, to enforce correct temporal ordering and strengthen fine-grained temporal reasoning, we incorporate reinforcement learning with specially designed reward functions. Moreover, we construct ChronusAV, a temporally-accurate, modality-complete, and cross-modal-aligned dataset to support the training and evaluation on audiovisual temporal grounding task. Experimental results demonstrate that ChronusOmni achieves state-of-the-art performance on ChronusAV with more than 30% improvement and top results on most metrics upon other temporal grounding benchmarks. This highlights the strong temporal awareness of our model across modalities, while preserving general video and audio understanding capabilities.

