---
layout: default
title: Streaming Video Instruction Tuning
---

# Streaming Video Instruction Tuning
**arXiv**：[2512.21334v1](https://arxiv.org/abs/2512.21334) · [PDF](https://arxiv.org/pdf/2512.21334.pdf)  
**作者**：Jiaer Xia, Peixian Chen, Mengdan Zhang, Xing Sun, Kaiyang Zhou  

**一句话要点**：提出Streamo实时流视频大模型，作为通用交互助手以统一处理连续视频流任务。

**关键词**：流视频理解, 指令调优, 实时交互, 多任务学习, 时间推理

## 3 点简述
- 核心问题：现有在线视频模型局限于问答或字幕，缺乏实时流视频的通用交互能力。
- 方法要点：构建Streamo-Instruct-465K大规模指令数据集，支持多任务统一训练，实现端到端流视频理解。
- 实验或效果：Streamo在多种流视频基准测试中展现强时间推理、响应交互和广泛泛化能力。

## 摘要（原文）

> We present Streamo, a real-time streaming video LLM that serves as a general-purpose interactive assistant. Unlike existing online video models that focus narrowly on question answering or captioning, Streamo performs a broad spectrum of streaming video tasks, including real-time narration, action understanding, event captioning, temporal event grounding, and time-sensitive question answering. To develop such versatility, we construct Streamo-Instruct-465K, a large-scale instruction-following dataset tailored for streaming video understanding. The dataset covers diverse temporal contexts and multi-task supervision, enabling unified training across heterogeneous streaming tasks. After training end-to-end on the instruction-following dataset through a streamlined pipeline, Streamo exhibits strong temporal reasoning, responsive interaction, and broad generalization across a variety of streaming benchmarks. Extensive experiments show that Streamo bridges the gap between offline video perception models and real-time multimodal assistants, making a step toward unified, intelligent video understanding in continuous video streams.

