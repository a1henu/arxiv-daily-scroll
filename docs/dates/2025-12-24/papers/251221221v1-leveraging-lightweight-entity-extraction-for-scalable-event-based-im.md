---
layout: default
title: Leveraging Lightweight Entity Extraction for Scalable Event-Based Image Retrieval
---

# Leveraging Lightweight Entity Extraction for Scalable Event-Based Image Retrieval
**arXiv**：[2512.21221v1](https://arxiv.org/abs/2512.21221) · [PDF](https://arxiv.org/pdf/2512.21221.pdf)  
**作者**：Dao Sy Duy Minh, Huynh Trung Kiet, Nguyen Lam Phu Quy, Phu-Hoa Pham, Tran Chi Nguyen  

**一句话要点**：提出基于轻量级实体提取的两阶段检索方法，以提升事件图像检索的准确性和可扩展性。

**关键词**：事件图像检索, 实体提取, 多模态检索, 轻量级检索, BEiT-3模型, OpenEvents基准

## 3 点简述
- 核心问题：自然语言描述检索图像面临查询模糊、语言多变和可扩展性挑战。
- 方法要点：采用事件实体提取进行候选过滤，结合BEiT-3模型进行深度多模态语义重排序。
- 实验或效果：在OpenEvents v1基准上达到0.559的平均精度，显著优于先前基线。

## 摘要（原文）

> Retrieving images from natural language descriptions is a core task at the intersection of computer vision and natural language processing, with wide-ranging applications in search engines, media archiving, and digital content management. However, real-world image-text retrieval remains challenging due to vague or context-dependent queries, linguistic variability, and the need for scalable solutions. In this work, we propose a lightweight two-stage retrieval pipeline that leverages event-centric entity extraction to incorporate temporal and contextual signals from real-world captions. The first stage performs efficient candidate filtering using BM25 based on salient entities, while the second stage applies BEiT-3 models to capture deep multimodal semantics and rerank the results. Evaluated on the OpenEvents v1 benchmark, our method achieves a mean average precision of 0.559, substantially outperforming prior baselines. These results highlight the effectiveness of combining event-guided filtering with long-text vision-language modeling for accurate and efficient retrieval in complex, real-world scenarios. Our code is available at https://github.com/PhamPhuHoa-23/Event-Based-Image-Retrieval

