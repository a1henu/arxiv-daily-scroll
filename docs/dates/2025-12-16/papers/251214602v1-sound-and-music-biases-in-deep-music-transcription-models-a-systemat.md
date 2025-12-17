---
layout: default
title: Sound and Music Biases in Deep Music Transcription Models: A Systematic Analysis
---

# Sound and Music Biases in Deep Music Transcription Models: A Systematic Analysis
**arXiv**：[2512.14602v1](https://arxiv.org/abs/2512.14602) · [PDF](https://arxiv.org/pdf/2512.14602.pdf)  
**作者**：Lukáš Samuel Marták, Patricia Hu, Gerhard Widmer  

**一句话要点**：提出MDS语料库以分析深度音乐转录模型在音乐维度分布偏移下的性能偏差

**关键词**：自动音乐转录, 分布偏移, 音乐语料库, 性能评估, 泛化能力, 深度学习

## 3 点简述
- 核心问题：深度音乐转录模型在古典钢琴数据上训练，对其他音乐上下文（如流派、动态、复音）的泛化能力未知
- 方法要点：引入MDS语料库模拟不同分布偏移轴，评估多个先进模型在传统和音乐感知指标下的性能
- 实验或效果：发现声音和流派导致性能显著下降，动态估计比起始预测更易受音乐变化影响，非音乐序列揭示极端偏移下的局限性

## 摘要（原文）

> Automatic Music Transcription (AMT) -- the task of converting music audio into note representations -- has seen rapid progress, driven largely by deep learning systems. Due to the limited availability of richly annotated music datasets, much of the progress in AMT has been concentrated on classical piano music, and even a few very specific datasets. Whether these systems can generalize effectively to other musical contexts remains an open question. Complementing recent studies on distribution shifts in sound (e.g., recording conditions), in this work we investigate the musical dimension -- specifically, variations in genre, dynamics, and polyphony levels. To this end, we introduce the MDS corpus, comprising three distinct subsets -- (1) Genre, (2) Random, and (3) MAEtest -- to emulate different axes of distribution shift. We evaluate the performance of several state-of-the-art AMT systems on the MDS corpus using both traditional information-retrieval and musically-informed performance metrics. Our extensive evaluation isolates and exposes varying degrees of performance degradation under specific distribution shifts. In particular, we measure a note-level F1 performance drop of 20 percentage points due to sound, and 14 due to genre. Generally, we find that dynamics estimation proves more vulnerable to musical variation than onset prediction. Musically informed evaluation metrics, particularly those capturing harmonic structure, help identify potential contributing factors. Furthermore, experiments with randomly generated, non-musical sequences reveal clear limitations in system performance under extreme musical distribution shifts. Altogether, these findings offer new evidence of the persistent impact of the Corpus Bias problem in deep AMT systems.

