---
layout: default
title: Vision Language Models Map Logos to Text via Semantic Entanglement in the Visual Projector
---

# Vision Language Models Map Logos to Text via Semantic Entanglement in the Visual Projector
**arXiv**：[2510.12287v1](https://arxiv.org/abs/2510.12287) · [PDF](https://arxiv.org/pdf/2510.12287.pdf)  
**作者**：Sifan Li, Hongkai Chen, Yujun Cai, Qingwen Ye, Liyang Chen, Junsong Yuan, Yiwei Wang  

**一句话要点**：揭示视觉语言模型因投影器语义纠缠导致徽标幻觉，并提出缓解方法

**关键词**：视觉语言模型, 徽标幻觉, 投影器分析, 语义纠缠, OCR引导解码, 多模态鲁棒性

## 3 点简述
- 核心问题：视觉语言模型在无文字徽标上产生品牌名称幻觉，依赖符号先验而非真实字形感知。
- 方法要点：通过嵌入分析和针对性消融，识别并减少投影器维度中的幻觉相关子空间。
- 实验效果：在扰动和遮挡测试中，幻觉持续存在，消融方法显著降低错误并保持OCR准确性。

## 摘要（原文）

> Vision Language Models (VLMs) have achieved impressive progress in multimodal
> reasoning; yet, they remain vulnerable to hallucinations, where outputs are not
> grounded in visual evidence. In this paper, we investigate a previously
> overlooked setting: logo hallucination, where models generate brand names or
> textual content despite logos containing no visible words. Using curated splits
> of pure symbols, hybrids, and text-bearing logos, as well as the challenging
> Hard-60 subset, we systematically measure hallucination across leading VLMs. We
> further probe robustness through nine structured perturbations and show that
> hallucinations persist even under strong distortions, with occlusion exposing
> the sharpest weaknesses. Embedding-level analysis with open-weight LLaVA
> demonstrates that hallucination is tied to a small subset of projector
> dimensions, and targeted ablation substantially reduces errors while preserving
> OCR accuracy. Together, these findings reveal that VLMs often rely on symbolic
> priors rather than genuine glyph perception, particularly for iconic circular
> logos, and that projector subspaces play a decisive role in this failure mode.
> Our work contributes both a novel diagnostic lens and actionable mitigation
> insights, highlighting projector disentanglement and OCR-guided decoding as
> promising directions for building more trustworthy multimodal systems.

