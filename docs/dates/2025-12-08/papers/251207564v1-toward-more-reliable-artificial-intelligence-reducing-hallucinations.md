---
layout: default
title: Toward More Reliable Artificial Intelligence: Reducing Hallucinations in Vision-Language Models
---

# Toward More Reliable Artificial Intelligence: Reducing Hallucinations in Vision-Language Models
**arXiv**：[2512.07564v1](https://arxiv.org/abs/2512.07564) · [PDF](https://arxiv.org/pdf/2512.07564.pdf)  
**作者**：Kassoum Sanogo, Renzo Ardiccioni  

**一句话要点**：提出无需训练的自校正框架以减少视觉语言模型中的幻觉内容

**关键词**：视觉语言模型, 幻觉减少, 不确定性量化, 自校正框架, 无需训练, 注意力机制

## 3 点简述
- 核心问题：视觉语言模型常生成看似合理但错误的图像内容描述，即幻觉问题。
- 方法要点：通过不确定性引导的视觉重注意机制，结合多维不确定性量化和注意力裁剪，迭代优化响应。
- 实验或效果：在POPE和MMHAL BENCH基准上，幻觉率降低9.8个百分点，对抗性分割的对象存在准确率提升4.7点。

## 摘要（原文）

> Vision-language models (VLMs) frequently generate hallucinated content plausible but incorrect claims about image content. We propose a training-free self-correction framework enabling VLMs to iteratively refine responses through uncertainty-guided visual re-attention. Our method combines multidimensional uncertainty quantification (token entropy, attention dispersion, semantic consistency, claim confidence) with attention-guided cropping of under-explored regions. Operating entirely with frozen, pretrained VLMs, our framework requires no gradient updates. We validate our approach on the POPE and MMHAL BENCH benchmarks using the Qwen2.5-VL-7B [23] architecture. Experimental results demonstrate that our method reduces hallucination rates by 9.8 percentage points compared to the baseline, while improving object existence accuracy by 4.7 points on adversarial splits. Furthermore, qualitative analysis confirms that uncertainty-guided re-attention successfully grounds corrections in visual evidence where standard decoding fails. We validate our approach on Qwen2.5-VL-7B [23], with plans to extend validation across diverse architectures in future versions. We release our code and methodology to facilitate future research in trustworthy multimodal systems.

