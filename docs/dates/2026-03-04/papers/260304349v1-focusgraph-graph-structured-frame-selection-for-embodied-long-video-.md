---
layout: default
title: FocusGraph: Graph-Structured Frame Selection for Embodied Long Video Question Answering
---

# FocusGraph: Graph-Structured Frame Selection for Embodied Long Video Question Answering
**arXiv**：[2603.04349v1](https://arxiv.org/abs/2603.04349) · [PDF](https://arxiv.org/pdf/2603.04349.pdf)  
**作者**：Tatiana Zemskova, Solomon Andryushenko, Ilya Obrubov, Viktoriia Khoruzhaia, Ekaterina Eroshenko, Ekaterina Derevyanka, Dmitry Yudin  

**一句话要点**：提出FocusGraph框架，通过图结构帧选择解决具身长视频问答中的关键帧选择问题。

**关键词**：长视频理解, 关键帧选择, 图结构字幕, 具身智能, 多模态大语言模型, 无训练方法

## 3 点简述
- 核心问题：长视频问答中，多模态大语言模型随输入帧数增加，响应质量下降且推理时间增长。
- 方法要点：使用轻量可训练的Scene-Caption LLM Selector基于图结构字幕选择相关片段，并采用无训练的PSFR方法从片段中选取关键帧。
- 实验或效果：在FindingDory和HourVideo基准上达到先进水平，显著减少推理时间。

## 摘要（原文）

> The ability to understand long videos is vital for embodied intelligent agents, because their effectiveness depends on how well they can accumulate, organize, and leverage long-horizon perceptual memories. Recently, multimodal LLMs have been gaining popularity for solving the long video understanding task due to their general ability to understand natural language and to leverage world knowledge. However, as the number of frames provided to an MLLM increases, the quality of its responses tends to degrade, and inference time grows. Therefore, when using MLLMs for long video understanding, a crucial step is selecting key frames from the video to answer user queries.
>   In this work, we develop FocusGraph, a framework for keyframe selection for question answering over long egocentric videos. It leverages a lightweight trainable Scene-Caption LLM Selector that selects query-relevant clips based on their graph-based captions, and a training-free method for selecting keyframes from these clips. Unlike existing methods, the proposed Scene-Caption LLM Selector does not rely on the original sequence of low-resolution frames; instead, it operates on a compact textual representation of the scene. We then design a training-free Patch-wise Sparse-Flow Retention (PSFR) method to select keyframes from the resulting sequence of clips, which are fed into an MLLM to produce the final answer. Together, these components enable FocusGraph to achieve state-of-the-art results on challenging egocentric long-video question answering benchmarks, including FindingDory and HourVideo, while significantly reducing inference time relative to baseline approaches.

