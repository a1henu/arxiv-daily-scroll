---
layout: default
title: Anomaly Detection by Effectively Leveraging Synthetic Images
---

# Anomaly Detection by Effectively Leveraging Synthetic Images
**arXiv**：[2512.23227v1](https://arxiv.org/abs/2512.23227) · [PDF](https://arxiv.org/pdf/2512.23227.pdf)  
**作者**：Sungho Kang, Hyunkyu Park, Yeonho Lee, Hanbyul Lee, Mijoo Jeong, YeongHyeon Park, Injae Lee, Juneho Yi  

**一句话要点**：提出基于图像检索与两阶段训练的合成图像有效利用框架，以提升工业异常检测性能。

**关键词**：异常检测, 合成图像生成, 图像检索, 两阶段训练, 工业制造

## 3 点简述
- 核心问题：工业异常检测中真实缺陷图像稀缺，现有合成方法在成本与真实性间存在权衡。
- 方法要点：利用预训练文本引导图像翻译模型和图像检索模型高效生成高质量合成缺陷图像，并采用两阶段训练策略。
- 实验或效果：在MVTec AD数据集上验证了方法的有效性，显著降低数据收集成本并提升检测性能。

## 摘要（原文）

> Anomaly detection plays a vital role in industrial manufacturing. Due to the scarcity of real defect images, unsupervised approaches that rely solely on normal images have been extensively studied. Recently, diffusion-based generative models brought attention to training data synthesis as an alternative solution. In this work, we focus on a strategy to effectively leverage synthetic images to maximize the anomaly detection performance. Previous synthesis strategies are broadly categorized into two groups, presenting a clear trade-off. Rule-based synthesis, such as injecting noise or pasting patches, is cost-effective but often fails to produce realistic defect images. On the other hand, generative model-based synthesis can create high-quality defect images but requires substantial cost. To address this problem, we propose a novel framework that leverages a pre-trained text-guided image-to-image translation model and image retrieval model to efficiently generate synthetic defect images. Specifically, the image retrieval model assesses the similarity of the generated images to real normal images and filters out irrelevant outputs, thereby enhancing the quality and relevance of the generated defect images. To effectively leverage synthetic images, we also introduce a two stage training strategy. In this strategy, the model is first pre-trained on a large volume of images from rule-based synthesis and then fine-tuned on a smaller set of high-quality images. This method significantly reduces the cost for data collection while improving the anomaly detection performance. Experiments on the MVTec AD dataset demonstrate the effectiveness of our approach.

