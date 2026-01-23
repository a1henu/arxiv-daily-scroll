---
layout: default
title: Consistency-Regularized GAN for Few-Shot SAR Target Recognition
---

# Consistency-Regularized GAN for Few-Shot SAR Target Recognition
**arXiv**：[2601.15681v1](https://arxiv.org/abs/2601.15681) · [PDF](https://arxiv.org/pdf/2601.15681.pdf)  
**作者**：Yikui Zhai, Shikuang Liu, Wenlve Zhou, Hongsheng Zhang, Zhiheng Zhou, Xiaolin Tian, C. L. Philip Chen  

**一句话要点**：提出一致性正则化GAN以解决少样本SAR目标识别中的数据稀缺问题

**关键词**：少样本学习, 合成孔径雷达, 生成对抗网络, 自监督学习, 目标识别

## 3 点简述
- 核心问题：少样本SAR识别中，传统GAN因数据不足训练不稳定，与少样本学习前提矛盾。
- 方法要点：设计Cr-GAN，采用双分支判别器分离对抗训练与表示学习，结合通道特征插值和双域循环一致性机制。
- 实验或效果：在MSTAR和SRSDD数据集上，8-shot设置下分别达到71.21%和51.64%准确率，显著优于基线，参数量仅为扩散模型的约5%。

## 摘要（原文）

> Few-shot recognition in synthetic aperture radar (SAR) imagery remains a critical bottleneck for real-world applications due to extreme data scarcity. A promising strategy involves synthesizing a large dataset with a generative adversarial network (GAN), pre-training a model via self-supervised learning (SSL), and then fine-tuning on the few labeled samples. However, this approach faces a fundamental paradox: conventional GANs themselves require abundant data for stable training, contradicting the premise of few-shot learning. To resolve this, we propose the consistency-regularized generative adversarial network (Cr-GAN), a novel framework designed to synthesize diverse, high-fidelity samples even when trained under these severe data limitations. Cr-GAN introduces a dual-branch discriminator that decouples adversarial training from representation learning. This architecture enables a channel-wise feature interpolation strategy to create novel latent features, complemented by a dual-domain cycle consistency mechanism that ensures semantic integrity. Our Cr-GAN framework is adaptable to various GAN architectures, and its synthesized data effectively boosts multiple SSL algorithms. Extensive experiments on the MSTAR and SRSDD datasets validate our approach, with Cr-GAN achieving a highly competitive accuracy of 71.21% and 51.64%, respectively, in the 8-shot setting, significantly outperforming leading baselines, while requiring only ~5 of the parameters of state-of-the-art diffusion models. Code is available at: https://github.com/yikuizhai/Cr-GAN.

