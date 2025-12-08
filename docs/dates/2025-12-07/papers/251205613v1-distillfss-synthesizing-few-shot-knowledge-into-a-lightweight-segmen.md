---
layout: default
title: DistillFSS: Synthesizing Few-Shot Knowledge into a Lightweight Segmentation Model
---

# DistillFSS: Synthesizing Few-Shot Knowledge into a Lightweight Segmentation Model
**arXiv**：[2512.05613v1](https://arxiv.org/abs/2512.05613) · [PDF](https://arxiv.org/pdf/2512.05613.pdf)  
**作者**：Pasquale De Marinis, Pieter M. Blok, Uzay Kaymak, Rogier Brussee, Gennaro Vessio, Giovanna Castellano  

**一句话要点**：提出DistillFSS框架，通过蒸馏将少样本知识嵌入模型参数，解决跨域少样本语义分割的挑战。

**关键词**：跨域少样本语义分割, 知识蒸馏, 轻量级模型, 参数嵌入, 多域基准, 高效推理

## 3 点简述
- 核心问题：跨域少样本语义分割面临域分布偏移、标签空间不重叠和支持样本稀缺的挑战。
- 方法要点：采用教师-学生蒸馏，将少样本推理内化到学生网络专用层，无需测试时支持图像。
- 实验或效果：在新基准上匹配或超越先进基线，尤其在多类多样本场景，显著提升效率。

## 摘要（原文）

> Cross-Domain Few-Shot Semantic Segmentation (CD-FSS) seeks to segment unknown classes in unseen domains using only a few annotated examples. This setting is inherently challenging: source and target domains exhibit substantial distribution shifts, label spaces are disjoint, and support images are scarce--making standard episodic methods unreliable and computationally demanding at test time. To address these constraints, we propose DistillFSS, a framework that embeds support-set knowledge directly into a model's parameters through a teacher--student distillation process. By internalizing few-shot reasoning into a dedicated layer within the student network, DistillFSS eliminates the need for support images at test time, enabling fast, lightweight inference, while allowing efficient extension to novel classes in unseen domains through rapid teacher-driven specialization. Combined with fine-tuning, the approach scales efficiently to large support sets and significantly reduces computational overhead. To evaluate the framework under realistic conditions, we introduce a new CD-FSS benchmark spanning medical imaging, industrial inspection, and remote sensing, with disjoint label spaces and variable support sizes. Experiments show that DistillFSS matches or surpasses state-of-the-art baselines, particularly in multi-class and multi-shot scenarios, while offering substantial efficiency gains. The code is available at https://github.com/pasqualedem/DistillFSS.

