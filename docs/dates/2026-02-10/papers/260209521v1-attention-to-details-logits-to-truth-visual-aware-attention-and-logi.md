---
layout: default
title: Attention to details, logits to truth: visual-aware attention and logits enhancement to mitigate hallucinations in LVLMs
---

# Attention to details, logits to truth: visual-aware attention and logits enhancement to mitigate hallucinations in LVLMs
**arXiv**：[2602.09521v1](https://arxiv.org/abs/2602.09521) · [PDF](https://arxiv.org/pdf/2602.09521.pdf)  
**作者**：Jingyi Wang, Fei Li, Rujie Liu  

**一句话要点**：提出视觉感知注意力与对数增强方法，以缓解大型视觉语言模型中的幻觉问题

**关键词**：大型视觉语言模型, 幻觉缓解, 注意力机制, 视觉-文本相似性, 无训练干预, 解码增强

## 3 点简述
- 核心问题：现有大型视觉语言模型视觉注意力不足，导致幻觉，且增强所有视觉令牌注意力会引入无关信息
- 方法要点：基于视觉-文本相似性，设计无训练注意力干预算法，重分配注意力至任务相关令牌，并在解码中注入视觉注意力值
- 实验或效果：实验表明，该方法显著减少主流模型幻觉，同时保持生成内容的准确性和连贯性

## 摘要（原文）

> Existing Large Vision-Language Models (LVLMs) exhibit insufficient visual attention, leading to hallucinations. To alleviate this problem, some previous studies adjust and amplify visual attention. These methods present a limitation that boosting attention for all visual tokens inevitably increases attention to task irrelevant tokens. To tackle this challenge, we propose a training free attentional intervention algorithm to enhance the attention of task-relevant tokens based on the argument that task-relevant tokens generally demonstrate high visual-textual similarities. Specifically, the vision-text cross-attention submatrices, which represent visual-textual correlations, are extracted to construct the reweighting matrices to reallocate attention. Besides, to enhance the contribution of visual tokens, we inject visual attention values into the beam search decoding to identify solutions with higher visual attention. Extensive experiments demonstrate that this method significantly reduces hallucinations across mainstream LVLMs, while preserving the accuracy and coherence of generated content.

