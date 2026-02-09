---
layout: default
title: Zero-shot Multi-Contrast Brain MRI Registration by Intensity Randomizing T1-weighted MRI (LUMIR25)
---

# Zero-shot Multi-Contrast Brain MRI Registration by Intensity Randomizing T1-weighted MRI (LUMIR25)
**arXiv**：[2602.06292v1](https://arxiv.org/abs/2602.06292) · [PDF](https://arxiv.org/pdf/2602.06292.pdf)  
**作者**：Hengjie Liu, Yimeng Dou, Di Xu, Xinyi Fu, Dan Ruan, Ke Sheng  

**一句话要点**：提出基于强度随机化和MIND损失的零样本多对比脑MRI配准方法，以解决仅用T1加权MRI训练时的域偏移问题。

**关键词**：零样本配准, 多对比MRI, 强度随机化, MIND损失, 域偏移泛化, 脑影像处理

## 3 点简述
- 核心问题：零样本配准在域偏移（如高场MRI、病理脑、多对比）下，仅用T1加权MRI训练数据实现泛化。
- 方法要点：采用MIND多模态损失、强度随机化增强和轻量级实例特定优化，提升模型对不同对比度的适应性。
- 实验或效果：在LUMIR25挑战赛中测试集排名第一，验证集上实现合理的T1-T2配准精度并保持良好变形规律。

## 摘要（原文）

> In this paper, we summarize the methods and results of our submission to the LUMIR25 challenge in Learn2Reg 2025, which achieved 1st place overall on the test set. Extended from LUMIR24, this year's task focuses on zero-shot registration under domain shifts (high-field MRI, pathological brains, and various MRI contrasts), while the training data comprise only in-domain T1-weighted brain MRI. We start with a meticulous analysis of LUMIR24 winners to identify the main contributors to good monomodal registration performance. To achieve good generalization with diverse contrasts from a model trained with T1-weighted MRI only, we employ three simple but effective strategies: (i) a multimodal loss based on the modality-independent neighborhood descriptor (MIND), (ii) intensity randomization for appearance augmentation, and (iii) lightweight instance-specific optimization (ISO) on feature encoders at inference time. On the validation set, our approach achieves reasonable T1-T2 registration accuracy while maintaining good deformation regularity.

