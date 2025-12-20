---
layout: default
title: Domain-Agnostic Causal-Aware Audio Transformer for Infant Cry Classification
---

# Domain-Agnostic Causal-Aware Audio Transformer for Infant Cry Classification
**arXiv**：[2512.16271v1](https://arxiv.org/abs/2512.16271) · [PDF](https://arxiv.org/pdf/2512.16271.pdf)  
**作者**：Geofrey Owino, Bernard Shibwabo Kasamani, Ahmed M. Abdelmoniem, Edem Wornyo  

**一句话要点**：提出DACH-TIC模型以解决婴儿哭声分类中的噪声和领域偏移问题。

**关键词**：婴儿哭声分类, 因果注意力, 对抗领域泛化, 多任务学习, 音频Transformer

## 3 点简述
- 核心问题：现有方法依赖相关性驱动表示，易受噪声和领域变化影响。
- 方法要点：集成因果注意力、分层表示学习、多任务监督和对抗领域泛化。
- 实验或效果：在Baby Chillanto和Donate-a-Cry数据集上优于基线，准确率提升2.6%。

## 摘要（原文）

> Accurate and interpretable classification of infant cry paralinguistics is essential for early detection of neonatal distress and clinical decision support. However, many existing deep learning methods rely on correlation-driven acoustic representations, which makes them vulnerable to noise, spurious cues, and domain shifts across recording environments. We propose DACH-TIC, a Domain-Agnostic Causal-Aware Hierarchical Audio Transformer for robust infant cry classification. The model integrates causal attention, hierarchical representation learning, multi-task supervision, and adversarial domain generalization within a unified framework.
>   DACH-TIC employs a structured transformer backbone with local token-level and global semantic encoders, augmented by causal attention masking and controlled perturbation training to approximate counterfactual acoustic variations. A domain-adversarial objective promotes environment-invariant representations, while multi-task learning jointly optimizes cry type recognition, distress intensity estimation, and causal relevance prediction. The model is evaluated on the Baby Chillanto and Donate-a-Cry datasets, with ESC-50 environmental noise overlays for domain augmentation.
>   Experimental results show that DACH-TIC outperforms state-of-the-art baselines, including HTS-AT and SE-ResNet Transformer, achieving improvements of 2.6 percent in accuracy and 2.2 points in macro-F1 score, alongside enhanced causal fidelity. The model generalizes effectively to unseen acoustic environments, with a domain performance gap of only 2.4 percent, demonstrating its suitability for real-world neonatal acoustic monitoring systems.

