---
layout: default
title: Do Foundation Models Know Geometry? Probing Frozen Features for Continuous Physical Measurement
---

# Do Foundation Models Know Geometry? Probing Frozen Features for Continuous Physical Measurement
**arXiv**：[2603.06459v1](https://arxiv.org/abs/2603.06459) · [PDF](https://arxiv.org/pdf/2603.06459.pdf)  
**作者**：Yakov Pyotr Shkolnikov  

**一句话要点**：探究基础模型的几何知识：通过轻量级线性探针从冻结特征中提取连续物理测量

**关键词**：基础模型, 几何知识, 线性探针, 特征提取, 视觉语言模型, 功能收敛

## 3 点简述
- 核心问题：视觉语言模型在文本路径中无法充分表达其编码的连续几何信息，导致几何测量瓶颈。
- 方法要点：使用线性探针和LoRA微调从冻结特征中提取几何信号，分析不同训练目标和架构的影响。
- 实验或效果：线性探针在关节角度测量上达到6.1度MAE，优于文本输出的20.0度，且不同编码器在功能上收敛。

## 摘要（原文）

> Vision-language models encode continuous geometry that their text pathway fails to express: a 6,000-parameter linear probe extracts hand joint angles at 6.1 degrees MAE from frozen features, while the best text output achieves only 20.0 degrees -- a 3.3x bottleneck. LoRA fine-tuning (r=16, 2,000 images) narrows this gap to 6.5 degrees, providing evidence for a pathway-training deficit rather than a representational one. Training objective determines accuracy more than architecture: five encoders spanning self-supervised, contrastive, and hybrid paradigms converge to statistically equivalent accuracy (R^2 approximately 0.55, TOST-equivalent at delta=0.03) despite sharing as little as CKA=0.41 representational similarity -- functional convergence without representational convergence. Autoregressive generation damages geometric fidelity, but the damage originates in the generation process, not in language alignment: Qwen2.5-VL's LLM layers actually improve probe accuracy over its raw vision encoder. Layer-wise analysis reveals a universal mid-network accuracy peak across all architectures, with attention heads in layers 18-22 carrying disproportionate geometric signal. These findings enable a single frozen backbone to function as a multi-task geometric sensor through lightweight probes, without fine-tuning or text generation.

