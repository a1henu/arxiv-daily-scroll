---
layout: default
title: Generalization of Diffusion Models Arises with a Balanced Representation Space
---

# Generalization of Diffusion Models Arises with a Balanced Representation Space
**arXiv**：[2512.20963v1](https://arxiv.org/abs/2512.20963) · [PDF](https://arxiv.org/pdf/2512.20963.pdf)  
**作者**：Zekai Zhang, Xiao Li, Xiang Li, Lianghe Shi, Meng Wu, Molei Tao, Qing Qu  

**一句话要点**：提出基于表示学习的扩散模型泛化理论，通过平衡表示空间检测记忆化并实现训练自由编辑

**关键词**：扩散模型, 表示学习, 泛化理论, 记忆化检测, 训练自由编辑, 去噪自编码器

## 3 点简述
- 分析扩散模型中记忆化与泛化的区别，通过两层ReLU去噪自编码器证明记忆化对应局部尖峰表示，泛化对应平衡表示
- 在无条件与文本到图像扩散模型中验证理论，展示深层生成模型中出现相同表示结构
- 提出基于表示的方法检测记忆化，以及通过表示引导实现训练自由编辑技术

## 摘要（原文）

> Diffusion models excel at generating high-quality, diverse samples, yet they risk memorizing training data when overfit to the training objective. We analyze the distinctions between memorization and generalization in diffusion models through the lens of representation learning. By investigating a two-layer ReLU denoising autoencoder (DAE), we prove that (i) memorization corresponds to the model storing raw training samples in the learned weights for encoding and decoding, yielding localized "spiky" representations, whereas (ii) generalization arises when the model captures local data statistics, producing "balanced" representations. Furthermore, we validate these theoretical findings on real-world unconditional and text-to-image diffusion models, demonstrating that the same representation structures emerge in deep generative models with significant practical implications. Building on these insights, we propose a representation-based method for detecting memorization and a training-free editing technique that allows precise control via representation steering. Together, our results highlight that learning good representations is central to novel and meaningful generative modeling.

