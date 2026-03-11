---
layout: default
title: OddGridBench: Exposing the Lack of Fine-Grained Visual Discrepancy Sensitivity in Multimodal Large Language Models
---

# OddGridBench: Exposing the Lack of Fine-Grained Visual Discrepancy Sensitivity in Multimodal Large Language Models
**arXiv**：[2603.09326v1](https://arxiv.org/abs/2603.09326) · [PDF](https://arxiv.org/pdf/2603.09326.pdf)  
**作者**：Tengjin Weng, Wenhao Jiang, Jingyi Wang, Ming Li, Lin Ma, Zhong Ming  

**一句话要点**：提出OddGridBench基准和OddGrid-GRPO框架以评估和提升多模态大语言模型的细粒度视觉差异感知能力

**关键词**：视觉差异感知, 多模态大语言模型, 基准评估, 强化学习, 细粒度视觉

## 3 点简述
- 核心问题：多模态大语言模型在细粒度视觉差异检测方面表现不佳，缺乏系统评估。
- 方法要点：构建可控网格图像基准OddGridBench，并设计集成课程学习和距离感知奖励的强化学习框架OddGrid-GRPO。
- 实验或效果：实验显示现有模型远低于人类水平，OddGrid-GRPO显著提升模型视觉辨别能力。

## 摘要（原文）

> Multimodal large language models (MLLMs) have achieved remarkable performance across a wide range of vision language tasks. However, their ability in low-level visual perception, particularly in detecting fine-grained visual discrepancies, remains underexplored and lacks systematic analysis. In this work, we introduce OddGridBench, a controllable benchmark for evaluating the visual discrepancy sensitivity of MLLMs. OddGridBench comprises over 1,400 grid-based images, where a single element differs from all others by one or multiple visual attributes such as color, size, rotation, or position. Experiments reveal that all evaluated MLLMs, including open-source families such as Qwen3-VL and InternVL3.5, and proprietary systems like Gemini-2.5-Pro and GPT-5, perform far below human levels in visual discrepancy detection. We further propose OddGrid-GRPO, a reinforcement learning framework that integrates curriculum learning and distance-aware reward. By progressively controlling the difficulty of training samples and incorporating spatial proximity constraints into the reward design, OddGrid-GRPO significantly enhances the model's fine-grained visual discrimination ability. We hope OddGridBench and OddGrid-GRPO will lay the groundwork for advancing perceptual grounding and visual discrepancy sensitivity in multimodal intelligence. Code and dataset are available at https://wwwtttjjj.github.io/OddGridBench/.

