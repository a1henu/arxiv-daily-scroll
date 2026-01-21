---
layout: default
title: MooneyMaker: A Python package to create ambiguous two-tone images
---

# MooneyMaker: A Python package to create ambiguous two-tone images
**arXiv**：[2601.14077v1](https://arxiv.org/abs/2601.14077) · [PDF](https://arxiv.org/pdf/2601.14077.pdf)  
**作者**：Lars C. Reining, Thabo Matthies, Luisa Haussner, Rabea Turon, Thomas S. A. Wallis  

**一句话要点**：提出MooneyMaker开源Python包，自动化生成模糊双色调图像以支持视觉感知研究

**关键词**：Mooney图像生成, 视觉感知研究, Python包, 图像处理, 深度学习模型, 实验验证

## 3 点简述
- 传统手动创建Mooney图像耗时且不一致，需自动化替代方案
- MooneyMaker提供多种生成技术，包括基于图像统计和深度学习的方法
- 实验验证生成图像初始模糊性高，模板呈现后识别率提升，提供技术选择指南

## 摘要（原文）

> Mooney images are high-contrast, two-tone visual stimuli, created by thresholding photographic images. They allow researchers to separate image content from image understanding, making them valuable for studying visual perception. An ideal Mooney image for this purpose achieves a specific balance: it initially appears unrecognizable but becomes fully interpretable to the observer after seeing the original template. Researchers traditionally created these stimuli manually using subjective criteria, which is labor-intensive and can introduce inconsistencies across studies. Automated generation techniques now offer an alternative to this manual approach. Here, we present MooneyMaker, an open-source Python package that automates the generation of ambiguous Mooney images using several complementary approaches. Users can choose between various generation techniques that range from approaches based on image statistics to deep learning models. These models strategically alter edge information to increase initial ambiguity. The package lets users create two-tone images with multiple methods and directly compare the results visually. In an experiment, we validate MooneyMaker by generating Mooney images using different techniques and assess their recognizability for human observers before and after disambiguating them by presenting the template images. Our results reveal that techniques with lower initial recognizability are associated with higher post-template recognition (i.e. a larger disambiguation effect). To help vision scientists build effective databases of Mooney stimuli, we provide practical guidelines for technique selection. By standardizing the generation process, MooneyMaker supports more consistent and reproducible visual perception research.

