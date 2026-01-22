---
layout: default
title: Training-Efficient Text-to-Music Generation with State-Space Modeling
---

# Training-Efficient Text-to-Music Generation with State-Space Modeling
**arXiv**：[2601.14786v1](https://arxiv.org/abs/2601.14786) · [PDF](https://arxiv.org/pdf/2601.14786.pdf)  
**作者**：Wei-Jaw Lee, Fang-Chih Hsieh, Xuanjun Chen, Fang-Duo Tsai, Yi-Hsuan Yang  

**一句话要点**：提出基于状态空间模型的文本到音乐生成方法，以提升训练效率与数据开放性。

**关键词**：文本到音乐生成, 状态空间模型, 训练效率, 开源模型, 公开数据集

## 3 点简述
- 核心问题：现有文本到音乐生成模型计算成本高且依赖私有数据，需更高效开放方案。
- 方法要点：用状态空间模型替换Transformer，探索单阶段与两阶段混合设计，参数约3亿。
- 实验或效果：在公开数据集上训练，仅用9%计算量和2%数据量，性能与基准竞争。

## 摘要（原文）

> Recent advances in text-to-music generation (TTM) have yielded high-quality results, but often at the cost of extensive compute and the use of large proprietary internal data. To improve the affordability and openness of TTM training, an open-source generative model backbone that is more training- and data-efficient is needed. In this paper, we constrain the number of trainable parameters in the generative model to match that of the MusicGen-small benchmark (with about 300M parameters), and replace its Transformer backbone with the emerging class of state-space models (SSMs). Specifically, we explore different SSM variants for sequence modeling, and compare a single-stage SSM-based design with a decomposable two-stage SSM/diffusion hybrid design. All proposed models are trained from scratch on a purely public dataset comprising 457 hours of CC-licensed music, ensuring full openness. Our experimental findings are three-fold. First, we show that SSMs exhibit superior training efficiency compared to the Transformer counterpart. Second, despite using only 9% of the FLOPs and 2% of the training data size compared to the MusicGen-small benchmark, our model achieves competitive performance in both objective metrics and subjective listening tests based on MusicCaps captions. Finally, our scaling-down experiment demonstrates that SSMs can maintain competitive performance relative to the Transformer baseline even at the same training budget (measured in iterations), when the model size is reduced to four times smaller. To facilitate the democratization of TTM research, the processed captions, model checkpoints, and source code are available on GitHub via the project page: https://lonian6.github.io/ssmttm/.

