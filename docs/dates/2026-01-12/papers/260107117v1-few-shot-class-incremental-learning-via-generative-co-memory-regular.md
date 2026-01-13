---
layout: default
title: Few-shot Class-Incremental Learning via Generative Co-Memory Regularization
---

# Few-shot Class-Incremental Learning via Generative Co-Memory Regularization
**arXiv**：[2601.07117v1](https://arxiv.org/abs/2601.07117) · [PDF](https://arxiv.org/pdf/2601.07117.pdf)  
**作者**：Kexin Bao, Yong Li, Dan Zeng, Shiming Ge  

**一句话要点**：提出生成式协同记忆正则化方法以解决少样本类增量学习中的灾难性遗忘和过拟合问题。

**关键词**：少样本学习, 类增量学习, 生成式模型, 记忆正则化, 灾难性遗忘

## 3 点简述
- 核心问题：少样本类增量学习需在少量新类数据下学习，同时避免对旧类的灾难性遗忘和新类的过拟合。
- 方法要点：通过生成式域适应微调构建表示和权重记忆，在增量学习中协同正则化分类器训练。
- 实验或效果：在流行基准测试中优于现有方法，提高识别精度并缓解遗忘和过拟合。

## 摘要（原文）

> Few-shot class-incremental learning (FSCIL) aims to incrementally learn models from a small amount of novel data, which requires strong representation and adaptation ability of models learned under few-example supervision to avoid catastrophic forgetting on old classes and overfitting to novel classes. This work proposes a generative co-memory regularization approach to facilitate FSCIL. In the approach, the base learning leverages generative domain adaptation finetuning to finetune a pretrained generative encoder on a few examples of base classes by jointly incorporating a masked autoencoder (MAE) decoder for feature reconstruction and a fully-connected classifier for feature classification, which enables the model to efficiently capture general and adaptable representations. Using the finetuned encoder and learned classifier, we construct two class-wise memories: representation memory for storing the mean features for each class, and weight memory for storing the classifier weights. After that, the memory-regularized incremental learning is performed to train the classifier dynamically on the examples of few-shot classes in each incremental session by simultaneously optimizing feature classification and co-memory regularization. The memories are updated in a class-incremental manner and they collaboratively regularize the incremental learning. In this way, the learned models improve recognition accuracy, while mitigating catastrophic forgetting over old classes and overfitting to novel classes. Extensive experiments on popular benchmarks clearly demonstrate that our approach outperforms the state-of-the-arts.

