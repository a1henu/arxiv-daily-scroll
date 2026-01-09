---
layout: default
title: SOVABench: A Vehicle Surveillance Action Retrieval Benchmark for Multimodal Large Language Models
---

# SOVABench: A Vehicle Surveillance Action Retrieval Benchmark for Multimodal Large Language Models
**arXiv**：[2601.04824v1](https://arxiv.org/abs/2601.04824) · [PDF](https://arxiv.org/pdf/2601.04824.pdf)  
**作者**：Oriol Rabasseda, Zenjie Li, Kamal Nasrollahi, Sergio Escalera  

**一句话要点**：提出SOVABench基准和基于MLLM的训练免费框架，以解决监控视频中车辆动作检索的挑战。

**关键词**：监控视频检索, 车辆动作识别, 多模态大语言模型, 训练免费框架, 基准评估

## 3 点简述
- 核心问题：现有视频检索基准缺乏针对监控场景的动作区分评估，难以支持事件识别和行为分析。
- 方法要点：构建SOVABench基准，定义两种评估协议，并利用MLLM生成可解释嵌入，无需训练即可处理图像和视频。
- 实验或效果：在SOVABench及空间与计数基准上表现优异，优于现有对比视觉语言模型，代码和标注公开。

## 摘要（原文）

> Automatic identification of events and recurrent behavior analysis are critical for video surveillance. However, most existing content-based video retrieval benchmarks focus on scene-level similarity and do not evaluate the action discrimination required in surveillance. To address this gap, we introduce SOVABench (Surveillance Opposite Vehicle Actions Benchmark), a real-world retrieval benchmark built from surveillance footage and centered on vehicle-related actions. SOVABench defines two evaluation protocols (inter-pair and intra-pair) to assess cross-action discrimination and temporal direction understanding. Although action distinctions are generally intuitive for human observers, our experiments show that they remain challenging for state-of-the-art vision and multimodal models.
>   Leveraging the visual reasoning and instruction-following capabilities of Multimodal Large Language Models (MLLMs), we present a training-free framework for producing interpretable embeddings from MLLM-generated descriptions for both images and videos. The framework achieves strong performance on SOVABench as well as on several spatial and counting benchmarks where contrastive Vision-Language Models often fail. The code, annotations, and instructions to construct the benchmark are publicly available.

