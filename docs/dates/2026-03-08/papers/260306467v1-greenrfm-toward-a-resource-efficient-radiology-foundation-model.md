---
layout: default
title: GreenRFM: Toward a resource-efficient radiology foundation model
---

# GreenRFM: Toward a resource-efficient radiology foundation model
**arXiv**：[2603.06467v1](https://arxiv.org/abs/2603.06467) · [PDF](https://arxiv.org/pdf/2603.06467.pdf)  
**作者**：Yingtai Li, Shuai Ming, Mingyue Zhao, Haoran Lai, Rongsheng Wang, Rui Zhou, Rundong Wang, Yujia Li, Wei Wei, Shaohua Kevin Zhou  

**一句话要点**：提出GreenRFM资源高效预训练框架，以解决放射学基础模型依赖暴力扩展的问题。

**关键词**：放射学基础模型, 资源高效预训练, MUST监督, 计算效率, 多模态泛化

## 3 点简述
- 核心问题：现有放射学基础模型依赖暴力扩展，导致模型脆弱且计算成本高。
- 方法要点：采用MUST监督设计，最大化利用监督信号，而非单纯增加数据量。
- 实验或效果：在多个数据集上超越基线模型，计算需求大幅降低，支持单GPU快速训练。

## 摘要（原文）

> The development of radiology foundation models (RFMs) is hindered by a reliance on brute-force scaling. Existing approaches often directly translate methods for natural images, which prioritize scale over precision and hence lead to brittle and expensive models in clinical practice. To address this, we present a resource-efficient pre-training framework, GreenRFM, that achieves state-of-the-art performance. Our framework ensures robust generalization across diverse patient populations and imaging protocols, reducing computational requirements by orders of magnitude while surpassing complex, parameter-heavy models. These capabilities stem from principled supervision design that aims to maximally utilize supervisory signals via More distilled, Ubiquitous, Semantic-enforcing, and Task-aligning (MUST) supervision, rather than simply piling up the quantity of training data. We offer two GreenRFM configurations: (i) a performant model that establishes a new state-of-the-art using a single 24GB GPU within 24 hours, and (ii) a lightweight model that matches existing benchmarks with 6GB VRAM in 4 hours. We conduct extensive experiments using over 200,000 images from four institutions and of two modalities. GreenRFMs achieve superior performances on chest and abdominal CT datasets, regardless of public or private benchmark, surpassing a range of baseline models. In addition, the results on internal musculoskeletal MRI images show that the same supervision principles transfer between different modalities. Our performance and efficiency challenge the ``scale is all you need'' dogma and democratize the equitable development of state-of-the-art RFMs for clinicians even on a laptop.

