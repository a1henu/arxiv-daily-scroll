---
layout: default
title: Half-Truths Break Similarity-Based Retrieval
---

# Half-Truths Break Similarity-Based Retrieval
**arXiv**：[2602.23906v1](https://arxiv.org/abs/2602.23906) · [PDF](https://arxiv.org/pdf/2602.23906.pdf)  
**作者**：Bora Kargi, Arnas Uselis, Seong Joon Oh  

**一句话要点**：提出CS-CLIP以解决CLIP模型在文本扩展错误细节时相似度评分异常的问题

**关键词**：图像文本相似度, 组合理解, 弱监督学习, CLIP模型, 微调方法

## 3 点简述
- 核心问题：CLIP模型在文本描述添加错误细节时相似度评分可能上升，违反直觉。
- 方法要点：通过分解文本为实体和关系单元，构建最小编辑的负样本进行微调。
- 实验或效果：CS-CLIP将半真准确率提升至69.3%，并在组合基准上平均提升5.7分。

## 摘要（原文）

> When a text description is extended with an additional detail, image-text similarity should drop if that detail is wrong. We show that CLIP-style dual encoders often violate this intuition: appending a plausible but incorrect object or relation to an otherwise correct description can increase the similarity score. We call such cases half-truths. On COCO, CLIP prefers the correct shorter description only 40.6% of the time, and performance drops to 32.9% when the added detail is a relation. We trace this vulnerability to weak supervision on caption parts: contrastive training aligns full sentences but does not explicitly enforce that individual entities and relations are grounded. We propose CS-CLIP (Component-Supervised CLIP), which decomposes captions into entity and relation units, constructs a minimally edited foil for each unit, and fine-tunes the model to score the correct unit above its foil while preserving standard dual-encoder inference. CS-CLIP raises half-truth accuracy to 69.3% and improves average performance on established compositional benchmarks by 5.7 points, suggesting that reducing half-truth errors aligns with broader gains in compositional understanding. Code is publicly available at: https://github.com/kargibora/CS-CLIP

