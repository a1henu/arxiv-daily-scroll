---
layout: default
title: Visual Merit or Linguistic Crutch? A Close Look at DeepSeek-OCR
---

# Visual Merit or Linguistic Crutch? A Close Look at DeepSeek-OCR
**arXiv**：[2601.03714v1](https://arxiv.org/abs/2601.03714) · [PDF](https://arxiv.org/pdf/2601.03714.pdf)  
**作者**：Yunhao Liang, Ruixuan Ying, Bo Li, Hong Li, Kai Yan, Qingwen Li, Min Yang, Okamoto Satoshi, Zhe Cui, Shiwen Ni  

**一句话要点**：揭示DeepSeek-OCR性能依赖语言先验，挑战光学压缩缓解长上下文瓶颈的假设

**关键词**：光学字符识别, 视觉文本压缩, 语言先验, 长上下文瓶颈, 模型鲁棒性, 幻觉风险

## 3 点简述
- 核心问题：探究DeepSeek-OCR性能主要源于视觉能力还是语言先验
- 方法要点：通过语义破坏实验分离OCR能力与语言依赖，对比13个基线模型
- 实验或效果：无语言支持时性能从90%降至20%，传统OCR更稳健，压缩加剧幻觉风险

## 摘要（原文）

> DeepSeek-OCR utilizes an optical 2D mapping approach to achieve high-ratio vision-text compression, claiming to decode text tokens exceeding ten times the input visual tokens. While this suggests a promising solution for the LLM long-context bottleneck, we investigate a critical question: "Visual merit or linguistic crutch - which drives DeepSeek-OCR's performance?" By employing sentence-level and word-level semantic corruption, we isolate the model's intrinsic OCR capabilities from its language priors. Results demonstrate that without linguistic support, DeepSeek-OCR's performance plummets from approximately 90% to 20%. Comparative benchmarking against 13 baseline models reveals that traditional pipeline OCR methods exhibit significantly higher robustness to such semantic perturbations than end-to-end methods. Furthermore, we find that lower visual token counts correlate with increased reliance on priors, exacerbating hallucination risks. Context stress testing also reveals a total model collapse around 10,000 text tokens, suggesting that current optical compression techniques may paradoxically aggravate the long-context bottleneck. This study empirically defines DeepSeek-OCR's capability boundaries and offers essential insights for future optimizations of the vision-text compression paradigm. We release all data, results and scripts used in this study at https://github.com/dududuck00/DeepSeekOCR.

