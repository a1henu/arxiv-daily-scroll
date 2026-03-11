---
layout: default
title: SCENEBench: An Audio Understanding Benchmark Grounded in Assistive and Industrial Use Cases
---

# SCENEBench: An Audio Understanding Benchmark Grounded in Assistive and Industrial Use Cases
**arXiv**：[2603.09853v1](https://arxiv.org/abs/2603.09853) · [PDF](https://arxiv.org/pdf/2603.09853.pdf)  
**作者**：Laya Iyer, Angelina Wang, Sanmi Koyejo  

**一句话要点**：提出SCENEBench基准套件，以评估辅助技术和工业噪声监控中的音频理解能力。

**关键词**：音频理解基准, 辅助技术, 工业噪声监控, 大型音频语言模型, 合成音频验证

## 3 点简述
- 核心问题：现有大型音频语言模型在自动语音识别之外的音频理解能力评估不足。
- 方法要点：构建包含背景声音理解、噪声定位、跨语言语音理解和声音特征识别的合成音频基准。
- 实验或效果：评估五个先进模型，发现性能差异大，部分任务低于随机水平，提供改进方向。

## 摘要（原文）

> Advances in large language models (LLMs) have enabled significant capabilities in audio processing, resulting in state-of-the-art models now known as Large Audio Language Models (LALMs). However, minimal work has been done to measure audio understanding beyond automatic speech recognition (ASR). This paper closes that gap by proposing a benchmark suite, SCENEBench (Spatial, Cross-lingual, Environmental, Non-speech Evaluation), that targets a broad form of audio comprehension across four real-world categories: background sound understanding, noise localization, cross-linguistic speech understanding, and vocal characterizer recognition. These four categories are selected based on understudied needs from accessibility technology and industrial noise monitoring. In addition to performance, we also measure model latency. The purpose of this benchmark suite is to assess audio beyond just what words are said - rather, how they are said and the non-speech components of the audio. Because our audio samples are synthetically constructed (e.g., by overlaying two natural audio samples), we further validate our benchmark against 20 natural audio items per task, sub-sampled from existing datasets to match our task criteria, to assess ecological validity. We assess five state-of-the-art LALMs and find critical gaps: performance varies across tasks, with some tasks performing below random chance and others achieving high accuracy. These results provide direction for targeted improvements in model capabilities.

