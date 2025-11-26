---
layout: default
title: Frequency Bias Matters: Diving into Robust and Generalized Deep Image Forgery Detection
---

# Frequency Bias Matters: Diving into Robust and Generalized Deep Image Forgery Detection
**arXiv**：[2511.19886v1](https://arxiv.org/abs/2511.19886) · [PDF](https://arxiv.org/pdf/2511.19886.pdf)  
**作者**：Chi Liu, Tianqing Zhu, Wanlei Zhou, Wei Zhao  

**一句话要点**：提出频率对齐方法以提升深度图像伪造检测的泛化性与鲁棒性

**关键词**：图像伪造检测, 频率分析, 泛化性, 鲁棒性, 对抗攻击, 防御方法

## 3 点简述
- 核心问题：深度伪造检测器存在频率偏差，导致泛化与鲁棒性问题
- 方法要点：基于频率分析，开发两步频率对齐方法消除真假图像差异
- 实验或效果：在多种检测器、伪造模型和指标下验证方法有效性

## 摘要（原文）

> As deep image forgery powered by AI generative models, such as GANs, continues to challenge today's digital world, detecting AI-generated forgeries has become a vital security topic. Generalizability and robustness are two critical concerns of a forgery detector, determining its reliability when facing unknown GANs and noisy samples in an open world. Although many studies focus on improving these two properties, the root causes of these problems have not been fully explored, and it is unclear if there is a connection between them. Moreover, despite recent achievements in addressing these issues from image forensic or anti-forensic aspects, a universal method that can contribute to both sides simultaneously remains practically significant yet unavailable. In this paper, we provide a fundamental explanation of these problems from a frequency perspective. Our analysis reveals that the frequency bias of a DNN forgery detector is a possible cause of generalization and robustness issues. Based on this finding, we propose a two-step frequency alignment method to remove the frequency discrepancy between real and fake images, offering double-sided benefits: it can serve as a strong black-box attack against forgery detectors in the anti-forensic context or, conversely, as a universal defense to improve detector reliability in the forensic context. We also develop corresponding attack and defense implementations and demonstrate their effectiveness, as well as the effect of the frequency alignment method, in various experimental settings involving twelve detectors, eight forgery models, and five metrics.

