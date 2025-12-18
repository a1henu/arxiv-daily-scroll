---
layout: default
title: Bits for Privacy: Evaluating Post-Training Quantization via Membership Inference
---

# Bits for Privacy: Evaluating Post-Training Quantization via Membership Inference
**arXiv**：[2512.15335v1](https://arxiv.org/abs/2512.15335) · [PDF](https://arxiv.org/pdf/2512.15335.pdf)  
**作者**：Chenxiang Zhang, Tongxi Qu, Zhong Li, Tian Zhang, Jun Pang, Sjouke Mauw  

**一句话要点**：评估后训练量化通过成员推理揭示隐私保护效果，发现低精度模型可降低隐私泄露风险。

**关键词**：后训练量化, 成员推理攻击, 隐私保护, 模型量化, 深度学习隐私, 隐私-效用权衡

## 3 点简述
- 核心问题：量化如何影响深度学习模型的隐私泄露，现有研究主要关注全精度模型。
- 方法要点：系统研究后训练量化的隐私-效用关系，分析AdaRound、BRECQ和OBC算法在多种精度下的表现。
- 实验或效果：低精度量化可显著减少成员推理漏洞，但以效用下降为代价，最后一层高精度量化提供细粒度控制。

## 摘要（原文）

> Deep neural networks are widely deployed with quantization techniques to reduce memory and computational costs by lowering the numerical precision of their parameters. While quantization alters model parameters and their outputs, existing privacy analyses primarily focus on full-precision models, leaving a gap in understanding how bit-width reduction can affect privacy leakage. We present the first systematic study of the privacy-utility relationship in post-training quantization (PTQ), a versatile family of methods that can be applied to pretrained models without further training. Using membership inference attacks as our evaluation framework, we analyze three popular PTQ algorithms-AdaRound, BRECQ, and OBC-across multiple precision levels (4-bit, 2-bit, and 1.58-bit) on CIFAR-10, CIFAR-100, and TinyImageNet datasets. Our findings consistently show that low-precision PTQs can reduce privacy leakage. In particular, lower-precision models demonstrate up to an order of magnitude reduction in membership inference vulnerability compared to their full-precision counterparts, albeit at the cost of decreased utility. Additional ablation studies on the 1.58-bit quantization level show that quantizing only the last layer at higher precision enables fine-grained control over the privacy-utility trade-off. These results offer actionable insights for practitioners to balance efficiency, utility, and privacy protection in real-world deployments.

