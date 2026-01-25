---
layout: default
title: Uncertainty-guided Generation of Dark-field Radiographs
---

# Uncertainty-guided Generation of Dark-field Radiographs
**arXiv**：[2601.15859v1](https://arxiv.org/abs/2601.15859) · [PDF](https://arxiv.org/pdf/2601.15859.pdf)  
**作者**：Lina Felsner, Henriette Bast, Tina Dorosti, Florian Schaff, Franz Pfeiffer, Daniela Pfeiffer, Julia Schnabel  

**一句话要点**：提出不确定性引导的渐进生成对抗网络，从标准衰减胸片生成暗场图像以解决数据稀缺问题。

**关键词**：暗场X射线成像, 生成对抗网络, 不确定性建模, 图像合成, 医学影像

## 3 点简述
- 核心问题：暗场X射线成像数据稀缺，阻碍深度学习模型开发。
- 方法要点：结合偶然和认知不确定性，提升生成图像的可靠性和可解释性。
- 实验或效果：生成图像结构保真度高，定量指标持续改进，泛化能力强。

## 摘要（原文）

> X-ray dark-field radiography provides complementary diagnostic information to conventional attenuation imaging by visualizing microstructural tissue changes through small-angle scattering. However, the limited availability of such data poses challenges for developing robust deep learning models. In this work, we present the first framework for generating dark-field images directly from standard attenuation chest X-rays using an Uncertainty-Guided Progressive Generative Adversarial Network. The model incorporates both aleatoric and epistemic uncertainty to improve interpretability and reliability. Experiments demonstrate high structural fidelity of the generated images, with consistent improvement of quantitative metrics across stages. Furthermore, out-of-distribution evaluation confirms that the proposed model generalizes well. Our results indicate that uncertainty-guided generative modeling enables realistic dark-field image synthesis and provides a reliable foundation for future clinical applications.

