---
layout: default
title: TildeOpen LLM: Leveraging Curriculum Learning to Achieve Equitable Language Representation
---

# TildeOpen LLM: Leveraging Curriculum Learning to Achieve Equitable Language Representation
**arXiv**：[2603.08182v1](https://arxiv.org/abs/2603.08182) · [PDF](https://arxiv.org/pdf/2603.08182.pdf)  
**作者**：Toms Bergmanis, Martins Kronis, Ingus Jānis Pretkalniņš, Dāvis Nicmanis, Jeļizaveta Jeļinska, Roberts Rozis, Rinalds Vīksna, Mārcis Pinnis  

**一句话要点**：提出TildeOpen LLM，通过课程学习提升欧洲低资源语言性能，促进语言公平。

**关键词**：多语言大语言模型, 课程学习, 数据平衡, 欧洲语言, 开放权重模型, 语言公平

## 3 点简述
- 核心问题：大语言模型因训练数据中英语主导，在欧洲多语言表现不佳。
- 方法要点：结合数据集上采样与课程学习，交替均匀和自然语言分布训练。
- 实验或效果：在多项基准测试中超越现有开放权重模型，人类评估显示语言错误减少达十倍。

## 摘要（原文）

> Large language models often underperform in many European languages due to the dominance of English and a few high-resource languages in training data. This paper presents TildeOpen LLM, a 30-billion-parameter open-weight foundational model trained for 34 European languages to promote linguistic equity and improve performance for low-resource languages. To address the data imbalance, we combine dataset upsampling with a curriculum-based training schedule that alternates between uniform and natural language distributions. The resulting model performs favorably compared to other multilingual LLMs despite being trained with significantly fewer computing resources. Evaluation across multiple multilingual benchmarks shows that TildeOpen surpasses existing open-weight models in text generation and comprehension, particularly for Baltic, Finno-Ugric, and Slavic languages. Human evaluations confirm an up to tenfold reduction in linguistic errors relative to leading baselines. The model and associated resources are fully open-weight and publicly available at huggingface.co/TildeAI/TildeOpen-30b. These outcomes demonstrate that careful data curation and balanced training strategies can substantially enhance multilingual model quality without increasing model size or training volume.

