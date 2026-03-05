---
layout: default
title: Real5-OmniDocBench: A Full-Scale Physical Reconstruction Benchmark for Robust Document Parsing in the Wild
---

# Real5-OmniDocBench: A Full-Scale Physical Reconstruction Benchmark for Robust Document Parsing in the Wild
**arXiv**：[2603.04205v1](https://arxiv.org/abs/2603.04205) · [PDF](https://arxiv.org/pdf/2603.04205.pdf)  
**作者**：Changda Zhou, Ziyue Gao, Xueqing Wang, Tingquan Gao, Cheng Cui, Jing Tang, Yi Liu  

**一句话要点**：提出Real5-OmniDocBench基准，通过全尺度物理重建评估文档解析在真实场景中的鲁棒性。

**关键词**：文档解析基准, 物理重建评估, 视觉语言模型, 鲁棒性测试, 现实差距分析

## 3 点简述
- 核心问题：视觉语言模型在数字文档基准上表现优异，但在物理世界中的性能未知，缺乏可控且现实的评估。
- 方法要点：首次对OmniDocBench v1.5进行全尺度一对一物理重建，覆盖扫描、扭曲、屏幕摄影、光照和倾斜五种关键场景。
- 实验或效果：基准提供完整真实映射，能严格归因性能下降，揭示文档解析的“现实差距”远未解决，并作为诊断工具指导发展。

## 摘要（原文）

> While Vision-Language Models (VLMs) achieve near-perfect scores on digital document benchmarks like OmniDocBench, their performance in the unpredictable physical world remains largely unknown due to the lack of controlled yet realistic evaluations. We introduce Real5-OmniDocBench, the first benchmark that performs a full-scale, one-to-one physical reconstruction of the entire OmniDocBench v1.5 (1,355 images) across five critical real-world scenarios: Scanning, Warping, Screen-Photography, Illumination, and Skew. Unlike prior benchmark that either lack digital correspondence or employ partial sampling, our complete ground-truth mapping enables, for the first time, rigorous factor-wise attribution of performance degradation-allowing us to pinpoint whether failures stem from geometric distortions, optical artifacts, or model limitations. Our benchmark establishes a challenging new standard for the community, demonstrating that the 'reality gap' in document parsing is far from closed, and provides a diagnostic tool to guide the development of truly resilient document intelligence.

