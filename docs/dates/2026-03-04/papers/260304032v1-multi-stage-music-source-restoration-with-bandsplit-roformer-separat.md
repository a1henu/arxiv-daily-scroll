---
layout: default
title: Multi-Stage Music Source Restoration with BandSplit-RoFormer Separation and HiFi++ GAN
---

# Multi-Stage Music Source Restoration with BandSplit-RoFormer Separation and HiFi++ GAN
**arXiv**：[2603.04032v1](https://arxiv.org/abs/2603.04032) · [PDF](https://arxiv.org/pdf/2603.04032.pdf)  
**作者**：Tobias Morocutti, Emmanouil Karystinaios, Jonathan Greif, Gerhard Widmer  

**一句话要点**：提出多阶段音乐源恢复系统，结合BandSplit-RoFormer分离与HiFi++ GAN恢复，用于ICASSP 2025挑战赛。

**关键词**：音乐源恢复, BandSplit-RoFormer分离, HiFi++ GAN, 多阶段训练, 波形恢复, ICASSP挑战赛

## 3 点简述
- 核心问题：音乐源恢复需从混合音频中恢复原始乐器音轨，处理非线性混合和制作效应。
- 方法要点：使用BandSplit-RoFormer分离器预测多音轨，并通过三阶段课程训练；应用HiFi++ GAN进行波形恢复，从通用到专家化。
- 实验或效果：系统针对ICASSP 2025挑战赛设计，具体性能未知，但整合了分离与恢复两阶段处理。

## 摘要（原文）

> Music Source Restoration (MSR) targets recovery of original, unprocessed instrument stems from fully mixed and mastered audio, where production effects and distribution artifacts violate common linear-mixture assumptions. This technical report presents the CP-JKU team's system for the MSR ICASSP Challenge 2025. Our approach decomposes MSR into separation and restoration. First, a single BandSplit-RoFormer separator predicts eight stems plus an auxiliary other stem, and is trained with a three-stage curriculum that progresses from 4-stem warm-start fine-tuning (with LoRA) to 8-stem extension via head expansion. Second, we apply a HiFi++ GAN waveform restorer trained as a generalist and then specialized into eight instrument-specific experts.

