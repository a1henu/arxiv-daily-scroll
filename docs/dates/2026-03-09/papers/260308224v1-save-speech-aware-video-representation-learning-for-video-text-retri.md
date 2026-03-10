---
layout: default
title: SAVE: Speech-Aware Video Representation Learning for Video-Text Retrieval
---

# SAVE: Speech-Aware Video Representation Learning for Video-Text Retrieval
**arXiv**：[2603.08224v1](https://arxiv.org/abs/2603.08224) · [PDF](https://arxiv.org/pdf/2603.08224.pdf)  
**作者**：Ruixiang Zhao, Zhihao Xu, Bangxiang Lan, Zijie Xin, Jingyu Liu, Xirong Li  

**一句话要点**：提出SAVE方法以解决视频-文本检索中语音内容表示不足和视听融合不佳的问题。

**关键词**：视频-文本检索, 语音表示学习, 视听融合, 多模态学习, CLIP扩展

## 3 点简述
- 核心问题：现有方法忽略视频音轨，导致语音内容表示无效和视听融合不优。
- 方法要点：基于AVIGATE改进，增加专用语音分支和软ALBEF进行早期视听对齐。
- 实验或效果：在五个基准测试中优于SOTA，如MSRVTT-9k提升4.1%。

## 摘要（原文）

> For video-text retrieval, the use of CLIP has been a de facto choice. Since CLIP provides only image and text encoders, this consensus has led to a biased paradigm that entirely ignores the sound track of videos. While several attempts have been made to reintroduce audio -- typically by incorporating an audio encoder and fusing its output with visual features -- these methods face two challenges: ineffective representation of speech content and suboptimal vision-audio fusion. To address these issues jointly, we propose SAVE, a Speech Aware Video rEpresentation learning method. SAVE improves upon AVIGATE, a SOTA audiovisual method, with a dedicated speech branch for more effective speech embedding. Furthermore, we introduce soft-ALBEF for early vision-audio alignment that facilitates fusion. Extensive experiments on five benchmarks show that SAVE compares favorably against the SOTA, outperforming AVIGATE by +4.1% on MSRVTT-9k, +1.9% on MSRVTT-7k, +2.5% on VATEX, +9.8% on Charades, and +2.1% on LSMDC, in light of the SumR metric.

