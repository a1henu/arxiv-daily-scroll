---
layout: default
title: Patch-Discontinuity Mining for Generalized Deepfake Detection
---

# Patch-Discontinuity Mining for Generalized Deepfake Detection
**arXiv**：[2512.22027v1](https://arxiv.org/abs/2512.22027) · [PDF](https://arxiv.org/pdf/2512.22027.pdf)  
**作者**：Huanhuan Yuan, Yang Ping, Zhengqin Xu, Junyi Cao, Shuai Jia, Chao Ma  

**一句话要点**：提出GenDF框架以提升深度伪造检测的泛化能力

**关键词**：深度伪造检测, 泛化能力, 特征空间重分布, 分类不变增强, 大规模视觉模型

## 3 点简述
- 核心问题：现有方法依赖手工特征，在未见伪造模式时性能显著下降
- 方法要点：利用大规模视觉模型，结合特征空间重分布和分类不变增强策略
- 实验或效果：在跨域和跨操作设置中达到先进泛化性能，仅需0.28M可训练参数

## 摘要（原文）

> The rapid advancement of generative artificial intelligence has enabled the creation of highly realistic fake facial images, posing serious threats to personal privacy and the integrity of online information. Existing deepfake detection methods often rely on handcrafted forensic cues and complex architectures, achieving strong performance in intra-domain settings but suffering significant degradation when confronted with unseen forgery patterns. In this paper, we propose GenDF, a simple yet effective framework that transfers a powerful large-scale vision model to the deepfake detection task with a compact and neat network design. GenDF incorporates deepfake-specific representation learning to capture discriminative patterns between real and fake facial images, feature space redistribution to mitigate distribution mismatch, and a classification-invariant feature augmentation strategy to enhance generalization without introducing additional trainable parameters. Extensive experiments demonstrate that GenDF achieves state-of-the-art generalization performance in cross-domain and cross-manipulation settings while requiring only 0.28M trainable parameters, validating the effectiveness and efficiency of the proposed framework.

