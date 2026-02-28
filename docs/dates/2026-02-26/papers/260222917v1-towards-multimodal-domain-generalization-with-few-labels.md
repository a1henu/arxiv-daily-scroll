---
layout: default
title: Towards Multimodal Domain Generalization with Few Labels
---

# Towards Multimodal Domain Generalization with Few Labels
**arXiv**：[2602.22917v1](https://arxiv.org/abs/2602.22917) · [PDF](https://arxiv.org/pdf/2602.22917.pdf)  
**作者**：Hongzhao Li, Hao Dong, Hualei Wan, Shupan Li, Mingliang Xu, Muhammad Haris Khan  

**一句话要点**：提出半监督多模态域泛化框架，以少量标签学习鲁棒模型并处理模态缺失。

**关键词**：多模态学习, 域泛化, 半监督学习, 模态缺失处理, 一致性正则化, 原型对齐

## 3 点简述
- 核心问题：现有方法无法有效结合多模态、域泛化和半监督学习，导致数据效率和泛化能力不足。
- 方法要点：通过共识驱动一致性正则化、分歧感知正则化和跨模态原型对齐，提升模型鲁棒性和域不变性。
- 实验或效果：在新建基准上优于基线，在标准及模态缺失场景中均表现一致。

## 摘要（原文）

> Multimodal models ideally should generalize to unseen domains while remaining data-efficient to reduce annotation costs. To this end, we introduce and study a new problem, Semi-Supervised Multimodal Domain Generalization (SSMDG), which aims to learn robust multimodal models from multi-source data with few labeled samples. We observe that existing approaches fail to address this setting effectively: multimodal domain generalization methods cannot exploit unlabeled data, semi-supervised multimodal learning methods ignore domain shifts, and semi-supervised domain generalization methods are confined to single-modality inputs. To overcome these limitations, we propose a unified framework featuring three key components: Consensus-Driven Consistency Regularization, which obtains reliable pseudo-labels through confident fused-unimodal consensus; Disagreement-Aware Regularization, which effectively utilizes ambiguous non-consensus samples; and Cross-Modal Prototype Alignment, which enforces domain- and modality-invariant representations while promoting robustness under missing modalities via cross-modal translation. We further establish the first SSMDG benchmarks, on which our method consistently outperforms strong baselines in both standard and missing-modality scenarios. Our benchmarks and code are available at https://github.com/lihongzhao99/SSMDG.

