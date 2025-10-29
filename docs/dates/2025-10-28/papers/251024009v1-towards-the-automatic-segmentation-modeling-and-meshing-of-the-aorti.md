---
layout: default
title: Towards the Automatic Segmentation, Modeling and Meshing of the Aortic Vessel Tree from Multicenter Acquisitions: An Overview of the SEG.A. 2023 Segmentation of the Aorta Challenge
---

# Towards the Automatic Segmentation, Modeling and Meshing of the Aortic Vessel Tree from Multicenter Acquisitions: An Overview of the SEG.A. 2023 Segmentation of the Aorta Challenge
**arXiv**：[2510.24009v1](https://arxiv.org/abs/2510.24009) · [PDF](https://arxiv.org/pdf/2510.24009.pdf)  
**作者**：Yuan Jin, Antonio Pepe, Gian Marco Melito, Yuxuan Chen, Yunsu Byeon, Hyeseong Kim, Kyungwon Kim, Doohyun Park, Euijoon Choi, Dosik Hwang, Andriy Myronenko, Dong Yang, Yufan He, Daguang Xu, Ayman El-Ghotni, Mohamed Nabil, Hossam El-Kady, Ahmed Ayyad, Amr Nasr, Marek Wodzinski, Henning Müller, Hyeongyu Kim, Yejee Shin, Abbas Khan, Muhammad Asad, Alexander Zolotarev, Caroline Roney, Anthony Mathur, Martin Benning, Gregory Slabaugh, Theodoros Panagiotis Vagenas, Konstantinos Georgas, George K. Matsopoulos, Jihan Zhang, Zhen Zhang, Liqin Huang, Christian Mayer, Heinrich Mächler, Jan Egger  

**一句话要点**：提出SEG.A挑战赛以解决主动脉血管树自动分割的数据缺乏问题

**关键词**：主动脉血管树分割, 深度学习, 3D U-Net, 模型集成, 医学图像分析, 多中心数据集

## 3 点简述
- 核心问题：主动脉血管树自动分割缺乏高质量共享数据，阻碍临床应用。
- 方法要点：引入大型多机构数据集，并基于3D U-Net等深度学习模型进行分割。
- 实验或效果：集成模型显著优于单一模型，性能与算法设计和训练数据相关。

## 摘要（原文）

> The automated analysis of the aortic vessel tree (AVT) from computed
> tomography angiography (CTA) holds immense clinical potential, but its
> development has been impeded by a lack of shared, high-quality data. We
> launched the SEG.A. challenge to catalyze progress in this field by introducing
> a large, publicly available, multi-institutional dataset for AVT segmentation.
> The challenge benchmarked automated algorithms on a hidden test set, with
> subsequent optional tasks in surface meshing for computational simulations. Our
> findings reveal a clear convergence on deep learning methodologies, with 3D
> U-Net architectures dominating the top submissions. A key result was that an
> ensemble of the highest-ranking algorithms significantly outperformed
> individual models, highlighting the benefits of model fusion. Performance was
> strongly linked to algorithmic design, particularly the use of customized
> post-processing steps, and the characteristics of the training data. This
> initiative not only establishes a new performance benchmark but also provides a
> lasting resource to drive future innovation toward robust, clinically
> translatable tools.

