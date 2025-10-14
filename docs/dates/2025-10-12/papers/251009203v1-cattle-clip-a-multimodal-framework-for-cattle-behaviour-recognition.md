---
layout: default
title: Cattle-CLIP: A Multimodal Framework for Cattle Behaviour Recognition
---

# Cattle-CLIP: A Multimodal Framework for Cattle Behaviour Recognition
**arXiv**：[2510.09203v1](https://arxiv.org/abs/2510.09203) · [PDF](https://arxiv.org/pdf/2510.09203.pdf)  
**作者**：Huimin Liu, Jing Gao, Daria Baran, AxelX Montout, Neill W Campbell, Andrew W Dowsey  

**一句话要点**：提出Cattle-CLIP多模态框架，利用语义提示提升牛只行为识别性能。

**关键词**：多模态学习, 牛只行为识别, CLIP模型, 少样本学习, 数据增强, 时间集成

## 3 点简述
- 核心问题：牛只行为识别对健康监测至关重要，但数据稀缺场景下性能受限。
- 方法要点：基于CLIP模型，添加时间集成模块，并采用数据增强和专用文本提示。
- 实验或效果：在CattleBehaviours6数据集上，监督学习准确率达96.1%，少样本学习泛化性强。

## 摘要（原文）

> Cattle behaviour is a crucial indicator of an individual animal health,
> productivity and overall well-being. Video-based monitoring, combined with deep
> learning techniques, has become a mainstream approach in animal biometrics, and
> it can offer high accuracy in some behaviour recognition tasks. We present
> Cattle-CLIP, a multimodal deep learning framework for cattle behaviour
> recognition, using semantic cues to improve the performance of video-based
> visual feature recognition. It is adapted from the large-scale image-language
> model CLIP by adding a temporal integration module. To address the domain gap
> between web data used for the pre-trained model and real-world cattle
> surveillance footage, we introduce tailored data augmentation strategies and
> specialised text prompts. Cattle-CLIP is evaluated under both fully-supervised
> and few-shot learning scenarios, with a particular focus on data-scarce
> behaviour recognition - an important yet under-explored goal in livestock
> monitoring. To evaluate the proposed method, we release the CattleBehaviours6
> dataset, which comprises six types of indoor behaviours: feeding, drinking,
> standing-self-grooming, standing-ruminating, lying-self-grooming and
> lying-ruminating. The dataset consists of 1905 clips collected from our John
> Oldacre Centre dairy farm research platform housing 200 Holstein-Friesian cows.
> Experiments show that Cattle-CLIP achieves 96.1% overall accuracy across six
> behaviours in a supervised setting, with nearly 100% recall for feeding,
> drinking and standing-ruminating behaviours, and demonstrates robust
> generalisation with limited data in few-shot scenarios, highlighting the
> potential of multimodal learning in agricultural and animal behaviour analysis.

