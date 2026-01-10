---
layout: default
title: V-FAT: Benchmarking Visual Fidelity Against Text-bias
---

# V-FAT: Benchmarking Visual Fidelity Against Text-bias
**arXiv**：[2601.04897v1](https://arxiv.org/abs/2601.04897) · [PDF](https://arxiv.org/pdf/2601.04897.pdf)  
**作者**：Ziteng Wang, Yujie He, Guanliang Li, Siqi Yang, Jiaqi Xiong, Songxiang Liu  

**一句话要点**：提出V-FAT基准以评估多模态大语言模型在视觉保真度与文本偏见间的冲突

**关键词**：多模态大语言模型, 视觉保真度, 文本偏见, VQA基准, 评估框架, 视觉鲁棒性得分

## 3 点简述
- 核心问题：多模态大语言模型过度依赖语言捷径而非真实视觉基础，存在文本偏见现象
- 方法要点：设计V-FAT基准，包含4026个VQA实例，采用三级评估框架量化视觉与文本冲突
- 实验或效果：评估12个前沿模型，显示在高语言主导下视觉性能显著下降

## 摘要（原文）

> Recent advancements in Multimodal Large Language Models (MLLMs) have demonstrated impressive performance on standard visual reasoning benchmarks. However, there is growing concern that these models rely excessively on linguistic shortcuts rather than genuine visual grounding, a phenomenon we term Text Bias. In this paper, we investigate the fundamental tension between visual perception and linguistic priors. We decouple the sources of this bias into two dimensions: Internal Corpus Bias, stemming from statistical correlations in pretraining, and External Instruction Bias, arising from the alignment-induced tendency toward sycophancy. To quantify this effect, we introduce V-FAT (Visual Fidelity Against Text-bias), a diagnostic benchmark comprising 4,026 VQA instances across six semantic domains. V-FAT employs a Three-Level Evaluation Framework that systematically increases the conflict between visual evidence and textual information: (L1) internal bias from atypical images, (L2) external bias from misleading instructions, and (L3) synergistic bias where both coincide. We introduce the Visual Robustness Score (VRS), a metric designed to penalize "lucky" linguistic guesses and reward true visual fidelity. Our evaluation of 12 frontier MLLMs reveals that while models excel in existing benchmarks, they experience significant visual collapse under high linguistic dominance.

