---
layout: default
title: RF-GPT: Teaching AI to See the Wireless World
---

# RF-GPT: Teaching AI to See the Wireless World
**arXiv**：[2602.14833v1](https://arxiv.org/abs/2602.14833) · [PDF](https://arxiv.org/pdf/2602.14833.pdf)  
**作者**：Hang Zou, Yu Tian, Bohao Wang, Lina Bariah, Samson Lasaulce, Chongwen Huang, Mérouane Debbah  

**一句话要点**：提出RF-GPT，通过视觉编码器处理射频谱图，将射频感知与高级推理结合。

**关键词**：射频语言模型, 多模态大模型, 射频谱图处理, 指令微调, 无线技术识别, 合成数据生成

## 3 点简述
- 核心问题：现有大模型不支持射频信号，射频感知与高级推理存在鸿沟。
- 方法要点：利用多模态大模型的视觉编码器处理射频谱图，注入射频令牌到解码器大模型。
- 实验或效果：在多个射频任务基准测试中表现优异，通用视觉语言模型则大多失败。

## 摘要（原文）

> Large language models (LLMs) and multimodal models have become powerful general-purpose reasoning systems. However, radio-frequency (RF) signals, which underpin wireless systems, are still not natively supported by these models. Existing LLM-based approaches for telecom focus mainly on text and structured data, while conventional RF deep-learning models are built separately for specific signal-processing tasks, highlighting a clear gap between RF perception and high-level reasoning. To bridge this gap, we introduce RF-GPT, a radio-frequency language model (RFLM) that utilizes the visual encoders of multimodal LLMs to process and understand RF spectrograms. In this framework, complex in-phase/quadrature (IQ) waveforms are mapped to time-frequency spectrograms and then passed to pretrained visual encoders. The resulting representations are injected as RF tokens into a decoder-only LLM, which generates RF-grounded answers, explanations, and structured outputs. To train RF-GPT, we perform supervised instruction fine-tuning of a pretrained multimodal LLM using a fully synthetic RF corpus. Standards-compliant waveform generators produce wideband scenes for six wireless technologies, from which we derive time-frequency spectrograms, exact configuration metadata, and dense captions. A text-only LLM then converts these captions into RF-grounded instruction-answer pairs, yielding roughly 12,000 RF scenes and 0.625 million instruction examples without any manual labeling. Across benchmarks for wideband modulation classification, overlap analysis, wireless-technology recognition, WLAN user counting, and 5G NR information extraction, RF-GPT achieves strong multi-task performance, whereas general-purpose VLMs with no RF grounding largely fail.

