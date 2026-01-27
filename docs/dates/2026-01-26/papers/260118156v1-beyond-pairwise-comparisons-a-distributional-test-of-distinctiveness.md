---
layout: default
title: Beyond Pairwise Comparisons: A Distributional Test of Distinctiveness for Machine-Generated Works in Intellectual Property Law
---

# Beyond Pairwise Comparisons: A Distributional Test of Distinctiveness for Machine-Generated Works in Intellectual Property Law
**arXiv**：[2601.18156v1](https://arxiv.org/abs/2601.18156) · [PDF](https://arxiv.org/pdf/2601.18156.pdf)  
**作者**：Anirban Mukherjee, Hannah Hanwen Chang  

**一句话要点**：提出基于分布的两样本测试，以评估机器生成作品在知识产权法中的独特性。

**关键词**：分布测试, 最大均值差异, 语义嵌入, 机器生成作品, 知识产权法, 样本效率

## 3 点简述
- 核心问题：传统成对比较方法不适用于评估机器生成过程的无限输出空间。
- 方法要点：使用最大均值差异和语义嵌入进行分布测试，无需任务特定训练。
- 实验或效果：在图像和文本领域验证，样本效率高，揭示生成模型输出分布与人类基线统计可区分。

## 摘要（原文）

> Key doctrines, including novelty (patent), originality (copyright), and distinctiveness (trademark), turn on a shared empirical question: whether a body of work is meaningfully distinct from a relevant reference class. Yet analyses typically operationalize this set-level inquiry using item-level evidence: pairwise comparisons among exemplars. That unit-of-analysis mismatch may be manageable for finite corpora of human-created works, where it can be bridged by ad hoc aggregations. But it becomes acute for machine-generated works, where the object of evaluation is not a fixed set of works but a generative process with an effectively unbounded output space. We propose a distributional alternative: a two-sample test based on maximum mean discrepancy computed on semantic embeddings to determine if two creative processes-whether human or machine-produce statistically distinguishable output distributions. The test requires no task-specific training-obviating the need for discovery of proprietary training data to characterize the generative process-and is sample-efficient, often detecting differences with as few as 5-10 images and 7-20 texts. We validate the framework across three domains: handwritten digits (controlled images), patent abstracts (text), and AI-generated art (real-world images). We reveal a perceptual paradox: even when human evaluators distinguish AI outputs from human-created art with only about 58% accuracy, our method detects distributional distinctiveness. Our results present evidence contrary to the view that generative models act as mere regurgitators of training data. Rather than producing outputs statistically indistinguishable from a human baseline-as simple regurgitation would predict-they produce outputs that are semantically human-like yet stochastically distinct, suggesting their dominant function is as a semantic interpolator within a learned latent space.

