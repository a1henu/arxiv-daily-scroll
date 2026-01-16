---
layout: default
title: Multilingual-To-Multimodal (M2M): Unlocking New Languages with Monolingual Text
---

# Multilingual-To-Multimodal (M2M): Unlocking New Languages with Monolingual Text
**arXiv**：[2601.10096v1](https://arxiv.org/abs/2601.10096) · [PDF](https://arxiv.org/pdf/2601.10096.pdf)  
**作者**：Piyush Singh Pasi  

**一句话要点**：提出METAL方法，通过仅用英语文本学习线性层，实现多语言文本到多模态空间的零样本对齐。

**关键词**：多模态对齐, 零样本学习, 文本到图像检索, 多语言处理, 轻量级方法

## 3 点简述
- 核心问题：多模态模型在非英语语言上性能下降，因缺乏多语言多模态数据。
- 方法要点：METAL使用轻量级对齐，仅训练少量线性层，将多语言文本嵌入映射到多模态空间。
- 实验或效果：在XTD检索中，英语性能达94.9% Recall@10，11种语言平均89.5% Recall@10，并推广到音频-文本检索和跨语言图像生成。

## 摘要（原文）

> Multimodal models excel in English, supported by abundant image-text and audio-text data, but performance drops sharply for other languages due to limited multilingual multimodal resources. Existing solutions rely heavily on machine translation, while advances in multilingual text modeling remain underutilized. We introduce METAL, a lightweight alignment method that learns only a few linear layers using English text alone to map multilingual text embeddings into a multimodal space. Despite its simplicity, METAL matches baseline performance in English (94.9 percent Recall at 10) and achieves strong zero-shot transfer (89.5 percent Recall at 10 averaged across 11 languages, 10 unseen) on XTD text-to-image retrieval. Qualitative t-SNE visualizations show that multilingual embeddings align tightly with multimodal representations, while weight analysis reveals that the transformation reshapes embedding geometry rather than performing trivial rotations. Beyond image-text retrieval, METAL generalizes to audio-text retrieval and cross-lingual text-to-image generation. We release code and checkpoints at https://github.com/m2m-codebase/M2M , as well as multilingual evaluation datasets including MSCOCO Multilingual 30K (https://huggingface.co/datasets/piyushsinghpasi/mscoco-multilingual-30k ), AudioCaps Multilingual (https://huggingface.co/datasets/piyushsinghpasi/audiocaps-multilingual ), and Clotho Multilingual (https://huggingface.co/datasets/piyushsinghpasi/clotho-multilingual ), to facilitate further research.

