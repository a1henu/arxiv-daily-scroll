---
layout: default
title: StegaFFD: Privacy-Preserving Face Forgery Detection via Fine-Grained Steganographic Domain Lifting
---

# StegaFFD: Privacy-Preserving Face Forgery Detection via Fine-Grained Steganographic Domain Lifting
**arXiv**：[2603.02886v1](https://arxiv.org/abs/2603.02886) · [PDF](https://arxiv.org/pdf/2603.02886.pdf)  
**作者**：Guoqing Ma, Xun Lin, Hui Ma, Ajian Liu, Yizhong Liu, Wenzhong Tang, Shan Yu, Chenqi Kong, Yi Yu  

**一句话要点**：提出StegaFFD框架，通过细粒度隐写域提升实现隐私保护的面部伪造检测

**关键词**：隐私保护, 面部伪造检测, 隐写术, 特征增强, 域对齐

## 3 点简述
- 核心问题：现有隐私保护方法在面部伪造检测中易引起攻击者警觉并降低检测精度
- 方法要点：利用隐写术隐藏面部图像，结合LFAD、SFDA和SDA技术增强隐写域中的特征感知
- 实验或效果：在七个数据集上验证了高不可感知性和优于现有方法的检测准确性

## 摘要（原文）

> Most existing Face Forgery Detection (FFD) models assume access to raw face images. In practice, under a client-server framework, private facial data may be intercepted during transmission or leaked by untrusted servers. Previous privacy protection approaches, such as anonymization, encryption, or distortion, partly mitigate leakage but often introduce severe semantic distortion, making images appear obviously protected. This alerts attackers, provoking more aggressive strategies and turning the process into a cat-and-mouse game. Moreover, these methods heavily manipulate image contents, introducing degradation or artifacts that may confuse FFD models, which rely on extremely subtle forgery traces. Inspired by advances in image steganography, which enable high-fidelity hiding and recovery, we propose a Stega}nography-based Face Forgery Detection framework (StegaFFD) to protect privacy without raising suspicion. StegaFFD hides facial images within natural cover images and directly conducts forgery detection in the steganographic domain. However, the hidden forgery-specific features are extremely subtle and interfered with by cover semantics, posing significant challenges. To address this, we propose Low-Frequency-Aware Decomposition (LFAD) and Spatial-Frequency Differential Attention (SFDA), which suppress interference from low-frequency cover semantics and enhance hidden facial feature perception. Furthermore, we introduce Steganographic Domain Alignment (SDA) to align the representations of hidden faces with those of their raw counterparts, enhancing the model's ability to perceive subtle facial cues in the steganographic domain. Extensive experiments on seven FFD datasets demonstrate that StegaFFD achieves strong imperceptibility, avoids raising attackers' suspicion, and better preserves FFD accuracy compared to existing facial privacy protection methods.

