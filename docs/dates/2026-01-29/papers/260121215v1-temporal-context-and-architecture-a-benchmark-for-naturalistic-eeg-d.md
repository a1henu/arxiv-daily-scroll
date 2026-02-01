---
layout: default
title: Temporal Context and Architecture: A Benchmark for Naturalistic EEG Decoding
---

# Temporal Context and Architecture: A Benchmark for Naturalistic EEG Decoding
**arXiv**：[2601.21215v1](https://arxiv.org/abs/2601.21215) · [PDF](https://arxiv.org/pdf/2601.21215.pdf)  
**作者**：Mehmet Ergezer  

**一句话要点**：研究模型架构与时间上下文在自然脑电解码中的交互，揭示效率与鲁棒性权衡

**关键词**：脑电解码, 时间上下文, 模型架构基准, 鲁棒性评估, 参数效率

## 3 点简述
- 核心问题：模型架构如何与时间上下文长度交互影响自然脑电解码性能
- 方法要点：在HBN电影观看数据集上，基准测试CNN、LSTM、EEGXF、S4和S5架构，评估不同段长下的4类任务
- 实验或效果：S5在64秒上下文达到98.7%准确率且参数更少，但EEGXF在频率偏移和OOD任务中更鲁棒

## 摘要（原文）

> We study how model architecture and temporal context interact in naturalistic EEG decoding. Using the HBN movie-watching dataset, we benchmark five architectures, CNN, LSTM, a stabilized Transformer (EEGXF), S4, and S5, on a 4-class task across segment lengths from 8s to 128s. Accuracy improves with longer context: at 64s, S5 reaches 98.7%+/-0.6 and CNN 98.3%+/-0.3, while S5 uses ~20x fewer parameters than CNN. To probe real-world robustness, we evaluate zero-shot cross-frequency shifts, cross-task OOD inputs, and leave-one-subject-out generalization. S5 achieves stronger cross-subject accuracy but makes over-confident errors on OOD tasks; EEGXF is more conservative and stable under frequency shifts, though less calibrated in-distribution. These results reveal a practical efficiency-robustness trade-off: S5 for parameter-efficient peak accuracy; EEGXF when robustness and conservative uncertainty are critical.

