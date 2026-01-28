---
layout: default
title: AROMMA: Unifying Olfactory Embeddings for Single Molecules and Mixtures
---

# AROMMA: Unifying Olfactory Embeddings for Single Molecules and Mixtures
**arXiv**：[2601.19561v1](https://arxiv.org/abs/2601.19561) · [PDF](https://arxiv.org/pdf/2601.19561.pdf)  
**作者**：Dayoung Kang, JongWon Kim, Jiho Park, Keonseock Lee, Ji-Woong Choi, Jinhyun So  

**一句话要点**：提出AROMMA框架以统一单分子与混合物的嗅觉嵌入空间

**关键词**：嗅觉嵌入, 化学基础模型, 注意力聚合, 知识蒸馏, 伪标签对齐

## 3 点简述
- 公共嗅觉数据集小且分散，限制通用气味表示学习
- 基于化学基础模型编码单分子，注意力聚合器处理混合物
- 在单分子和分子对数据集上实现SOTA性能，AUROC提升达19.1%

## 摘要（原文）

> Public olfaction datasets are small and fragmented across single molecules and mixtures, limiting learning of generalizable odor representations. Recent works either learn single-molecule embeddings or address mixtures via similarity or pairwise label prediction, leaving representations separate and unaligned. In this work, we propose AROMMA, a framework that learns a unified embedding space for single molecules and two-molecule mixtures. Each molecule is encoded by a chemical foundation model and the mixtures are composed by an attention-based aggregator, ensuring both permutation invariance and asymmetric molecular interactions. We further align odor descriptor sets using knowledge distillation and class-aware pseudo-labeling to enrich missing mixture annotations. AROMMA achieves state-of-the-art performance in both single-molecule and molecule-pair datasets, with up to 19.1% AUROC improvement, demonstrating a robust generalization in two domains.

