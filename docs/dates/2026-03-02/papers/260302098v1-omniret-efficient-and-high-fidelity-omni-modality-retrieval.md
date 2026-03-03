---
layout: default
title: OmniRet: Efficient and High-Fidelity Omni Modality Retrieval
---

# OmniRet: Efficient and High-Fidelity Omni Modality Retrieval
**arXiv**：[2603.02098v1](https://arxiv.org/abs/2603.02098) · [PDF](https://arxiv.org/pdf/2603.02098.pdf)  
**作者**：Chuong Huynh, Manh Luong, Abhinav Shrivastava  

**一句话要点**：提出OmniRet模型以高效处理文本、视觉和音频的跨模态检索任务

**关键词**：跨模态检索, 注意力机制, 表示学习, 音频检索, 组合查询, 多模态基准

## 3 点简述
- 核心问题：现有检索模型局限于文本和视觉，无法处理多模态组合查询
- 方法要点：引入注意力重采样机制和注意力切片Wasserstein池化以提升效率和表示保真度
- 实验或效果：在13个检索任务上表现优异，尤其在组合查询和音频视频检索中显著改进

## 摘要（原文）

> Multimodal retrieval is the task of aggregating information from queries across heterogeneous modalities to retrieve desired targets. State-of-the-art multimodal retrieval models can understand complex queries, yet they are typically limited to two modalities: text and vision. This limitation impedes the development of universal retrieval systems capable of comprehending queries that combine more than two modalities. To advance toward this goal, we present OmniRet, the first retrieval model capable of handling complex, composed queries spanning three key modalities: text, vision, and audio. Our OmniRet model addresses two critical challenges for universal retrieval: computational efficiency and representation fidelity. First, feeding massive token sequences from modality-specific encoders to Large Language Models (LLMs) is computationally inefficient. We therefore introduce an attention-based resampling mechanism to generate compact, fixed-size representations from these sequences. Second, compressing rich omni-modal data into a single embedding vector inevitably causes information loss and discards fine-grained details. We propose Attention Sliced Wasserstein Pooling to preserve these fine-grained details, leading to improved omni-modal representations. OmniRet is trained on an aggregation of approximately 6 million query-target pairs spanning 30 datasets. We benchmark our model on 13 retrieval tasks and a MMEBv2 subset. Our model demonstrates significant improvements on composed query, audio and video retrieval tasks, while achieving on-par performance with state-of-the-art models on others. Furthermore, we curate a new Audio-Centric Multimodal Benchmark (ACM). This new benchmark introduces two critical, previously missing tasks-composed audio retrieval and audio-visual retrieval to more comprehensively evaluate a model's omni-modal embedding capacity.

