---
layout: default
title: LiteUpdate: A Lightweight Framework for Updating AI-Generated Image Detectors
---

# LiteUpdate: A Lightweight Framework for Updating AI-Generated Image Detectors
**arXiv**：[2511.07192v1](https://arxiv.org/abs/2511.07192) · [PDF](https://arxiv.org/pdf/2511.07192.pdf)  
**作者**：Jiajie Lu, Zhenkan Fu, Na Zhao, Long Xing, Kejiang Chen, Weiming Zhang, Nenghai Yu  

**一句话要点**：提出LiteUpdate框架以高效更新AI生成图像检测器并缓解灾难性遗忘

**关键词**：AI生成图像检测, 灾难性遗忘缓解, 轻量级更新框架, 样本选择, 模型融合, 检测器适应

## 3 点简述
- 核心问题：生成AI模型快速演进，现有检测器性能下降，更新效率低且易遗忘旧知识。
- 方法要点：使用置信度和梯度特征选择边界样本，融合多轨迹权重以平衡适应性和知识保留。
- 实验或效果：在AIDE数据集上，Midjourney检测准确率从87.63%提升至93.03%。

## 摘要（原文）

> The rapid progress of generative AI has led to the emergence of new
> generative models, while existing detection methods struggle to keep pace,
> resulting in significant degradation in the detection performance. This
> highlights the urgent need for continuously updating AI-generated image
> detectors to adapt to new generators. To overcome low efficiency and
> catastrophic forgetting in detector updates, we propose LiteUpdate, a
> lightweight framework for updating AI-generated image detectors. LiteUpdate
> employs a representative sample selection module that leverages image
> confidence and gradient-based discriminative features to precisely select
> boundary samples. This approach improves learning and detection accuracy on new
> distributions with limited generated images, significantly enhancing detector
> update efficiency. Additionally, LiteUpdate incorporates a model merging module
> that fuses weights from multiple fine-tuning trajectories, including
> pre-trained, representative, and random updates. This balances the adaptability
> to new generators and mitigates the catastrophic forgetting of prior knowledge.
> Experiments demonstrate that LiteUpdate substantially boosts detection
> performance in various detectors. Specifically, on AIDE, the average detection
> accuracy on Midjourney improved from 87.63% to 93.03%, a 6.16% relative
> increase.

