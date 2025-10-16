---
layout: default
title: UniME-V2: MLLM-as-a-Judge for Universal Multimodal Embedding Learning
---

# UniME-V2: MLLM-as-a-Judge for Universal Multimodal Embedding Learning
**arXiv**：[2510.13515v1](https://arxiv.org/abs/2510.13515) · [PDF](https://arxiv.org/pdf/2510.13515.pdf)  
**作者**：Tiancheng Gu, Kaicheng Yang, Kaichen Zhang, Xiang An, Ziyong Feng, Yueyi Zhang, Weidong Cai, Jiankang Deng, Lidong Bing  

**一句话要点**：提出UniME-V2模型，利用MLLM作为评判者增强多模态嵌入学习，解决语义差异捕捉和负样本多样性问题。

**关键词**：多模态嵌入学习, 硬负样本挖掘, MLLM评判机制, 语义匹配分数, 重排序模型, 检索任务

## 3 点简述
- 现有方法难以捕捉候选间细微语义差异，且负样本缺乏多样性，导致嵌入判别能力有限。
- 引入MLLM-as-a-Judge机制，评估查询-候选对语义对齐，生成软匹配分数用于硬负样本挖掘和软标签对齐。
- 在MMEB基准和多个检索任务上实验，平均性能达到最先进水平。

## 摘要（原文）

> Universal multimodal embedding models are foundational to various tasks.
> Existing approaches typically employ in-batch negative mining by measuring the
> similarity of query-candidate pairs. However, these methods often struggle to
> capture subtle semantic differences among candidates and lack diversity in
> negative samples. Moreover, the embeddings exhibit limited discriminative
> ability in distinguishing false and hard negatives. In this paper, we leverage
> the advanced understanding capabilities of MLLMs to enhance representation
> learning and present a novel Universal Multimodal Embedding (UniME-V2) model.
> Our approach first constructs a potential hard negative set through global
> retrieval. We then introduce the MLLM-as-a-Judge mechanism, which utilizes
> MLLMs to assess the semantic alignment of query-candidate pairs and generate
> soft semantic matching scores. These scores serve as a foundation for hard
> negative mining, mitigating the impact of false negatives and enabling the
> identification of diverse, high-quality hard negatives. Furthermore, the
> semantic matching scores are used as soft labels to mitigate the rigid
> one-to-one mapping constraint. By aligning the similarity matrix with the soft
> semantic matching score matrix, the model learns semantic distinctions among
> candidates, significantly enhancing its discriminative capacity. To further
> improve performance, we propose UniME-V2-Reranker, a reranking model trained on
> our mined hard negatives through a joint pairwise and listwise optimization
> approach. We conduct comprehensive experiments on the MMEB benchmark and
> multiple retrieval tasks, demonstrating that our method achieves
> state-of-the-art performance on average across all tasks.

