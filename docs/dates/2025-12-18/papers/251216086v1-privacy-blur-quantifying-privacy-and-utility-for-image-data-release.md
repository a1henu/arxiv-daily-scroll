---
layout: default
title: Privacy Blur: Quantifying Privacy and Utility for Image Data Release
---

# Privacy Blur: Quantifying Privacy and Utility for Image Data Release
**arXiv**：[2512.16086v1](https://arxiv.org/abs/2512.16086) · [PDF](https://arxiv.org/pdf/2512.16086.pdf)  
**作者**：Saeed Mahloujifar, Narine Kokhlikyan, Chuan Guo, Kamalika Chaudhuri  

**一句话要点**：提出Privacy Blur软件包，评估图像模糊化方法的隐私与效用权衡，揭示高斯模糊隐私风险。

**关键词**：隐私保护, 图像模糊化, 隐私效用权衡, 高斯模糊, 像素化, 软件包

## 3 点简述
- 核心问题：图像数据发布中高斯模糊等模糊化方法可能泄露隐私信息，需平衡隐私保护与模型训练效用。
- 方法要点：比较高斯模糊、像素化、像素化加噪声和裁剪四种模糊化算法，通过反转和识别攻击评估隐私，模型训练评估效用。
- 实验或效果：高斯模糊在低精度实现中隐私最差，像素化及加噪声方法在适当粒度下能兼顾隐私与多种计算机视觉任务效用。

## 摘要（原文）

> Image data collected in the wild often contains private information such as faces and license plates, and responsible data release must ensure that this information stays hidden. At the same time, released data should retain its usefulness for model-training. The standard method for private information obfuscation in images is Gaussian blurring. In this work, we show that practical implementations of Gaussian blurring are reversible enough to break privacy. We then take a closer look at the privacy-utility tradeoffs offered by three other obfuscation algorithms -- pixelization, pixelization and noise addition (DP-Pix), and cropping. Privacy is evaluated by reversal and discrimination attacks, while utility by the quality of the learnt representations when the model is trained on data with obfuscated faces. We show that the most popular industry-standard method, Gaussian blur is the least private of the four -- being susceptible to reversal attacks in its practical low-precision implementations. In contrast, pixelization and pixelization plus noise addition, when used at the right level of granularity, offer both privacy and utility for a number of computer vision tasks. We make our proposed methods together with suggested parameters available in a software package called Privacy Blur.

