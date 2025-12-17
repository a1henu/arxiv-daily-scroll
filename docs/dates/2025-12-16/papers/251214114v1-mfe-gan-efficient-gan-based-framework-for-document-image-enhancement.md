---
layout: default
title: MFE-GAN: Efficient GAN-based Framework for Document Image Enhancement and Binarization with Multi-scale Feature Extraction
---

# MFE-GAN: Efficient GAN-based Framework for Document Image Enhancement and Binarization with Multi-scale Feature Extraction
**arXiv**：[2512.14114v1](https://arxiv.org/abs/2512.14114) · [PDF](https://arxiv.org/pdf/2512.14114.pdf)  
**作者**：Rui-Yang Ju, KokSheik Wong, Yanlin Jin, Jen-Shiun Chiang  

**一句话要点**：提出MFE-GAN框架，通过多尺度特征提取提升文档图像增强与二值化效率

**关键词**：文档图像增强, 生成对抗网络, 多尺度特征提取, Haar小波变换, 二值化, OCR预处理

## 3 点简述
- 核心问题：现有方法使用多个GAN处理不同颜色通道，导致训练和推理时间长
- 方法要点：引入Haar小波变换和归一化预处理，结合新生成器、判别器和损失函数
- 实验或效果：在多个数据集上显著减少训练和推理时间，性能与SOTA方法相当

## 摘要（原文）

> Document image enhancement and binarization are commonly performed prior to document analysis and recognition tasks for improving the efficiency and accuracy of optical character recognition (OCR) systems. This is because directly recognizing text in degraded documents, particularly in color images, often results in unsatisfactory recognition performance. To address these issues, existing methods train independent generative adversarial networks (GANs) for different color channels to remove shadows and noise, which, in turn, facilitates efficient text information extraction. However, deploying multiple GANs results in long training and inference times. To reduce both training and inference times of document image enhancement and binarization models, we propose MFE-GAN, an efficient GAN-based framework with multi-scale feature extraction (MFE), which incorporates Haar wavelet transformation (HWT) and normalization to process document images before feeding them into GANs for training. In addition, we present novel generators, discriminators, and loss functions to improve the model's performance, and we conduct ablation studies to demonstrate their effectiveness. Experimental results on the Benchmark, Nabuco, and CMATERdb datasets demonstrate that the proposed MFE-GAN significantly reduces the total training and inference times while maintaining comparable performance with respect to state-of-the-art (SOTA) methods. The implementation of this work is available at https://ruiyangju.github.io/MFE-GAN.

