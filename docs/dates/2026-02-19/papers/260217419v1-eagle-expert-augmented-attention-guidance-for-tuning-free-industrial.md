---
layout: default
title: EAGLE: Expert-Augmented Attention Guidance for Tuning-Free Industrial Anomaly Detection in Multimodal Large Language Models
---

# EAGLE: Expert-Augmented Attention Guidance for Tuning-Free Industrial Anomaly Detection in Multimodal Large Language Models
**arXiv**：[2602.17419v1](https://arxiv.org/abs/2602.17419) · [PDF](https://arxiv.org/pdf/2602.17419.pdf)  
**作者**：Xiaomeng Peng, Xilang Huang, Seon Han Choi  

**一句话要点**：提出EAGLE框架，无需调优即可提升多模态大语言模型在工业异常检测中的性能与可解释性。

**关键词**：工业异常检测, 多模态大语言模型, 无需调优框架, 注意力引导, 可解释性分析

## 3 点简述
- 工业异常检测常缺乏语义解释，现有MLLMs方法需调优且性能提升有限。
- EAGLE集成专家模型输出，引导MLLMs实现准确检测和可解释描述，无需参数更新。
- 实验表明EAGLE在MVTec-AD和VisA数据集上提升多MLLMs性能，效果媲美调优方法。

## 摘要（原文）

> Industrial anomaly detection is important for smart manufacturing, but many deep learning approaches produce only binary decisions and provide limited semantic explanations. Multimodal large language models (MLLMs) can potentially generate fine-grained, language-based analyses, yet existing methods often require costly fine-tuning and do not consistently improve anomaly detection accuracy compared to lightweight specialist detectors. We propose expert-augmented attention guidance for industrial anomaly detection in MLLMs (EAGLE), a tuning-free framework that integrates outputs from expert model to guide MLLMs toward both accurate detection and interpretable anomaly descriptions. We further study how EAGLE affects MLLMs internals by examining the attention distribution of MLLMs to the anomalous image regions in the intermediate layers. We observe that successful anomaly detection is associated with increased attention concentration on anomalous regions, and EAGLE tends to encourage this alignment. Experiments on MVTec-AD and VisA show that EAGLE improves anomaly detection performance across multiple MLLMs without any parameter updates, achieving results comparable to fine-tuning based methods. Code is available at \href{https://github.com/shengtun/Eagle}{https://github.com/shengtun/Eagle}

