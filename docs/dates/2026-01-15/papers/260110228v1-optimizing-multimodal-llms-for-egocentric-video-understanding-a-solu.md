---
layout: default
title: Optimizing Multimodal LLMs for Egocentric Video Understanding: A Solution for the HD-EPIC VQA Challenge
---

# Optimizing Multimodal LLMs for Egocentric Video Understanding: A Solution for the HD-EPIC VQA Challenge
**arXiv**：[2601.10228v1](https://arxiv.org/abs/2601.10228) · [PDF](https://arxiv.org/pdf/2601.10228.pdf)  
**作者**：Sicheng Yang, Yukai Huang, Shitong Sun, Weitong Cai, Jiankang Deng, Jifei Song, Zhensong Zhang  

**一句话要点**：提出集成查询预处理、领域微调、时序思维链提示和后处理的框架，以优化多模态大语言模型在HD-EPIC VQA挑战中的自我中心视频理解。

**关键词**：自我中心视频理解, 多模态大语言模型, 时序推理, 微调优化, 视频问答, 管道优化

## 3 点简述
- 核心问题：多模态大语言模型在HD-EPIC VQA等复杂视频问答基准中表现不佳，原因包括查询/选项模糊、长程时序推理能力差和非标准化输出。
- 方法要点：框架整合查询/选择预处理、领域特定的Qwen2.5-VL微调、新颖的时序思维链提示用于多步推理，以及鲁棒的后处理。
- 实验或效果：系统在HD-EPIC VQA上达到41.6%的准确率，强调了在苛刻视频理解任务中整体管道优化的必要性。

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) struggle with complex video QA benchmarks like HD-EPIC VQA due to ambiguous queries/options, poor long-range temporal reasoning, and non-standardized outputs. We propose a framework integrating query/choice pre-processing, domain-specific Qwen2.5-VL fine-tuning, a novel Temporal Chain-of-Thought (T-CoT) prompting for multi-step reasoning, and robust post-processing. This system achieves 41.6% accuracy on HD-EPIC VQA, highlighting the need for holistic pipeline optimization in demanding video understanding. Our code, fine-tuned models are available at https://github.com/YoungSeng/Egocentric-Co-Pilot.

