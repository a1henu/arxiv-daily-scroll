---
layout: default
title: Enhancing the quality of gauge images captured in smoke and haze scenes through deep learning
---

# Enhancing the quality of gauge images captured in smoke and haze scenes through deep learning
**arXiv**：[2601.10537v1](https://arxiv.org/abs/2601.10537) · [PDF](https://arxiv.org/pdf/2601.10537.pdf)  
**作者**：Oscar H. Ramírez-Agudelo, Akshay N. Shewatkar, Edoardo Milana, Roland C. Aydin, Kai Franke  

**一句话要点**：提出基于FFA-Net和AECR-Net的深度学习模型，以增强烟雾和雾霾场景中仪表图像的可见性，支持自动读数。

**关键词**：图像去雾, 仪表图像增强, 深度学习, 合成数据集, 自动读数, 烟雾场景处理

## 3 点简述
- 核心问题：烟雾和雾霾环境导致仪表图像可见性降低，影响基础设施监控和应急服务。
- 方法要点：使用FFA-Net和AECR-Net架构处理图像，并基于Unreal Engine生成超过14,000张合成数据集进行训练。
- 实验或效果：在合成雾霾数据集上，SSIM约0.98、PSNR约43dB，AECR-Net表现更优；烟雾数据集效果较差，但模型仍取得一定成果。

## 摘要（原文）

> Images captured in hazy and smoky environments suffer from reduced visibility, posing a challenge when monitoring infrastructures and hindering emergency services during critical situations. The proposed work investigates the use of the deep learning models to enhance the automatic, machine-based readability of gauge in smoky environments, with accurate gauge data interpretation serving as a valuable tool for first responders. The study utilizes two deep learning architectures, FFA-Net and AECR-Net, to improve the visibility of gauge images, corrupted with light up to dense haze and smoke. Since benchmark datasets of analog gauge images are unavailable, a new synthetic dataset, containing over 14,000 images, was generated using the Unreal Engine. The models were trained with an 80\% train, 10\% validation, and 10\% test split for the haze and smoke dataset, respectively. For the synthetic haze dataset, the SSIM and PSNR metrics are about 0.98 and 43\,dB, respectively, comparing well to state-of-the art results. Additionally, more robust results are retrieved from the AECR-Net, when compared to the FFA-Net. Although the results from the synthetic smoke dataset are poorer, the trained models achieve interesting results. In general, imaging in the presence of smoke are more difficult to enhance given the inhomogeneity and high density. Secondly, FFA-Net and AECR-Net are implemented to dehaze and not to desmoke images. This work shows that use of deep learning architectures can improve the quality of analog gauge images captured in smoke and haze scenes immensely. Finally, the enhanced output images can be successfully post-processed for automatic autonomous reading of gauges

