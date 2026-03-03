---
layout: default
title: DOCFORGE-BENCH: A Comprehensive Benchmark for Document Forgery Detection and Analysis
---

# DOCFORGE-BENCH: A Comprehensive Benchmark for Document Forgery Detection and Analysis
**arXiv**：[2603.01433v1](https://arxiv.org/abs/2603.01433) · [PDF](https://arxiv.org/pdf/2603.01433.pdf)  
**作者**：Zengqi Zhao, Weidi Xia, Peter Wei, Yan Zhang, Yiyi Zhang, Jane Mo, Tiannan Zhang, Yuanqin Dai, Zexi Chen, Simiao Ren  

**一句话要点**：提出DOCFORGE-BENCH基准，评估零样本文档伪造检测方法在真实部署场景中的性能。

**关键词**：文档伪造检测, 零样本基准, 校准失败, 阈值适应, 像素级评估, 生成AI未知

## 3 点简述
- 核心问题：现有方法在文档伪造检测中普遍存在校准失败，导致Pixel-F1接近零，尽管Pixel-AUC较高。
- 方法要点：设计统一零样本基准，评估14种方法在8个数据集上，使用预训练权重且无领域适应。
- 实验或效果：通过阈值校准实验，证明调整单一阈值可显著提升性能，校准是实际部署的关键瓶颈。

## 摘要（原文）

> We present DOCFORGE-BENCH, the first unified zero-shot benchmark for document forgery detection, evaluating 14 methods across eight datasets spanning text tampering, receipt forgery, and identity document manipulation. Unlike fine-tuning-oriented evaluations such as ForensicHub [Du et al., 2025], DOCFORGE-BENCH applies all methods with their published pretrained weights and no domain adaptation -- a deliberate design choice that reflects the realistic deployment scenario where practitioners lack labeled document training data. Our central finding is a pervasive calibration failure invisible under single-threshold protocols: methods achieve moderate Pixel-AUC (>=0.76) yet near-zero Pixel-F1. This AUC-F1 gap is not a discrimination failure but a score-distribution shift: tampered regions occupy only 0.27-4.17% of pixels in document images -- an order of magnitude less than in natural image benchmarks -- making the standard tau=0.5 threshold catastrophically miscalibrated. Oracle-F1 is 2-10x higher than fixed-threshold Pixel-F1, confirming that calibration, not representation, is the bottleneck. A controlled calibration experiment validates this: adapting a single threshold on N=10 domain images recovers 39-55% of the Oracle-F1 gap, demonstrating that threshold adaptation -- not retraining -- is the key missing step for practical deployment. Overall, no evaluated method works reliably out-of-the-box on diverse document types, underscoring that document forgery detection remains an unsolved problem. We further note that all eight datasets predate the era of generative AI editing; benchmarks covering diffusion- and LLM-based document forgeries represent a critical open gap on the modern attack surface.

