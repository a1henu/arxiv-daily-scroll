---
layout: default
title: MERLIN: Building Low-SNR Robust Multimodal LLMs for Electromagnetic Signals
---

# MERLIN: Building Low-SNR Robust Multimodal LLMs for Electromagnetic Signals
**arXiv**：[2603.08174v1](https://arxiv.org/abs/2603.08174) · [PDF](https://arxiv.org/pdf/2603.08174.pdf)  
**作者**：Junyu Shen, Zhendong She, Chenghanyu Zhang, Yuchuang Sun, Luqing Luo, Dingwei Tan, Zonghao Guo, Bo Guo, Zehua Han, Wupeng Xie, Yaxin Mu, Peng Zhang, Peipei Li, Fengxiang Wang, Yangang Sun, Maosong Sun  

**一句话要点**：提出MERLIN框架以解决电磁信号多模态大语言模型在低信噪比环境下的鲁棒性问题

**关键词**：电磁信号处理, 多模态大语言模型, 低信噪比鲁棒性, 数据集构建, 基准评估, 信号文本对齐

## 3 点简述
- 核心问题：电磁信号多模态大语言模型面临数据稀缺、基准缺失和低信噪比环境下的性能脆弱性。
- 方法要点：构建EM-100k数据集、提出EM-Bench基准，并设计MERLIN框架以增强低信噪比鲁棒性。
- 实验或效果：MERLIN在EM-Bench上达到最先进性能，并在低信噪比设置中表现出显著鲁棒性。

## 摘要（原文）

> The paradigm of Multimodal Large Language Models (MLLMs) offers a promising blueprint for advancing the electromagnetic (EM) domain. However, prevailing approaches often deviate from the native MLLM paradigm, instead using task-specific or pipelined architectures that lead to fundamental limitations in model performance and generalization. Fully realizing the MLLM potential in EM domain requires overcoming three main challenges: (1) Data. The scarcity of high-quality datasets with paired EM signals and descriptive text annotations used for MLLMs pre-training; (2) Benchmark. The absence of comprehensive benchmarks to systematically evaluate and compare the performance of models on EM signal-to-text tasks; (3) Model. A critical fragility in low Signal-to-Noise Ratio (SNR) environments, where critical signal features can be obscured, leading to significant performance degradation.
>   To address these challenges, we introduce a tripartite contribution to establish a foundation for MLLMs in the EM domain. First, to overcome data scarcity, we construct and release EM-100k, a large-scale dataset comprising over 100,000 EM signal-text pairs. Second, to enable rigorous and standardized evaluation, we propose EM-Bench, the most comprehensive benchmark featuring diverse downstream tasks spanning from perception to reasoning. Finally, to tackle the core modeling challenge, we present MERLIN, a novel training framework designed not only to align low-level signal representations with high-level semantic text, but also to explicitly enhance model robustness and performance in challenging low-SNR environments. Comprehensive experiments validate our method, showing that MERLIN is state-of-the-art in the EM-Bench and exhibits remarkable robustness in low-SNR settings.

