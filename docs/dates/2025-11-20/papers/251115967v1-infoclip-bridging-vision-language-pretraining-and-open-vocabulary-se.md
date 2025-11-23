---
layout: default
title: InfoCLIP: Bridging Vision-Language Pretraining and Open-Vocabulary Semantic Segmentation via Information-Theoretic Alignment Transfer
---

# InfoCLIP: Bridging Vision-Language Pretraining and Open-Vocabulary Semantic Segmentation via Information-Theoretic Alignment Transfer
**arXiv**：[2511.15967v1](https://arxiv.org/abs/2511.15967) · [PDF](https://arxiv.org/pdf/2511.15967.pdf)  
**作者**：Muyao Yuan, Yuanhong Zhang, Weizhan Zhang, Lan Ma, Yuan Gao, Jiangyong Ying, Yudeng Xin  

**一句话要点**：提出InfoCLIP以解决CLIP微调中模态对齐退化问题

**关键词**：开放词汇语义分割, 视觉语言预训练, 信息理论对齐, CLIP微调, 模态对齐转移

## 3 点简述
- 核心问题：CLIP微调于分割任务易过拟合，破坏预训练视觉语言对齐
- 方法要点：基于互信息压缩对齐噪声并最大化知识转移
- 实验或效果：多基准测试验证其在开放词汇分割中的优越性

## 摘要（原文）

> Recently, the strong generalization ability of CLIP has facilitated open-vocabulary semantic segmentation, which labels pixels using arbitrary text. However, existing methods that fine-tune CLIP for segmentation on limited seen categories often lead to overfitting and degrade the pretrained vision-language alignment. To stabilize modality alignment during fine-tuning, we propose InfoCLIP, which leverages an information-theoretic perspective to transfer alignment knowledge from pretrained CLIP to the segmentation task. Specifically, this transfer is guided by two novel objectives grounded in mutual information. First, we compress the pixel-text modality alignment from pretrained CLIP to reduce noise arising from its coarse-grained local semantic representations learned under image-text supervision. Second, we maximize the mutual information between the alignment knowledge of pretrained CLIP and the fine-tuned model to transfer compact local semantic relations suited for the segmentation task. Extensive evaluations across various benchmarks validate the effectiveness of InfoCLIP in enhancing CLIP fine-tuning for open-vocabulary semantic segmentation, demonstrating its adaptability and superiority in asymmetric transfer.

