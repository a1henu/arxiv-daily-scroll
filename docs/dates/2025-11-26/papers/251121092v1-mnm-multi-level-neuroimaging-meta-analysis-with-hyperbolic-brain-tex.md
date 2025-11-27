---
layout: default
title: MNM : Multi-level Neuroimaging Meta-analysis with Hyperbolic Brain-Text Representations
---

# MNM : Multi-level Neuroimaging Meta-analysis with Hyperbolic Brain-Text Representations
**arXiv**：[2511.21092v1](https://arxiv.org/abs/2511.21092) · [PDF](https://arxiv.org/pdf/2511.21092.pdf)  
**作者**：Seunghun Baek, Jaejin Lee, Jaeyoon Sim, Minjae Jeong, Won Hwa Kim  

**一句话要点**：提出基于双曲几何的多层次神经影像元分析框架，以解决小样本问题。

**关键词**：神经影像元分析, 双曲几何, 脑-文本表示, 多层次对齐, 语义嵌入

## 3 点简述
- 神经影像研究常因小样本量限制可靠性，元分析可聚合多研究识别一致脑活动模式。
- 利用双曲空间嵌入脑图像和文本，捕捉语义相似性和层次结构，实现多层次对齐。
- 实验显示模型优于基线，提供鲁棒且可解释的脑-文本表示元分析范式。

## 摘要（原文）

> Various neuroimaging studies suffer from small sample size problem which often limit their reliability. Meta-analysis addresses this challenge by aggregating findings from different studies to identify consistent patterns of brain activity. However, traditional approaches based on keyword retrieval or linear mappings often overlook the rich hierarchical structure in the brain. In this work, we propose a novel framework that leverages hyperbolic geometry to bridge the gap between neuroscience literature and brain activation maps. By embedding text from research articles and corresponding brain images into a shared hyperbolic space via the Lorentz model, our method captures both semantic similarity and hierarchical organization inherent in neuroimaging data. In the hyperbolic space, our method performs multi-level neuroimaging meta-analysis (MNM) by 1) aligning brain and text embeddings for semantic correspondence, 2) guiding hierarchy between text and brain activations, and 3) preserving the hierarchical relationships within brain activation patterns. Experimental results demonstrate that our model outperforms baselines, offering a robust and interpretable paradigm of multi-level neuroimaging meta-analysis via hyperbolic brain-text representation.

