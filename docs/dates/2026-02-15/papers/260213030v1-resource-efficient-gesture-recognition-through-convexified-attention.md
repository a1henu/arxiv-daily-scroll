---
layout: default
title: Resource-Efficient Gesture Recognition through Convexified Attention
---

# Resource-Efficient Gesture Recognition through Convexified Attention
**arXiv**：[2602.13030v1](https://arxiv.org/abs/2602.13030) · [PDF](https://arxiv.org/pdf/2602.13030.pdf)  
**作者**：Daniel Schwartz, Dario Salvucci, Yusuf Osmanlioglu, Richard Vallett, Genevieve Dion, Ali Shokoufandeh  

**一句话要点**：提出凸化注意力机制，以解决可穿戴电子织物界面中手势识别资源受限问题。

**关键词**：手势识别, 凸优化, 可穿戴设备, 电子织物, 资源效率, 注意力机制

## 3 点简述
- 核心问题：可穿戴电子织物界面因功耗、计算能力和尺寸限制，传统深度学习不适用。
- 方法要点：采用非扩张单纯形投影和凸损失函数，实现凸化注意力，确保全局收敛。
- 实验或效果：在四连接点电容传感器上，实现100%准确率，参数减少97%，推理时间低于300微秒。

## 摘要（原文）

> Wearable e-textile interfaces require gesture recognition capabilities but face severe constraints in power consumption, computational capacity, and form factor that make traditional deep learning impractical. While lightweight architectures like MobileNet improve efficiency, they still demand thousands of parameters, limiting deployment on textile-integrated platforms. We introduce a convexified attention mechanism for wearable applications that dynamically weights features while preserving convexity through nonexpansive simplex projection and convex loss functions. Unlike conventional attention mechanisms using non-convex softmax operations, our approach employs Euclidean projection onto the probability simplex combined with multi-class hinge loss, ensuring global convergence guarantees. Implemented on a textile-based capacitive sensor with four connection points, our approach achieves 100.00\% accuracy on tap gestures and 100.00\% on swipe gestures -- consistent across 10-fold cross-validation and held-out test evaluation -- while requiring only 120--360 parameters, a 97\% reduction compared to conventional approaches. With sub-millisecond inference times (290--296$μ$s) and minimal storage requirements ($<$7KB), our method enables gesture interfaces directly within e-textiles without external processing. Our evaluation, conducted in controlled laboratory conditions with a single-user dataset, demonstrates feasibility for basic gesture interactions. Real-world deployment would require validation across multiple users, environmental conditions, and more complex gesture vocabularies. These results demonstrate how convex optimization can enable efficient on-device machine learning for textile interfaces.

