---
layout: default
title: Active Learning for Animal Re-Identification with Ambiguity-Aware Sampling
---

# Active Learning for Animal Re-Identification with Ambiguity-Aware Sampling
**arXiv**：[2511.06658v1](https://arxiv.org/abs/2511.06658) · [PDF](https://arxiv.org/pdf/2511.06658.pdf)  
**作者**：Depanshu Sani, Mehar Khurana, Saket Anand  

**一句话要点**：提出主动学习框架以解决动物重识别中标注数据稀缺问题

**关键词**：动物重识别, 主动学习, 聚类方法, 嵌入空间, 零样本学习, 约束聚类

## 3 点简述
- 核心问题：动物重识别面临零样本性能差和标注成本高，现有方法效果不佳。
- 方法要点：利用聚类方法识别嵌入空间模糊区域，采样信息丰富且代表性样本对。
- 实验或效果：仅用0.033%标注，在13个数据集上平均mAP提升超10%，优于基线方法。

## 摘要（原文）

> Animal Re-ID has recently gained substantial attention in the AI research
> community due to its high impact on biodiversity monitoring and unique research
> challenges arising from environmental factors. The subtle distinguishing
> patterns, handling new species and the inherent open-set nature make the
> problem even harder. To address these complexities, foundation models trained
> on labeled, large-scale and multi-species animal Re-ID datasets have recently
> been introduced to enable zero-shot Re-ID. However, our benchmarking reveals
> significant gaps in their zero-shot Re-ID performance for both known and
> unknown species. While this highlights the need for collecting labeled data in
> new domains, exhaustive annotation for Re-ID is laborious and requires domain
> expertise. Our analyses show that existing unsupervised (USL) and AL Re-ID
> methods underperform for animal Re-ID. To address these limitations, we
> introduce a novel AL Re-ID framework that leverages complementary clustering
> methods to uncover and target structurally ambiguous regions in the embedding
> space for mining pairs of samples that are both informative and broadly
> representative. Oracle feedback on these pairs, in the form of must-link and
> cannot-link constraints, facilitates a simple annotation interface, which
> naturally integrates with existing USL methods through our proposed constrained
> clustering refinement algorithm. Through extensive experiments, we demonstrate
> that, by utilizing only 0.033% of all annotations, our approach consistently
> outperforms existing foundational, USL and AL baselines. Specifically, we
> report an average improvement of 10.49%, 11.19% and 3.99% (mAP) on 13 wildlife
> datasets over foundational, USL and AL methods, respectively, while attaining
> state-of-the-art performance on each dataset. Furthermore, we also show an
> improvement of 11.09%, 8.2% and 2.06% for unknown individuals in an open-world
> setting.

