---
layout: default
title: Hierarchical Vision-Language Interaction for Facial Action Unit Detection
---

# Hierarchical Vision-Language Interaction for Facial Action Unit Detection
**arXiv**：[2602.14425v1](https://arxiv.org/abs/2602.14425) · [PDF](https://arxiv.org/pdf/2602.14425.pdf)  
**作者**：Yong Li, Yi Ren, Yizhe Zhang, Wenhua Zhang, Tianyi Zhang, Muyun Jiang, Guo-Sen Xie, Cuntai Guan  

**一句话要点**：提出HiVA方法，利用文本描述增强面部动作单元检测，解决有限标注数据下的表示学习问题。

**关键词**：面部动作单元检测, 视觉-语言交互, 分层注意力, 动态图模块, 跨模态学习, 语义增强

## 3 点简述
- 核心问题：面部动作单元检测在有限标注数据下学习判别性和泛化性表示困难。
- 方法要点：结合大语言模型生成文本描述，通过动态图模块和分层跨模态注意力机制实现细粒度与全局视觉-语言交互。
- 实验或效果：实验显示HiVA超越现有方法，定性分析表明其能产生语义激活模式，提升检测鲁棒性和可解释性。

## 摘要（原文）

> Facial Action Unit (AU) detection seeks to recognize subtle facial muscle activations as defined by the Facial Action Coding System (FACS). A primary challenge w.r.t AU detection is the effective learning of discriminative and generalizable AU representations under conditions of limited annotated data. To address this, we propose a Hierarchical Vision-language Interaction for AU Understanding (HiVA) method, which leverages textual AU descriptions as semantic priors to guide and enhance AU detection. Specifically, HiVA employs a large language model to generate diverse and contextually rich AU descriptions to strengthen language-based representation learning. To capture both fine-grained and holistic vision-language associations, HiVA introduces an AU-aware dynamic graph module that facilitates the learning of AU-specific visual representations. These features are further integrated within a hierarchical cross-modal attention architecture comprising two complementary mechanisms: Disentangled Dual Cross-Attention (DDCA), which establishes fine-grained, AU-specific interactions between visual and textual features, and Contextual Dual Cross-Attention (CDCA), which models global inter-AU dependencies. This collaborative, cross-modal learning paradigm enables HiVA to leverage multi-grained vision-based AU features in conjunction with refined language-based AU details, culminating in robust and semantically enriched AU detection capabilities. Extensive experiments show that HiVA consistently surpasses state-of-the-art approaches. Besides, qualitative analyses reveal that HiVA produces semantically meaningful activation patterns, highlighting its efficacy in learning robust and interpretable cross-modal correspondences for comprehensive facial behavior analysis.

