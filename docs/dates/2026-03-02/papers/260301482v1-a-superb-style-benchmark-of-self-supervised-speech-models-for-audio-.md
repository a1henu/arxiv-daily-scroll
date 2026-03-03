---
layout: default
title: A SUPERB-Style Benchmark of Self-Supervised Speech Models for Audio Deepfake Detection
---

# A SUPERB-Style Benchmark of Self-Supervised Speech Models for Audio Deepfake Detection
**arXiv**：[2603.01482v1](https://arxiv.org/abs/2603.01482) · [PDF](https://arxiv.org/pdf/2603.01482.pdf)  
**作者**：Hashim Ali, Nithin Sai Adupa, Surya Subramani, Hafiz Malik  

**一句话要点**：提出Spoof-SUPERB基准，系统评估自监督语音模型在音频深度伪造检测中的性能。

**关键词**：音频深度伪造检测, 自监督学习, 基准评估, 判别式模型, 声学鲁棒性

## 3 点简述
- 音频深度伪造检测缺乏标准化基准，影响模型公平比较与安全应用。
- 引入Spoof-SUPERB，涵盖20个自监督模型，包括生成式、判别式和基于频谱图的架构。
- 实验显示大规模判别式模型在跨域和声学退化下表现稳健，提供实用选择指导。

## 摘要（原文）

> Self-supervised learning (SSL) has transformed speech processing, with benchmarks such as SUPERB establishing fair comparisons across diverse downstream tasks. Despite it's security-critical importance, Audio deepfake detection has remained outside these efforts. In this work, we introduce Spoof-SUPERB, a benchmark for audio deepfake detection that systematically evaluates 20 SSL models spanning generative, discriminative, and spectrogram-based architectures. We evaluated these models on multiple in-domain and out-of-domain datasets. Our results reveal that large-scale discriminative models such as XLS-R, UniSpeech-SAT, and WavLM Large consistently outperform other models, benefiting from multilingual pretraining, speaker-aware objectives, and model scale. We further analyze the robustness of these models under acoustic degradations, showing that generative approaches degrade sharply, while discriminative models remain resilient. This benchmark establishes a reproducible baseline and provides practical insights into which SSL representations are most reliable for securing speech systems against audio deepfakes.

