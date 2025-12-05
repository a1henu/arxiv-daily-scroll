---
layout: default
title: OmniScaleSR: Unleashing Scale-Controlled Diffusion Prior for Faithful and Realistic Arbitrary-Scale Image Super-Resolution
---

# OmniScaleSR: Unleashing Scale-Controlled Diffusion Prior for Faithful and Realistic Arbitrary-Scale Image Super-Resolution
**arXiv**：[2512.04699v1](https://arxiv.org/abs/2512.04699) · [PDF](https://arxiv.org/pdf/2512.04699.pdf)  
**作者**：Xinning Chai, Zhengxue Cheng, Yuhong Zhang, Hengsheng Zhang, Yingsheng Qin, Yucai Yang, Rong Xie, Li Song  

**一句话要点**：提出OmniScaleSR以解决任意尺度超分辨率中真实感与保真度平衡问题

**关键词**：任意尺度超分辨率, 扩散模型, 尺度控制, 真实感图像超分辨率, 多域保真度增强

## 3 点简述
- 现有任意尺度超分辨率方法依赖隐式神经表示，细节合成能力有限，导致真实感低。
- OmniScaleSR引入显式扩散原生尺度控制机制，协同隐式尺度适应，实现尺度感知的扩散过程调制。
- 在双三次降质基准和真实数据集上，OmniScaleSR在保真度和感知真实感上超越现有方法，尤其在大放大因子下表现强劲。

## 摘要（原文）

> Arbitrary-scale super-resolution (ASSR) overcomes the limitation of traditional super-resolution (SR) methods that operate only at fixed scales (e.g., 4x), enabling a single model to handle arbitrary magnification. Most existing ASSR approaches rely on implicit neural representation (INR), but its regression-driven feature extraction and aggregation intrinsically limit the ability to synthesize fine details, leading to low realism. Recent diffusion-based realistic image super-resolution (Real-ISR) models leverage powerful pre-trained diffusion priors and show impressive results at the 4x setting. We observe that they can also achieve ASSR because the diffusion prior implicitly adapts to scale by encouraging high-realism generation. However, without explicit scale control, the diffusion process cannot be properly adjusted for different magnification levels, resulting in excessive hallucination or blurry outputs, especially under ultra-high scales. To address these issues, we propose OmniScaleSR, a diffusion-based realistic arbitrary-scale SR framework designed to achieve both high fidelity and high realism. We introduce explicit, diffusion-native scale control mechanisms that work synergistically with implicit scale adaptation, enabling scale-aware and content-aware modulation of the diffusion process. In addition, we incorporate multi-domain fidelity enhancement designs to further improve reconstruction accuracy. Extensive experiments on bicubic degradation benchmarks and real-world datasets show that OmniScaleSR surpasses state-of-the-art methods in both fidelity and perceptual realism, with particularly strong performance at large magnification factors. Code will be released at https://github.com/chaixinning/OmniScaleSR.

