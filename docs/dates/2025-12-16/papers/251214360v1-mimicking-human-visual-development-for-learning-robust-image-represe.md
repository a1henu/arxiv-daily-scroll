---
layout: default
title: Mimicking Human Visual Development for Learning Robust Image Representations
---

# Mimicking Human Visual Development for Learning Robust Image Representations
**arXiv**：[2512.14360v1](https://arxiv.org/abs/2512.14360) · [PDF](https://arxiv.org/pdf/2512.14360.pdf)  
**作者**：Ankita Raj, Kaashika Prajaapat, Tapan Kumar Gandhi, Chetan Arora  

**一句话要点**：提出渐进模糊课程学习，模仿人类视觉发展以提升卷积神经网络泛化与鲁棒性。

**关键词**：渐进模糊课程学习, 卷积神经网络泛化, 人类视觉发展模仿, 鲁棒图像表示, 分布偏移鲁棒性

## 3 点简述
- 核心问题：卷积神经网络在输入分布变化时泛化能力不足，难以匹配人类视觉适应性。
- 方法要点：通过从高度模糊图像开始训练，逐步减少模糊，优先学习全局结构而非高频伪影。
- 实验或效果：在CIFAR-10-C和ImageNet-100-C上降低平均腐败误差，提升对分布偏移和噪声的鲁棒性。

## 摘要（原文）

> The human visual system is remarkably adept at adapting to changes in the input distribution; a capability modern convolutional neural networks (CNNs) still struggle to match. Drawing inspiration from the developmental trajectory of human vision, we propose a progressive blurring curriculum to improve the generalization and robustness of CNNs. Human infants are born with poor visual acuity, gradually refining their ability to perceive fine details. Mimicking this process, we begin training CNNs on highly blurred images during the initial epochs and progressively reduce the blur as training advances. This approach encourages the network to prioritize global structures over high-frequency artifacts, improving robustness against distribution shifts and noisy inputs. Challenging prior claims that blurring in the initial training epochs imposes a stimulus deficit and irreversibly harms model performance, we reveal that early-stage blurring enhances generalization with minimal impact on in-domain accuracy. Our experiments demonstrate that the proposed curriculum reduces mean corruption error (mCE) by up to 8.30% on CIFAR-10-C and 4.43% on ImageNet-100-C datasets, compared to standard training without blurring. Unlike static blur-based augmentation, which applies blurred images randomly throughout training, our method follows a structured progression, yielding consistent gains across various datasets. Furthermore, our approach complements other augmentation techniques, such as CutMix and MixUp, and enhances both natural and adversarial robustness against common attack methods. Code is available at https://github.com/rajankita/Visual_Acuity_Curriculum.

