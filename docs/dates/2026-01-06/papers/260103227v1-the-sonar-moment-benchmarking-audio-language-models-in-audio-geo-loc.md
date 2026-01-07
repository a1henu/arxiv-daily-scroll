---
layout: default
title: The Sonar Moment: Benchmarking Audio-Language Models in Audio Geo-Localization
---

# The Sonar Moment: Benchmarking Audio-Language Models in Audio Geo-Localization
**arXiv**：[2601.03227v1](https://arxiv.org/abs/2601.03227) · [PDF](https://arxiv.org/pdf/2601.03227.pdf)  
**作者**：Ruixing Zhang, Zihan Liu, Leilei Sun, Tongyu Zhu, Weifeng Lv  

**一句话要点**：提出AGL1K基准以解决音频语言模型在音频地理定位中缺乏高质量数据的问题。

**关键词**：音频地理定位, 音频语言模型, 基准数据集, 地理空间推理, 音频本地化度量

## 3 点简述
- 音频地理定位因缺乏高质量音频-位置配对数据而受限。
- 引入AGL1K基准，包含1,444个精选音频片段，覆盖72个国家和地区。
- 评估16个ALMs显示闭源模型优于开源模型，语言线索主导预测。

## 摘要（原文）

> Geo-localization aims to infer the geographic origin of a given signal. In computer vision, geo-localization has served as a demanding benchmark for compositional reasoning and is relevant to public safety. In contrast, progress on audio geo-localization has been constrained by the lack of high-quality audio-location pairs. To address this gap, we introduce AGL1K, the first audio geo-localization benchmark for audio language models (ALMs), spanning 72 countries and territories. To extract reliably localizable samples from a crowd-sourced platform, we propose the Audio Localizability metric that quantifies the informativeness of each recording, yielding 1,444 curated audio clips. Evaluations on 16 ALMs show that ALMs have emerged with audio geo-localization capability. We find that closed-source models substantially outperform open-source models, and that linguistic clues often dominate as a scaffold for prediction. We further analyze ALMs' reasoning traces, regional bias, error causes, and the interpretability of the localizability metric. Overall, AGL1K establishes a benchmark for audio geo-localization and may advance ALMs with better geospatial reasoning capability.

