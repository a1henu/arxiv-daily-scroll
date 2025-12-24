---
layout: default
title: FlashVLM: Text-Guided Visual Token Selection for Large Multimodal Models
---

# FlashVLM: Text-Guided Visual Token Selection for Large Multimodal Models
**arXiv**：[2512.20561v1](https://arxiv.org/abs/2512.20561) · [PDF](https://arxiv.org/pdf/2512.20561.pdf)  
**作者**：Kaitong Cai, Jusheng Zhang, Jing Yang, Yijia Fan, Pengtao Xie, Jian Wang, Keze Wang  

**一句话要点**：提出FlashVLM框架，通过文本引导动态选择视觉令牌以提升多模态模型效率

**关键词**：视觉令牌选择, 多模态模型效率, 文本引导压缩, 跨模态相似性, 动态适应查询

## 3 点简述
- 核心问题：大型视觉语言模型处理大量视觉令牌导致计算成本高和冗余
- 方法要点：基于跨模态相似性和视觉显著性融合，动态适应查询选择令牌
- 实验或效果：在LLaVA 1.5上压缩77.8%令牌，精度略超基线，14个基准测试显示高效能

## 摘要（原文）

> Large vision-language models (VLMs) typically process hundreds or thousands of visual tokens per image or video frame, incurring quadratic attention cost and substantial redundancy. Existing token reduction methods often ignore the textual query or rely on deep attention maps, whose instability under aggressive pruning leads to degraded semantic alignment.
>   We propose FlashVLM, a text guided visual token selection framework that dynamically adapts visual inputs to the query. Instead of relying on noisy attention weights, FlashVLM computes an explicit cross modal similarity between projected image tokens and normalized text embeddings in the language model space. This extrinsic relevance is fused with intrinsic visual saliency using log domain weighting and temperature controlled sharpening. In addition, a diversity preserving partition retains a minimal yet representative set of background tokens to maintain global context.
>   Under identical token budgets and evaluation protocols, FlashVLM achieves beyond lossless compression, slightly surpassing the unpruned baseline while pruning up to 77.8 percent of visual tokens on LLaVA 1.5, and maintaining 92.8 percent accuracy even under 94.4 percent compression. Extensive experiments on 14 image and video benchmarks demonstrate that FlashVLM delivers state of the art efficiency performance trade offs while maintaining strong robustness and generalization across mainstream VLMs.

