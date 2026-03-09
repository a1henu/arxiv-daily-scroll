---
layout: default
title: VLM-RobustBench: A Comprehensive Benchmark for Robustness of Vision-Language Models
---

# VLM-RobustBench: A Comprehensive Benchmark for Robustness of Vision-Language Models
**arXiv**：[2603.06148v1](https://arxiv.org/abs/2603.06148) · [PDF](https://arxiv.org/pdf/2603.06148.pdf)  
**作者**：Rohit Saxena, Alessandro Suglia, Pasquale Minervini  

**一句话要点**：提出VLM-RobustBench以评估视觉语言模型在图像失真下的鲁棒性

**关键词**：视觉语言模型, 鲁棒性评估, 图像失真, 基准测试, 几何扰动, 性能分析

## 3 点简述
- 核心问题：视觉语言模型在真实世界图像失真下的性能尚不明确
- 方法要点：构建包含49种增强类型和133种损坏设置的全面基准
- 实验或效果：发现模型对空间扰动更脆弱，几何失真导致性能下降最大

## 摘要（原文）

> Vision-language models (VLMs) achieve strong performance on standard, high-quality datasets, but we still do not fully understand how they perform under real-world image distortions. We present VLM-RobustBench, a benchmark spanning 49 augmentation types across noise, blur, weather, digital, and geometric perturbations, evaluated under graded severities (low/mid/high) and binary transforms, yielding 133 corrupted settings. We evaluate VLMs from four families (Qwen, InternVL, Molmo, Gemma) on two complementary benchmarks: MMBench (visually grounded) and MMMU-Pro (reasoning-oriented). Our results reveal that visual severity is a weak predictor of difficulty: low-severity spatial perturbations often degrade performance more than visually severe photometric corruptions. In particular, low-severity glass_blur reduces MMBench accuracy by about 8 pp on average across models, while the largest drops arise from resampling and geometric distortions (e.g., upsample, elastic_transform), reaching up to 34 pp. Overall, our findings suggest current VLMs are semantically strong but spatially fragile, motivating the definition of novel robustness evaluation protocols and training regimes that emphasize resampling and geometric invariances.

