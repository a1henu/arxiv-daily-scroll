---
layout: default
title: Unified Multimodal Brain Decoding via Cross-Subject Soft-ROI Fusion
---

# Unified Multimodal Brain Decoding via Cross-Subject Soft-ROI Fusion
**arXiv**：[2512.20249v1](https://arxiv.org/abs/2512.20249) · [PDF](https://arxiv.org/pdf/2512.20249.pdf)  
**作者**：Xuanyu Hu  

**一句话要点**：提出BrainROI模型，通过跨被试软ROI融合提升多模态脑解码的泛化性与可解释性。

**关键词**：多模态脑解码, 跨被试泛化, 软功能分区, 提示优化, 脑-字幕生成, fMRI编码

## 3 点简述
- 核心问题：多模态脑解码在跨被试泛化和可解释性方面面临挑战，如功能脑拓扑异质性和提示方法不稳定。
- 方法要点：设计fMRI编码器，使用软功能分区作为共享空间，引入体素门控融合机制和全局标签对齐以增强跨被试可转移性。
- 实验或效果：在NSD数据集上实现领先的脑-字幕评估结果，BLEU-4和CIDEr等指标在跨被试设置下优于现有方法。

## 摘要（原文）

> Multimodal brain decoding aims to reconstruct semantic information that is consistent with visual stimuli from brain activity signals such as fMRI, and then generate readable natural language descriptions. However, multimodal brain decoding still faces key challenges in cross-subject generalization and interpretability. We propose a BrainROI model and achieve leading-level results in brain-captioning evaluation on the NSD dataset. Under the cross-subject setting, compared with recent state-of-the-art methods and representative baselines, metrics such as BLEU-4 and CIDEr show clear improvements. Firstly, to address the heterogeneity of functional brain topology across subjects, we design a new fMRI encoder. We use multi-atlas soft functional parcellations (soft-ROI) as a shared space. We extend the discrete ROI Concatenation strategy in MINDLLM to a voxel-wise gated fusion mechanism (Voxel-gate). We also ensure consistent ROI mapping through global label alignment, which enhances cross-subject transferability. Secondly, to overcome the limitations of manual and black-box prompting methods in stability and transparency, we introduce an interpretable prompt optimization process. In a small-sample closed loop, we use a locally deployed Qwen model to iteratively generate and select human-readable prompts. This process improves the stability of prompt design and preserves an auditable optimization trajectory. Finally, we impose parameterized decoding constraints during inference to further improve the stability and quality of the generated descriptions.

