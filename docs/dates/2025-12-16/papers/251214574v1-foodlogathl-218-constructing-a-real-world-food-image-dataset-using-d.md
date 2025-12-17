---
layout: default
title: FoodLogAthl-218: Constructing a Real-World Food Image Dataset Using Dietary Management Applications
---

# FoodLogAthl-218: Constructing a Real-World Food Image Dataset Using Dietary Management Applications
**arXiv**：[2512.14574v1](https://arxiv.org/abs/2512.14574) · [PDF](https://arxiv.org/pdf/2512.14574.pdf)  
**作者**：Mitsuki Watanabe, Sosuke Amano, Kiyoharu Aizawa, Yoko Yamakata  

**一句话要点**：提出FoodLogAthl-218数据集，基于真实膳食管理应用构建，以提升食物图像分类在现实场景中的性能。

**关键词**：食物图像分类, 真实世界数据集, 膳食管理应用, 上下文感知分类, 增量学习

## 3 点简述
- 核心问题：现有食物图像数据集多依赖网络爬取，与用户真实餐照存在差异，影响模型实用性。
- 方法要点：从膳食管理应用收集真实用户餐照，构建包含218类、6925张图像的数据集，提供丰富元数据。
- 实验或效果：引入分类基准和特定任务，如增量微调和上下文感知分类，并使用大型多模态模型进行评估。

## 摘要（原文）

> Food image classification models are crucial for dietary management applications because they reduce the burden of manual meal logging. However, most publicly available datasets for training such models rely on web-crawled images, which often differ from users' real-world meal photos. In this work, we present FoodLogAthl-218, a food image dataset constructed from real-world meal records collected through the dietary management application FoodLog Athl. The dataset contains 6,925 images across 218 food categories, with a total of 14,349 bounding boxes. Rich metadata, including meal date and time, anonymized user IDs, and meal-level context, accompany each image. Unlike conventional datasets-where a predefined class set guides web-based image collection-our data begins with user-submitted photos, and labels are applied afterward. This yields greater intra-class diversity, a natural frequency distribution of meal types, and casual, unfiltered images intended for personal use rather than public sharing. In addition to (1) a standard classification benchmark, we introduce two FoodLog-specific tasks: (2) an incremental fine-tuning protocol that follows the temporal stream of users' logs, and (3) a context-aware classification task where each image contains multiple dishes, and the model must classify each dish by leveraging the overall meal context. We evaluate these tasks using large multimodal models (LMMs). The dataset is publicly available at https://huggingface.co/datasets/FoodLog/FoodLogAthl-218.

