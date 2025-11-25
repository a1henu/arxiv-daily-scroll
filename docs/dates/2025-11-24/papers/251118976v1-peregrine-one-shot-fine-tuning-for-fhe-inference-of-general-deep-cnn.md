---
layout: default
title: Peregrine: One-Shot Fine-Tuning for FHE Inference of General Deep CNNs
---

# Peregrine: One-Shot Fine-Tuning for FHE Inference of General Deep CNNs
**arXiv**：[2511.18976v1](https://arxiv.org/abs/2511.18976) · [PDF](https://arxiv.org/pdf/2511.18976.pdf)  
**作者**：Huaming Ling, Ying Wang, Si Chen, Junfeng Fan  

**一句话要点**：提出单阶段微调和广义交错打包方案，以解决全同态加密下CNN推理的激活近似和容量限制问题。

**关键词**：全同态加密推理, CNN微调, 多项式激活近似, 交错打包, 对象检测, 低阶多项式

## 3 点简述
- 核心问题：全同态加密推理中，ReLU等非线性激活的近似和密文容量限制高分辨率图像处理。
- 方法要点：使用低阶多项式近似激活，单阶段微调直接转换预训练CNN，减少训练开销。
- 实验效果：在CIFAR-10、ImageNet和MS COCO上，FHE友好CNN达到与ReLU/SiLU基线相当的精度。

## 摘要（原文）

> We address two fundamental challenges in adapting general deep CNNs for FHE-based inference: approximating non-linear activations such as ReLU with low-degree polynomials while minimizing accuracy degradation, and overcoming the ciphertext capacity barrier that constrains high-resolution image processing on FHE inference. Our contributions are twofold: (1) a single-stage fine-tuning (SFT) strategy that directly converts pre-trained CNNs into FHE-friendly forms using low-degree polynomials, achieving competitive accuracy with minimal training overhead; and (2) a generalized interleaved packing (GIP) scheme that is compatible with feature maps of virtually arbitrary spatial resolutions, accompanied by a suite of carefully designed homomorphic operators that preserve the GIP-form encryption throughout computation. These advances enable efficient, end-to-end FHE inference across diverse CNN architectures. Experiments on CIFAR-10, ImageNet, and MS COCO demonstrate that the FHE-friendly CNNs obtained via our SFT strategy achieve accuracy comparable to baselines using ReLU or SiLU activations. Moreover, this work presents the first demonstration of FHE-based inference for YOLO architectures in object detection leveraging low-degree polynomial activations.

