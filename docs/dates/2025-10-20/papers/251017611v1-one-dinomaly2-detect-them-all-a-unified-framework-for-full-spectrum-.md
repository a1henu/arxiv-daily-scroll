---
layout: default
title: One Dinomaly2 Detect Them All: A Unified Framework for Full-Spectrum Unsupervised Anomaly Detection
---

# One Dinomaly2 Detect Them All: A Unified Framework for Full-Spectrum Unsupervised Anomaly Detection
**arXiv**：[2510.17611v1](https://arxiv.org/abs/2510.17611) · [PDF](https://arxiv.org/pdf/2510.17611.pdf)  
**作者**：Jia Guo, Shuai Lu, Lei Fan, Zelin Li, Donglin Di, Yang Song, Weihang Zhang, Wenbing Zhu, Hong Yan, Fang Chen, Huiqi Li, Hongen Liao  

**一句话要点**：提出Dinomaly2统一框架，解决全谱无监督异常检测性能与通用性问题

**关键词**：无监督异常检测, 多类检测, 重构框架, 全谱应用, 少样本学习

## 3 点简述
- 现有多类无监督异常检测模型性能落后于单类模型，且方法碎片化阻碍部署
- 基于重构框架，协调五个简单元素实现高性能，无需修改即可扩展多任务
- 在12个基准测试中，多类、少样本等场景下表现优异，如MVTec-AD达99.9% AUROC

## 摘要（原文）

> Unsupervised anomaly detection (UAD) has evolved from building specialized
> single-class models to unified multi-class models, yet existing multi-class
> models significantly underperform the most advanced one-for-one counterparts.
> Moreover, the field has fragmented into specialized methods tailored to
> specific scenarios (multi-class, 3D, few-shot, etc.), creating deployment
> barriers and highlighting the need for a unified solution. In this paper, we
> present Dinomaly2, the first unified framework for full-spectrum image UAD,
> which bridges the performance gap in multi-class models while seamlessly
> extending across diverse data modalities and task settings. Guided by the "less
> is more" philosophy, we demonstrate that the orchestration of five simple
> element achieves superior performance in a standard reconstruction-based
> framework. This methodological minimalism enables natural extension across
> diverse tasks without modification, establishing that simplicity is the
> foundation of true universality. Extensive experiments on 12 UAD benchmarks
> demonstrate Dinomaly2's full-spectrum superiority across multiple modalities
> (2D, multi-view, RGB-3D, RGB-IR), task settings (single-class, multi-class,
> inference-unified multi-class, few-shot) and application domains (industrial,
> biological, outdoor). For example, our multi-class model achieves unprecedented
> 99.9% and 99.3% image-level (I-) AUROC on MVTec-AD and VisA respectively. For
> multi-view and multi-modal inspection, Dinomaly2 demonstrates state-of-the-art
> performance with minimum adaptations. Moreover, using only 8 normal examples
> per class, our method surpasses previous full-shot models, achieving 98.7% and
> 97.4% I-AUROC on MVTec-AD and VisA. The combination of minimalistic design,
> computational scalability, and universal applicability positions Dinomaly2 as a
> unified solution for the full spectrum of real-world anomaly detection
> applications.

