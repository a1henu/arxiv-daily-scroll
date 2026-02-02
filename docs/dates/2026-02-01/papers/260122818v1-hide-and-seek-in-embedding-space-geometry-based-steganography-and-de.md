---
layout: default
title: Hide and Seek in Embedding Space: Geometry-based Steganography and Detection in Large Language Models
---

# Hide and Seek in Embedding Space: Geometry-based Steganography and Detection in Large Language Models
**arXiv**：[2601.22818v1](https://arxiv.org/abs/2601.22818) · [PDF](https://arxiv.org/pdf/2601.22818.pdf)  
**作者**：Charles Westphal, Keivan Navaie, Fernando E. Rosas  

**一句话要点**：提出基于嵌入空间的低可恢复性隐写术及机制可解释性检测方法，以应对LLMs中的隐写攻击。

**关键词**：隐写术, 大语言模型, 嵌入空间, 机制可解释性, 微调攻击, 检测方法

## 3 点简述
- 核心问题：微调LLMs可通过隐写通道秘密编码提示，现有方法可恢复性高，威胁隐蔽性不足。
- 方法要点：引入低可恢复性隐写术，利用嵌入空间映射替代任意映射，降低有效载荷可恢复性。
- 实验或效果：在Llama和Ministral模型上，秘密恢复率提升78%-123%，同时可恢复性降低；机制可解释性检测准确率提高33%。

## 摘要（原文）

> Fine-tuned LLMs can covertly encode prompt secrets into outputs via steganographic channels. Prior work demonstrated this threat but relied on trivially recoverable encodings. We formalize payload recoverability via classifier accuracy and show previous schemes achieve 100\% recoverability. In response, we introduce low-recoverability steganography, replacing arbitrary mappings with embedding-space-derived ones. For Llama-8B (LoRA) and Ministral-8B (LoRA) trained on TrojanStego prompts, exact secret recovery rises from 17$\rightarrow$30\% (+78\%) and 24$\rightarrow$43\% (+80\%) respectively, while on Llama-70B (LoRA) trained on Wiki prompts, it climbs from 9$\rightarrow$19\% (+123\%), all while reducing payload recoverability. We then discuss detection. We argue that detecting fine-tuning-based steganographic attacks requires approaches beyond traditional steganalysis. Standard approaches measure distributional shift, which is an expected side-effect of fine-tuning. Instead, we propose a mechanistic interpretability approach: linear probes trained on later-layer activations detect the secret with up to 33\% higher accuracy in fine-tuned models compared to base models, even for low-recoverability schemes. This suggests that malicious fine-tuning leaves actionable internal signatures amenable to interpretability-based defenses.

