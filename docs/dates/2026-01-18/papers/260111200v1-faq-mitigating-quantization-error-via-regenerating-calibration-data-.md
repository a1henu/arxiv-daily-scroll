---
layout: default
title: FAQ: Mitigating Quantization Error via Regenerating Calibration Data with Family-Aware Quantization
---

# FAQ: Mitigating Quantization Error via Regenerating Calibration Data with Family-Aware Quantization
**arXiv**：[2601.11200v1](https://arxiv.org/abs/2601.11200) · [PDF](https://arxiv.org/pdf/2601.11200.pdf)  
**作者**：Haiyang Xiao, Weiqing Li, Jinyue Guo, Guochao Jiang, Guohua Liu, Yuewei Zhang  

**一句话要点**：提出FAQ框架，通过家族感知量化再生校准数据以缓解量化误差

**关键词**：后训练量化, 校准数据再生, 家族感知量化, 大语言模型部署, 量化误差缓解

## 3 点简述
- 核心问题：传统后训练量化依赖有限校准样本，难以捕捉推理激活分布，导致量化参数偏差
- 方法要点：利用同家族大语言模型先验知识，再生高保真校准数据，经专家指导选择最佳样本
- 实验或效果：在Qwen3-8B等模型上，FAQ相比基线减少准确率损失达28.5%

## 摘要（原文）

> Although post-training quantization (PTQ) provides an efficient numerical compression scheme for deploying large language models (LLMs) on resource-constrained devices, the representativeness and universality of calibration data remain a core bottleneck in determining the accuracy of quantization parameters. Traditional PTQ methods typically rely on limited samples, making it difficult to capture the activation distribution during the inference phase, leading to biases in quantization parameters. To address this, we propose \textbf{FAQ} (Family-Aware Quantization), a calibration data regeneration framework that leverages prior knowledge from LLMs of the same family to generate high-fidelity calibration samples. Specifically, FAQ first inputs the original calibration samples into a larger LLM from the same family as the target model, regenerating a series of high-fidelity calibration data using a highly consistent knowledge system. Subsequently, this data, carrying Chain-of-Thought reasoning and conforming to the expected activation distribution, undergoes group competition under expert guidance to select the best samples, which are then re-normalized to enhance the effectiveness of standard PTQ. Experiments on multiple model series, including Qwen3-8B, show that FAQ reduces accuracy loss by up to 28.5\% compared to the baseline with original calibration data, demonstrating its powerful potential and contribution.

