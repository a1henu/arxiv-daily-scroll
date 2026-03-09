---
layout: default
title: Do Compact SSL Backbones Matter for Audio Deepfake Detection? A Controlled Study with RAPTOR
---

# Do Compact SSL Backbones Matter for Audio Deepfake Detection? A Controlled Study with RAPTOR
**arXiv**：[2603.06164v1](https://arxiv.org/abs/2603.06164) · [PDF](https://arxiv.org/pdf/2603.06164.pdf)  
**作者**：Ajinkya Kulkarni, Sandipana Dowerah, Atharva Kulkarni, Tanel Alumäe, Mathew Magimai Doss  

**一句话要点**：提出RAPTOR框架，通过对比紧凑SSL骨干网在音频深度伪造检测中的性能，揭示多语言预训练对跨域鲁棒性的关键作用。

**关键词**：音频深度伪造检测, 自监督学习, 紧凑骨干网, 跨域鲁棒性, 模型校准, 测试时增强

## 3 点简述
- 核心问题：现有音频深度伪造检测研究多聚焦于大型wav2vec2-XLSR骨干网，紧凑SSL骨干网的性能与鲁棒性未充分探索。
- 方法要点：设计RAPTOR检测器，统一融合HuBERT和WavLM等紧凑SSL骨干网，并进行受控研究，评估跨域性能。
- 实验或效果：多语言HuBERT预训练是跨域鲁棒性的主要驱动力，100M参数模型可媲美大型商业系统；引入测试时增强协议，揭示WavLM变体在扰动下存在过度自信校准问题。

## 摘要（原文）

> Self-supervised learning (SSL) underpins modern audio deepfake detection, yet most prior work centers on a single large wav2vec2-XLSR backbone, leaving compact under studied. We present RAPTOR, Representation Aware Pairwise-gated Transformer for Out-of-domain Recognition a controlled study of compact SSL backbones from the HuBERT and WavLM within a unified pairwise-gated fusion detector, evaluated across 14 cross-domain benchmarks. We show that multilingual HuBERT pre-training is the primary driver of cross-domain robustness, enabling 100M models to match larger and commercial systems. Beyond EER, we introduce a test-time augmentation protocol with perturbation-based aleatoric uncertainty to expose calibration differences invisible to standard metrics: WavLM variants exhibit overconfident miscalibration under perturbation, whereas iterative mHuBERT remains stable. These findings indicate that SSL pre-training trajectory, not model scale, drives reliable audio deepfake detection.

