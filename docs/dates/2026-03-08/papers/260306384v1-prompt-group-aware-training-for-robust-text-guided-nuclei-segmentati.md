---
layout: default
title: Prompt Group-Aware Training for Robust Text-Guided Nuclei Segmentation
---

# Prompt Group-Aware Training for Robust Text-Guided Nuclei Segmentation
**arXiv**：[2603.06384v1](https://arxiv.org/abs/2603.06384) · [PDF](https://arxiv.org/pdf/2603.06384.pdf)  
**作者**：Yonghuang Wu, Zhenyang Liang, Wenwen Zeng, Xuan Xie, Jinhua Yu  

**一句话要点**：提出提示组感知训练框架以提升文本引导细胞核分割的鲁棒性

**关键词**：文本引导分割, 提示敏感性, 组一致性训练, 医学图像分析, 计算病理学, 鲁棒性提升

## 3 点简述
- 核心问题：基础模型如SAM3在文本引导医学图像分割中，预测对提示表述高度敏感，语义等效描述导致不一致掩码，影响临床可靠性。
- 方法要点：将提示敏感性重构为组间一致性问题，组织语义相关提示为共享真实掩码的提示组，结合质量引导组正则化和带停止梯度策略的logit级一致性约束进行训练。
- 实验或效果：在多数据集细胞核基准测试中，文本提示下性能提升，提示质量水平间性能方差显著降低；在六个零样本跨数据集任务上，平均Dice提升2.16点。

## 摘要（原文）

> Foundation models such as Segment Anything Model 3 (SAM3) enable flexible text-guided medical image segmentation, yet their predictions remain highly sensitive to prompt formulation. Even semantically equivalent descriptions can yield inconsistent masks, limiting reliability in clinical and pathology workflows. We reformulate prompt sensitivity as a group-wise consistency problem. Semantically related prompts are organized into \emph{prompt groups} sharing the same ground-truth mask, and a prompt group-aware training framework is introduced for robust text-guided nuclei segmentation. The approach combines (i) a quality-guided group regularization that leverages segmentation loss as an implicit ranking signal, and (ii) a logit-level consistency constraint with a stop-gradient strategy to align predictions within each group. The method requires no architectural modification and leaves inference unchanged. Extensive experiments on multi-dataset nuclei benchmarks show consistent gains under textual prompting and markedly reduced performance variance across prompt quality levels. On six zero-shot cross-dataset tasks, our method improves Dice by an average of 2.16 points. These results demonstrate improved robustness and generalization for vision-language segmentation in computational pathology.

