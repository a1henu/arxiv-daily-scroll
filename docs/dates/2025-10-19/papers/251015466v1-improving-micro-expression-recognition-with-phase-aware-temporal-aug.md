---
layout: default
title: Improving Micro-Expression Recognition with Phase-Aware Temporal Augmentation
---

# Improving Micro-Expression Recognition with Phase-Aware Temporal Augmentation
**arXiv**：[2510.15466v1](https://arxiv.org/abs/2510.15466) · [PDF](https://arxiv.org/pdf/2510.15466.pdf)  
**作者**：Vu Tram Anh Khuong, Luu Tu Nguyen, Thanh Ha Le, Thi Duyen Ngo  

**一句话要点**：提出相位感知时序增强方法以解决微表情识别中数据稀缺问题

**关键词**：微表情识别, 时序增强, 动态图像, 相位分解, 数据稀缺, 模型无关方法

## 3 点简述
- 核心问题：微表情数据集稀缺限制模型泛化和运动模式多样性
- 方法要点：将表情序列分解为起始到顶点和顶点到结束两阶段，生成双阶段动态图像
- 实验或效果：在CASME-II和SAMM数据集上，结合空间增强实现最高10%准确率提升

## 摘要（原文）

> Micro-expressions (MEs) are brief, involuntary facial movements that reveal
> genuine emotions, typically lasting less than half a second. Recognizing these
> subtle expressions is critical for applications in psychology, security, and
> behavioral analysis. Although deep learning has enabled significant advances in
> micro-expression recognition (MER), its effectiveness is limited by the
> scarcity of annotated ME datasets. This data limitation not only hinders
> generalization but also restricts the diversity of motion patterns captured
> during training. Existing MER studies predominantly rely on simple spatial
> augmentations (e.g., flipping, rotation) and overlook temporal augmentation
> strategies that can better exploit motion characteristics. To address this gap,
> this paper proposes a phase-aware temporal augmentation method based on dynamic
> image. Rather than encoding the entire expression as a single onset-to-offset
> dynamic image (DI), our approach decomposes each expression sequence into two
> motion phases: onset-to-apex and apex-to-offset. A separate DI is generated for
> each phase, forming a Dual-phase DI augmentation strategy. These phase-specific
> representations enrich motion diversity and introduce complementary temporal
> cues that are crucial for recognizing subtle facial transitions. Extensive
> experiments on CASME-II and SAMM datasets using six deep architectures,
> including CNNs, Vision Transformer, and the lightweight LEARNet, demonstrate
> consistent performance improvements in recognition accuracy, unweighted
> F1-score, and unweighted average recall, which are crucial for addressing class
> imbalance in MER. When combined with spatial augmentations, our method achieves
> up to a 10\% relative improvement. The proposed augmentation is simple,
> model-agnostic, and effective in low-resource settings, offering a promising
> direction for robust and generalizable MER.

