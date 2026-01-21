---
layout: default
title: Attention-space Contrastive Guidance for Efficient Hallucination Mitigation in LVLMs
---

# Attention-space Contrastive Guidance for Efficient Hallucination Mitigation in LVLMs
**arXiv**：[2601.13707v1](https://arxiv.org/abs/2601.13707) · [PDF](https://arxiv.org/pdf/2601.13707.pdf)  
**作者**：Yujin Jo, Sangyoon Bae, Taesup Kim  

**一句话要点**：提出注意力空间对比引导以高效缓解大视觉语言模型中的幻觉问题

**关键词**：大视觉语言模型, 幻觉缓解, 对比引导, 注意力机制, 计算效率

## 3 点简述
- 核心问题：大视觉语言模型因语言先验主导视觉证据而产生对象误识别和视觉不一致描述
- 方法要点：在自注意力层内构建视觉-语言和纯语言注意力路径，通过正交化校正减少近似偏差
- 实验或效果：在CHAIR和POPE基准上实现最先进的忠实度和字幕质量，计算成本显著降低

## 摘要（原文）

> Hallucinations in large vision-language models (LVLMs) often arise when language priors dominate over visual evidence, causing object misidentification and visually inconsistent descriptions. We address this issue by framing hallucination mitigation as contrastive guidance, steering generation toward visually grounded and semantically faithful text. This approach regulates the model's internal behavior by reducing over-dependence on language priors and contrasting visually grounded with language-only representations. We propose Attention-space Contrastive Guidance (ACG), a single-pass mechanism that operates within self-attention layers to construct both vision-language and language-only attention paths in a single forward computation. This integration enables computationally efficient guidance directly embedded in the model's representation contextualization. To correct approximation bias introduced by the single-pass formulation, we further apply an orthogonalized correction that removes components aligned with the language-only path, selectively amplifying visual contributions. Experiments on the CHAIR and POPE benchmarks show that ACG achieves state-of-the-art faithfulness and caption quality while significantly reducing computational cost. Our method establishes a principled and efficient alternative, reducing latency by up to 2x compared to prior contrastive decoding methods that require multiple forward passes.

