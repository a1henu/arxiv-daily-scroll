---
layout: default
title: GSE: Evaluating Sticker Visual Semantic Similarity via a General Sticker Encoder
---

# GSE: Evaluating Sticker Visual Semantic Similarity via a General Sticker Encoder
**arXiv**：[2511.04977v1](https://arxiv.org/abs/2511.04977) · [PDF](https://arxiv.org/pdf/2511.04977.pdf)  
**作者**：Heng Er Metilda Chee, Jiayin Wang, Zhiqiang Guo, Weizhi Ma, Min Zhang  

**一句话要点**：提出通用贴纸编码器GSE以解决贴纸语义相似性评估问题

**关键词**：贴纸语义相似性, 通用贴纸编码器, Triple-S基准, 多模态嵌入, 贴纸检索

## 3 点简述
- 核心问题：贴纸语义关系理解困难，因其内容多样且符号化
- 方法要点：构建Triple-S基准，并设计轻量级GSE模型学习鲁棒嵌入
- 实验或效果：GSE在未见贴纸上表现优异，支持情感分类和检索任务

## 摘要（原文）

> Stickers have become a popular form of visual communication, yet
> understanding their semantic relationships remains challenging due to their
> highly diverse and symbolic content. In this work, we formally {define the
> Sticker Semantic Similarity task} and introduce {Triple-S}, the first benchmark
> for this task, consisting of 905 human-annotated positive and negative sticker
> pairs. Through extensive evaluation, we show that existing pretrained vision
> and multimodal models struggle to capture nuanced sticker semantics. To address
> this, we propose the {General Sticker Encoder (GSE)}, a lightweight and
> versatile model that learns robust sticker embeddings using both Triple-S and
> additional datasets. GSE achieves superior performance on unseen stickers, and
> demonstrates strong results on downstream tasks such as emotion classification
> and sticker-to-sticker retrieval. By releasing both Triple-S and GSE, we
> provide standardized evaluation tools and robust embeddings, enabling future
> research in sticker understanding, retrieval, and multimodal content
> generation. The Triple-S benchmark and GSE have been publicly released and are
> available here.

