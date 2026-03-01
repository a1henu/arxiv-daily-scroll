---
layout: default
title: GFRRN: Explore the Gaps in Single Image Reflection Removal
---

# GFRRN: Explore the Gaps in Single Image Reflection Removal
**arXiv**：[2602.22695v1](https://arxiv.org/abs/2602.22695) · [PDF](https://arxiv.org/pdf/2602.22695.pdf)  
**作者**：Yu Chen, Zewei He, Xingyu Liu, Zixuan Chen, Zheming Lu  

**一句话要点**：提出GFRRN以解决单图像反射去除中的特征语义差距和标签不一致问题

**关键词**：单图像反射去除, 参数高效微调, 标签生成, 自适应频率学习, 动态注意力

## 3 点简述
- 核心问题：预训练模型特征与反射去除模型间的语义理解差距，以及合成与真实数据反射标签不一致
- 方法要点：采用参数高效微调策略和标签生成器，引入高斯自适应频率学习块和动态代理注意力机制
- 实验或效果：在单图像反射去除任务中表现优异，超越现有先进方法

## 摘要（原文）

> Prior dual-stream methods with the feature interaction mechanism have achieved remarkable performance in single image reflection removal (SIRR). However, they often struggle with (1) semantic understanding gap between the features of pre-trained models and those of reflection removal models, and (2) reflection label inconsistencies between synthetic and real-world training data. In this work, we first adopt the parameter efficient fine-tuning (PEFT) strategy by integrating several learnable Mona layers into the pre-trained model to align the training directions. Then, a label generator is designed to unify the reflection labels for both synthetic and real-world data. In addition, a Gaussian-based Adaptive Frequency Learning Block (G-AFLB) is proposed to adaptively learn and fuse the frequency priors, and a Dynamic Agent Attention (DAA) is employed as an alternative to window-based attention by dynamically modeling the significance levels across windows (inter-) and within an individual window (intra-). These components constitute our proposed Gap-Free Reflection Removal Network (GFRRN). Extensive experiments demonstrate the effectiveness of our GFRRN, achieving superior performance against state-of-the-art SIRR methods.

