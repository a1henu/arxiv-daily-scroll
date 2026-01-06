---
layout: default
title: BiPrompt: Bilateral Prompt Optimization for Visual and Textual Debiasing in Vision-Language Models
---

# BiPrompt: Bilateral Prompt Optimization for Visual and Textual Debiasing in Vision-Language Models
**arXiv**：[2601.02147v1](https://arxiv.org/abs/2601.02147) · [PDF](https://arxiv.org/pdf/2601.02147.pdf)  
**作者**：Sunny Gupta, Shounak Das, Amit Sethi  

**一句话要点**：提出BiPrompt双边提示优化框架，以解决视觉语言模型在测试时适应中的视觉和文本模态偏见问题。

**关键词**：视觉语言模型, 测试时适应, 去偏, 提示优化, 多模态学习, 因果推理

## 3 点简述
- 核心问题：视觉语言基础模型如CLIP在零样本泛化中易受视觉和文本模态间虚假相关性的影响，现有去偏方法常仅处理单一模态，导致部分鲁棒性和分布偏移下的不稳定适应。
- 方法要点：BiPrompt通过视觉侧的结构化注意力引导擦除抑制背景激活并强制因果与虚假区域间的正交预测一致性，文本侧的平衡提示归一化对齐类别嵌入至各向同性语义空间，联合最小化虚假线索与预测间的条件互信息。
- 实验或效果：在真实世界和合成偏见基准上的广泛评估显示，相比先前测试时去偏方法，BiPrompt在平均和最差组准确率上均取得一致改进，无需重训练或领域监督。

## 摘要（原文）

> Vision language foundation models such as CLIP exhibit impressive zero-shot generalization yet remain vulnerable to spurious correlations across visual and textual modalities. Existing debiasing approaches often address a single modality either visual or textual leading to partial robustness and unstable adaptation under distribution shifts. We propose a bilateral prompt optimization framework (BiPrompt) that simultaneously mitigates non-causal feature reliance in both modalities during test-time adaptation. On the visual side, it employs structured attention-guided erasure to suppress background activations and enforce orthogonal prediction consistency between causal and spurious regions. On the textual side, it introduces balanced prompt normalization, a learnable re-centering mechanism that aligns class embeddings toward an isotropic semantic space. Together, these modules jointly minimize conditional mutual information between spurious cues and predictions, steering the model toward causal, domain invariant reasoning without retraining or domain supervision. Extensive evaluations on real-world and synthetic bias benchmarks demonstrate consistent improvements in both average and worst-group accuracies over prior test-time debiasing methods, establishing a lightweight yet effective path toward trustworthy and causally grounded vision-language adaptation.

