---
layout: default
title: Fine-tuning Small Language Models as Efficient Enterprise Search Relevance Labelers
---

# Fine-tuning Small Language Models as Efficient Enterprise Search Relevance Labelers
**arXiv**：[2601.03211v1](https://arxiv.org/abs/2601.03211) · [PDF](https://arxiv.org/pdf/2601.03211.pdf)  
**作者**：Yue Kang, Zhuoyi Huang, Benji Schussheim, Diana Licon, Dina Atia, Shixing Cao, Jacob Danovitch, Kunho Kim, Billy Norcilien, Jonah Karpman, Mahmound Sayed, Mike Taylor, Tao Sun, Pavel Metrikov, Vipul Agarwal, Chris Quirk, Ye-Yi Wang, Nick Craswell, Irene Shaffer, Tianwei Chen, Sulaiman Vesal, Soundar Srinivasan  

**一句话要点**：提出微调小语言模型作为高效企业搜索相关性标注器，以解决标注数据稀缺问题。

**关键词**：企业搜索, 相关性标注, 小语言模型, 数据合成, 模型蒸馏, 成本效益

## 3 点简述
- 核心问题：企业搜索中高质量标注数据获取困难，阻碍数据集构建。
- 方法要点：利用大语言模型合成查询和相关性分数，结合BM25检索负样本，蒸馏至小模型。
- 实验或效果：在923对人工标注基准上，小模型与人类一致性媲美或优于大模型，吞吐量提升17倍且成本降低19倍。

## 摘要（原文）

> In enterprise search, building high-quality datasets at scale remains a central challenge due to the difficulty of acquiring labeled data. To resolve this challenge, we propose an efficient approach to fine-tune small language models (SLMs) for accurate relevance labeling, enabling high-throughput, domain-specific labeling comparable or even better in quality to that of state-of-the-art large language models (LLMs). To overcome the lack of high-quality and accessible datasets in the enterprise domain, our method leverages on synthetic data generation. Specifically, we employ an LLM to synthesize realistic enterprise queries from a seed document, apply BM25 to retrieve hard negatives, and use a teacher LLM to assign relevance scores. The resulting dataset is then distilled into an SLM, producing a compact relevance labeler. We evaluate our approach on a high-quality benchmark consisting of 923 enterprise query-document pairs annotated by trained human annotators, and show that the distilled SLM achieves agreement with human judgments on par with or better than the teacher LLM. Furthermore, our fine-tuned labeler substantially improves throughput, achieving 17 times increase while also being 19 times more cost-effective. This approach enables scalable and cost-effective relevance labeling for enterprise-scale retrieval applications, supporting rapid offline evaluation and iteration in real-world settings.

