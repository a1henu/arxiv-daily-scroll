---
layout: default
title: CoVA: Text-Guided Composed Video Retrieval for Audio-Visual Content
---

# CoVA: Text-Guided Composed Video Retrieval for Audio-Visual Content
**arXiv**：[2601.22508v1](https://arxiv.org/abs/2601.22508) · [PDF](https://arxiv.org/pdf/2601.22508.pdf)  
**作者**：Gyuwon Han, Young Kyun Jang, Chanho Eom  

**一句话要点**：提出CoVA任务和AVT方法，以解决音频-视觉组合视频检索中忽略音频变化的问题。

**关键词**：组合视频检索, 音频-视觉融合, 跨模态对齐, 基准构建, 文本引导检索

## 3 点简述
- 核心问题：现有组合视频检索基准仅考虑视觉变化，忽略音频差异，导致检索不准确。
- 方法要点：提出AVT Compositional Fusion，通过选择性对齐查询到最相关模态，整合视频、音频和文本特征。
- 实验或效果：构建AV-Comp基准，AVT方法优于传统单模态融合，为CoVA任务提供强基线。

## 摘要（原文）

> Composed Video Retrieval (CoVR) aims to retrieve a target video from a large gallery using a reference video and a textual query specifying visual modifications. However, existing benchmarks consider only visual changes, ignoring videos that differ in audio despite visual similarity. To address this limitation, we introduce Composed retrieval for Video with its Audio CoVA, a new retrieval task that accounts for both visual and auditory variations. To support this, we construct AV-Comp, a benchmark consisting of video pairs with cross-modal changes and corresponding textual queries that describe the differences. We also propose AVT Compositional Fusion (AVT), which integrates video, audio, and text features by selectively aligning the query to the most relevant modality. AVT outperforms traditional unimodal fusion and serves as a strong baseline for CoVA. Examples from the proposed dataset, including both visual and auditory information, are available at https://perceptualai-lab.github.io/CoVA/.

