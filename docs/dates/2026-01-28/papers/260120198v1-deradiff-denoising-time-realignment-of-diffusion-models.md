---
layout: default
title: DeRaDiff: Denoising Time Realignment of Diffusion Models
---

# DeRaDiff: Denoising Time Realignment of Diffusion Models
**arXiv**：[2601.20198v1](https://arxiv.org/abs/2601.20198) · [PDF](https://arxiv.org/pdf/2601.20198.pdf)  
**作者**：Ratnavibusena Don Shahain Manujith, Yang Zhang, Teoh Tze Tzun, Kenji Kawaguchi  

**一句话要点**：提出DeRaDiff方法，通过采样时调整正则化强度，高效近似不同强度对齐的扩散模型。

**关键词**：扩散模型对齐, 正则化强度调整, 采样时重对齐, 几何混合后验, 计算效率优化

## 3 点简述
- 核心问题：扩散模型对齐中正则化强度选择困难，需昂贵超参数扫描。
- 方法要点：引入去噪时间重对齐，用几何混合后验替换参考分布，实现单参数动态控制。
- 实验效果：在文本图像对齐和质量指标上，有效近似从头训练模型，大幅降低计算成本。

## 摘要（原文）

> Recent advances align diffusion models with human preferences to increase aesthetic appeal and mitigate artifacts and biases. Such methods aim to maximize a conditional output distribution aligned with higher rewards whilst not drifting far from a pretrained prior. This is commonly enforced by KL (Kullback Leibler) regularization. As such, a central issue still remains: how does one choose the right regularization strength? Too high of a strength leads to limited alignment and too low of a strength leads to "reward hacking". This renders the task of choosing the correct regularization strength highly non-trivial. Existing approaches sweep over this hyperparameter by aligning a pretrained model at multiple regularization strengths and then choose the best strength. Unfortunately, this is prohibitively expensive. We introduce DeRaDiff, a denoising time realignment procedure that, after aligning a pretrained model once, modulates the regularization strength during sampling to emulate models trained at other regularization strengths without any additional training or finetuning. Extending decoding-time realignment from language to diffusion models, DeRaDiff operates over iterative predictions of continuous latents by replacing the reverse step reference distribution by a geometric mixture of an aligned and reference posterior, thus giving rise to a closed form update under common schedulers and a single tunable parameter, lambda, for on the fly control. Our experiments show that across multiple text image alignment and image-quality metrics, our method consistently provides a strong approximation for models aligned entirely from scratch at different regularization strengths. Thus, our method yields an efficient way to search for the optimal strength, eliminating the need for expensive alignment sweeps and thereby substantially reducing computational costs.

