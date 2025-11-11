---
layout: default
title: Classification of Microplastic Particles in Water using Polarized Light Scattering and Machine Learning Methods
---

# Classification of Microplastic Particles in Water using Polarized Light Scattering and Machine Learning Methods
**arXiv**：[2511.06901v1](https://arxiv.org/abs/2511.06901) · [PDF](https://arxiv.org/pdf/2511.06901.pdf)  
**作者**：Leonard Saur, Marc von Pawlowski, Ulrich Gengenbach, Ingo Sieber, Hossein Shirali, Lorenz Wührl, Rainer Kiko, Christian Pylatiuk  

**一句话要点**：提出基于偏振光散射和深度学习的反射方法，用于水体中微塑料的原位分类。

**关键词**：微塑料分类, 偏振光散射, 深度学习, 原位监测, 反射成像

## 3 点简述
- 核心问题：传统方法在水体中受传输干扰，难以实现大规模微塑料连续监测。
- 方法要点：使用线性偏振激光照射微塑料，偏振敏感相机捕获反射信号。
- 实验或效果：CNN分类三种聚合物，测试集最高准确率80%，AOLP信号更抗噪。

## 摘要（原文）

> Facing the critical need for continuous, large-scale microplastic monitoring,
> which is hindered by the limitations of gold-standard methods in aquatic
> environments, this paper introduces and validates a novel, reflection-based
> approach for the in-situ classification and identification of microplastics
> directly in water bodies, which is based on polarized light scattering. In this
> experiment, we classify colorless microplastic particles (50-300 $\mu$m) by
> illuminating them with linearly polarized laser light and capturing their
> reflected signals using a polarization-sensitive camera. This reflection-based
> technique successfully circumvents the transmission-based interference issues
> that plague many conventional methods when applied in water. Using a deep
> convolutional neural network (CNN) for image-based classification, we
> successfully identified three common polymer types, high-density polyethylene,
> low-density polyethylene, and polypropylene, achieving a peak mean
> classification accuracy of 80% on the test dataset. A subsequent feature
> hierarchy analysis demonstrated that the CNN's decision-making process relies
> mainly on the microstructural integrity and internal texture (polarization
> patterns) of the particle rather than its macroshape. Critically, we found that
> the Angle of Linear Polarization (AOLP) signal is significantly more robust
> against contextual noise than the Degree of Linear Polarization (DOLP) signal.
> While the AOLP-based classification achieved superior overall performance, its
> strength lies in distinguishing between the two polyethylene plastics, showing
> a lower confusion rate between high-density and low-density polyethylene.
> Conversely, the DOLP signal demonstrated slightly worse overall classification
> results but excels at accurately identifying the polypropylene class, which it
> isolated with greater success than AOLP.

