---
layout: default
title: Pay Attention Later: From Vector Space Diffusion to Linearithmic Spectral Phase-Locking
---

# Pay Attention Later: From Vector Space Diffusion to Linearithmic Spectral Phase-Locking
**arXiv**：[2512.01208v1](https://arxiv.org/abs/2512.01208) · [PDF](https://arxiv.org/pdf/2512.01208.pdf)  
**作者**：Alper Yıldırım, İbrahim Yücedağ  

**一句话要点**：提出PRISM模型以解决Transformer在实时知识适应中的可塑性-稳定性困境

**关键词**：Transformer优化, 可塑性-稳定性困境, 谐波表示, 门控谐波卷积, 实时知识适应, WMT14翻译

## 3 点简述
- 标准Transformer存在语义对齐税，导致优化成本高且难以适应新概念
- PRISM使用复域谐振频率编码语义，以门控谐波卷积替代二次自注意力
- 在WMT14翻译任务中，PRISM展示无损可塑性，而Transformer出现灾难性遗忘

## 摘要（原文）

> Standard Transformers suffer from a "Semantic Alignment Tax", a prohibitive optimization cost required to organize a chaotic initialization into a coherent geometric map via local gradient diffusion. We hypothesize that this reliance on diffusive learning creates "Catastrophic Rigidity", rendering models unable to adapt to novel concepts without destroying their pre-trained reasoning capabilities. To isolate this phenomenon, we introduce Iterative Semantic Map Refinement (ISMR), a diagnostic protocol revealing that alignment is a fixed geometric barrier that scaling cannot solve; a 20-layer model overcomes this barrier no faster than a 1-layer model. We introduce the Phase-Resonant Intelligent Spectral Model (PRISM). PRISM encodes semantic identity as resonant frequencies in the complex domain (C^d) and replaces quadratic self-attention with linearithmic O(N log N) Gated Harmonic Convolutions. We validate PRISM on the WMT14 translation task. While the Standard Transformer maintains a slight edge in general competence on static benchmarks (23.88 vs 21.40 BLEU), it fails the "Plasticity-Stability" stress test completely. When injected with novel concepts, the Transformer suffers Catastrophic Forgetting, degrading by -10.55 BLEU points while achieving only 60% acquisition. In contrast, PRISM demonstrates Lossless Plasticity, achieving 96% 5-shot acquisition with negligible degradation (-0.84 BLEU). These results suggest that harmonic representations effectively decouple memory from reasoning, offering a structural solution to the plasticity-stability dilemma in real-time knowledge adaptation.

