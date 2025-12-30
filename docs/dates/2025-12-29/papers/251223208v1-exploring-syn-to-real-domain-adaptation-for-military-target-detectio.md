---
layout: default
title: Exploring Syn-to-Real Domain Adaptation for Military Target Detection
---

# Exploring Syn-to-Real Domain Adaptation for Military Target Detection
**arXiv**：[2512.23208v1](https://arxiv.org/abs/2512.23208) · [PDF](https://arxiv.org/pdf/2512.23208.pdf)  
**作者**：Jongoh Jeong, Youngjin Oh, Gyeongrae Nam, Jeongeun Lee, Kuk-Jin Yoon  

**一句话要点**：提出使用虚幻引擎生成合成数据，以解决军事目标检测中的跨域适应问题。

**关键词**：军事目标检测, 合成到真实域适应, 虚幻引擎, 跨域检测, RGB合成数据

## 3 点简述
- 核心问题：军事目标检测缺乏真实数据集，且现有域适应方法局限于自然或自动驾驶场景。
- 方法要点：利用虚幻引擎生成逼真RGB合成数据，用于合成到真实域的迁移学习。
- 实验或效果：在合成数据训练、真实数据验证的实验中，发现带最小提示的域适应方法优于无监督或半监督方法。

## 摘要（原文）

> Object detection is one of the key target tasks of interest in the context of civil and military applications. In particular, the real-world deployment of target detection methods is pivotal in the decision-making process during military command and reconnaissance. However, current domain adaptive object detection algorithms consider adapting one domain to another similar one only within the scope of natural or autonomous driving scenes. Since military domains often deal with a mixed variety of environments, detecting objects from multiple varying target domains poses a greater challenge. Several studies for armored military target detection have made use of synthetic aperture radar (SAR) data due to its robustness to all weather, long range, and high-resolution characteristics. Nevertheless, the costs of SAR data acquisition and processing are still much higher than those of the conventional RGB camera, which is a more affordable alternative with significantly lower data processing time. Furthermore, the lack of military target detection datasets limits the use of such a low-cost approach. To mitigate these issues, we propose to generate RGB-based synthetic data using a photorealistic visual tool, Unreal Engine, for military target detection in a cross-domain setting. To this end, we conducted synthetic-to-real transfer experiments by training our synthetic dataset and validating on our web-collected real military target datasets. We benchmark the state-of-the-art domain adaptation methods distinguished by the degree of supervision on our proposed train-val dataset pair, and find that current methods using minimal hints on the image (e.g., object class) achieve a substantial improvement over unsupervised or semi-supervised DA methods. From these observations, we recognize the current challenges that remain to be overcome.

