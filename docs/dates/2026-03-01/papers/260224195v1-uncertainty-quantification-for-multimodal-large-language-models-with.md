---
layout: default
title: Uncertainty Quantification for Multimodal Large Language Models with Incoherence-adjusted Semantic Volume
---

# Uncertainty Quantification for Multimodal Large Language Models with Incoherence-adjusted Semantic Volume
**arXiv**：[2602.24195v1](https://arxiv.org/abs/2602.24195) · [PDF](https://arxiv.org/pdf/2602.24195.pdf)  
**作者**：Gregory Kang Ruey Lau, Hieu Dao, Nicole Kan Hui Lin, Bryan Kian Hsiang Low  

**一句话要点**：提出UMPIRE框架以量化多模态大语言模型的不确定性，提升部署可靠性。

**关键词**：不确定性量化, 多模态大语言模型, 语义体积, 训练免费框架, 错误检测

## 3 点简述
- 多模态大语言模型输出可能错误，现有不确定性度量方法存在模态限制或计算成本高。
- UMPIRE基于模型内部特征，计算响应样本的不一致性调整语义体积，无需训练或外部工具。
- 实验显示UMPIRE在图像、音频和视频文本基准上优于基线，适用于对抗和分布外场景。

## 摘要（原文）

> Despite their capabilities, Multimodal Large Language Models (MLLMs) may produce plausible but erroneous outputs, hindering reliable deployment. Accurate uncertainty metrics could enable escalation of unreliable queries to human experts or larger models for improved performance. However, existing uncertainty metrics have practical constraints, such as being designed only for specific modalities, reliant on external tools, or computationally expensive. We introduce UMPIRE, a training-free uncertainty quantification framework for MLLMs that works efficiently across various input and output modalities without external tools, relying only on the models' own internal modality features. UMPIRE computes the incoherence-adjusted semantic volume of sampled MLLM responses for a given task instance, effectively capturing both the global semantic diversity of samples and the local incoherence of responses based on internal model confidence. We propose uncertainty desiderata for MLLMs and provide theoretical analysis motivating UMPIRE's design. Extensive experiments show that UMPIRE consistently outperforms baseline metrics in error detection and uncertainty calibration across image, audio, and video-text benchmarks, including adversarial and out-of-distribution settings. We also demonstrate UMPIRE's generalization to non-text output tasks, including image and audio generation.

