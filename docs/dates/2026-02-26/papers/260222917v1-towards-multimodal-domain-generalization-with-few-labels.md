---
layout: default
title: Towards Multimodal Domain Generalization with Few Labels
---

# Towards Multimodal Domain Generalization with Few Labels
**arXiv**：[2602.22917v1](https://arxiv.org/abs/2602.22917) · [PDF](https://arxiv.org/pdf/2602.22917.pdf)  
**作者**：Hongzhao Li, Hao Dong, Hualei Wan, Shupan Li, Mingliang Xu, Muhammad Haris Khan  

**一句话要点**：提出半监督多模态域泛化框架，以解决少标签下多源数据中的域偏移与模态缺失问题。

**关键词**：半监督学习, 多模态学习, 域泛化, 伪标签生成, 跨模态对齐, 模态缺失鲁棒性

## 3 点简述
- 核心问题：现有方法无法有效结合半监督学习与多模态域泛化，导致在少标签场景下泛化能力不足。
- 方法要点：通过共识驱动一致性正则化、分歧感知正则化和跨模态原型对齐，提升模型鲁棒性和数据效率。
- 实验或效果：在新建基准测试中，该方法在标准与模态缺失场景下均优于基线模型。

## 摘要（原文）

> Multimodal models ideally should generalize to unseen domains while remaining data-efficient to reduce annotation costs. To this end, we introduce and study a new problem, Semi-Supervised Multimodal Domain Generalization (SSMDG), which aims to learn robust multimodal models from multi-source data with few labeled samples. We observe that existing approaches fail to address this setting effectively: multimodal domain generalization methods cannot exploit unlabeled data, semi-supervised multimodal learning methods ignore domain shifts, and semi-supervised domain generalization methods are confined to single-modality inputs. To overcome these limitations, we propose a unified framework featuring three key components: Consensus-Driven Consistency Regularization, which obtains reliable pseudo-labels through confident fused-unimodal consensus; Disagreement-Aware Regularization, which effectively utilizes ambiguous non-consensus samples; and Cross-Modal Prototype Alignment, which enforces domain- and modality-invariant representations while promoting robustness under missing modalities via cross-modal translation. We further establish the first SSMDG benchmarks, on which our method consistently outperforms strong baselines in both standard and missing-modality scenarios. Our benchmarks and code are available at https://github.com/lihongzhao99/SSMDG.

