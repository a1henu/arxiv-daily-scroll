---
layout: default
title: Negative Entity Suppression for Zero-Shot Captioning with Synthetic Images
---

# Negative Entity Suppression for Zero-Shot Captioning with Synthetic Images
**arXiv**：[2511.08909v1](https://arxiv.org/abs/2511.08909) · [PDF](https://arxiv.org/pdf/2511.08909.pdf)  
**作者**：Zimao Lu, Hui Xu, Bing Liu, Ke Wang  

**一句话要点**：提出负实体抑制方法以解决零样本图像描述中的幻觉问题

**关键词**：零样本图像描述, 负实体抑制, 合成图像, 跨域泛化, 幻觉减少

## 3 点简述
- 核心问题：零样本图像描述在跨域时易产生幻觉内容，检索方法可能加剧此问题
- 方法要点：使用合成图像、过滤负实体、注意力级抑制来减少幻觉
- 实验或效果：在多个基准上保持域内性能，提升跨域迁移并降低幻觉率

## 摘要（原文）

> Text-only training provides an attractive approach to address data scarcity challenges in zero-shot image captioning (ZIC), avoiding the expense of collecting paired image-text annotations. However, although these approaches perform well within training domains, they suffer from poor cross-domain generalization, often producing hallucinated content when encountering novel visual environments. Retrieval-based methods attempt to mitigate this limitation by leveraging external knowledge, but they can paradoxically exacerbate hallucination when retrieved captions contain entities irrelevant to the inputs. We introduce the concept of negative entities--objects that appear in generated caption but are absent from the input--and propose Negative Entity Suppression (NES) to tackle this challenge. NES seamlessly integrates three stages: (1) it employs synthetic images to ensure consistent image-to-text retrieval across both training and inference; (2) it filters negative entities from retrieved content to enhance accuracy; and (3) it applies attention-level suppression using identified negative entities to further minimize the impact of hallucination-prone features. Evaluation across multiple benchmarks demonstrates that NES maintains competitive in-domain performance while improving cross-domain transfer and reducing hallucination rates, achieving new state-of-the-art results in ZIC. Our code is available at https://github.com/nidongpinyinme/NESCap.

