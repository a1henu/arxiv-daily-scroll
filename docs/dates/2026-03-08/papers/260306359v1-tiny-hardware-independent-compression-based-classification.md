---
layout: default
title: Tiny, Hardware-Independent, Compression-based Classification
---

# Tiny, Hardware-Independent, Compression-based Classification
**arXiv**：[2603.06359v1](https://arxiv.org/abs/2603.06359) · [PDF](https://arxiv.org/pdf/2603.06359.pdf)  
**作者**：Charles Meyers, Aaron MacSween, Erik Elmroth, Tommy Löfstedt  

**一句话要点**：提出基于归一化压缩距离的轻量级分类方法，以支持客户端隐私保护机器学习。

**关键词**：归一化压缩距离, 客户端机器学习, 隐私保护, 轻量级分类, 核方法

## 3 点简述
- 核心问题：现有机器学习方法依赖大量标注数据和高计算成本，不适合客户端隐私保护场景。
- 方法要点：利用归一化压缩距离作为核方法，改进训练效率，无需正式度量属性。
- 实验或效果：在少量样本上训练，模型准确率媲美或优于其他方法，计算成本低，适合客户端部署。

## 摘要（原文）

> The recent developments in machine learning have highlighted a conflict between online platforms and their users in terms of privacy. The importance of user privacy and the struggle for power over user data has been intensified as regulators and operators attempt to police online platforms. As users have become increasingly aware of privacy issues, client-side data storage, management, and analysis have become a favoured approach to large-scale centralised machine learning. However, state-of-the-art machine learning methods require vast amounts of labelled user data, making them unsuitable for models that reside client-side and only have access to a single user's data. State-of-the-art methods are also computationally expensive, which degrades the user experience on compute-limited hardware and also reduces battery life. A recent alternative approach has proven remarkably successful in classification tasks across a wide variety of data -- using a compression-based distance measure (called normalised compression distance) to measure the distance between generic objects in classical distance-based machine learning methods. In this work, we demonstrate that the normalised compression distance is actually not a metric; develop it for the wider context of kernel methods to allow modelling of complex data; and present techniques to improve the training time of models that use this distance measure. We demonstrate that the normalised compression distance works as well as and sometimes better than other metrics and kernels -- while requiring only marginally more computational costs and in spite of the lack of formal metric properties. The end results is a simple model with remarkable accuracy even when trained on a very small number of samples allowing for models that are small and effective enough to run entirely on a client device using only user-supplied data.

