---
layout: default
title: Diversity Has Always Been There in Your Visual Autoregressive Models
---

# Diversity Has Always Been There in Your Visual Autoregressive Models
**arXiv**：[2511.17074v1](https://arxiv.org/abs/2511.17074) · [PDF](https://arxiv.org/pdf/2511.17074.pdf)  
**作者**：Tong Wang, Guanyu Yang, Nian Liu, Kai Wang, Yaxing Wang, Abdelrahman M Shaker, Salman Khan, Fahad Shahbaz Khan, Senmao Li  

**一句话要点**：提出DiverseVAR以解决视觉自回归模型的多样性崩溃问题

**关键词**：视觉自回归模型, 生成多样性, 特征图组件, 无训练优化, 高保真合成

## 3 点简述
- VAR模型存在多样性崩溃，输出变异性降低，类似少步蒸馏扩散模型
- 通过抑制输入和放大输出的关键特征图组件，无需额外训练恢复多样性
- 实验显示显著增强生成多样性，对性能影响可忽略，保持高保真合成

## 摘要（原文）

> Visual Autoregressive (VAR) models have recently garnered significant attention for their innovative next-scale prediction paradigm, offering notable advantages in both inference efficiency and image quality compared to traditional multi-step autoregressive (AR) and diffusion models. However, despite their efficiency, VAR models often suffer from the diversity collapse i.e., a reduction in output variability, analogous to that observed in few-step distilled diffusion models. In this paper, we introduce DiverseVAR, a simple yet effective approach that restores the generative diversity of VAR models without requiring any additional training. Our analysis reveals the pivotal component of the feature map as a key factor governing diversity formation at early scales. By suppressing the pivotal component in the model input and amplifying it in the model output, DiverseVAR effectively unlocks the inherent generative potential of VAR models while preserving high-fidelity synthesis. Empirical results demonstrate that our approach substantially enhances generative diversity with only neglectable performance influences. Our code will be publicly released at https://github.com/wangtong627/DiverseVAR.

