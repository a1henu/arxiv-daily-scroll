---
layout: default
title: AFTER: Mitigating the Object Hallucination of LVLM via Adaptive Factual-Guided Activation Editing
---

# AFTER: Mitigating the Object Hallucination of LVLM via Adaptive Factual-Guided Activation Editing
**arXiv**：[2601.01957v1](https://arxiv.org/abs/2601.01957) · [PDF](https://arxiv.org/pdf/2601.01957.pdf)  
**作者**：Tianbo Wang, Yuqing Ma, Kewei Liao, Zhange Zhang, Simin Li, Jinyang Guo, Xianglong Liu  

**一句话要点**：提出AFTER方法，通过自适应事实引导激活编辑缓解大型视觉语言模型的对象幻觉问题

**关键词**：对象幻觉缓解, 激活编辑, 视觉语言模型, 事实引导, 自适应优化

## 3 点简述
- 核心问题：大型视觉语言模型因语言偏见易产生对象幻觉，阻碍可信AI应用
- 方法要点：结合事实增强激活引导和查询自适应偏移优化，自适应调整激活以对齐事实语义
- 实验或效果：在标准基准测试中显著减少幻觉，如在AMBER基准上比基线降低16.3%

## 摘要（原文）

> Large Vision-Language Models (LVLMs) have achieved substantial progress in cross-modal tasks. However, due to language bias, LVLMs are susceptible to object hallucination, which can be primarily divided into category, attribute, and relation hallucination, significantly impeding the trustworthy AI applications. Editing the internal activations of LVLMs has shown promising effectiveness in mitigating hallucinations with minimal cost. However, previous editing approaches neglect the effective guidance offered by factual textual semantics, thereby struggling to explicitly mitigate language bias. To address these issues, we propose Adaptive Factual-guided Visual-Textual Editing for hallucination mitigation (AFTER), which comprises Factual-Augmented Activation Steering (FAS) and Query-Adaptive Offset Optimization (QAO), to adaptively guides the original biased activations towards factual semantics. Specifically, FAS is proposed to provide factual and general guidance for activation editing, thereby explicitly modeling the precise visual-textual associations. Subsequently, QAO introduces a query-aware offset estimator to establish query-specific editing from the general steering vector, enhancing the diversity and granularity of editing. Extensive experiments on standard hallucination benchmarks across three widely adopted LVLMs validate the efficacy of the proposed AFTER, notably achieving up to a 16.3% reduction of hallucination over baseline on the AMBER benchmark. Our code and data will be released for reproducibility.

