---
layout: default
title: NeuroCanvas: VLLM-Powered Robust Seizure Detection by Reformulating Multichannel EEG as Image
---

# NeuroCanvas: VLLM-Powered Robust Seizure Detection by Reformulating Multichannel EEG as Image
**arXiv**：[2602.04769v1](https://arxiv.org/abs/2602.04769) · [PDF](https://arxiv.org/pdf/2602.04769.pdf)  
**作者**：Yan Chen, Jie Peng, Moajjem Hossain Chowdhury, Tianlong Chen, Yunmei Liu  

**一句话要点**：提出NeuroCanvas框架，通过将多通道EEG重构为图像，以解决癫痫检测中的通道异质性和计算效率问题。

**关键词**：癫痫检测, 多通道EEG, 视觉表示, 通道选择, 计算效率, 实时检测

## 3 点简述
- 核心问题：多通道EEG信号存在通道异质性和计算效率低，影响癫痫检测的准确性和实时性。
- 方法要点：采用熵引导通道选择器筛选相关通道，并通过神经元信号画布将信号转换为结构化视觉表示。
- 实验或效果：在多个数据集上，F1分数提升20%，推理延迟降低88%，代码将开源。

## 摘要（原文）

> Accurate and timely seizure detection from Electroencephalography (EEG) is critical for clinical intervention, yet manual review of long-term recordings is labor-intensive. Recent efforts to encode EEG signals into large language models (LLMs) show promise in handling neural signals across diverse patients, but two significant challenges remain: (1) multi-channel heterogeneity, as seizure-relevant information varies substantially across EEG channels, and (2) computing inefficiency, as the EEG signals need to be encoded into a massive number of tokens for the prediction. To address these issues, we draw the EEG signal and propose the novel NeuroCanvas framework. Specifically, NeuroCanvas consists of two modules: (i) The Entropy-guided Channel Selector (ECS) selects the seizure-relevant channels input to LLM and (ii) the following Canvas of Neuron Signal (CNS) converts selected multi-channel heterogeneous EEG signals into structured visual representations. The ECS module alleviates the multi-channel heterogeneity issue, and the CNS uses compact visual tokens to represent the EEG signals that improve the computing efficiency. We evaluate NeuroCanvas across multiple seizure detection datasets, demonstrating a significant improvement of $20\%$ in F1 score and reductions of $88\%$ in inference latency. These results highlight NeuroCanvas as a scalable and effective solution for real-time and resource-efficient seizure detection in clinical practice.The code will be released at https://github.com/Yanchen30247/seizure_detect.

