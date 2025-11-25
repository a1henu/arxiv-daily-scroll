---
layout: default
title: Scale What Counts, Mask What Matters: Evaluating Foundation Models for Zero-Shot Cross-Domain Wi-Fi Sensing
---

# Scale What Counts, Mask What Matters: Evaluating Foundation Models for Zero-Shot Cross-Domain Wi-Fi Sensing
**arXiv**：[2511.18792v1](https://arxiv.org/abs/2511.18792) · [PDF](https://arxiv.org/pdf/2511.18792.pdf)  
**作者**：Cheng Jiang, Yihe Yan, Yanxiang Wang, Chun Tung Chou, Wen Hu  

**一句话要点**：应用基础模型与掩码自编码提升Wi-Fi感知的跨域零样本性能

**关键词**：Wi-Fi感知, 跨域泛化, 掩码自编码, 基础模型, 零样本学习, 信道状态信息

## 3 点简述
- Wi-Fi感知面临域偏移问题，模型在新环境、硬件或用户下泛化能力差
- 采用掩码自编码预训练，利用大规模异构数据集提升数据多样性和规模
- 实验显示数据规模是关键瓶颈，预训练在跨域任务中提升准确率2.2%至15.7%

## 摘要（原文）

> While Wi-Fi sensing offers a compelling, privacy-preserving alternative to cameras, its practical utility has been fundamentally undermined by a lack of robustness across domains. Models trained in one setup fail to generalize to new environments, hardware, or users, a critical "domain shift" problem exacerbated by modest, fragmented public datasets. We shift from this limited paradigm and apply a foundation model approach, leveraging Masked Autoencoding (MAE) style pretraining on the largest and most heterogeneous Wi-Fi CSI datasets collection assembled to date. Our study pretrains and evaluates models on over 1.3 million samples extracted from 14 datasets, collected using 4 distinct devices across the 2.4/5/6 GHz bands and bandwidths from 20 to 160 MHz. Our large-scale evaluation is the first to systematically disentangle the impacts of data diversity versus model capacity on cross-domain performance. The results establish scaling trends on Wi-Fi CSI sensing. First, our experiments show log-linear improvements in unseen domain performance as the amount of pretraining data increases, suggesting that data scale and diversity are key to domain generalization. Second, based on the current data volume, larger model can only provide marginal gains for cross-domain performance, indicating that data, rather than model capacity, is the current bottleneck for Wi-Fi sensing generalization. Finally, we conduct a series of cross-domain evaluations on human activity recognition, human gesture recognition and user identification tasks. The results show that the large-scale pretraining improves cross-domain accuracy ranging from 2.2% to 15.7%, compared to the supervised learning baseline. Overall, our findings provide insightful direction for designing future Wi-Fi sensing systems that can eventually be robust enough for real-world deployment.

