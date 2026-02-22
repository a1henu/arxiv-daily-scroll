---
layout: default
title: EAGLE: Expert-Augmented Attention Guidance for Tuning-Free Industrial Anomaly Detection in Multimodal Large Language Models
---

# EAGLE: Expert-Augmented Attention Guidance for Tuning-Free Industrial Anomaly Detection in Multimodal Large Language Models
**arXiv**：[2602.17419v1](https://arxiv.org/abs/2602.17419) · [PDF](https://arxiv.org/pdf/2602.17419.pdf)  
**作者**：Xiaomeng Peng, Xilang Huang, Seon Han Choi  

**一句话要点**：提出EAGLE框架，通过专家增强注意力引导实现免调优的工业异常检测与解释

**关键词**：工业异常检测, 多模态大语言模型, 注意力引导, 免调优框架, 可解释性分析

## 3 点简述
- 工业异常检测常缺乏语义解释，现有MLLMs方法需调优且效果有限
- EAGLE集成专家模型输出，引导MLLMs进行准确检测和可解释描述
- 实验显示EAGLE在MVTec-AD和VisA上提升性能，无需参数更新

## 摘要（原文）

> Industrial anomaly detection is important for smart manufacturing, but many deep learning approaches produce only binary decisions and provide limited semantic explanations. Multimodal large language models (MLLMs) can potentially generate fine-grained, language-based analyses, yet existing methods often require costly fine-tuning and do not consistently improve anomaly detection accuracy compared to lightweight specialist detectors. We propose expert-augmented attention guidance for industrial anomaly detection in MLLMs (EAGLE), a tuning-free framework that integrates outputs from expert model to guide MLLMs toward both accurate detection and interpretable anomaly descriptions. We further study how EAGLE affects MLLMs internals by examining the attention distribution of MLLMs to the anomalous image regions in the intermediate layers. We observe that successful anomaly detection is associated with increased attention concentration on anomalous regions, and EAGLE tends to encourage this alignment. Experiments on MVTec-AD and VisA show that EAGLE improves anomaly detection performance across multiple MLLMs without any parameter updates, achieving results comparable to fine-tuning based methods. Code is available at \href{https://github.com/shengtun/Eagle}{https://github.com/shengtun/Eagle}

