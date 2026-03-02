---
layout: default
title: Footprint-Guided Exemplar-Free Continual Histopathology Report Generation
---

# Footprint-Guided Exemplar-Free Continual Histopathology Report Generation
**arXiv**：[2602.23817v1](https://arxiv.org/abs/2602.23817) · [PDF](https://arxiv.org/pdf/2602.23817.pdf)  
**作者**：Pratibha Kumari, Daniel Reisenbüchler, Afshin Bozorgpour, yousef Sadegheih, Priyankar Choudhary, Dorit Merhof  

**一句话要点**：提出基于足迹引导的无样本持续学习框架，用于病理报告生成以应对临床数据动态变化。

**关键词**：病理报告生成, 持续学习, 生成式回放, 域足迹, 灾难性遗忘, 风格描述符

## 3 点简述
- 核心问题：病理报告生成中，新器官、机构或报告惯例的持续出现导致传统方法面临灾难性遗忘。
- 方法要点：构建紧凑域足迹，包括形态学令牌代码本和共现摘要，支持生成式回放以合成伪WSI表示，避免存储原始数据。
- 实验或效果：在多个公开持续学习基准上，优于无样本和有限缓冲基线，验证了足迹引导生成回放的实用性。

## 摘要（原文）

> Rapid progress in vision-language modeling has enabled pathology report generation from gigapixel whole-slide images, but most approaches assume static training with simultaneous access to all data. In clinical deployment, however, new organs, institutions, and reporting conventions emerge over time, and sequential fine-tuning can cause catastrophic forgetting. We introduce an exemplar-free continual learning framework for WSI-to-report generation that avoids storing raw slides or patch exemplars. The core idea is a compact domain footprint built in a frozen patch-embedding space: a small codebook of representative morphology tokens together with slide-level co-occurrence summaries and lightweight patch-count priors. These footprints support generative replay by synthesizing pseudo-WSI representations that reflect domain-specific morphological mixtures, while a teacher snapshot provides pseudo-reports to supervise the updated model without retaining past data. To address shifting reporting conventions, we distill domain-specific linguistic characteristics into a compact style descriptor and use it to steer generation. At inference, the model identifies the most compatible descriptor directly from the slide signal, enabling domain-agnostic setup without requiring explicit domain identifiers. Evaluated across multiple public continual learning benchmarks, our approach outperforms exemplar-free and limited-buffer rehearsal baselines, highlighting footprint-based generative replay as a practical solution for deployment in evolving clinical settings.

