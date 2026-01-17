---
layout: default
title: Optimizing Multimodal LLMs for Egocentric Video Understanding: A Solution for the HD-EPIC VQA Challenge
---

# Optimizing Multimodal LLMs for Egocentric Video Understanding: A Solution for the HD-EPIC VQA Challenge
**arXiv**：[2601.10228v1](https://arxiv.org/abs/2601.10228) · [PDF](https://arxiv.org/pdf/2601.10228.pdf)  
**作者**：Sicheng Yang, Yukai Huang, Shitong Sun, Weitong Cai, Jiankang Deng, Jifei Song, Zhensong Zhang  

**一句话要点**：提出集成框架以优化多模态大语言模型在HD-EPIC VQA挑战中的第一人称视频理解

**关键词**：第一人称视频理解, 多模态大语言模型, 时序推理, 微调优化, 视频问答

## 3 点简述
- 核心问题：多模态大语言模型在HD-EPIC VQA中面临查询模糊、长程时序推理差和非标准化输出等挑战。
- 方法要点：结合查询/选项预处理、领域特定Qwen2.5-VL微调、新颖时序思维链提示和鲁棒后处理。
- 实验或效果：系统在HD-EPIC VQA上达到41.6%准确率，强调整体管道优化的重要性。

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) struggle with complex video QA benchmarks like HD-EPIC VQA due to ambiguous queries/options, poor long-range temporal reasoning, and non-standardized outputs. We propose a framework integrating query/choice pre-processing, domain-specific Qwen2.5-VL fine-tuning, a novel Temporal Chain-of-Thought (T-CoT) prompting for multi-step reasoning, and robust post-processing. This system achieves 41.6% accuracy on HD-EPIC VQA, highlighting the need for holistic pipeline optimization in demanding video understanding. Our code, fine-tuned models are available at https://github.com/YoungSeng/Egocentric-Co-Pilot.

