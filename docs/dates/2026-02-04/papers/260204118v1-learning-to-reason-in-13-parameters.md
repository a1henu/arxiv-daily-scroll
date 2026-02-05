---
layout: default
title: Learning to Reason in 13 Parameters
---

# Learning to Reason in 13 Parameters
**arXiv**：[2602.04118v1](https://arxiv.org/abs/2602.04118) · [PDF](https://arxiv.org/pdf/2602.04118.pdf)  
**作者**：John X. Morris, Niloofar Mireshghallah, Mark Ibrahim, Saeed Mahloujifar  

**一句话要点**：提出TinyLoRA方法，以13个参数在推理任务中实现高效微调。

**关键词**：低秩适配器, 推理学习, 强化学习, 参数高效微调, 语言模型

## 3 点简述
- 核心问题：传统LoRA无法在模型维度以下缩放，质疑低秩适配器是否必要。
- 方法要点：开发TinyLoRA，将低秩适配器规模缩小至单个参数。
- 实验或效果：在GSM8K上达到91%准确率，多个基准上以千倍少参数恢复90%性能提升。

## 摘要（原文）

> Recent research has shown that language models can learn to \textit{reason}, often via reinforcement learning. Some work even trains low-rank parameterizations for reasoning, but conventional LoRA cannot scale below the model dimension. We question whether even rank=1 LoRA is necessary for learning to reason and propose TinyLoRA, a method for scaling low-rank adapters to sizes as small as one parameter. Within our new parameterization, we are able to train the 8B parameter size of Qwen2.5 to 91\% accuracy on GSM8K with only 13 trained parameters in bf16 (26 total bytes). We find this trend holds in general: we are able to recover 90\% of performance improvements while training $1000x$ fewer parameters across a suite of more difficult learning-to-reason benchmarks such as AIME, AMC, and MATH500. Notably, we are only able to achieve such strong performance with RL: models trained using SFT require $100-1000x$ larger updates to reach the same performance.

