---
layout: default
title: Noise-Robust Tiny Object Localization with Flows
---

# Noise-Robust Tiny Object Localization with Flows
**arXiv**：[2601.00617v1](https://arxiv.org/abs/2601.00617) · [PDF](https://arxiv.org/pdf/2601.00617.pdf)  
**作者**：Huixin Sun, Linlin Yang, Ronyu Chen, Kerui Gu, Baochang Zhang, Angela Yao, Xianbin Cao  

**一句话要点**：提出TOLF框架以解决小目标定位中的噪声鲁棒性问题

**关键词**：小目标定位, 噪声鲁棒性, 归一化流, 不确定性建模, 目标检测

## 3 点简述
- 小目标检测性能差，对标注噪声敏感，易导致过拟合
- 使用归一化流建模非高斯预测分布，实现噪声鲁棒学习
- 通过不确定性引导梯度调制，抑制噪声样本学习，提升基线性能

## 摘要（原文）

> Despite significant advances in generic object detection, a persistent performance gap remains for tiny objects compared to normal-scale objects. We demonstrate that tiny objects are highly sensitive to annotation noise, where optimizing strict localization objectives risks noise overfitting. To address this, we propose Tiny Object Localization with Flows (TOLF), a noise-robust localization framework leveraging normalizing flows for flexible error modeling and uncertainty-guided optimization. Our method captures complex, non-Gaussian prediction distributions through flow-based error modeling, enabling robust learning under noisy supervision. An uncertainty-aware gradient modulation mechanism further suppresses learning from high-uncertainty, noise-prone samples, mitigating overfitting while stabilizing training. Extensive experiments across three datasets validate our approach's effectiveness. Especially, TOLF boosts the DINO baseline by 1.2% AP on the AI-TOD dataset.

